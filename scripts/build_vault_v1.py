#!/usr/bin/env python3
"""Fast Obsidian vault materializer for corpus v1.0.

This intentionally favors "visible and searchable now" over rich enrichment.
It reads the frozen raw v1.0 selected corpus and writes a derived Obsidian vault
with source-family folders, provenance frontmatter, manifests, and reports.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
RAW_ROOT = REPO_ROOT / "corpus_v1" / "raw-v1.0"
VAULT_ROOT = REPO_ROOT / "corpus_v1" / "vault-v1.0"

NORMALIZATION_VERSION = "vault-v1.0-fast"
CAPTURED_AT = "2026-06-01"
GENERATED_BY = "scripts/build_vault_v1.py"


def repo_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def slugify(value: str, *, max_len: int = 70) -> str:
    value = value.strip().lower()
    value = value.encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return (value or "untitled")[:max_len].strip("-") or "untitled"


def short_hash(value: str, n: int = 10) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:n]


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def split_frontmatter(text: str) -> tuple[dict[str, Any], str, bool]:
    if not text.startswith("---"):
        return {}, text, False
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text, False
    try:
        fm = yaml.safe_load(parts[1]) or {}
        if not isinstance(fm, dict):
            return {}, text, False
        return fm, parts[2].lstrip("\n"), True
    except yaml.YAMLError:
        return {}, text, False


def dump_frontmatter(fm: dict[str, Any]) -> str:
    return yaml.safe_dump(
        fm,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
        width=120,
    ).strip()


def write_generated_note(path: Path, fm: dict[str, Any], body: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    fm = dict(fm)
    fm.setdefault("normalization_version", NORMALIZATION_VERSION)
    fm.setdefault("generated_by", GENERATED_BY)
    content = f"---\n{dump_frontmatter(fm)}\n---\n\n{body.rstrip()}\n"
    content = content.replace("\r\n", "\n").replace("\r", "\n")
    if path.exists():
        existing = read_text(path)
        if existing == content:
            return False
        if (
            f"generated_by: {GENERATED_BY}" not in existing
            and not existing.startswith("# Corpus v1.0 Vault Build Summary")
        ):
            raise RuntimeError(f"Refusing to overwrite non-generated note: {path}")
    path.write_text(content, encoding="utf-8")
    return True


def extract_date(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value)
    m = re.search(r"(\d{4})[-/](\d{1,2})[-/](\d{1,2})", text)
    if not m:
        return None
    y, mo, d = m.groups()
    return f"{int(y):04d}-{int(mo):02d}-{int(d):02d}"


def find_note_created_date(fm: dict[str, Any], body: str) -> str | None:
    for key in ("created_at", "created", "date"):
        date = extract_date(fm.get(key))
        if date:
            return date
    for line in body.splitlines()[:80]:
        m = re.match(r"^(created_at|created|date):\s*(.+)$", line.strip(), re.I)
        if not m:
            continue
        date = extract_date(m.group(2))
        if date:
            return date
    return None


def iso_from_unix(value: Any) -> str | None:
    if value in (None, ""):
        return None
    try:
        return datetime.fromtimestamp(float(value), timezone.utc).isoformat()
    except (TypeError, ValueError, OSError):
        return None


def date_prefix(iso_value: str | None) -> str:
    if not iso_value:
        return "unknown-date"
    date = extract_date(iso_value)
    return date or "unknown-date"


def markdown_escape(value: Any) -> str:
    text = "" if value is None else str(value)
    return text.replace("\n", " ").strip()


def text_from_content_blocks(content: Any) -> str:
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    parts: list[str] = []
    for block in content:
        if isinstance(block, str):
            parts.append(block)
        elif isinstance(block, dict):
            if block.get("type") in {"text", "input_text", "output_text"}:
                parts.append(str(block.get("text", "")))
            elif "content" in block:
                parts.append(text_from_content_blocks(block.get("content")))
    return "\n".join(p for p in parts if p).strip()


def truncate(text: str, limit: int = 12000) -> str:
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + f"\n\n[truncated {len(text) - limit} chars]"


class VaultBuilder:
    def __init__(self, raw_root: Path, vault_root: Path, apply: bool) -> None:
        self.raw_root = raw_root
        self.vault_root = vault_root
        self.apply = apply
        self.selected_root = raw_root / "selected"
        self.inventory_rows: list[dict[str, Any]] = []
        self.build_rows: list[dict[str, Any]] = []
        self.failures: list[dict[str, Any]] = []
        self.counts: Counter[str] = Counter()
        self.writes = 0

    def run(self) -> int:
        if not self.selected_root.is_dir():
            print(f"Missing selected corpus: {self.selected_root}", file=sys.stderr)
            return 2
        self.scaffold()
        self.build_inventory()
        self.materialize_obsidian()
        self.materialize_chatgpt()
        self.materialize_claude_web()
        self.materialize_claude_code()
        self.materialize_codex()
        self.write_indexes_and_reports()
        self.validate()
        print(f"vault_root={self.vault_root}")
        print(f"inventory_rows={len(self.inventory_rows)}")
        print(f"generated_notes={len(self.build_rows)}")
        print(f"new_or_changed_notes={self.writes}")
        print(f"failures={len(self.failures)}")
        return 0 if not self.failures else 1

    def scaffold(self) -> None:
        folders = [
            "00-index",
            "10-current-state",
            "20-projects",
            "30-systems-and-workflows",
            "40-decisions-and-trajectories",
            "50-timeline",
            "60-sessions-and-conversations/chatgpt",
            "60-sessions-and-conversations/claude-web",
            "60-sessions-and-conversations/claude-code",
            "60-sessions-and-conversations/codex",
            "70-artifacts-and-reference/claude-code-support",
            "80-candidates/obsidian",
            "90-raw-provenance",
            "_manifests",
            "_reports",
        ]
        if not self.apply:
            return
        for folder in folders:
            (self.vault_root / folder).mkdir(parents=True, exist_ok=True)

    def build_inventory(self) -> None:
        for path in sorted(self.selected_root.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(self.selected_root)
            source_kind = self.classify_source(rel)
            row = {
                "source_kind": source_kind,
                "source_path": repo_rel(path),
                "selected_rel_path": str(rel),
                "size_bytes": path.stat().st_size,
                "sha256": file_sha256(path),
            }
            self.inventory_rows.append(row)
            self.counts[f"inventory:{source_kind}"] += 1

    def classify_source(self, rel: Path) -> str:
        parts = rel.parts
        if parts[:1] == ("obsidian-SSD",):
            return "obsidian"
        if parts[:1] == ("chatgpt",):
            return "chatgpt"
        if parts[:1] == ("claude-web",):
            return "claude_web"
        if parts[:2] == ("cli", "claude-code-mac"):
            if rel.suffix == ".jsonl":
                return "claude_code_session"
            return "claude_code_support"
        if parts[:2] == ("cli", "codex-mac"):
            return "codex_session"
        return "unknown"

    def record_build(
        self,
        *,
        source_path: Path,
        output_path: Path,
        source_kind: str,
        note_role: str,
        title: str,
    ) -> None:
        self.build_rows.append({
            "source_kind": source_kind,
            "note_role": note_role,
            "title": title,
            "source_path": repo_rel(source_path),
            "output_path": repo_rel(output_path),
        })
        self.counts[f"generated:{source_kind}"] += 1
        self.counts[f"role:{note_role}"] += 1

    def record_failure(self, source_path: Path, source_kind: str, error: str) -> None:
        self.failures.append({
            "source_kind": source_kind,
            "source_path": repo_rel(source_path),
            "error": error,
        })
        self.counts[f"failure:{source_kind}"] += 1

    def note_write(self, path: Path, fm: dict[str, Any], body: str) -> None:
        if not self.apply:
            return
        if write_generated_note(path, fm, body):
            self.writes += 1

    def provenance_fm(
        self,
        source_path: Path,
        source_kind: str,
        source_id: str,
        *,
        occurred_at: str | None = None,
        title: str | None = None,
        note_role: str | None = None,
    ) -> dict[str, Any]:
        fm: dict[str, Any] = {
            "normalization_version": NORMALIZATION_VERSION,
            "generated_by": GENERATED_BY,
            "source_kind": source_kind,
            "source_id": source_id,
            "source_path": repo_rel(source_path),
            "captured_at": CAPTURED_AT,
            "concepts": [],
            "tags": [],
        }
        if title:
            fm["title"] = title
        if occurred_at:
            fm["occurred_at"] = occurred_at
        if note_role:
            fm["note_role"] = note_role
        return fm

    def materialize_obsidian(self) -> None:
        root = self.selected_root / "obsidian-SSD"
        if not root.is_dir():
            return
        for source_path in sorted(root.rglob("*.md")):
            rel = source_path.relative_to(root)
            try:
                text = read_text(source_path)
                existing_fm, body, parsed = split_frontmatter(text)
                source_id = short_hash(str(rel))
                occurred_at = find_note_created_date(existing_fm, body)
                fm = dict(existing_fm) if parsed else {}
                generated = self.provenance_fm(
                    source_path,
                    "obsidian",
                    source_id,
                    occurred_at=occurred_at,
                    title=source_path.stem,
                    note_role="source_note",
                )
                for key, value in generated.items():
                    fm.setdefault(key, value)
                fm.setdefault("original_vault_path", str(rel))
                fm.setdefault("concepts", [])
                fm.setdefault("tags", existing_fm.get("tags", []))
                if not parsed and text.startswith("---"):
                    fm.setdefault("frontmatter_warning", "source frontmatter could not be parsed")
                    body = text
                out_path = self.vault_root / "80-candidates" / "obsidian" / rel
                self.note_write(out_path, fm, body)
                self.record_build(
                    source_path=source_path,
                    output_path=out_path,
                    source_kind="obsidian",
                    note_role="source_note",
                    title=source_path.stem,
                )
            except Exception as exc:
                self.record_failure(source_path, "obsidian", str(exc))

    def materialize_chatgpt(self) -> None:
        from context_refinery.adapters.chatgpt import parse_chatgpt_conversation

        path = self.selected_root / "chatgpt" / "conversations-2026-04-22-to-2026-05-22.json"
        if not path.exists():
            return
        conversations = json.loads(read_text(path))
        for conv in conversations:
            try:
                doc = parse_chatgpt_conversation(conv)
                conv_id = str(doc.get("id") or conv.get("conversation_id") or short_hash(json.dumps(conv, sort_keys=True)))
                title = str(doc.get("title") or "Untitled Conversation")
                created_at = doc.get("timestamps", {}).get("created_at")
                updated_at = doc.get("timestamps", {}).get("updated_at")
                prefix = date_prefix(created_at)
                filename = f"{prefix} - {slugify(title)} - {conv_id[:8]}-{short_hash(conv_id)}.md"
                out_path = self.vault_root / "60-sessions-and-conversations" / "chatgpt" / filename
                body = self.render_conversation_body(
                    title=title,
                    source_label="ChatGPT",
                    source_path=path,
                    source_id=conv_id,
                    created_at=created_at,
                    updated_at=updated_at,
                    markdown=doc.get("content", {}).get("cleaned_markdown", ""),
                )
                fm = self.provenance_fm(
                    path,
                    "chatgpt",
                    conv_id,
                    occurred_at=created_at,
                    title=title,
                    note_role="conversation",
                )
                fm["updated_at"] = updated_at
                self.note_write(out_path, fm, body)
                self.record_build(
                    source_path=path,
                    output_path=out_path,
                    source_kind="chatgpt",
                    note_role="conversation",
                    title=title,
                )
            except Exception as exc:
                self.record_failure(path, "chatgpt", str(exc))

    def materialize_claude_web(self) -> None:
        from context_refinery.adapters.claude import parse_claude_conversation

        path = self.selected_root / "claude-web" / "conversations-2026-04-22-to-2026-05-22.json"
        if not path.exists():
            return
        conversations = json.loads(read_text(path))
        for conv in conversations:
            try:
                doc = parse_claude_conversation(conv)
                conv_id = str(doc.get("id") or conv.get("uuid") or short_hash(json.dumps(conv, sort_keys=True)))
                title = str(doc.get("title") or "Untitled Conversation")
                created_at = doc.get("timestamps", {}).get("created_at")
                updated_at = doc.get("timestamps", {}).get("updated_at")
                prefix = date_prefix(created_at)
                filename = f"{prefix} - {slugify(title)} - {conv_id[:8]}-{short_hash(conv_id)}.md"
                out_path = self.vault_root / "60-sessions-and-conversations" / "claude-web" / filename
                body = self.render_conversation_body(
                    title=title,
                    source_label="Claude Web",
                    source_path=path,
                    source_id=conv_id,
                    created_at=created_at,
                    updated_at=updated_at,
                    markdown=doc.get("content", {}).get("cleaned_markdown", ""),
                )
                fm = self.provenance_fm(
                    path,
                    "claude_web",
                    conv_id,
                    occurred_at=created_at,
                    title=title,
                    note_role="conversation",
                )
                fm["updated_at"] = updated_at
                self.note_write(out_path, fm, body)
                self.record_build(
                    source_path=path,
                    output_path=out_path,
                    source_kind="claude_web",
                    note_role="conversation",
                    title=title,
                )
            except Exception as exc:
                self.record_failure(path, "claude_web", str(exc))

    def render_conversation_body(
        self,
        *,
        title: str,
        source_label: str,
        source_path: Path,
        source_id: str,
        created_at: str | None,
        updated_at: str | None,
        markdown: str,
    ) -> str:
        return "\n".join([
            f"# {title}",
            "",
            "## Conversation Identity",
            f"- Source: {source_label}",
            f"- Source id: `{source_id}`",
            f"- Created: {markdown_escape(created_at)}",
            f"- Updated: {markdown_escape(updated_at)}",
            "",
            "## Provenance",
            f"- Raw source: `{repo_rel(source_path)}`",
            "",
            "## Raw Conversation",
            markdown.rstrip() or "_No text extracted._",
        ])

    def materialize_claude_code(self) -> None:
        from context_refinery.adapters.claude_code import parse_claude_session

        root = self.selected_root / "cli" / "claude-code-mac"
        if not root.is_dir():
            return
        for source_path in sorted(root.rglob("*.jsonl")):
            rel = source_path.relative_to(root)
            is_subagent = "subagents" in rel.parts
            source_kind = "claude_code_subagent" if is_subagent else "claude_code_session"
            try:
                doc = parse_claude_session(str(source_path))
                session_id = str(doc.get("id") or source_path.stem)
                title = str(doc.get("title") or source_path.stem)
                created_at = doc.get("timestamps", {}).get("created_at")
                updated_at = doc.get("timestamps", {}).get("updated_at")
                prefix = date_prefix(created_at)
                folder = "subagents" if is_subagent else "sessions"
                filename = f"{prefix} - {slugify(title)} - {session_id[:8]}-{short_hash(str(rel))}.md"
                out_path = self.vault_root / "60-sessions-and-conversations" / "claude-code" / folder / filename
                provenance = doc.get("provenance", {})
                body = "\n".join([
                    f"# {title}",
                    "",
                    "## Session Identity",
                    f"- Source: Claude Code",
                    f"- Session id: `{session_id}`",
                    f"- Created: {markdown_escape(created_at)}",
                    f"- Updated: {markdown_escape(updated_at)}",
                    f"- CWD: `{markdown_escape(provenance.get('cwd'))}`",
                    f"- Git branch: `{markdown_escape(provenance.get('git_branch'))}`",
                    "",
                    "## Provenance",
                    f"- Raw source: `{repo_rel(source_path)}`",
                    "",
                    "## Session Text",
                    doc.get("content", {}).get("cleaned_markdown", "").rstrip() or "_No text extracted._",
                ])
                fm = self.provenance_fm(
                    source_path,
                    source_kind,
                    session_id,
                    occurred_at=created_at,
                    title=title,
                    note_role="cli_session",
                )
                fm["updated_at"] = updated_at
                fm["cwd"] = provenance.get("cwd")
                fm["git_branch"] = provenance.get("git_branch")
                self.note_write(out_path, fm, body)
                self.record_build(
                    source_path=source_path,
                    output_path=out_path,
                    source_kind=source_kind,
                    note_role="cli_session",
                    title=title,
                )
            except Exception as exc:
                self.record_failure(source_path, source_kind, str(exc))

        for source_path in sorted(p for p in root.rglob("*") if p.is_file() and p.suffix != ".jsonl"):
            self.materialize_support_file(source_path, root, "claude_code_support")

    def materialize_support_file(self, source_path: Path, root: Path, source_kind: str) -> None:
        rel = source_path.relative_to(root)
        try:
            text = read_text(source_path)
            title = source_path.stem
            out_rel = rel if source_path.suffix == ".md" else Path(str(rel) + ".md")
            out_path = self.vault_root / "70-artifacts-and-reference" / "claude-code-support" / out_rel
            source_id = short_hash(str(rel))
            if source_path.suffix == ".md":
                existing_fm, body, parsed = split_frontmatter(text)
                fm = dict(existing_fm) if parsed else {}
                for key, value in self.provenance_fm(
                    source_path,
                    source_kind,
                    source_id,
                    title=title,
                    note_role="support_file",
                ).items():
                    fm.setdefault(key, value)
                if not parsed and text.startswith("---"):
                    fm.setdefault("frontmatter_warning", "source frontmatter could not be parsed")
                    body = text
            else:
                fm = self.provenance_fm(
                    source_path,
                    source_kind,
                    source_id,
                    title=title,
                    note_role="support_file",
                )
                body = "\n".join([
                    f"# {title}",
                    "",
                    "## Provenance",
                    f"- Raw source: `{repo_rel(source_path)}`",
                    "",
                    "## Raw Text",
                    "```text",
                    truncate(text, 40000),
                    "```",
                ])
            self.note_write(out_path, fm, body)
            self.record_build(
                source_path=source_path,
                output_path=out_path,
                source_kind=source_kind,
                note_role="support_file",
                title=title,
            )
        except Exception as exc:
            self.record_failure(source_path, source_kind, str(exc))

    def materialize_codex(self) -> None:
        root = self.selected_root / "cli" / "codex-mac"
        if not root.is_dir():
            return
        for source_path in sorted(root.rglob("*.jsonl")):
            try:
                parsed = self.parse_codex_rollout(source_path)
                session_id = parsed["session_id"]
                title = parsed["title"]
                created_at = parsed["created_at"]
                prefix = date_prefix(created_at)
                filename = f"{prefix} - {slugify(title)} - {session_id[:8]}-{short_hash(repo_rel(source_path))}.md"
                out_path = self.vault_root / "60-sessions-and-conversations" / "codex" / filename
                body = "\n".join([
                    f"# {title}",
                    "",
                    "## Session Identity",
                    "- Source: Codex",
                    f"- Session id: `{session_id}`",
                    f"- Created: {markdown_escape(created_at)}",
                    f"- CWD: `{markdown_escape(parsed.get('cwd'))}`",
                    f"- Model provider: `{markdown_escape(parsed.get('model_provider'))}`",
                    "",
                    "## Provenance",
                    f"- Raw source: `{repo_rel(source_path)}`",
                    "",
                    "## Session Text",
                    parsed["markdown"].rstrip() or "_No text extracted._",
                ])
                fm = self.provenance_fm(
                    source_path,
                    "codex_session",
                    session_id,
                    occurred_at=created_at,
                    title=title,
                    note_role="cli_session",
                )
                fm["cwd"] = parsed.get("cwd")
                fm["model_provider"] = parsed.get("model_provider")
                self.note_write(out_path, fm, body)
                self.record_build(
                    source_path=source_path,
                    output_path=out_path,
                    source_kind="codex_session",
                    note_role="cli_session",
                    title=title,
                )
            except Exception as exc:
                self.record_failure(source_path, "codex_session", str(exc))

    def parse_codex_rollout(self, source_path: Path) -> dict[str, Any]:
        session_id = source_path.stem
        created_at = None
        cwd = None
        model_provider = None
        chunks: list[str] = []
        first_user = None
        tool_count = 0
        with source_path.open(encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    continue
                item_type = obj.get("type")
                payload = obj.get("payload") or {}
                if item_type == "session_meta":
                    meta = payload
                    session_id = str(meta.get("id") or session_id)
                    created_at = meta.get("timestamp") or obj.get("timestamp") or created_at
                    cwd = meta.get("cwd") or cwd
                    model_provider = meta.get("model_provider") or model_provider
                    continue
                if item_type == "response_item":
                    ptype = payload.get("type")
                    if ptype == "message":
                        role = payload.get("role", "unknown")
                        if role in {"developer", "system"}:
                            continue
                        text = text_from_content_blocks(payload.get("content"))
                        if not text:
                            continue
                        if role == "user" and first_user is None:
                            first_user = text.strip().splitlines()[0][:120]
                        chunks.append(f"### {role.title()}\n\n{truncate(text, 24000)}")
                    elif ptype == "function_call":
                        tool_count += 1
                        name = payload.get("name") or "tool"
                        chunks.append(f"### Tool Call: {name}\n\n`{markdown_escape(payload.get('call_id'))}`")
                    elif ptype == "function_call_output":
                        output = str(payload.get("output") or "")
                        if output:
                            chunks.append(f"### Tool Output\n\n```text\n{truncate(output, 4000)}\n```")
                elif item_type == "event_msg" and payload.get("type") == "user_message":
                    msg = payload.get("message")
                    if msg and first_user is None:
                        first_user = str(msg).strip().splitlines()[0][:120]
        title = first_user or cwd or source_path.stem
        if tool_count:
            chunks.insert(0, f"### Tool Call Count\n\n{tool_count}")
        return {
            "session_id": session_id,
            "title": title,
            "created_at": created_at,
            "cwd": cwd,
            "model_provider": model_provider,
            "markdown": "\n\n".join(chunks),
        }

    def write_indexes_and_reports(self) -> None:
        if not self.apply:
            return
        self.write_home()
        self.write_source_counts()
        self.write_project_stubs()
        self.write_jsonl(self.vault_root / "_manifests" / "inventory.jsonl", self.inventory_rows)
        self.write_jsonl(self.vault_root / "_manifests" / "build-manifest.jsonl", self.build_rows)
        self.write_jsonl(self.vault_root / "_reports" / "parse-failures.jsonl", self.failures)
        summary = self.render_summary()
        summary_fm = {
            "normalization_version": NORMALIZATION_VERSION,
            "generated_by": GENERATED_BY,
            "note_role": "build_report",
            "tags": ["corpus-v1", "report"],
        }
        self.note_write(self.vault_root / "_reports" / "build-summary.md", summary_fm, summary)
        self.note_write(self.vault_root / "README.md", summary_fm, summary)

    def write_jsonl(self, path: Path, rows: list[dict[str, Any]]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
            encoding="utf-8",
        )

    def write_home(self) -> None:
        fm = {
            "normalization_version": NORMALIZATION_VERSION,
            "generated_by": GENERATED_BY,
            "note_role": "index",
            "tags": ["corpus-v1", "home"],
        }
        body = """# Corpus v1.0 Home

## Start Here

- [[Source Counts]]
- [[../_reports/build-summary|Build Summary]]
- [[../80-candidates/obsidian|Obsidian source notes]]
- [[../60-sessions-and-conversations/chatgpt|ChatGPT conversations]]
- [[../60-sessions-and-conversations/claude-web|Claude web conversations]]
- [[../60-sessions-and-conversations/claude-code|Claude Code sessions]]
- [[../60-sessions-and-conversations/codex|Codex sessions]]

## Purpose

This vault is the fast Obsidian-visible materialization of the selected corpus
v1.0 raw bundle. It is meant to be browsed, searched, inspected, and later
indexed by Khoj from the shaped Markdown substrate.
"""
        self.note_write(self.vault_root / "00-index" / "Home.md", fm, body)

    def write_source_counts(self) -> None:
        fm = {
            "normalization_version": NORMALIZATION_VERSION,
            "generated_by": GENERATED_BY,
            "note_role": "index",
            "tags": ["corpus-v1", "counts"],
        }
        rows = "\n".join(
            f"| {key} | {value} |" for key, value in sorted(self.counts.items())
        )
        body = f"""# Source Counts

| Count | Value |
| --- | ---: |
{rows}
"""
        self.note_write(self.vault_root / "00-index" / "Source Counts.md", fm, body)

    def write_project_stubs(self) -> None:
        for project in ("MyAPI", "GDDP", "DevInfra", "Vault Normalization"):
            folder = self.vault_root / "20-projects" / project
            body = f"""# {project}

## Current State

- [?] Populate this from the first enrichment pass.

## Useful Searches

- Search this vault for `{project}`
- Search sessions and conversations for `{project}`

## Provenance

This is a scaffold note generated before enrichment.
"""
            fm = {
                "normalization_version": NORMALIZATION_VERSION,
                "generated_by": GENERATED_BY,
                "note_role": "project_index",
                "tags": ["corpus-v1", "project"],
                "concepts": [project],
            }
            self.note_write(folder / f"{project} Index.md", fm, body)

    def render_summary(self) -> str:
        counts = "\n".join(
            f"| {key} | {value} |" for key, value in sorted(self.counts.items())
        )
        return f"""# Corpus v1.0 Vault Build Summary

Captured at: `{CAPTURED_AT}`

## Paths

- Raw root: `{repo_rel(self.raw_root)}`
- Vault root: `{repo_rel(self.vault_root)}`
- Inventory: `corpus_v1/vault-v1.0/_manifests/inventory.jsonl`
- Build manifest: `corpus_v1/vault-v1.0/_manifests/build-manifest.jsonl`
- Parse failures: `corpus_v1/vault-v1.0/_reports/parse-failures.jsonl`

## Counts

| Count | Value |
| --- | ---: |
| inventory rows | {len(self.inventory_rows)} |
| generated notes | {len(self.build_rows)} |
| failures | {len(self.failures)} |

## Detailed Counts

| Count | Value |
| --- | ---: |
{counts}

## Open In Obsidian

Open this folder as a vault:

```text
{self.vault_root}
```

This is the fast visible substrate. Khoj/API indexing should consume an
allowlisted shaped slice of this vault later.
"""

    def validate(self) -> None:
        if not self.apply:
            return
        md_files = sorted(self.vault_root.rglob("*.md"))
        parse_errors = []
        for path in md_files:
            text = read_text(path)
            fm, _, parsed = split_frontmatter(text)
            if not parsed or not isinstance(fm, dict):
                parse_errors.append(repo_rel(path))
        report = {
            "markdown_files": len(md_files),
            "frontmatter_parse_errors": parse_errors,
            "build_manifest_rows": len(self.build_rows),
            "inventory_rows": len(self.inventory_rows),
        }
        (self.vault_root / "_reports" / "validation-summary.json").write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        self.counts["validation:markdown_files"] = len(md_files)
        self.counts["validation:frontmatter_parse_errors"] = len(parse_errors)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cmd", nargs="?", choices=["all"], default="all")
    parser.add_argument("--raw-root", type=Path, default=RAW_ROOT)
    parser.add_argument("--vault-root", type=Path, default=VAULT_ROOT)
    parser.add_argument("--apply", action="store_true", help="Write the derived vault")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    builder = VaultBuilder(args.raw_root.resolve(), args.vault_root.resolve(), args.apply)
    return builder.run()


if __name__ == "__main__":
    raise SystemExit(main())
