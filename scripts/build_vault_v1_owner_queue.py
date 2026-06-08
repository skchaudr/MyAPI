#!/usr/bin/env python3
"""Build a focused owner-pass queue for the generated vault-v1.0 corpus.

This is a review scaffold for Pass B. It scans generated Markdown notes,
flags notes that violate the minimal vault-v1.0 metadata floor, and writes a
triage-compatible JSON queue plus a Markdown summary.

It intentionally does not apply V4 Obsidian schema rules. In particular, it
flags experimental fields that handoff 012 says not to add yet.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import yaml

DEFAULT_VAULT = Path("/Users/saboor/repos/MyAPI/corpus_v1/vault-v1.0")

REQUIRED_FIELDS = {
    "normalization_version",
    "source_kind",
    "source_id",
    "source_path",
    "captured_at",
    "occurred_at",
    "concepts",
    "tags",
    "derived_from",
}

VALID_NOTE_ROLES = {
    "anchor",
    "current_state",
    "work_queue",
    "timeline_event",
    "artifact_summary",
    "raw_pointer",
}

FORBIDDEN_FIELDS = {
    "project",
    "area",
    "status",
    "confidence",
    "canonical",
    "supersedes",
}

LIST_FIELDS = {"concepts", "tags", "derived_from"}
SKIP_DIRS = {".obsidian", "_reports", "_manifests"}
SECRET_PATTERNS = (
    re.compile(r"sk-[A-Za-z0-9_-]{16,}"),
    re.compile(r"AIza[0-9A-Za-z_-]{16,}"),
    re.compile(r"[A-Za-z0-9_-]{40,}"),
)


@dataclass
class QueueItem:
    path: str
    confidence: str
    destination_folder: str = ""
    reasons: list[str] = field(default_factory=list)
    review_needed: list[str] = field(default_factory=list)
    current: dict[str, Any] = field(default_factory=dict)
    suggested: dict[str, Any] = field(default_factory=dict)
    duplicate_group: str | None = None


def split_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    try:
        parsed = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def looks_like_secret(value: Any) -> bool:
    return any(pattern.search(str(value)) for pattern in SECRET_PATTERNS)


def duplicate_key(path: Path) -> str:
    key = path.stem.lower().replace("_", "-")
    key = re.sub(r"\s+", "-", key)
    key = re.sub(r"-+", "-", key)
    return key.strip("-")


def should_scan(path: Path, vault_root: Path) -> bool:
    rel_parts = path.relative_to(vault_root).parts
    return not any(part in SKIP_DIRS for part in rel_parts)


def expected_role_from_path(path: Path, vault_root: Path) -> str | None:
    parts = path.relative_to(vault_root).parts
    if not parts:
        return None
    top = parts[0]
    name = path.stem.lower()
    if top == "50-timeline":
        return "timeline_event"
    if top == "90-raw-provenance":
        return "raw_pointer"
    if "current state" in name:
        return "current_state"
    if "work queue" in name:
        return "work_queue"
    if "anchor" in name or "index" in name:
        return "anchor"
    if top in {"60-sessions-and-conversations", "70-artifacts-and-reference"}:
        return "artifact_summary"
    return None


def issues_for(path: Path, vault_root: Path) -> QueueItem | None:
    fm = split_frontmatter(path)
    rel = str(path.relative_to(vault_root))
    review_needed: list[str] = []
    reasons: list[str] = []
    suggested: dict[str, Any] = {}

    if not fm:
        review_needed.append("frontmatter missing or invalid")

    missing = sorted(field for field in REQUIRED_FIELDS if field not in fm)
    for field_name in missing:
        review_needed.append(f"missing required field `{field_name}`")

    if fm.get("normalization_version") not in {None, "vault-v1.0"}:
        suggested["normalization_version"] = "vault-v1.0"
        review_needed.append("normalization_version must be `vault-v1.0`")

    for field_name in sorted(FORBIDDEN_FIELDS & set(fm)):
        review_needed.append(f"forbidden experimental field present `{field_name}`")

    for field_name in sorted(LIST_FIELDS & set(fm)):
        if not isinstance(fm.get(field_name), list):
            suggested[field_name] = as_list(fm.get(field_name))
            review_needed.append(f"`{field_name}` must be a list")
        if any(looks_like_secret(item) for item in as_list(fm.get(field_name))):
            review_needed.append(f"`{field_name}` contains secret-shaped text")

    note_role = fm.get("note_role")
    if note_role and note_role not in VALID_NOTE_ROLES:
        review_needed.append(f"invalid note_role `{note_role}`")

    expected_role = expected_role_from_path(path, vault_root)
    if expected_role and not note_role:
        suggested["note_role"] = expected_role
        review_needed.append(f"note_role likely needed: `{expected_role}`")

    if note_role == "timeline_event" and not fm.get("occurred_at"):
        review_needed.append("timeline_event needs occurred_at")

    if note_role in {"artifact_summary", "raw_pointer"} and not fm.get("source_path"):
        review_needed.append(f"{note_role} needs source_path")

    if "02 Areas/Confidential" in str(fm.get("source_path", "")):
        review_needed.append("source_path references confidential Obsidian path")

    if not review_needed:
        return None

    confidence = "review"
    if all(issue.startswith("note_role likely needed") for issue in review_needed):
        confidence = "medium"

    current = {
        key: fm.get(key)
        for key in sorted(REQUIRED_FIELDS | {"note_role"} | FORBIDDEN_FIELDS)
        if key in fm
    }
    reasons.append("vault-v1.0 owner pass needed")
    return QueueItem(
        path=rel,
        confidence=confidence,
        reasons=reasons,
        review_needed=review_needed,
        current=current,
        suggested=suggested,
    )


def choose_duplicate_keeper(items: list[QueueItem]) -> QueueItem:
    def score(item: QueueItem) -> tuple[int, int, str]:
        preferred = 1 if item.path.startswith(("20-projects/", "50-timeline/")) else 0
        return (preferred, -len(item.review_needed), item.path)

    return sorted(items, key=score, reverse=True)[0]


def build_queue(vault_root: Path, subdir: str, collapse_duplicates: bool) -> tuple[list[QueueItem], dict[str, list[QueueItem]]]:
    scan_root = vault_root / subdir
    items = [
        item
        for path in sorted(scan_root.rglob("*.md"))
        if should_scan(path, vault_root) and (item := issues_for(path, vault_root)) is not None
    ]

    groups: dict[str, list[QueueItem]] = defaultdict(list)
    for item in items:
        groups[duplicate_key(Path(item.path))].append(item)

    duplicate_groups = {key: vals for key, vals in groups.items() if len(vals) > 1}
    if not collapse_duplicates:
        return items, duplicate_groups

    queue: list[QueueItem] = []
    for key, vals in groups.items():
        if len(vals) == 1:
            queue.append(vals[0])
            continue
        keeper = choose_duplicate_keeper(vals)
        keeper.duplicate_group = key
        keeper.review_needed.append(f"duplicate cluster collapsed for owner pass: {len(vals)} files")
        queue.append(keeper)

    return sorted(queue, key=lambda item: item.path), duplicate_groups


def write_markdown(path: Path, queue: list[QueueItem], duplicate_groups: dict[str, list[QueueItem]], vault_root: Path, subdir: str) -> None:
    lines = [
        "# Vault V1 Owner Queue",
        "",
        f"Vault root: `{vault_root}`",
        f"Subdir: `{subdir}`",
        "",
        "## Summary",
        "",
        f"- Queue items: {len(queue)}",
        f"- Duplicate clusters: {len(duplicate_groups)}",
        "",
        "## Queue",
        "",
    ]
    for item in queue:
        lines.extend([
            f"### {item.path}",
            "",
            f"- Confidence: `{item.confidence}`",
            f"- Review needed: {'; '.join(item.review_needed)}",
            "",
        ])

    if duplicate_groups:
        lines.extend(["## Duplicate Clusters", ""])
        for key, vals in sorted(duplicate_groups.items()):
            lines.append(f"### {key}")
            for item in vals:
                lines.append(f"- `{item.path}`")
            lines.append("")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault-root", default=str(DEFAULT_VAULT))
    parser.add_argument("--subdir", default=".")
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-md", required=True)
    parser.add_argument("--include-duplicates", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    vault_root = Path(args.vault_root).expanduser()
    queue, duplicate_groups = build_queue(
        vault_root=vault_root,
        subdir=args.subdir,
        collapse_duplicates=not args.include_duplicates,
    )
    out_json = Path(args.out_json)
    out_md = Path(args.out_md)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps([asdict(item) for item in queue], indent=2), encoding="utf-8")
    write_markdown(out_md, queue, duplicate_groups, vault_root, args.subdir)
    print(f"queue_items={len(queue)}")
    print(f"duplicate_clusters={len(duplicate_groups)}")
    print(f"json={out_json}")
    print(f"markdown={out_md}")


if __name__ == "__main__":
    main()
