#!/usr/bin/env python3
"""Print a read-only manifest of sab-air MyAPI source roots."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Source:
    source_family: str
    path: Path
    parser_available: bool
    suffixes: tuple[str, ...] = ()


DEFAULT_SOURCES = (
    Source("obsidian", Path("/Users/sab-mini/Obsidian/SSD"), True, (".md",)),
    Source("codex_sessions", Path("/Users/sab-mini/.codex/sessions"), False, (".jsonl",)),
    Source("claude_projects", Path("/Users/sab-mini/.claude/projects"), True, (".jsonl",)),
    Source("pi_agent_sessions", Path("/Users/sab-mini/.pi/agent/sessions"), False, (".jsonl",)),
    Source("pi_needle", Path("/Users/sab-mini/.pi/needle"), False, (".jsonl", ".md")),
    Source("pi_handoffs", Path("/Users/sab-mini/.pi/.handoffs"), False, (".md",)),
    Source("pi_agent_handoffs", Path("/Users/sab-mini/.pi/agent/handoffs"), False, (".md",)),
    Source(
        "corpus_v1_baseline",
        Path("/Users/sab-mini/repos/MyAPI/Corpus v1.0"),
        True,
        (".md",),
    ),
)


def _iter_files(root: Path, suffixes: tuple[str, ...]) -> Iterable[Path]:
    for path in root.rglob("*"):
        if path.is_file() and (not suffixes or path.suffix in suffixes):
            yield path


def _mtime_iso(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()


def summarize_source(source: Source) -> dict[str, object]:
    root = source.path.expanduser()
    row: dict[str, object] = {
        "source_family": source.source_family,
        "path": str(root),
        "exists": root.exists(),
        "file_count": 0,
        "newest_file": None,
        "newest_mtime_iso": None,
        "parser_available": "yes" if source.parser_available else "no",
    }

    if not root.exists():
        return row

    if root.is_file():
        row["file_count"] = 1
        row["newest_file"] = str(root)
        row["newest_mtime_iso"] = _mtime_iso(root)
        return row

    newest_file: Path | None = None
    newest_mtime = -1.0
    file_count = 0

    for file_path in _iter_files(root, source.suffixes):
        file_count += 1
        mtime = file_path.stat().st_mtime
        if mtime > newest_mtime:
            newest_mtime = mtime
            newest_file = file_path

    row["file_count"] = file_count
    if newest_file is not None:
        row["newest_file"] = str(newest_file)
        row["newest_mtime_iso"] = _mtime_iso(newest_file)

    return row


def build_manifest(sources: Iterable[Source] = DEFAULT_SOURCES) -> list[dict[str, object]]:
    return [summarize_source(source) for source in sources]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print JSON summary rows")
    args = parser.parse_args()

    if not args.json:
        parser.error("Only --json output is supported for this dry-run tool.")

    print(json.dumps(build_manifest(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
