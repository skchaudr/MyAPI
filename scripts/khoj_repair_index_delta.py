#!/usr/bin/env python3
"""Delete stale Khoj files and PATCH missing local files."""

import argparse
import os
import sys

import requests

from khoj_index_diff import fetch_indexed_files


def patch_missing_files(base_url: str, client: str, notes_dir: str, missing: list[str], timeout: int) -> None:
    file_tuples = []
    for name in missing:
        path = os.path.join(notes_dir, name)
        with open(path, "rb") as handle:
            file_tuples.append(("files", (name, handle.read(), "text/markdown")))

    response = requests.patch(
        f"{base_url}/api/content",
        params={"client": client},
        files=file_tuples,
        timeout=timeout,
    )
    response.raise_for_status()


def delete_extra_files(base_url: str, client: str, extra: list[str], timeout: int) -> None:
    response = requests.delete(
        f"{base_url}/api/content/files",
        params={"client": client},
        json={"files": extra},
        timeout=timeout,
    )
    response.raise_for_status()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--notes-dir", default="/home/saboor/khoj-data/notes")
    parser.add_argument("--url", default="http://localhost:42110")
    parser.add_argument("--client", default="api")
    parser.add_argument("--timeout", type=int, default=900)
    args = parser.parse_args()

    local = sorted(
        name
        for name in os.listdir(args.notes_dir)
        if name.endswith(".md") and not name.startswith("._")
    )
    indexed = fetch_indexed_files(args.url, args.client)
    local_set = set(local)
    indexed_set = set(indexed)
    missing = [name for name in local if name not in indexed_set]
    extra = sorted(indexed_set - local_set)

    print(f"BEFORE local={len(local)} indexed_unique={len(indexed_set)} missing={len(missing)} extra={len(extra)}", flush=True)
    print(f"MISSING_HEAD={missing[:20]}", flush=True)
    print(f"EXTRA_HEAD={extra[:20]}", flush=True)

    if extra:
        print(f"Deleting {len(extra)} stale indexed files", flush=True)
        delete_extra_files(args.url, args.client, extra, args.timeout)
        print("Delete complete", flush=True)

    if missing:
        print(f"Patching {len(missing)} missing local files", flush=True)
        patch_missing_files(args.url, args.client, args.notes_dir, missing, args.timeout)
        print("Patch complete", flush=True)

    indexed_after = fetch_indexed_files(args.url, args.client)
    indexed_after_set = set(indexed_after)
    missing_after = [name for name in local if name not in indexed_after_set]
    extra_after = sorted(indexed_after_set - local_set)

    print(
        f"AFTER local={len(local)} indexed_unique={len(indexed_after_set)} "
        f"missing={len(missing_after)} extra={len(extra_after)}",
        flush=True,
    )
    print(f"MISSING_AFTER_HEAD={missing_after[:20]}", flush=True)
    print(f"EXTRA_AFTER_HEAD={extra_after[:20]}", flush=True)

    return 0 if not missing_after and not extra_after else 1


if __name__ == "__main__":
    sys.exit(main())
