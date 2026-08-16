#!/usr/bin/env python3
"""Stage the Part 1 decision corpus as the exact Markdown bytes Khoj will ingest."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile


ROOM = Path(__file__).resolve().parent
DEFAULT_SOURCE = ROOM.parent / "02-corpus" / "output" / "corpus"
DEFAULT_OUTPUT = ROOM / "output" / "khoj-corpus"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy the deterministic decision corpus byte-for-byte into Khoj staging."
    )
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def source_files(source: Path) -> list[Path]:
    if source.is_symlink() or not source.is_dir():
        raise ValueError(f"source must be a non-symlink directory: {source}")

    entries = sorted(source.iterdir(), key=lambda path: path.name)
    invalid = [path.name for path in entries if not path.is_file() or path.suffix != ".md"]
    if invalid:
        raise ValueError(
            "source must be flat and contain only Markdown files; invalid entries: "
            + ", ".join(invalid)
        )
    if not entries:
        raise ValueError(f"source corpus is empty: {source}")
    return entries


def manifest(files: list[Path]) -> dict[str, str]:
    return {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in files}


def manifest_digest(entries: dict[str, str]) -> str:
    canonical = json.dumps(entries, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def replace_output(source: Path, output: Path) -> tuple[int, str]:
    source = source.expanduser().resolve()
    files = source_files(source)
    expected = manifest(files)

    output = output.expanduser()
    if output.is_symlink():
        raise ValueError(f"refusing to replace symlink output: {output}")
    output = output.resolve()
    if output == source:
        raise ValueError("source and output directories must differ")
    output.parent.mkdir(parents=True, exist_ok=True)

    staging = Path(tempfile.mkdtemp(prefix=f".{output.name}.transform-", dir=output.parent))
    backup: Path | None = None
    try:
        for source_file in files:
            shutil.copyfile(source_file, staging / source_file.name)

        actual_files = source_files(staging)
        actual = manifest(actual_files)
        if actual != expected:
            raise ValueError("staged file set or bytes differ from the source corpus")

        if output.exists():
            if not output.is_dir():
                raise ValueError(f"output exists and is not a directory: {output}")
            backup = Path(tempfile.mkdtemp(prefix=f".{output.name}.backup-", dir=output.parent))
            backup.rmdir()
            os.replace(output, backup)
        os.replace(staging, output)
        if backup is not None:
            shutil.rmtree(backup)
    except Exception:
        if backup is not None and backup.exists() and not output.exists():
            os.replace(backup, output)
        raise
    finally:
        if staging.exists():
            shutil.rmtree(staging)

    return len(expected), manifest_digest(expected)


def main() -> int:
    args = parse_args()
    try:
        count, digest = replace_output(args.source, args.output)
    except (OSError, ValueError) as exc:
        raise SystemExit(f"error: {exc}") from exc

    print(f"staged {count} Markdown files in {args.output}")
    print(f"manifest sha256: {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
