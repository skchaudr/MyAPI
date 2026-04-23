#!/usr/bin/env python3
"""Build a focused V4 owner-pass queue from current vault state.

This is for recurring folder maintenance after the bulk normalizer has run.
It scans a target folder, keeps only notes that still need owner attention,
and writes a triage-compatible JSON queue plus a Markdown summary.
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

VALID_TYPES = {"project", "area", "resource", "concept", "event", "periodic"}
VALID_STATUSES = {"active", "backlog", "blocked", "done"}
TAG_PREFIXES = ("topic/", "tool/", "lang/", "scope/")
SECRET_PATTERNS = (
    re.compile(r"sk-[A-Za-z0-9_-]{16,}"),
    re.compile(r"AIza[0-9A-Za-z_-]{16,}"),
    re.compile(r"[A-Za-z0-9_-]{32,}"),
)

DEFAULT_VAULT = Path("/Users/saboor/obsidian/SoloDeveloper")


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


def is_wikilink(value: Any) -> bool:
    text = str(value).strip()
    return text.startswith("[[") and text.endswith("]]")


def valid_tag(value: Any) -> bool:
    text = str(value).strip()
    return text.startswith(TAG_PREFIXES)


def duplicate_key(path: Path) -> str:
    key = path.stem.lower()
    key = key.replace("_", "-")
    key = re.sub(r"\bmy[- ]?neovim\b", "neovim", key)
    key = re.sub(r"\s+", "-", key)
    key = re.sub(r"-+", "-", key)
    return key.strip("-")


def infer_area(path: Path, vault_root: Path) -> str:
    parts = path.relative_to(vault_root).parts
    if "My_DevInfra" in parts:
        return "[[My_DevInfra]]"
    if "Health" in parts:
        return "[[Health]]"
    if "Learning" in parts:
        return "[[Learning]]"
    if "Career" in parts:
        return "[[Career]]"
    return ""


def infer_type(path: Path, fm: dict[str, Any]) -> str:
    current = str(fm.get("type") or "").strip().lower()
    if current in VALID_TYPES:
        return current
    parts = path.parts
    if "00 Inbox" in parts:
        return "resource"
    if "04 Periodic" in parts:
        return "periodic"
    return "resource"


def issues_for(path: Path, vault_root: Path) -> QueueItem | None:
    fm = split_frontmatter(path)
    rel = str(path.relative_to(vault_root))
    current = {
        key: fm.get(key)
        for key in ("title", "type", "status", "area", "project", "concepts", "tags", "review_flags")
        if key in fm
    }
    suggested: dict[str, Any] = {}
    review_needed: list[str] = []
    reasons: list[str] = []

    note_type = infer_type(path, fm)
    if fm.get("type") != note_type:
        suggested["type"] = note_type
        review_needed.append(f"type needs V4 value `{note_type}`")
    else:
        suggested["type"] = note_type

    if note_type in {"project", "event"}:
        if fm.get("status") not in VALID_STATUSES:
            suggested["status"] = "active"
            review_needed.append("status needed for project/event")
    elif fm.get("status"):
        review_needed.append("status exists on non-project/event")

    if not fm.get("area") and not fm.get("project"):
        area = infer_area(path, vault_root)
        if area:
            suggested["area"] = area
            review_needed.append("area missing")
        else:
            review_needed.append("area/project missing")
    elif fm.get("area") and not is_wikilink(fm.get("area")):
        review_needed.append("area needs wikilink")

    concepts = as_list(fm.get("concepts"))
    if not concepts:
        review_needed.append("concepts need owner assignment")
    else:
        bad_concepts = [c for c in concepts if not is_wikilink(c)]
        tag_like = [c for c in concepts if str(c).strip("[ ]").startswith(TAG_PREFIXES)]
        secretish = [c for c in concepts if looks_like_secret(c)]
        if secretish:
            review_needed.append("concepts contain secret-shaped text")
        if bad_concepts:
            review_needed.append("concepts need wikilinks")
        if tag_like:
            review_needed.append("concepts contain tag-shaped values")

    tags = as_list(fm.get("tags"))
    if not tags:
        review_needed.append("tags missing")
    else:
        if any(looks_like_secret(tag) for tag in tags):
            review_needed.append("tags contain secret-shaped text")
        bad_tags = [tag for tag in tags if not valid_tag(tag)]
        if bad_tags:
            review_needed.append("tags need V4 prefixes")

    if not review_needed:
        return None

    confidence = "review"
    if review_needed == ["concepts need owner assignment"]:
        confidence = "medium"
    elif all(issue in {"concepts need owner assignment", "tags missing", "area missing"} for issue in review_needed):
        confidence = "medium"

    reasons.append("current V4 validation still needs owner attention")
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
        path = item.path
        preferred = 0
        if "/AI/" in path or "/My_Neovim/" in path or "/OpenClaw/" in path:
            preferred += 2
        if "/myNeovim/" in path:
            preferred -= 2
        return (preferred, -len(item.review_needed), path)

    return sorted(items, key=score, reverse=True)[0]


def build_queue(vault_root: Path, subdir: str, collapse_duplicates: bool) -> tuple[list[QueueItem], dict[str, list[QueueItem]]]:
    scan_root = vault_root / subdir
    items = [
        item
        for path in sorted(scan_root.rglob("*.md"))
        if (item := issues_for(path, vault_root)) is not None
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
        "# V4 Owner Queue",
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

    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault-root", default=str(DEFAULT_VAULT))
    parser.add_argument("--subdir", required=True)
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
