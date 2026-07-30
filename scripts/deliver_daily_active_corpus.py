#!/usr/bin/env python3
"""Deliver latest (or named) daily active corpus markdown into Khoj.

- Health-checks Khoj first; if down, exits 0 with receipt status=skipped_unreachable
  so launchd does not thrash (bundle still built locally).
- Incremental PUT batches of .md only. No full-corpus reindex.
- Env override: MYAPI_KHOJ_URL (default http://100.88.54.98:42110 — khoj-vm-restore).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LATEST = REPO_ROOT / "scratch" / "corpus-daily" / "latest"
DEFAULT_KHOJ_URL = os.environ.get("MYAPI_KHOJ_URL", "http://100.88.54.98:42110")


def _http_json(method: str, url: str, *, timeout: int = 10, data: bytes | None = None, headers: dict | None = None) -> tuple[int, bytes]:
    req = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read() if exc.fp else b""


def khoj_healthy(base_url: str, timeout: int = 5) -> bool:
    code, _ = _http_json("GET", f"{base_url.rstrip('/')}/api/health", timeout=timeout)
    return code == 200


def put_batch(base_url: str, files: list[Path], timeout: int) -> tuple[int, str]:
    """Multipart PUT without requests dependency (stdlib)."""
    import uuid

    boundary = f"----myapi{uuid.uuid4().hex}"
    body = bytearray()
    for path in files:
        name = path.name
        body.extend(f"--{boundary}\r\n".encode())
        body.extend(
            f'Content-Disposition: form-data; name="files"; filename="{name}"\r\n'.encode()
        )
        body.extend(b"Content-Type: text/markdown\r\n\r\n")
        body.extend(path.read_bytes())
        body.extend(b"\r\n")
    body.extend(f"--{boundary}--\r\n".encode())
    url = f"{base_url.rstrip('/')}/api/content?client=api"
    headers = {"Content-Type": f"multipart/form-data; boundary={boundary}"}
    code, raw = _http_json("PUT", url, timeout=timeout, data=bytes(body), headers=headers)
    return code, raw.decode("utf-8", errors="replace")[:300]


def _priority_key(path: Path) -> tuple[int, str]:
    name = path.name
    # Prefer MyAPI / pi handoffs / root docs over bulk obsidian.
    if name.startswith("myapi_"):
        return (0, name)
    if name.startswith("pi_handoffs") or name.startswith("pi_needle"):
        return (1, name)
    if name.startswith("obsidian"):
        return (3, name)
    return (2, name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bundle-dir",
        type=Path,
        default=DEFAULT_LATEST,
        help="Bundle dir or latest symlink",
    )
    parser.add_argument("--khoj-url", default=DEFAULT_KHOJ_URL)
    parser.add_argument("--batch-size", type=int, default=25)
    parser.add_argument(
        "--max-files",
        type=int,
        default=150,
        help="Safety cap (matches allowlist max_md_files)",
    )
    parser.add_argument("--start-index", type=int, default=0)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List files and health only; do not PUT",
    )
    parser.add_argument(
        "--require-khoj",
        action="store_true",
        help="Exit non-zero if Khoj unreachable (default: soft-skip)",
    )
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        default=True,
        help="On batch 500, retry files singly and continue (default true)",
    )
    args = parser.parse_args()

    bundle = args.bundle_dir.expanduser().resolve()
    md_dir = bundle / "md"
    if not md_dir.is_dir():
        print(f"ERROR: no md/ under {bundle}", file=sys.stderr)
        return 1

    files = sorted(
        (p for p in md_dir.iterdir() if p.is_file() and p.suffix.lower() == ".md"),
        key=_priority_key,
    )[: args.max_files]

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    delivery = {
        "generated_at": now,
        "bundle_dir": str(bundle),
        "khoj_url": args.khoj_url,
        "file_count": len(files),
        "start_index": args.start_index,
        "dry_run": args.dry_run,
        "status": "pending",
        "batches": [],
        "skipped": [],
        "delivered_count": 0,
    }

    healthy = khoj_healthy(args.khoj_url)
    delivery["khoj_healthy"] = healthy
    if not healthy:
        delivery["status"] = "skipped_unreachable"
        out = bundle / "delivery-receipt.json"
        out.write_text(json.dumps(delivery, indent=2, sort_keys=True) + "\n")
        print(json.dumps(delivery, indent=2, sort_keys=True))
        return 1 if args.require_khoj else 0

    if args.dry_run:
        delivery["status"] = "dry_run"
        delivery["sample"] = [p.name for p in files[:10]]
        out = bundle / "delivery-receipt.json"
        out.write_text(json.dumps(delivery, indent=2, sort_keys=True) + "\n")
        print(json.dumps(delivery, indent=2, sort_keys=True))
        return 0

    ok = 0
    hard_fail = False
    for start in range(args.start_index, len(files), args.batch_size):
        batch = files[start : start + args.batch_size]
        code, body = put_batch(args.khoj_url, batch, args.timeout)
        entry = {
            "start": start,
            "count": len(batch),
            "http_status": code,
            "body_snip": body,
        }
        delivery["batches"].append(entry)
        print(f"BATCH {start + 1}-{start + len(batch)}/{len(files)} -> {code}", flush=True)
        if code in (200, 201, 204):
            ok += len(batch)
            time.sleep(0.5)
            continue
        # Retry singles on server error
        if args.continue_on_error and code >= 500:
            for path in batch:
                sc, sb = put_batch(args.khoj_url, [path], args.timeout)
                if sc in (200, 201, 204):
                    ok += 1
                    print(f"  OK {path.name}", flush=True)
                else:
                    delivery["skipped"].append(
                        {"file": path.name, "http_status": sc, "body_snip": sb[:120]}
                    )
                    print(f"  SKIP {path.name} -> {sc}", flush=True)
                time.sleep(0.3)
            continue
        hard_fail = True
        break

    delivery["delivered_count"] = ok
    delivery["status"] = "error" if hard_fail else (
        "delivered_with_skips" if delivery["skipped"] else "delivered"
    )
    out = bundle / "delivery-receipt.json"
    out.write_text(json.dumps(delivery, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "status": delivery["status"],
                "delivered_count": ok,
                "skipped_count": len(delivery["skipped"]),
                "khoj_url": args.khoj_url,
                "bundle_dir": str(bundle),
            },
            indent=2,
        )
    )
    return 1 if hard_fail else 0



if __name__ == "__main__":
    raise SystemExit(main())
