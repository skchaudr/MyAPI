#!/usr/bin/env python3
"""Compare cleaned local notes against Khoj's indexed file list."""

import argparse
import os
import sys

import requests


def fetch_indexed_files(base_url: str, client: str) -> list[str]:
    indexed: list[str] = []
    first = requests.get(
        f"{base_url}/api/content/files",
        params={"client": client, "truncated": "true", "page": 0},
        timeout=60,
    )
    first.raise_for_status()
    first_data = first.json()
    pages = int(first_data.get("num_pages") or 0)

    for page in range(pages):
        if page == 0:
            data = first_data
        else:
            response = requests.get(
                f"{base_url}/api/content/files",
                params={"client": client, "truncated": "true", "page": page},
                timeout=60,
            )
            response.raise_for_status()
            data = response.json()

        indexed.extend(
            file_info["file_name"]
            for file_info in data.get("files", [])
            if file_info.get("file_name")
        )

    return indexed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--notes-dir", default="/home/saboor/khoj-data/notes")
    parser.add_argument("--url", default="http://localhost:42110")
    parser.add_argument("--client", default="api")
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

    contiguous = 0
    for name in local:
        if name not in indexed_set:
            break
        contiguous += 1

    print(f"LOCAL={len(local)}")
    print(f"INDEXED_RAW={len(indexed)}")
    print(f"INDEXED_UNIQUE={len(indexed_set)}")
    print(f"MISSING={len(missing)}")
    print(f"EXTRA={len(extra)}")
    print(f"CONTIGUOUS_PREFIX={contiguous}")
    print(f"MISSING_HEAD={missing[:20]}")
    print(f"EXTRA_HEAD={extra[:20]}")

    if missing:
        print("MISSING_ALL_PATH=/tmp/khoj_missing_files.txt")
        with open("/tmp/khoj_missing_files.txt", "w", encoding="utf-8") as handle:
            handle.write("\n".join(missing))
            handle.write("\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
