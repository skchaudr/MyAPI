#!/usr/bin/env python3
"""Print source-root summaries and corpus-tier manifests for MyAPI."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from context_refinery.normalization_schema import stamp_from_path


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

DURABLE_BASENAMES = frozenset({
    "AGENTS.md",
    "ARCHITECTURE.md",
    "PROJECT-BRIEF.md",
    "REBUILD-CONTEXT-ANCHOR.md",
})
DURABLE_PATH_PARTS = (
    "/source-of-truth-anchors/",
    "/project-documents/REBUILD-CONTEXT-ANCHOR.md",
    "/project-documents/ARCHITECTURE.md",
    "/project-documents/corpus-tier-policy-",
)
COLD_SOURCE_FAMILIES = frozenset({"corpus_v1_baseline"})
DEFAULT_HOT_DAYS = 30
DEFAULT_SOURCE_ROOT_SUFFIXES = (".md", ".jsonl")


@dataclass(frozen=True)
class TierDecision:
    tier: str
    reason: str
    include_in_active_bundle: bool


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


def classify_corpus_tier(
    path: Path,
    *,
    source_family: str,
    mtime: float | None,
    now: datetime | None = None,
    hot_days: int = DEFAULT_HOT_DAYS,
) -> TierDecision:
    """Classify one source file into the active-corpus tier model."""
    if now is None:
        now = datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)

    posix_path = path.as_posix()
    basename = path.name
    stamp = stamp_from_path(posix_path)

    if stamp.source_type in {"anchor", "handoff"}:
        return TierDecision("durable", f"durable_source_type:{stamp.source_type}", True)
    if basename in DURABLE_BASENAMES or any(part in posix_path for part in DURABLE_PATH_PARTS):
        return TierDecision("durable", "canonical_path", True)

    if source_family in COLD_SOURCE_FAMILIES:
        return TierDecision("cold", f"cold_source_family:{source_family}", False)

    if mtime is not None:
        mtime_dt = datetime.fromtimestamp(mtime, timezone.utc)
        if mtime_dt >= now - timedelta(days=hot_days):
            return TierDecision("hot", f"mtime_within_{hot_days}_days", True)

    return TierDecision("cold", "older_than_hot_window", False)


def manifest_row_for_file(
    source: Source,
    file_path: Path,
    *,
    now: datetime | None = None,
    hot_days: int = DEFAULT_HOT_DAYS,
) -> dict[str, object]:
    stat = file_path.stat()
    stamp = stamp_from_path(str(file_path), adapter=_adapter_for_source(source.source_family))
    tier = classify_corpus_tier(
        file_path,
        source_family=source.source_family,
        mtime=stat.st_mtime,
        now=now,
        hot_days=hot_days,
    )
    return {
        "path": str(file_path),
        "source_family": source.source_family,
        "parser_available": "yes" if source.parser_available else "no",
        "suffix": file_path.suffix,
        "mtime_iso": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
        "size_bytes": stat.st_size,
        "source_type": stamp.source_type,
        "temporal_mode": stamp.temporal_mode,
        "primary_project": stamp.primary_project,
        "corpus_tier": tier.tier,
        "tier_reason": tier.reason,
        "include_in_active_bundle": tier.include_in_active_bundle,
    }


def build_corpus_manifest(
    sources: Iterable[Source] = DEFAULT_SOURCES,
    *,
    now: datetime | None = None,
    hot_days: int = DEFAULT_HOT_DAYS,
    active_only: bool = False,
) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for source in sources:
        root = source.path.expanduser()
        if not root.exists():
            continue
        if root.is_file():
            candidates = (root,)
        else:
            candidates = _iter_files(root, source.suffixes)
        for file_path in candidates:
            row = manifest_row_for_file(source, file_path, now=now, hot_days=hot_days)
            if active_only and not row["include_in_active_bundle"]:
                continue
            rows.append(row)

    tier_counts = {"hot": 0, "durable": 0, "cold": 0}
    source_counts: dict[str, int] = {}
    for row in rows:
        tier_counts[str(row["corpus_tier"])] += 1
        family = str(row["source_family"])
        source_counts[family] = source_counts.get(family, 0) + 1

    generated_at = (now or datetime.now(timezone.utc)).replace(microsecond=0).isoformat()
    return {
        "generated_at": generated_at,
        "hot_days": hot_days,
        "active_only": active_only,
        "summary": {
            "file_count": len(rows),
            "tier_counts": tier_counts,
            "source_counts": source_counts,
        },
        "items": rows,
    }


def _adapter_for_source(source_family: str) -> str | None:
    if source_family == "codex_sessions":
        return "codex"
    if source_family == "claude_projects":
        return "claude_code"
    return None


def sources_from_roots(roots: Iterable[Path]) -> tuple[Source, ...]:
    return tuple(
        Source(
            f"local_override_{index}",
            Path(root).expanduser(),
            True,
            DEFAULT_SOURCE_ROOT_SUFFIXES,
        )
        for index, root in enumerate(roots, start=1)
    )


def emit_json(payload: object, output: Path | None = None) -> None:
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    if output is None:
        print(rendered)
        return
    target = output.expanduser()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(rendered + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print source-root JSON summary rows")
    parser.add_argument(
        "--corpus-manifest-json",
        action="store_true",
        help="Print per-file corpus manifest rows with hot/durable/cold tier stamps",
    )
    parser.add_argument(
        "--active-only",
        action="store_true",
        help="With --corpus-manifest-json, emit only hot+durable active bundle entries",
    )
    parser.add_argument(
        "--hot-days",
        type=int,
        default=DEFAULT_HOT_DAYS,
        help="Recency window for hot tier classification",
    )
    parser.add_argument(
        "--source-root",
        action="append",
        type=Path,
        default=[],
        help=(
            "With --corpus-manifest-json, replace default roots with this local source root. "
            "May be repeated."
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Write JSON to this path instead of stdout.",
    )
    args = parser.parse_args()

    if args.json and args.corpus_manifest_json:
        parser.error("Choose either --json or --corpus-manifest-json.")
    if args.active_only and not args.corpus_manifest_json:
        parser.error("--active-only requires --corpus-manifest-json.")
    if args.source_root and not args.corpus_manifest_json:
        parser.error("--source-root requires --corpus-manifest-json.")
    if args.hot_days < 1:
        parser.error("--hot-days must be >= 1.")

    if args.json:
        emit_json(build_manifest(), args.output)
        return 0
    if args.corpus_manifest_json:
        sources = sources_from_roots(args.source_root) if args.source_root else DEFAULT_SOURCES
        emit_json(
            build_corpus_manifest(
                sources=sources,
                hot_days=args.hot_days,
                active_only=args.active_only,
            ),
            args.output,
        )
        return 0

    parser.error("Choose --json or --corpus-manifest-json.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
