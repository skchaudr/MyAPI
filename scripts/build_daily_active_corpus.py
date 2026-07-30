#!/usr/bin/env python3
"""Build today's hot+durable active corpus bundle for MyAPI / Khoj.

Steps:
  1. Emit active-only corpus manifest (source_manifest).
  2. Materialize markdown into a dated bundle dir (hardlink when possible).
  3. Write receipt + SUMMARY for ops.

Does not reindex Khoj. Delivery is separate: deliver_daily_active_corpus.py
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.source_manifest import DEFAULT_HOT_DAYS, build_corpus_manifest

DEFAULT_OUT_ROOT = REPO_ROOT / "scratch" / "corpus-daily"
SKIP_NAME_PARTS = (
    ".env",
    "credentials",
    "secret",
    "auth.json",
    "application_default",
    "id_rsa",
    ".pem",
)


def _safe_bundle_name(source_path: str, source_family: str) -> str:
    """Stable flat filename for Khoj (no path traversal)."""
    digest = hashlib.sha1(source_path.encode("utf-8")).hexdigest()[:10]
    base = Path(source_path).name
    # Keep extension; strip oddities
    safe = "".join(c if c.isalnum() or c in "._-" else "_" for c in base)
    if not safe.endswith(".md"):
        safe = f"{safe}.md"
    return f"{source_family}__{digest}__{safe}"


def _should_skip(path: Path) -> bool:
    lower = path.as_posix().lower()
    return any(part in lower for part in SKIP_NAME_PARTS)


def materialize_markdown(
    items: list[dict],
    bundle_md_dir: Path,
    *,
    max_files: int,
    max_bytes: int,
) -> list[dict]:
    """Copy/hardlink active .md files into bundle_md_dir. Return materialized rows."""
    bundle_md_dir.mkdir(parents=True, exist_ok=True)
    out: list[dict] = []
    for item in items:
        if len(out) >= max_files:
            break
        path = Path(str(item["path"]))
        if path.suffix.lower() != ".md":
            continue
        if _should_skip(path):
            continue
        if not path.is_file():
            continue
        size = int(item.get("size_bytes") or path.stat().st_size)
        if size > max_bytes:
            continue
        dest_name = _safe_bundle_name(str(path), str(item["source_family"]))
        dest = bundle_md_dir / dest_name
        if dest.exists():
            dest.unlink()
        try:
            os.link(path, dest)
            link_mode = "hardlink"
        except OSError:
            shutil.copy2(path, dest)
            link_mode = "copy"
        out.append(
            {
                "source_path": str(path),
                "bundle_file": dest_name,
                "source_family": item["source_family"],
                "corpus_tier": item["corpus_tier"],
                "tier_reason": item["tier_reason"],
                "mtime_iso": item["mtime_iso"],
                "size_bytes": size,
                "link_mode": link_mode,
            }
        )
    return out


def write_summary(receipt: dict, path: Path) -> None:
    s = receipt["summary"]
    lines = [
        f"# Daily active corpus — {receipt['date']}",
        "",
        f"- generated_at: `{receipt['generated_at']}`",
        f"- hot_days: {receipt['hot_days']}",
        f"- active_items (all suffixes): {s['active_item_count']}",
        f"- materialized_md: {s['materialized_md_count']}",
        f"- tier_counts (active): {json.dumps(s['tier_counts'], sort_keys=True)}",
        f"- source_counts (active): {json.dumps(s['source_counts'], sort_keys=True)}",
        f"- md_by_family: {json.dumps(s['md_by_family'], sort_keys=True)}",
        f"- bundle_dir: `{receipt['bundle_dir']}`",
        "",
        "Khoj delivery is separate (`scripts/deliver_daily_active_corpus.py`).",
        "Cold Corpus v1.0 is excluded from active walks.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out-root",
        type=Path,
        default=DEFAULT_OUT_ROOT,
        help="Parent directory for dated bundles",
    )
    parser.add_argument("--hot-days", type=int, default=DEFAULT_HOT_DAYS)
    parser.add_argument(
        "--max-md-files",
        type=int,
        default=800,
        help="Cap markdown files materialized into the bundle",
    )
    parser.add_argument(
        "--max-file-bytes",
        type=int,
        default=1_500_000,
        help="Skip individual files larger than this",
    )
    parser.add_argument(
        "--date",
        help="Bundle date stamp YYYY-MM-DD (default: UTC today)",
    )
    args = parser.parse_args()
    if args.hot_days < 1:
        parser.error("--hot-days must be >= 1")

    now = datetime.now(timezone.utc)
    date_stamp = args.date or now.strftime("%Y-%m-%d")
    bundle_dir = args.out_root.expanduser() / date_stamp
    md_dir = bundle_dir / "md"
    bundle_dir.mkdir(parents=True, exist_ok=True)

    manifest = build_corpus_manifest(hot_days=args.hot_days, active_only=True)
    items = list(manifest["items"])
    manifest_path = bundle_dir / "active-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    materialized = materialize_markdown(
        items,
        md_dir,
        max_files=args.max_md_files,
        max_bytes=args.max_file_bytes,
    )
    mat_path = bundle_dir / "materialized.json"
    mat_path.write_text(
        json.dumps(materialized, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    md_by_family: dict[str, int] = {}
    for row in materialized:
        fam = str(row["source_family"])
        md_by_family[fam] = md_by_family.get(fam, 0) + 1

    receipt = {
        "date": date_stamp,
        "generated_at": now.replace(microsecond=0).isoformat(),
        "hot_days": args.hot_days,
        "bundle_dir": str(bundle_dir),
        "manifest_path": str(manifest_path),
        "materialized_path": str(mat_path),
        "md_dir": str(md_dir),
        "summary": {
            "active_item_count": len(items),
            "materialized_md_count": len(materialized),
            "tier_counts": manifest["summary"]["tier_counts"],
            "source_counts": manifest["summary"]["source_counts"],
            "md_by_family": md_by_family,
            "max_md_files": args.max_md_files,
            "max_file_bytes": args.max_file_bytes,
        },
        "latest_pointer": str(args.out_root.expanduser() / "latest"),
    }
    receipt_path = bundle_dir / "receipt.json"
    receipt_path.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    write_summary(receipt, bundle_dir / "SUMMARY.md")

    # Update latest symlink
    latest = args.out_root.expanduser() / "latest"
    if latest.is_symlink() or latest.exists():
        if latest.is_symlink() or latest.is_file():
            latest.unlink()
        else:
            # refuse to clobber a real directory named latest
            pass
    if not latest.exists():
        latest.symlink_to(bundle_dir, target_is_directory=True)

    print(json.dumps(receipt["summary"], indent=2, sort_keys=True))
    print(f"bundle_dir={bundle_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
