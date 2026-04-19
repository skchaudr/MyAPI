#!/usr/bin/env python3
"""Print the next safe start index from a Khoj reindex log."""

import argparse
import re
import sys


BATCH_RE = re.compile(r"BATCH\s+(\d+)-(\d+)/(\d+)\s+method=(PUT|PATCH)")
SUCCESS_RE = re.compile(r"->\s+(200|201|204)\s+\((\d+)\s+docs\)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("log_path")
    args = parser.parse_args()

    try:
        lines = open(args.log_path, encoding="utf-8").read().splitlines()
    except OSError as exc:
        print(f"ERROR: cannot read {args.log_path}: {exc}", file=sys.stderr)
        return 1

    pending_batch: tuple[int, int, int, str] | None = None
    last_success: tuple[int, int, int, str, int] | None = None

    for line in lines:
        batch_match = BATCH_RE.search(line)
        if batch_match:
            start, end, total, method = batch_match.groups()
            pending_batch = (int(start), int(end), int(total), method)
            continue

        success_match = SUCCESS_RE.search(line)
        if success_match and pending_batch:
            status, docs = success_match.groups()
            start, end, total, method = pending_batch
            last_success = (start, end, total, method, int(docs))
            pending_batch = None

    if not last_success:
        print("START_INDEX=0")
        print("LAST_SUCCESS=none")
        if pending_batch:
            start, end, total, method = pending_batch
            print(f"PENDING_BATCH={start}-{end}/{total} method={method}")
        return 0

    start, end, total, method, docs = last_success
    print(f"START_INDEX={end}")
    print(f"LAST_SUCCESS={start}-{end}/{total} method={method} docs={docs}")
    if end >= total:
        print("DONE=true")
    elif pending_batch:
        pending_start, pending_end, pending_total, pending_method = pending_batch
        print(f"PENDING_BATCH={pending_start}-{pending_end}/{pending_total} method={pending_method}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
