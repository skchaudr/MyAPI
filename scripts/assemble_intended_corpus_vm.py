#!/usr/bin/env python3
"""Assemble the *intended* hot corpus on khoj-38 and (optionally) index into Khoj.

Intended mix (Lane A / project side) — not the full chat-dump firehose:
  - project handoffs & project documents
  - golden briefs / product tip docs (from git origin/main when missing on tree)
  - graphify artifacts (manifests + bounded graph)
  - agent CLI session *summaries* (not raw transcripts)
  - git history digests for key repos
  - GDDP / aa-cli product-adjacent docs
  - corpus-hot wave-1 pack + SOTA anchors

Never ingests: full ~/.pi tree, auth/secrets, model weights, bulk unfiltered exports.

Usage:
  python3 scripts/assemble_intended_corpus_vm.py --dry-run
  python3 scripts/assemble_intended_corpus_vm.py --index
  python3 scripts/assemble_intended_corpus_vm.py --status
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

HOME = Path("/home/sab-mini")
REPO = Path(__file__).resolve().parents[1]
OUT_ROOT = Path(os.environ.get("INTENDED_CORPUS_ROOT", "/data/corpus-hot/intended-v1"))
STAGE_DIR = OUT_ROOT / "stage"
RECEIPT_DIR = OUT_ROOT / "receipts"
MANIFEST_PATH = OUT_ROOT / "manifest.json"
SOURCES_MD = OUT_ROOT / "SOURCES.md"
LAST_PATH = OUT_ROOT / "LAST.json"

MAX_FILE_BYTES = 600 * 1024
HOST = os.uname().nodename.split(".")[0]
DEFAULT_KHOJ = os.environ.get("MYAPI_KHOJ_URL", "http://127.0.0.1:42110").rstrip("/")

DENY_SUBSTRINGS = (
    "/.env",
    "auth.json",
    "credentials",
    "id_rsa",
    "id_ed25519",
    ".pem",
    "/weights/",
    "/blobs/",
    "token.json",
    "password",
)


@dataclass
class Spec:
    path: Path
    prefix: str
    recursive: bool = False
    max_files: int = 40
    glob: str = "*.md"
    required: bool = False
    category: str = "misc"


def log(msg: str) -> None:
    print(msg, flush=True)


def denied(path: Path) -> bool:
    s = str(path).lower()
    return any(x in s for x in DENY_SUBSTRINGS)


def safe_slug(text: str, max_len: int = 90) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s.-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-.")
    return (text[:max_len] or "untitled")


def sha_key(origin: str, body: str) -> str:
    h = hashlib.sha256()
    h.update(origin.encode("utf-8", errors="replace"))
    h.update(b"\0")
    h.update(body.encode("utf-8", errors="replace"))
    return h.hexdigest()


def wrap(origin: str, body: str, staged: str, category: str, key: str) -> str:
    header = (
        f"---\n"
        f"title: {Path(origin).name}\n"
        f"source: intended-corpus-vm\n"
        f"category: {category}\n"
        f"host: {HOST}\n"
        f"origin_path: {origin}\n"
        f"staged_as: {staged}\n"
        f"content_key: {key}\n"
        f"assembled_at: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\n"
        f"---\n\n"
    )
    if body.lstrip().startswith("---"):
        return (
            f"<!-- intended-corpus-vm cat={category} origin={origin} staged={staged} -->\n\n"
            + body
        )
    return header + body


def collect_paths(spec: Spec) -> list[Path]:
    p = spec.path
    if not p.exists():
        if spec.required:
            raise FileNotFoundError(f"required missing: {p}")
        return []
    if p.is_file():
        return [p]
    found: list[Path] = []
    if not spec.recursive:
        found = sorted(p.glob(spec.glob))
    else:
        for root, dirs, files in os.walk(p):
            dirs[:] = [
                d
                for d in dirs
                if d
                not in {".git", "node_modules", ".venv", "venv", "__pycache__", ".cache", "artifacts"}
                and not d.startswith(".")
            ]
            for name in files:
                if spec.glob == "*.md" and not name.endswith(".md"):
                    continue
                if name.startswith("._"):
                    continue
                fp = Path(root) / name
                if denied(fp):
                    continue
                found.append(fp)
    out: list[Path] = []
    for fp in sorted(found, key=lambda x: x.stat().st_mtime, reverse=True):
        try:
            if fp.stat().st_size > MAX_FILE_BYTES:
                continue
        except OSError:
            continue
        out.append(fp)
        if len(out) >= spec.max_files:
            break
    return out


def stage_name(spec: Spec, src: Path) -> str:
    if src.is_file() and spec.path.is_file():
        base = safe_slug(src.name)
    else:
        try:
            rel = src.relative_to(spec.path if spec.path.is_dir() else spec.path.parent)
        except ValueError:
            rel = Path(src.name)
        base = "-".join(safe_slug(part) for part in rel.parts)
    name = f"{spec.prefix}--{base}"
    if not name.endswith(".md"):
        name += ".md"
    return name


def write_staged(
    staged: list[tuple[Path, str, str]],
    origin: str,
    body: str,
    name: str,
    category: str,
) -> None:
    if len(body.encode("utf-8")) > MAX_FILE_BYTES:
        return
    key = sha_key(origin, body)
    dest = STAGE_DIR / name
    dest.write_text(wrap(origin, body, name, category, key), encoding="utf-8")
    staged.append((dest, key, category))


def disk_specs() -> list[Spec]:
    myapi = REPO
    return [
        # --- project handoffs & docs ---
        Spec(myapi / "handoffs", "proj-handoffs", recursive=True, max_files=50, category="project-handoffs", required=True),
        Spec(myapi / "project-docs", "proj-docs", recursive=True, max_files=60, category="project-documents"),
        Spec(
            myapi / "project-docs" / "source-of-truth-anchors",
            "proj-anchors",
            recursive=True,
            max_files=20,
            category="project-documents",
        ),
        Spec(myapi / "project-docs" / "khoj-goldens", "proj-goldens", recursive=True, max_files=20, category="project-documents"),
        Spec(myapi / "README.md", "proj-root", category="project-documents"),
        Spec(myapi / "AGENTS.md", "proj-root", category="project-documents"),
        Spec(myapi / "HANDOFF-PI-README.md", "proj-root", category="project-handoffs"),
        Spec(myapi / "docs", "proj-docs-root", recursive=True, max_files=15, category="project-documents"),
        # wayfinder / semantic graphify intent
        Spec(
            myapi / ".scratch" / "semantic-graphify-cold-start",
            "semantic-graphify",
            recursive=True,
            max_files=40,
            category="graphify-intent",
        ),
        # corpus-hot wave-1 pack (already curated)
        Spec(Path("/data/corpus-hot/v1/myapi"), "wave1-myapi", recursive=True, max_files=10, category="corpus-hot"),
        Spec(Path("/data/corpus-hot/v1/gddp"), "wave1-gddp", recursive=True, max_files=10, category="corpus-hot"),
        Spec(Path("/data/corpus-hot/v1/pi-needle-gemma"), "wave1-pi", recursive=True, max_files=10, category="corpus-hot"),
        Spec(Path("/data/corpus-hot/v1/README.md"), "wave1", category="corpus-hot"),
        Spec(Path("/data/corpus-hot/v1/DENYLIST.md"), "wave1", category="corpus-hot"),
        Spec(Path("/data/corpus-hot/smoke-questions.txt"), "wave1", category="corpus-hot"),
        # high-signal flat notes already in v1-notes (anchors etc.) — skip noisy claude-* dumps
        Spec(Path("/data/corpus-hot/v1-notes"), "v1-notes", recursive=False, max_files=80, category="project-notes"),
        # GDDP
        Spec(HOME / "gddp-runtime" / "PROJECT-BRIEF.md", "gddp-runtime", category="project-documents"),
        Spec(HOME / "gddp-runtime" / "TOPOLOGY.md", "gddp-runtime", category="project-documents"),
        Spec(HOME / "gddp-runtime" / "README.md", "gddp-runtime", category="project-documents"),
        Spec(HOME / "gddp-runtime" / "AGENTS.md", "gddp-runtime", category="project-documents"),
        Spec(HOME / "gddp-config" / "README.md", "gddp-config", category="project-documents"),
        Spec(HOME / "gddp-config" / "AGENTS.md", "gddp-config", category="project-documents"),
        Spec(
            HOME / "gddp-config" / "Wayfinder-Workflow-and-GDDP-Workflow.md",
            "gddp-config",
            category="project-documents",
        ),
        # aa-cli product adjacent
        Spec(HOME / "aa-cli" / "AGENTS.md", "aa-cli", category="project-documents"),
        Spec(HOME / "aa-cli" / "README.md", "aa-cli", category="project-documents"),
        Spec(HOME / "aa-cli" / ".handoffs", "aa-cli-handoffs", recursive=True, max_files=15, category="project-handoffs"),
        Spec(
            HOME / "aa-cli" / ".scratch" / "verify-pathway",
            "aa-cli-verify",
            recursive=True,
            max_files=30,
            category="project-documents",
        ),
        # Pi harness handoffs only (not full ~/.pi)
        Spec(HOME / ".pi" / "harness" / "sessions", "pi-handoffs", recursive=False, max_files=20, category="agent-sessions"),
        Spec(HOME / ".pi" / "needle" / "README.md", "pi-needle", category="project-documents"),
        Spec(HOME / ".pi" / "needle" / "README-KHOJ.md", "pi-needle", category="project-documents"),
        # Codex rollout *summaries* only
        Spec(
            HOME / ".codex" / "memories" / "rollout_summaries",
            "codex-summaries",
            recursive=False,
            max_files=40,
            category="agent-sessions",
        ),
        Spec(HOME / ".codex" / "memories" / "memory_summary.md", "codex-summaries", category="agent-sessions"),
        # VM root / lane claims
        Spec(HOME / "00-READ-ME-FIRST.md", "vm-root", category="project-documents"),
        Spec(HOME / "00-PROJECT-LANE.md", "vm-root", category="project-documents"),
        Spec(HOME / "001-MyAPI-VM-Situated.md", "vm-root", category="project-handoffs"),
    ]


def git_export_main(staged: list[tuple[Path, str, str]]) -> list[str]:
    """Pull product-tip docs from origin/main into stage."""
    notes: list[str] = []
    tips = [
        ("PROJECT-BRIEF.md", "git-main--PROJECT-BRIEF.md", "project-documents"),
        ("IMPLEMENTATION-PLAN.md", "git-main--IMPLEMENTATION-PLAN.md", "project-documents"),
        ("myapi-db-plan.md", "git-main--myapi-db-plan.md", "project-documents"),
        ("AGENTS.md", "git-main--AGENTS.md", "project-documents"),
        ("evals/eval-bank-v0.md", "git-main--eval-bank-v0.md", "project-documents"),
        (
            "evals/golden_briefs/get_project_context_myapi_rebuild.md",
            "git-main--golden-project-myapi.md",
            "golden-briefs",
        ),
        (
            "evals/golden_briefs/get_person_context_sab.md",
            "git-main--golden-person-sab.md",
            "golden-briefs",
        ),
        (
            "evals/golden_briefs/get_project_context_pi_needle.md",
            "git-main--golden-project-pi-needle.md",
            "golden-briefs",
        ),
        ("mcp/README.md", "git-main--mcp-README.md", "project-documents"),
        ("mcp/server.py", "git-main--mcp-server.md", "project-documents"),  # wrap as md
        ("repo-docs/graphify-hooks-and=handoff-hooks.md", "git-main--graphify-hooks.md", "graphify"),
        ("graphify-out/graph.json", "git-main--graphify-graph.md", "graphify"),
        ("gddp/nodes/prove-first-durable-handoff.yaml", "git-main--gddp-node-prove.md", "project-documents"),
    ]
    # all .handoffs on main
    proc = subprocess.run(
        ["git", "-C", str(REPO), "ls-tree", "-r", "--name-only", "origin/main", ".handoffs"],
        capture_output=True,
        text=True,
    )
    if proc.returncode == 0:
        for rel in proc.stdout.splitlines():
            if rel.endswith(".md"):
                tips.append((rel, f"git-main-handoff--{safe_slug(Path(rel).name)}", "project-handoffs"))

    for rel, out_name, cat in tips:
        proc = subprocess.run(
            ["git", "-C", str(REPO), "show", f"origin/main:{rel}"],
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            notes.append(f"miss origin/main:{rel}")
            continue
        body = proc.stdout
        if rel.endswith(".py") or rel.endswith(".json") or rel.endswith(".yaml"):
            body = f"# git:origin/main:{rel}\n\n```\n{body}\n```\n"
        if not out_name.endswith(".md"):
            out_name += ".md"
        write_staged(staged, f"git:origin/main:{rel}", body, out_name, cat)
        notes.append(f"ok origin/main:{rel}")
    return notes


def git_history_digest(staged: list[tuple[Path, str, str]]) -> list[str]:
    """Recent git history for key repos as markdown."""
    notes: list[str] = []
    repos = [
        (REPO, "myapi", 80),
        (HOME / "aa-cli", "aa-cli", 40),
        (HOME / "gddp-runtime", "gddp-runtime", 40),
        (HOME / "gddp-config", "gddp-config", 30),
    ]
    for path, name, n in repos:
        if not (path / ".git").exists() and not (path / ".git").is_file():
            # allow worktrees
            if not path.exists():
                notes.append(f"skip history {name}: missing")
                continue
        proc = subprocess.run(
            [
                "git",
                "-C",
                str(path),
                "log",
                f"-n{n}",
                "--date=short",
                "--pretty=format:%h | %ad | %an | %s",
            ],
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            notes.append(f"skip history {name}: {proc.stderr.strip()[:80]}")
            continue
        branch = subprocess.run(
            ["git", "-C", str(path), "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
        ).stdout.strip()
        tip = subprocess.run(
            ["git", "-C", str(path), "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
        ).stdout.strip()
        body = (
            f"# Git history digest — {name}\n\n"
            f"- path: `{path}`\n"
            f"- branch: `{branch}`\n"
            f"- tip: `{tip}`\n"
            f"- generated: {datetime.now(timezone.utc).isoformat()}\n\n"
            f"| commit | date | author | subject |\n"
            f"|--------|------|--------|---------|\n"
        )
        for line in proc.stdout.splitlines():
            parts = [p.strip() for p in line.split("|", 3)]
            if len(parts) == 4:
                body += f"| `{parts[0]}` | {parts[1]} | {parts[2]} | {parts[3]} |\n"
            else:
                body += f"| {line} |\n"
        write_staged(
            staged,
            f"git-log:{path}",
            body,
            f"git-history--{name}.md",
            "git-history",
        )
        notes.append(f"history {name}: {n} commits")
    return notes


def grok_session_summaries(staged: list[tuple[Path, str, str]], max_n: int = 50) -> list[str]:
    """Turn Grok summary.json into short markdown (no full transcripts)."""
    notes: list[str] = []
    root = HOME / ".grok" / "sessions"
    if not root.exists():
        return ["no grok sessions dir"]
    items: list[tuple[str, dict, Path]] = []
    for p in root.rglob("summary.json"):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        summary = (d.get("session_summary") or d.get("generated_title") or "").strip()
        if not summary:
            continue
        updated = d.get("updated_at") or d.get("last_active_at") or d.get("created_at") or ""
        items.append((updated, d, p))
    items.sort(key=lambda x: x[0], reverse=True)
    # Prefer project-ballpark keywords, then fill with recent
    keywords = re.compile(
        r"myapi|khoj|corpus|gddp|aa-cli|graphify|retrieval|verify|handoff|needle|mcp|cold.?start|semantic",
        re.I,
    )
    preferred = [x for x in items if keywords.search(x[1].get("session_summary") or "") or keywords.search(str(x[1].get("info", {}).get("cwd", "")))]
    rest = [x for x in items if x not in preferred]
    chosen = (preferred + rest)[:max_n]
    for i, (updated, d, p) in enumerate(chosen):
        info = d.get("info") or {}
        sid = info.get("id") or p.parent.name
        body = (
            f"# Agent session summary (Grok)\n\n"
            f"- id: `{sid}`\n"
            f"- cwd: `{info.get('cwd', '')}`\n"
            f"- title: {d.get('generated_title') or ''}\n"
            f"- summary: {d.get('session_summary') or ''}\n"
            f"- model: {d.get('current_model_id') or ''}\n"
            f"- agent: {d.get('agent_name') or ''}\n"
            f"- messages: chat={d.get('num_chat_messages')} total={d.get('num_messages')}\n"
            f"- created: {d.get('created_at')}\n"
            f"- updated: {d.get('updated_at') or d.get('last_active_at')}\n"
            f"- git: branch={d.get('head_branch')} tip={d.get('head_commit')}\n"
            f"- remotes: {d.get('git_remotes')}\n"
            f"- source_path: `{p}`\n"
        )
        write_staged(
            staged,
            str(p),
            body,
            f"grok-summary--{safe_slug(sid)[:40]}.md",
            "agent-sessions",
        )
    notes.append(f"grok summaries staged: {len(chosen)} (preferred={len(preferred)})")
    return notes


def filter_v1_notes_noise(name: str) -> bool:
    """Skip bulk chat dumps that drown the intended mix."""
    n = name.lower()
    if n.startswith("claude-local-command-caveat"):
        return False
    if n.startswith("claude-yo-claude"):
        return False
    if n.startswith("claude-web-converting") and "opclaw" in n:
        return True  # keep one project-ish
    # keep codex/project docs/anchors/wave1/corpus
    return True


def stage_all() -> tuple[list[tuple[Path, str, str]], list[str]]:
    STAGE_DIR.mkdir(parents=True, exist_ok=True)
    for old in STAGE_DIR.iterdir():
        if old.is_file():
            old.unlink()

    staged: list[tuple[Path, str, str]] = []
    warnings: list[str] = []

    for spec in disk_specs():
        try:
            files = collect_paths(spec)
        except FileNotFoundError as exc:
            raise
        if not files and not spec.path.exists():
            warnings.append(f"missing optional: {spec.path}")
            continue
        for src in files:
            if denied(src):
                warnings.append(f"denied: {src}")
                continue
            if spec.prefix == "v1-notes" and not filter_v1_notes_noise(src.name):
                continue
            # convert non-md tiny files
            try:
                raw = src.read_text(encoding="utf-8", errors="replace")
            except OSError as exc:
                warnings.append(f"read fail {src}: {exc}")
                continue
            if src.suffix == ".txt":
                raw = f"# {src.name}\n\n```\n{raw}\n```\n"
            name = stage_name(spec, src)
            write_staged(staged, str(src), raw, name, spec.category)

    warnings.extend(git_export_main(staged))
    warnings.extend(git_history_digest(staged))
    warnings.extend(grok_session_summaries(staged))

    # dedupe by staged name (last wins)
    by_name: dict[str, tuple[Path, str, str]] = {}
    for path, key, cat in staged:
        by_name[path.name] = (path, key, cat)
    staged = list(by_name.values())
    return staged, warnings


def write_sources_md(staged: list[tuple[Path, str, str]], warnings: list[str]) -> None:
    by_cat: dict[str, list[str]] = {}
    for path, _key, cat in staged:
        by_cat.setdefault(cat, []).append(path.name)
    lines = [
        "# Intended corpus v1 — SOURCES",
        "",
        f"Host: `{HOST}`",
        f"Assembled: {datetime.now(timezone.utc).isoformat()}",
        f"Stage: `{STAGE_DIR}`",
        f"Total files: **{len(staged)}**",
        "",
        "## Categories (intended mix)",
        "",
        "| Category | Count | What |",
        "|----------|------:|------|",
        "| project-handoffs | | Durable handoffs (MyAPI, aa-cli, main tip) |",
        "| project-documents | | Project docs, anchors, plans, AGENTS |",
        "| golden-briefs | | evals/golden_briefs from origin/main |",
        "| graphify / graphify-intent | | graphify-out + wayfinder cold-start pack |",
        "| agent-sessions | | Grok summary.json digests, Codex rollout summaries, Pi handoffs |",
        "| git-history | | Recent commit digests for key repos |",
        "| corpus-hot | | Wave-1 curated pack |",
        "| project-notes | | High-signal v1-notes (filtered) |",
        "",
        "## Counts this run",
        "",
    ]
    for cat in sorted(by_cat):
        lines.append(f"- **{cat}**: {len(by_cat[cat])}")
    lines += ["", "## Files", ""]
    for cat in sorted(by_cat):
        lines.append(f"### {cat}")
        for name in sorted(by_cat[cat]):
            lines.append(f"- `{name}`")
        lines.append("")
    if warnings:
        lines += ["## Warnings / notes", ""]
        for w in warnings[:80]:
            lines.append(f"- {w}")
    SOURCES_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    # also stage SOURCES itself into STAGE_DIR
    body = SOURCES_MD.read_text(encoding="utf-8")
    key = sha_key(str(SOURCES_MD), body)
    dest = STAGE_DIR / "intended-v1--SOURCES.md"
    dest.write_text(wrap(str(SOURCES_MD), body, dest.name, "corpus-hot", key), encoding="utf-8")


def load_manifest() -> dict[str, str]:
    if not MANIFEST_PATH.exists():
        return {}
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_manifest(m: dict[str, str]) -> None:
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(m, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def probe_khoj(base: str) -> str:
    req = urllib.request.Request(f"{base}/api/health", method="GET")
    with urllib.request.urlopen(req, timeout=8) as resp:
        if resp.status != 200:
            raise ConnectionError(f"health {resp.status}")
    return base


def index_batch(
    base: str,
    paths: list[Path],
    *,
    method: str,
    timeout: int = 600,
) -> int:
    """Multipart PUT/PATCH many files in one request.

    Khoj PUT = regenerate (wipes prior API content to the files in *this* call).
    Khoj PATCH = sync/merge. Never one-file PUT in a loop.
    """
    if not paths:
        return 200
    url = f"{base}/api/content?client=api"
    cmd = [
        "curl",
        "-sS",
        "-m",
        str(timeout),
        "-o",
        "/tmp/khoj_index_body.txt",
        "-w",
        "%{http_code}",
        "-X",
        method,
        url,
    ]
    for path in paths:
        cmd.extend(
            [
                "-F",
                f"files=@{path};filename={path.name};type=text/markdown",
            ]
        )
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout)
    try:
        return int(proc.stdout.strip())
    except ValueError as exc:
        raise RuntimeError(f"bad http code: {proc.stdout!r}") from exc


def index_staged(
    staged: list[tuple[Path, str, str]],
    force: bool = False,
    batch_size: int = 40,
) -> dict:
    base = probe_khoj(DEFAULT_KHOJ)
    manifest = load_manifest()
    # Prefer full restage of *all* staged files when force, else only changed.
    if force:
        to_upload = [(p, k) for p, k, _ in staged]
        skipped = 0
    else:
        to_upload = []
        skipped = 0
        for path, key, _cat in staged:
            if manifest.get(path.name) == key:
                skipped += 1
            else:
                to_upload.append((path, key))

    if not to_upload:
        return {
            "khoj_url": base,
            "indexed": 0,
            "skipped_unchanged": skipped,
            "failed": [],
            "to_upload": 0,
            "batches": 0,
        }

    # Priority order for first PUT batch (high-signal)
    pri_pat = re.compile(
        r"golden|brief|anchor|PROJECT|IMPLEMENTATION|wave1|semantic-graphify|"
        r"git-main--|gddp|myapi-status|STATUS|eval-bank|mcp-|intended-v1|"
        r"SOURCES|QUERIES|GAPS|handoff|CANONICAL|NODE-MAP|WAYFINDER",
        re.I,
    )
    to_upload.sort(key=lambda pk: (0 if pri_pat.search(pk[0].name) else 1, pk[0].name))

    failed: list[str] = []
    indexed = 0
    batches = 0
    paths_only = [p for p, _ in to_upload]

    # First batch PUT (regenerate core), remaining PATCH (merge).
    for i in range(0, len(paths_only), batch_size):
        chunk = paths_only[i : i + batch_size]
        method = "PUT" if i == 0 else "PATCH"
        log(f"  batch {batches + 1}: {method} {len(chunk)} files (offset {i})")
        try:
            code = index_batch(base, chunk, method=method, timeout=600)
        except Exception as exc:
            failed.append(f"batch@{i}:{exc}")
            log(f"  FAIL batch@{i}: {exc}")
            break
        if code not in (200, 201, 204):
            failed.append(f"batch@{i}:http={code}")
            log(f"  FAIL batch@{i} http={code}")
            break
        for path in chunk:
            # mark keys from staged list
            for p, k in to_upload:
                if p == path:
                    manifest[p.name] = k
                    break
        indexed += len(chunk)
        batches += 1
        time.sleep(1)

    save_manifest(manifest)
    return {
        "khoj_url": base,
        "indexed": indexed,
        "skipped_unchanged": skipped,
        "failed": failed,
        "to_upload": len(to_upload),
        "batches": batches,
        "note": "PUT first batch regenerates; PATCH merges rest",
    }


def run(dry_run: bool, index: bool, force: bool) -> int:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    RECEIPT_DIR.mkdir(parents=True, exist_ok=True)
    started = time.time()
    payload: dict = {
        "host": HOST,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "ok": False,
        "dry_run": dry_run,
        "index": index,
    }
    try:
        staged, warnings = stage_all()
        write_sources_md(staged, warnings)
        # re-count after SOURCES write
        staged_paths = sorted(STAGE_DIR.glob("*.md"))
        payload["staged_count"] = len(staged_paths)
        payload["warnings"] = warnings
        payload["stage_dir"] = str(STAGE_DIR)
        payload["categories"] = {}
        for _p, _k, cat in staged:
            payload["categories"][cat] = payload["categories"].get(cat, 0) + 1

        if len(staged_paths) < 10:
            raise RuntimeError(f"too few staged files: {len(staged_paths)}")

        log(f"STAGED {len(staged_paths)} files → {STAGE_DIR}")
        for cat, n in sorted(payload["categories"].items()):
            log(f"  {cat}: {n}")

        if dry_run or not index:
            payload["ok"] = True
            payload["message"] = "staged only" if not index else "dry"
            if not index and not dry_run:
                payload["message"] = "staged; pass --index to upload"
            payload["elapsed_s"] = round(time.time() - started, 2)
            LAST_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
            (RECEIPT_DIR / f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-stage.json").write_text(
                json.dumps(payload, indent=2) + "\n", encoding="utf-8"
            )
            log(f"OK stage-only count={len(staged_paths)} sources={SOURCES_MD}")
            return 0

        # rebuild staged list with keys from files for index
        manifest_list: list[tuple[Path, str, str]] = []
        for path in staged_paths:
            body = path.read_text(encoding="utf-8", errors="replace")
            # extract content_key if present
            m = re.search(r"content_key:\s*(\S+)", body)
            key = m.group(1) if m else sha_key(path.name, body)
            cat = "misc"
            m2 = re.search(r"category:\s*(\S+)", body)
            if m2:
                cat = m2.group(1)
            manifest_list.append((path, key, cat))

        result = index_staged(manifest_list, force=force)
        payload.update(result)
        if result["failed"]:
            raise RuntimeError(f"{len(result['failed'])} index failures: {result['failed'][:5]}")
        payload["ok"] = True
        payload["elapsed_s"] = round(time.time() - started, 2)
        payload["finished_at"] = datetime.now(timezone.utc).isoformat()
        LAST_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        (RECEIPT_DIR / f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-ok.json").write_text(
            json.dumps(payload, indent=2) + "\n", encoding="utf-8"
        )
        log(
            f"OK indexed={result['indexed']} skipped={result['skipped_unchanged']} "
            f"total_stage={len(staged_paths)}"
        )
        return 0
    except Exception as exc:
        payload["ok"] = False
        payload["error"] = f"{type(exc).__name__}: {exc}"
        payload["elapsed_s"] = round(time.time() - started, 2)
        LAST_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        log(f"FAIL {payload['error']}")
        return 1


def status() -> int:
    if not LAST_PATH.exists():
        print("NO RUN yet")
        return 2
    print(LAST_PATH.read_text(encoding="utf-8"))
    if STAGE_DIR.exists():
        print(f"stage_files={len(list(STAGE_DIR.glob('*.md')))}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="stage + SOURCES only")
    ap.add_argument("--index", action="store_true", help="PUT staged files into Khoj")
    ap.add_argument("--force", action="store_true", help="re-upload even if unchanged")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()
    if args.status:
        return status()
    return run(dry_run=args.dry_run, index=args.index, force=args.force)


if __name__ == "__main__":
    sys.exit(main())
