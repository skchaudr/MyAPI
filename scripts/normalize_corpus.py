#!/usr/bin/env python3
"""Corpus v1 normalization CLI.

Materializes a `corpus_v1/` staging area from the operator's local data
sources (Obsidian vault, ChatGPT/Claude exports, Claude Code/Codex
sessions) with v1 metadata stamps.

Subcommands:
    scan     Walk all sources and emit a JSONL manifest of inferred metadata.
    copy     Read a manifest and materialize corpus_v1/.
    inspect  Render one item's normalized markdown + metadata, read-only.

Design notes — see project-docs/corpus-v1-normalization-readiness.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import re
import shutil
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Optional

import yaml

# Add project root to import path
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from context_refinery.normalization_schema import (  # noqa: E402
    V1Stamp,
    merge_v1_into_frontmatter,
    stamp_from_path,
)

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("normalize_corpus")


# --- Source discovery -------------------------------------------------------

DEFAULT_OBSIDIAN_VAULT = "/home/sab-ssd/obsidian/SoloDeveloper"
DEFAULT_CLAUDE_PROJECTS = os.path.expanduser("~/.claude/projects")
DEFAULT_CLAUDE_SESSIONS = os.path.expanduser("~/.claude/sessions")
DEFAULT_CODEX_LOGS = os.path.expanduser("~/.codex/command-logs")
DEFAULT_REPO_DOCS_ROOTS = (
    str(REPO_ROOT / "project-docs"),
    str(REPO_ROOT / "handoffs"),
)

# Obsidian folders we deliberately exclude from the v1 corpus. These mirror
# the existing `ingest_obsidian` skip list plus a few extras for v1 hygiene.
OBSIDIAN_SKIP_TOP = frozenset({
    "00 Inbox", "09 Utilities", "Templates", "_tasks", "_tasks_converted",
    "_routines", "_dispatch", ".git", ".obsidian", ".trash", ".gemini",
    "TaskNotes",
})


@dataclass
class ManifestEntry:
    """One row in the scan manifest. Lightweight — no body load."""
    source: str                  # obsidian | chatgpt | claude_web | claude_code | codex
    src_path: str                # absolute path to the source artifact
    rel_path: str                # path relative to source root (for routing)
    title: str
    source_type: str
    temporal_mode: str
    primary_project: str
    review_status: str = "inferred"
    size_bytes: int = 0
    extra: dict = field(default_factory=dict)  # adapter-specific hints

    def as_dict(self) -> dict:
        return asdict(self)


# --- Scan: per-source walkers (no full body loads) --------------------------


def scan_obsidian(vault: str) -> Iterable[ManifestEntry]:
    """Walk an Obsidian vault. Yields one entry per .md file."""
    vault_path = Path(vault)
    if not vault_path.is_dir():
        logger.warning(f"Obsidian vault not found: {vault}")
        return

    for path in vault_path.rglob("*.md"):
        rel = path.relative_to(vault_path)
        top = rel.parts[0] if rel.parts else ""
        if top in OBSIDIAN_SKIP_TOP or top.startswith("."):
            continue

        rel_str = str(rel)
        title = path.stem
        stamp = stamp_from_path(rel_str, adapter="obsidian", title=title)

        try:
            size = path.stat().st_size
        except OSError:
            size = 0

        yield ManifestEntry(
            source="obsidian",
            src_path=str(path),
            rel_path=rel_str,
            title=title,
            source_type=stamp.source_type,
            temporal_mode=stamp.temporal_mode,
            primary_project=stamp.primary_project,
            size_bytes=size,
        )


def scan_repo_docs(roots: Iterable[str]) -> Iterable[ManifestEntry]:
    """Walk MyAPI repo doc directories (project-docs/, handoffs/).

    These are the canonical anchor/handoff sources. Path-derived
    source_type already maps them correctly.
    """
    for root in roots:
        root_path = Path(root)
        if not root_path.is_dir():
            logger.warning(f"Repo doc dir not found: {root}")
            continue

        for path in root_path.rglob("*.md"):
            rel = path.relative_to(REPO_ROOT)
            rel_str = str(rel)
            title = path.stem
            stamp = stamp_from_path(rel_str, adapter=None, title=title)

            try:
                size = path.stat().st_size
            except OSError:
                size = 0

            yield ManifestEntry(
                source="repo_docs",
                src_path=str(path),
                rel_path=rel_str,
                title=title,
                source_type=stamp.source_type,
                temporal_mode=stamp.temporal_mode,
                primary_project=stamp.primary_project,
                size_bytes=size,
            )


def scan_claude_code(root: str) -> Iterable[ManifestEntry]:
    """Walk Claude Code project sessions. Yields one entry per .jsonl file."""
    root_path = Path(root)
    if not root_path.is_dir():
        logger.warning(f"Claude Code projects dir not found: {root}")
        return

    for path in root_path.rglob("*.jsonl"):
        # Mirror adapter's exclusions
        if "subagents" in path.parts or "vercel-plugin" in path.parts:
            continue

        rel = path.relative_to(root_path)
        rel_str = str(rel)
        title = path.stem
        stamp = stamp_from_path(rel_str, adapter="claude_code", title=title)

        try:
            size = path.stat().st_size
        except OSError:
            size = 0

        # Top-level project folder is the project hint
        project_hint = rel.parts[0] if rel.parts else ""

        yield ManifestEntry(
            source="claude_code",
            src_path=str(path),
            rel_path=rel_str,
            title=title,
            source_type=stamp.source_type,  # cli_session
            temporal_mode=stamp.temporal_mode,
            primary_project=stamp.primary_project,
            size_bytes=size,
            extra={"project_folder": project_hint},
        )


def scan_codex(root: str) -> Iterable[ManifestEntry]:
    """Walk Codex CLI sessions. Yields one entry per session-meta.json dir."""
    root_path = Path(root)
    if not root_path.is_dir():
        logger.warning(
            f"Codex command-logs dir not found: {root} "
            "(Codex on this host may use a different layout — skipping.)"
        )
        return

    for meta_path in root_path.rglob("session-meta.json"):
        session_dir = meta_path.parent
        rel = session_dir.relative_to(root_path)
        rel_str = str(rel)
        title = session_dir.name
        stamp = stamp_from_path(rel_str, adapter="codex", title=title)

        try:
            size = sum(p.stat().st_size for p in session_dir.glob("*") if p.is_file())
        except OSError:
            size = 0

        yield ManifestEntry(
            source="codex",
            src_path=str(session_dir),
            rel_path=rel_str,
            title=title,
            source_type=stamp.source_type,
            temporal_mode=stamp.temporal_mode,
            primary_project=stamp.primary_project,
            size_bytes=size,
        )


def scan_chatgpt(zip_or_json: Optional[str]) -> Iterable[ManifestEntry]:
    """List conversations in a ChatGPT export. One entry per conversation."""
    if not zip_or_json:
        logger.info("ChatGPT: no export path provided; skipping.")
        return
    path = Path(zip_or_json)
    if not path.exists():
        logger.warning(f"ChatGPT export not found at {zip_or_json}; skipping.")
        return

    conversations = _load_chatgpt_blob(str(path)) or []

    for conv in conversations:
        title = conv.get("title") or "untitled"
        conv_id = conv.get("conversation_id") or conv.get("id") or ""
        rel_str = f"chatgpt/{conv_id or title}"
        stamp = stamp_from_path(rel_str, adapter="chatgpt", title=title)
        yield ManifestEntry(
            source="chatgpt",
            src_path=str(path),
            rel_path=rel_str,
            title=title,
            source_type=stamp.source_type,
            temporal_mode=stamp.temporal_mode,
            primary_project=stamp.primary_project,
            extra={"conversation_id": conv_id},
        )


def scan_claude_web(zip_path: Optional[str]) -> Iterable[ManifestEntry]:
    """List conversations in a Claude.ai export zip."""
    if not zip_path:
        logger.info("Claude web: no export zip provided; skipping.")
        return
    path = Path(zip_path)
    if not path.exists():
        logger.warning(f"Claude web export not found at {zip_path}; skipping.")
        return

    import zipfile
    with zipfile.ZipFile(zip_path) as z:
        candidates = [n for n in z.namelist() if n.endswith("conversations.json")]
        if not candidates:
            logger.warning(f"Claude web zip lacks conversations.json: {zip_path}")
            return
        conversations = json.loads(z.read(candidates[0]))

    for conv in conversations:
        title = conv.get("name") or conv.get("title") or "untitled"
        conv_id = conv.get("uuid") or conv.get("id") or ""
        rel_str = f"claude_web/{conv_id or title}"
        stamp = stamp_from_path(rel_str, adapter="claude_web", title=title)
        yield ManifestEntry(
            source="claude_web",
            src_path=str(path),
            rel_path=rel_str,
            title=title,
            source_type=stamp.source_type,
            temporal_mode=stamp.temporal_mode,
            primary_project=stamp.primary_project,
            extra={"conversation_id": conv_id},
        )


# --- Scan: top-level dispatcher --------------------------------------------


def run_scan(args: argparse.Namespace) -> int:
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    manifest_path = out_dir / f"scan-{today}.jsonl"

    walkers: list[tuple[str, Iterable[ManifestEntry]]] = []
    if not args.skip_obsidian:
        walkers.append(("obsidian", scan_obsidian(args.obsidian)))
    if not args.skip_repo_docs:
        walkers.append(("repo_docs", scan_repo_docs(args.repo_docs)))
    if not args.skip_claude_code:
        walkers.append(("claude_code", scan_claude_code(args.claude_code)))
    if not args.skip_codex:
        walkers.append(("codex", scan_codex(args.codex)))
    if not args.skip_chatgpt:
        walkers.append(("chatgpt", scan_chatgpt(args.chatgpt)))
    if not args.skip_claude_web:
        walkers.append(("claude_web", scan_claude_web(args.claude_web)))

    counts: dict[str, int] = {}
    source_type_counts: dict[str, int] = {}

    with manifest_path.open("w", encoding="utf-8") as f:
        for source, walker in walkers:
            n = 0
            for entry in walker:
                f.write(json.dumps(entry.as_dict(), ensure_ascii=False) + "\n")
                n += 1
                source_type_counts[entry.source_type] = (
                    source_type_counts.get(entry.source_type, 0) + 1
                )
            counts[source] = n
            logger.info(f"  {source}: {n} entries")

    total = sum(counts.values())
    logger.info(f"Wrote manifest with {total} entries → {manifest_path}")
    logger.info(f"By source: {counts}")
    logger.info(f"By source_type: {source_type_counts}")
    return 0


# --- Copy: materialize corpus_v1/ ------------------------------------------


SLUG_RE = re.compile(r"[^\w\s-]")


def slugify(text: str, max_len: int = 60) -> str:
    text = (text or "").lower().strip()
    text = SLUG_RE.sub("", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:max_len] or "untitled"


def entry_fingerprint(entry: dict) -> str:
    """Stable short suffix for avoiding filename collisions."""
    basis = "|".join(
        str(entry.get(key, ""))
        for key in ("source", "rel_path", "src_path")
    )
    return hashlib.sha1(basis.encode("utf-8")).hexdigest()[:8]


def read_frontmatter_and_body(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content. Returns ({}, content) if absent."""
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    try:
        fm = yaml.safe_load(parts[1]) or {}
        if not isinstance(fm, dict):
            fm = {}
        return fm, parts[2].lstrip("\n")
    except yaml.YAMLError:
        return {}, content


def write_doc(path: Path, frontmatter: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    yaml_str = yaml.dump(frontmatter, default_flow_style=False,
                         sort_keys=False, allow_unicode=True)
    path.write_text(f"---\n{yaml_str}---\n\n{body}\n", encoding="utf-8")


def copy_markdown_entry(entry: dict, out_root: Path, prefix: str) -> Optional[Path]:
    """Read a .md source, merge v1 frontmatter, write under documents/<prefix>/.

    Shared by obsidian + repo_docs flows. The prefix separates corpus namespaces
    so a future indexer can keep vault and repo trees disambiguated.
    """
    src = Path(entry["src_path"])
    if not src.exists():
        logger.warning(f"Missing source: {src}")
        return None

    content = src.read_text(encoding="utf-8", errors="replace")
    fm, body = read_frontmatter_and_body(content)

    stamp = V1Stamp(
        source_type=entry["source_type"],
        temporal_mode=entry["temporal_mode"],
        primary_project=entry["primary_project"],
    )
    merged = merge_v1_into_frontmatter(fm, stamp)

    out_path = out_root / "documents" / prefix / entry["rel_path"]
    write_doc(out_path, merged, body)
    return out_path


def copy_conversation_entry(
    entry: dict,
    out_root: Path,
    *,
    chatgpt_blob: Optional[list] = None,
    claude_blob: Optional[list] = None,
) -> Optional[Path]:
    """Materialize a single conversation. Delegates parsing to existing adapters."""
    from context_refinery.adapters.chatgpt import parse_chatgpt_conversation
    from context_refinery.adapters.claude import parse_claude_conversation

    source = entry["source"]
    conv_id = entry.get("extra", {}).get("conversation_id", "")

    if source == "chatgpt":
        if chatgpt_blob is None:
            return None
        match = next(
            (c for c in chatgpt_blob
             if c.get("conversation_id") == conv_id or c.get("id") == conv_id),
            None,
        )
        if match is None:
            return None
        doc = parse_chatgpt_conversation(match)
    elif source == "claude_web":
        if claude_blob is None:
            return None
        match = next(
            (c for c in claude_blob
             if c.get("uuid") == conv_id or c.get("id") == conv_id),
            None,
        )
        if match is None:
            return None
        doc = parse_claude_conversation(match)
    else:
        return None

    title = doc.get("title", entry["title"])
    slug = slugify(title)
    filename = f"{source}-{slug}-{conv_id[:8]}-{entry_fingerprint(entry)}.md"
    out_path = out_root / "conversations" / source / filename

    fm = {
        "id": doc.get("id"),
        "title": title,
        "source": doc.get("source", {}).get("system", source),
        "created_at": doc.get("timestamps", {}).get("created_at"),
        "author": doc.get("author"),
        "tags": doc.get("tags", []),
        "projects": doc.get("projects", []),
    }
    stamp = V1Stamp(
        source_type=entry["source_type"],
        temporal_mode=entry["temporal_mode"],
        primary_project=entry["primary_project"],
        thread_type=None,  # left for review
        signal_strength=None,
        raw_thread_weight="normal",
    )
    fm = merge_v1_into_frontmatter(fm, stamp)
    body = (doc.get("content", {}).get("cleaned_markdown")
            or doc.get("content", {}).get("raw_text", ""))

    write_doc(out_path, fm, body)
    return out_path


def copy_cli_session_entry(entry: dict, out_root: Path) -> Optional[Path]:
    """Materialize a Claude Code or Codex session via existing adapters."""
    from context_refinery.adapters.claude_code import parse_claude_session
    from context_refinery.adapters.codex import parse_codex_session

    source = entry["source"]
    src_path = entry["src_path"]

    try:
        if source == "claude_code":
            doc = parse_claude_session(src_path)
        elif source == "codex":
            doc = parse_codex_session(src_path)
        else:
            return None
    except Exception as e:
        logger.warning(f"Failed to parse {source} session {src_path}: {e}")
        return None

    title = doc.get("title", entry["title"])
    slug = slugify(title)
    sid = doc.get("id", "")[:8] or "unknown"
    filename = f"{source}-{slug}-{sid}-{entry_fingerprint(entry)}.md"
    out_path = out_root / "conversations" / source / filename

    fm = {
        "id": doc.get("id"),
        "title": title,
        "source": doc.get("source", {}).get("system", source),
        "created_at": doc.get("timestamps", {}).get("created_at"),
        "author": doc.get("author"),
        "tags": doc.get("tags", []),
        "projects": doc.get("projects", []),
    }
    stamp = V1Stamp(
        source_type=entry["source_type"],
        temporal_mode=entry["temporal_mode"],
        primary_project=entry["primary_project"],
        raw_thread_weight="normal",
    )
    fm = merge_v1_into_frontmatter(fm, stamp)
    body = (doc.get("content", {}).get("cleaned_markdown")
            or doc.get("content", {}).get("raw_text", ""))

    write_doc(out_path, fm, body)
    return out_path


def run_copy(args: argparse.Namespace) -> int:
    manifest = Path(args.manifest)
    out_root = Path(args.out_dir)
    if not manifest.exists():
        logger.error(f"Manifest not found: {manifest}")
        return 1

    out_root.mkdir(parents=True, exist_ok=True)
    for sub in ("documents", "conversations", "artifacts", "manifests"):
        (out_root / sub).mkdir(parents=True, exist_ok=True)

    # Pre-load chat blobs once if any conversation entries need them.
    entries = [json.loads(line) for line in manifest.read_text().splitlines() if line.strip()]
    needs_chatgpt = any(e["source"] == "chatgpt" for e in entries)
    needs_claude_web = any(e["source"] == "claude_web" for e in entries)
    chatgpt_blob = _load_chatgpt_blob(args.chatgpt) if needs_chatgpt else None
    claude_blob = _load_claude_web_blob(args.claude_web) if needs_claude_web else None

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    copy_manifest = out_root / "manifests" / f"copy-{today}.jsonl"

    limit = args.limit
    written = 0
    failed = 0
    with copy_manifest.open("w", encoding="utf-8") as cm:
        for entry in entries:
            if limit is not None and written >= limit:
                break
            try:
                source = entry["source"]
                if source == "obsidian":
                    out_path = copy_markdown_entry(entry, out_root, prefix="vault")
                elif source == "repo_docs":
                    out_path = copy_markdown_entry(entry, out_root, prefix="repo")
                elif source in ("chatgpt", "claude_web"):
                    out_path = copy_conversation_entry(
                        entry, out_root,
                        chatgpt_blob=chatgpt_blob,
                        claude_blob=claude_blob,
                    )
                elif source in ("claude_code", "codex"):
                    out_path = copy_cli_session_entry(entry, out_root)
                else:
                    out_path = None

                if out_path is None:
                    failed += 1
                    continue

                cm.write(json.dumps({
                    "src_path": entry["src_path"],
                    "out_path": str(out_path),
                    "source": source,
                    "source_type": entry["source_type"],
                    "primary_project": entry["primary_project"],
                }, ensure_ascii=False) + "\n")
                written += 1
            except Exception as e:
                failed += 1
                logger.warning(f"Copy failed for {entry.get('src_path')}: {e}")

    logger.info(f"Copied {written} items, {failed} failed → {out_root}")
    logger.info(f"Copy manifest: {copy_manifest}")
    return 0 if failed == 0 else (0 if written else 2)


def _load_chatgpt_blob(path: Optional[str]) -> Optional[list]:
    if not path or not os.path.exists(path):
        return None
    path_obj = Path(path)
    out: list = []
    if path_obj.is_dir():
        shards = sorted(path_obj.glob("conversations*.json"))
        for shard in shards:
            out.extend(json.loads(shard.read_text(encoding="utf-8")))
    elif path.endswith(".zip"):
        import zipfile
        with zipfile.ZipFile(path) as z:
            shards = sorted(
                n for n in z.namelist()
                if n.startswith("conversations") and n.endswith(".json")
            )
            for shard in shards:
                out.extend(json.loads(z.read(shard)))
    else:
        with open(path, "r", encoding="utf-8") as f:
            out = json.load(f)
    return out


def _load_claude_web_blob(path: Optional[str]) -> Optional[list]:
    if not path or not os.path.exists(path):
        return None
    import zipfile
    with zipfile.ZipFile(path) as z:
        candidates = [n for n in z.namelist() if n.endswith("conversations.json")]
        if not candidates:
            return None
        return json.loads(z.read(candidates[0]))


# --- Inspect ---------------------------------------------------------------


def run_inspect(args: argparse.Namespace) -> int:
    target = args.target
    # Two modes: a path on disk, or a manifest line lookup by rel_path
    if os.path.exists(target):
        path = Path(target)
    elif args.manifest and Path(args.manifest).exists():
        match = None
        for line in Path(args.manifest).read_text().splitlines():
            if not line.strip():
                continue
            entry = json.loads(line)
            if target in (entry["src_path"], entry["rel_path"]):
                match = entry
                break
        if match is None:
            logger.error(f"No manifest entry matched: {target}")
            return 1
        path = Path(match["src_path"])
    else:
        logger.error(f"Cannot resolve target: {target}")
        return 1

    if not path.exists():
        logger.error(f"Source path missing: {path}")
        return 1

    # Read + stamp + render in-memory only.
    content = path.read_text(encoding="utf-8", errors="replace")
    fm, body = read_frontmatter_and_body(content)

    # Infer adapter from path heuristic
    adapter = None
    p = str(path)
    if "/.claude/projects/" in p:
        adapter = "claude_code"
    elif "/.codex/" in p:
        adapter = "codex"
    elif "/obsidian/" in p:
        adapter = "obsidian"

    rel = path.name
    if args.manifest:
        # Try to use rel_path from manifest if found
        for line in Path(args.manifest).read_text().splitlines():
            if not line.strip():
                continue
            entry = json.loads(line)
            if entry["src_path"] == str(path):
                rel = entry["rel_path"]
                break

    stamp = stamp_from_path(rel, adapter=adapter, title=path.stem)
    merged = merge_v1_into_frontmatter(fm, stamp)

    print(f"# {path}")
    print(f"# adapter={adapter}  rel={rel}")
    print(f"# inferred: source_type={stamp.source_type} "
          f"temporal_mode={stamp.temporal_mode} "
          f"primary_project={stamp.primary_project}")
    print("---")
    print(yaml.dump(merged, default_flow_style=False, sort_keys=False,
                   allow_unicode=True), end="")
    print("---")
    preview = body[:1000]
    print(preview)
    if len(body) > 1000:
        print(f"\n... [truncated, {len(body)} chars total]")
    return 0


# --- Arg parsing -----------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Corpus v1 normalization CLI (scan / copy / inspect).",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    # scan
    ps = sub.add_parser("scan", help="Walk sources and emit a JSONL manifest.")
    ps.add_argument("--out-dir", default=str(REPO_ROOT / "corpus_v1" / "manifests"))
    ps.add_argument("--obsidian", default=DEFAULT_OBSIDIAN_VAULT)
    ps.add_argument("--repo-docs", nargs="+", default=list(DEFAULT_REPO_DOCS_ROOTS),
                    help="Repo doc dirs to include (project-docs/, handoffs/)")
    ps.add_argument("--claude-code", default=DEFAULT_CLAUDE_PROJECTS)
    ps.add_argument("--codex", default=DEFAULT_CODEX_LOGS)
    ps.add_argument("--chatgpt", default=None,
                    help="Path to ChatGPT conversations.json, export zip, or shard directory")
    ps.add_argument("--claude-web", default=None,
                    help="Path to Claude.ai export zip")
    ps.add_argument("--skip-obsidian", action="store_true")
    ps.add_argument("--skip-repo-docs", action="store_true")
    ps.add_argument("--skip-claude-code", action="store_true")
    ps.add_argument("--skip-codex", action="store_true")
    ps.add_argument("--skip-chatgpt", action="store_true")
    ps.add_argument("--skip-claude-web", action="store_true")
    ps.set_defaults(func=run_scan)

    # copy
    pc = sub.add_parser("copy", help="Materialize corpus_v1/ from a scan manifest.")
    pc.add_argument("--manifest", required=True,
                    help="Path to a scan-*.jsonl manifest")
    pc.add_argument("--out-dir", default=str(REPO_ROOT / "corpus_v1"))
    pc.add_argument("--chatgpt", default=None)
    pc.add_argument("--claude-web", default=None)
    pc.add_argument("--limit", type=int, default=None,
                    help="Cap items copied (useful for smoke tests)")
    pc.set_defaults(func=run_copy)

    # inspect
    pi = sub.add_parser("inspect", help="Render one item's normalized markdown + metadata.")
    pi.add_argument("target", help="Path to source file or rel_path in manifest")
    pi.add_argument("--manifest", default=None,
                    help="Optional manifest for rel_path lookups")
    pi.set_defaults(func=run_inspect)

    return p


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
