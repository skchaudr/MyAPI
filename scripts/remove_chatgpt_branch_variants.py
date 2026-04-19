#!/usr/bin/env python3
"""Identify and optionally remove duplicated ChatGPT branch-export variants.

By default this script is read-only. Use --apply to move matching files out of
the active Khoj bundle so they will not be reindexed.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
from dataclasses import dataclass
from pathlib import Path


PREFIX = "chatgpt-branch-"


@dataclass(frozen=True)
class Candidate:
    path: Path
    canonical_name: str
    sha256: str
    size: int


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonicalize(name: str) -> str:
    """Collapse chatgpt-branch-* variants back to their base chatgpt-* name."""
    stem = name.removeprefix("chatgpt-")
    while stem.startswith("branch-"):
        stem = stem.removeprefix("branch-")
    return f"chatgpt-{stem}"


def find_candidates(bundle_dir: Path) -> list[Candidate]:
    candidates = []
    for path in sorted(bundle_dir.glob(f"{PREFIX}*.md")):
        candidates.append(
            Candidate(
                path=path,
                canonical_name=canonicalize(path.name),
                sha256=sha256_file(path),
                size=path.stat().st_size,
            )
        )
    return candidates


def print_report(bundle_dir: Path, candidates: list[Candidate]) -> None:
    by_canonical: dict[str, list[Candidate]] = {}
    for candidate in candidates:
        by_canonical.setdefault(candidate.canonical_name, []).append(candidate)

    existing_canonicals = [
        canonical
        for canonical in sorted(by_canonical)
        if (bundle_dir / canonical).exists()
    ]

    total_bytes = sum(candidate.size for candidate in candidates)
    print(f"Bundle: {bundle_dir}")
    print(f"Candidates: {len(candidates)}")
    print(f"Bytes to move: {total_bytes}")
    print(f"Canonical matches already present: {len(existing_canonicals)}")
    print()

    print("Sample candidates:")
    for candidate in candidates[:25]:
        marker = "has canonical" if (bundle_dir / candidate.canonical_name).exists() else "no canonical"
        print(f"- {candidate.path.name} -> {candidate.canonical_name} ({marker})")

    if len(candidates) > 25:
        print(f"- ... {len(candidates) - 25} more")

    print()
    print("Top duplicate groups:")
    groups = sorted(by_canonical.items(), key=lambda item: len(item[1]), reverse=True)
    for canonical, group in groups[:15]:
        if len(group) > 1 or (bundle_dir / canonical).exists():
            print(f"- {canonical}: {len(group)} branch variant(s)")


def move_candidates(candidates: list[Candidate], target_dir: Path) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)
    for candidate in candidates:
        destination = target_dir / candidate.path.name
        if destination.exists():
            destination = target_dir / f"{candidate.sha256[:12]}-{candidate.path.name}"
        shutil.move(str(candidate.path), str(destination))
    print(f"Moved {len(candidates)} files to {target_dir}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Identify and optionally move chatgpt-branch-* duplicates out of a Khoj bundle."
    )
    parser.add_argument(
        "--bundle-dir",
        default="khoj-ready-bundle",
        help="Path to the active Khoj-ready markdown bundle.",
    )
    parser.add_argument(
        "--target-dir",
        default="khoj-ready-bundle.removed-chatgpt-branch-variants",
        help="Directory where files are moved when --apply is set.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually move files. Without this flag, the script only reports.",
    )
    args = parser.parse_args()

    bundle_dir = Path(args.bundle_dir).expanduser().resolve()
    target_dir = Path(args.target_dir).expanduser().resolve()

    if not bundle_dir.is_dir():
        raise SystemExit(f"Bundle directory not found: {bundle_dir}")

    candidates = find_candidates(bundle_dir)
    print_report(bundle_dir, candidates)

    if not args.apply:
        print("Dry run only. Re-run with --apply to move these files.")
        return 0

    move_candidates(candidates, target_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
