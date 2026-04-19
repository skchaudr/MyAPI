#!/usr/bin/env python3
"""Reindex Khoj notes via the /api/content multipart API.

This skips macOS AppleDouble files and supports resuming with PATCH-only runs.
"""

import argparse
import os
import sys
import time

import requests


def log(message: str, log_path: str) -> None:
    line = f"{time.strftime('%H:%M:%S')} {message}"
    print(line, flush=True)
    with open(log_path, "a", encoding="utf-8") as handle:
        handle.write(line + "\n")


def collect_files(notes_dir: str) -> list[str]:
    return sorted(
        name
        for name in os.listdir(notes_dir)
        if name.endswith(".md") and not name.startswith("._")
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--notes-dir", default=os.path.expanduser("~/khoj-data/notes"))
    parser.add_argument("--url", default="http://localhost:42110")
    parser.add_argument("--batch-size", type=int, default=250)
    parser.add_argument("--start-index", type=int, default=0)
    parser.add_argument("--max-files", type=int)
    parser.add_argument("--patch-only", action="store_true")
    parser.add_argument("--log", default="/tmp/reindex_khoj.log")
    parser.add_argument("--timeout", type=int, default=180)
    args = parser.parse_args()

    files = collect_files(args.notes_dir)
    if args.max_files is not None:
        files = files[: args.max_files]
    total = len(files)
    log(f"REAL_FILES={total} START_INDEX={args.start_index} BATCH_SIZE={args.batch_size}", args.log)

    for start in range(args.start_index, total, args.batch_size):
        batch = files[start : start + args.batch_size]
        end = start + len(batch)
        method = "PATCH" if args.patch_only or start > 0 else "PUT"
        log(f"BATCH {start + 1}-{end}/{total} method={method}", args.log)

        file_tuples = []
        for name in batch:
            path = os.path.join(args.notes_dir, name)
            with open(path, "rb") as handle:
                file_tuples.append(("files", (name, handle.read(), "text/markdown")))

        try:
            response = requests.request(
                method,
                f"{args.url}/api/content?client=api",
                files=file_tuples,
                timeout=args.timeout,
            )
        except Exception as exc:
            log(f"ERROR {type(exc).__name__}: {exc}", args.log)
            return 1

        log(f"-> {response.status_code} ({len(batch)} docs)", args.log)
        if response.status_code not in (200, 201, 204):
            log(f"BODY {response.text[:500]}", args.log)
            return 1
        time.sleep(2)

    log("DONE", args.log)
    return 0


if __name__ == "__main__":
    sys.exit(main())
