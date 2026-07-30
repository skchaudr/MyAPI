#!/usr/bin/env python3
"""Daily allowlisted corpus → Khoj (HTTP API). Air-oriented; fails loud.

Stages a bounded hot slice, PUTs changed files to Khoj /api/content, writes a
receipt. Never ingests full ~/.pi, auth, weights, or session firehoses.

Usage:
  python3 scripts/daily_corpus_to_khoj.py            # run
  python3 scripts/daily_corpus_to_khoj.py --status   # last receipt
  python3 scripts/daily_corpus_to_khoj.py --dry-run  # stage only
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

HOME = Path.home()
REPO = Path(__file__).resolve().parents[1]
STATE_DIR = REPO / "scratch" / "daily-corpus"
STAGE_DIR = STATE_DIR / "stage"
RECEIPT_DIR = STATE_DIR / "receipts"
MANIFEST_PATH = STATE_DIR / "manifest.json"
LAST_PATH = STATE_DIR / "LAST"
FAIL_PATH = STATE_DIR / "FAIL"

# Default Khoj (Tailscale hostname; IP fallback in probe order)
DEFAULT_KHOJ_URLS = [
    os.environ.get("MYAPI_KHOJ_URL", "").rstrip("/"),
    "http://khoj-vm-restore:42110",
    "http://100.88.54.98:42110",
]
DEFAULT_KHOJ_URLS = [u for u in DEFAULT_KHOJ_URLS if u]

MAX_FILE_BYTES = 512 * 1024  # 512 KiB per file
HOST_TAG = os.uname().nodename.split(".")[0]

# Deny substrings (path). Loud skip, not silent swallow of secrets.
DENY_SUBSTRINGS = (
    "/.env",
    "auth.json",
    "credentials",
    "id_rsa",
    "id_ed25519",
    ".pem",
    "secret",
    "/weights/",
    "/blobs/",
    "password",
    "token.json",
)


@dataclass
class SourceSpec:
    """One allowlisted root or file."""

    path: Path
    prefix: str  # stable name prefix in stage/Khoj
    recursive: bool = False
    max_files: int = 50
    glob: str = "*.md"
    required: bool = False  # if missing → fail when required


def allowlist() -> list[SourceSpec]:
    """Bounded hot corpus. Edit here — not full-tree walks of ~/.pi."""
    myapi = REPO
    return [
        # MyAPI product + handoffs
        SourceSpec(myapi / "handoffs", "myapi-handoffs", recursive=True, max_files=40, required=True),
        SourceSpec(myapi / "README.md", "myapi", required=True),
        SourceSpec(myapi / "AGENTS.md", "myapi"),
        SourceSpec(myapi / "HANDOFF-PI-README.md", "myapi"),
        SourceSpec(myapi / "docs", "myapi-docs", recursive=True, max_files=20),
        # Corpus v1.0 vault substrate (narrow buckets only)
        SourceSpec(
            HOME / "Obsidian" / "Corpus v1.0" / "00-index",
            "corpus-v1-00-index",
            recursive=True,
            max_files=30,
        ),
        SourceSpec(
            HOME / "Obsidian" / "Corpus v1.0" / "10-current-state",
            "corpus-v1-10-current",
            recursive=True,
            max_files=30,
        ),
        SourceSpec(
            HOME / "Obsidian" / "Corpus v1.0" / "20-projects",
            "corpus-v1-20-projects",
            recursive=True,
            max_files=40,
        ),
        # Operator notes (explicit files)
        SourceSpec(
            HOME / "Obsidian" / "SSD" / "What MyAPI v1 corpous normalization is really becoming.md",
            "ssd-myapi",
        ),
        SourceSpec(
            HOME
            / "Obsidian"
            / "SSD"
            / "The 10 task checklist for the upgraded corpus v1 normalization path for MyAPI.md",
            "ssd-myapi",
        ),
        SourceSpec(
            HOME / "Obsidian" / "SSD" / "02 Areas" / "Two Track Plan to Finishing GDD and MyAPI.md",
            "ssd-portfolio",
        ),
        SourceSpec(
            HOME
            / "Obsidian"
            / "SSD"
            / "00 Inbox"
            / "Needle Gemma Execution Plan.md",
            "ssd-needle",
        ),
        # GDDP (briefs + recent handoffs only)
        SourceSpec(HOME / "repos" / "gddp-runtime" / "PROJECT-BRIEF.md", "gddp-runtime", required=True),
        SourceSpec(HOME / "repos" / "gddp-runtime" / "TOPOLOGY.md", "gddp-runtime"),
        SourceSpec(
            HOME / "repos" / "gddp-runtime" / ".handoffs",
            "gddp-runtime-handoffs",
            recursive=True,
            max_files=8,
        ),
        SourceSpec(HOME / "repos" / "gddp-config" / "README.md", "gddp-config", required=True),
        SourceSpec(
            HOME / "repos" / "gddp-config" / ".handoffs",
            "gddp-config-handoffs",
            recursive=True,
            max_files=8,
        ),
        # Pi / Needle — scoped, not whole tree
        SourceSpec(HOME / ".pi" / "PROJECT-BRIEF.md", "pi"),
        SourceSpec(HOME / ".pi" / "needle" / "README.md", "pi-needle"),
        SourceSpec(
            HOME / ".pi" / "needle" / "docs" / "needle-gemma-v1-execution-ledger.md",
            "pi-needle",
        ),
        SourceSpec(
            HOME / ".pi" / "docs" / "needle_gemma_pi_harness_implementation_plan.md",
            "pi-needle",
        ),
        # corpus-hot briefs (pass-1 operator harvest) if present
        SourceSpec(
            myapi / "scratch" / "corpus-hot" / "myapi" / "BRIEF-DRAFT.md",
            "corpus-hot",
        ),
        SourceSpec(
            myapi / "scratch" / "corpus-hot" / "gddp" / "BRIEF-DRAFT.md",
            "corpus-hot",
        ),
        SourceSpec(
            myapi / "scratch" / "corpus-hot" / "pi-needle-gemma" / "BRIEF-DRAFT.md",
            "corpus-hot",
        ),
        SourceSpec(myapi / "scratch" / "corpus-hot" / "README.md", "corpus-hot"),
    ]


def log(msg: str) -> None:
    print(msg, flush=True)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def safe_slug(text: str, max_len: int = 80) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s.-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-.")
    return (text[:max_len] or "untitled")


def denied(path: Path) -> bool:
    s = str(path).lower()
    return any(x in s for x in DENY_SUBSTRINGS)


def collect_from_spec(spec: SourceSpec) -> list[Path]:
    p = spec.path.expanduser()
    if not p.exists():
        if spec.required:
            raise FileNotFoundError(f"required source missing: {p}")
        return []
    if p.is_file():
        return [p]
    if not spec.recursive:
        return sorted(p.glob(spec.glob))[: spec.max_files]

    found: list[Path] = []
    # Prefer top-level handoff markdown (numbered *.md) before nested artifacts/
    top_level = sorted(
        (fp for fp in p.glob("*.md") if fp.is_file() and not denied(fp)),
        key=lambda x: x.stat().st_mtime,
        reverse=True,
    )
    for fp in top_level:
        try:
            if fp.stat().st_size > MAX_FILE_BYTES:
                continue
        except OSError:
            continue
        found.append(fp)
    if len(found) >= spec.max_files:
        return found[: spec.max_files]

    for root, dirs, files in os.walk(p):
        # prune heavy / secret-ish / artifact dump dirs
        dirs[:] = [
            d
            for d in dirs
            if d
            not in {
                ".git",
                "node_modules",
                ".venv",
                "venv",
                "__pycache__",
                ".cache",
                "artifacts",
            }
            and not d.startswith(".")
        ]
        if Path(root) == p:
            continue  # already took top-level
        for name in files:
            if spec.glob == "*.md" and not name.endswith(".md"):
                continue
            fp = Path(root) / name
            if denied(fp):
                continue
            try:
                if fp.stat().st_size > MAX_FILE_BYTES:
                    continue
            except OSError:
                continue
            found.append(fp)
    # newest first for remaining nested files, then cap
    found[len(top_level) :] = sorted(
        found[len(top_level) :], key=lambda x: x.stat().st_mtime, reverse=True
    )
    return found[: spec.max_files]


def stage_name(spec: SourceSpec, src: Path) -> str:
    """Stable unique Khoj filename: prefix + relative path (no collisions)."""
    if spec.path.is_file():
        # include parent dir so sibling BRIEF-DRAFT.md files don't clobber
        try:
            rel = src.relative_to(spec.path.parent.parent)
        except ValueError:
            rel = Path(spec.path.parent.name) / src.name
        base = "-".join(safe_slug(part) for part in rel.parts)
    else:
        try:
            rel = src.relative_to(spec.path)
        except ValueError:
            rel = Path(src.name)
        base = "-".join(safe_slug(part) for part in rel.parts)
    return f"{spec.prefix}--{base}"


def wrap_markdown(src: Path, body: str, staged_name: str) -> str:
    """Add provenance frontmatter if missing."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    header = (
        f"---\n"
        f"title: {src.name}\n"
        f"source: myapi-daily-corpus\n"
        f"host: {HOST_TAG}\n"
        f"origin_path: {src}\n"
        f"staged_as: {staged_name}\n"
        f"ingested_at: {now}\n"
        f"status: incubating\n"
        f"doc_type: daily_corpus\n"
        f"---\n\n"
    )
    if body.lstrip().startswith("---"):
        # keep original FM; append provenance trailer at top as HTML comment-ish block
        return (
            f"<!-- myapi-daily-corpus host={HOST_TAG} origin={src} "
            f"staged={staged_name} at={now} -->\n\n{body}"
        )
    return header + body


def stage_all() -> tuple[list[Path], list[str]]:
    STAGE_DIR.mkdir(parents=True, exist_ok=True)
    # clean stage
    for old in STAGE_DIR.iterdir():
        if old.is_file():
            old.unlink()

    staged: list[Path] = []
    warnings: list[str] = []
    for spec in allowlist():
        try:
            files = collect_from_spec(spec)
        except FileNotFoundError as exc:
            raise
        if not files and spec.path.exists() is False:
            warnings.append(f"missing optional: {spec.path}")
            continue
        for src in files:
            if denied(src):
                warnings.append(f"denied: {src}")
                continue
            try:
                raw = src.read_text(encoding="utf-8", errors="replace")
            except OSError as exc:
                warnings.append(f"read fail {src}: {exc}")
                continue
            name = stage_name(spec, src)
            if not name.endswith(".md"):
                name = name + ".md"
            dest = STAGE_DIR / name
            dest.write_text(wrap_markdown(src, raw, name), encoding="utf-8")
            staged.append(dest)
    return staged, warnings


def load_manifest() -> dict[str, str]:
    if not MANIFEST_PATH.exists():
        return {}
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_manifest(m: dict[str, str]) -> None:
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(m, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def http_json(url: str, timeout: float = 15.0) -> tuple[int, bytes]:
    req = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read() if e.fp else b""
    except Exception as e:
        raise ConnectionError(str(e)) from e


def probe_khoj(urls: list[str]) -> str:
    last_err = ""
    for base in urls:
        try:
            code, body = http_json(f"{base}/api/health", timeout=8)
            if code == 200:
                log(f"Khoj health OK: {base} ({body.decode('utf-8', 'replace')[:80]})")
                return base
            last_err = f"{base} health http={code}"
        except Exception as e:
            last_err = f"{base}: {e}"
            log(f"probe fail: {last_err}")
    raise ConnectionError(f"no healthy Khoj endpoint; last={last_err}")


def put_file(base_url: str, path: Path, timeout: float = 60.0) -> int:
    """Multipart PUT one markdown file. Uses curl for reliable multipart."""
    url = f"{base_url}/api/content?client=api"
    cmd = [
        "curl",
        "-sS",
        "-m",
        str(int(timeout)),
        "-o",
        "/dev/null",
        "-w",
        "%{http_code}",
        "-X",
        "PUT",
        url,
        "-F",
        f"files=@{path};filename={path.name};type=text/markdown",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"curl failed: {proc.stderr.strip() or proc.stdout}")
    try:
        return int(proc.stdout.strip())
    except ValueError as e:
        raise RuntimeError(f"bad http code: {proc.stdout!r}") from e


def notify(title: str, message: str) -> None:
    """macOS notification — best effort."""
    script = f'display notification {json.dumps(message)} with title {json.dumps(title)}'
    subprocess.run(["osascript", "-e", script], capture_output=True)


def write_receipt(ok: bool, payload: dict) -> Path:
    RECEIPT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = RECEIPT_DIR / f"{ts}-{'ok' if ok else 'FAIL'}.json"
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    LAST_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if ok:
        if FAIL_PATH.exists():
            FAIL_PATH.unlink()
    else:
        FAIL_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def git_export_main_tips(staged: list[Path]) -> list[str]:
    """If working tree lacks main tip docs, export via git show into stage."""
    tips = [
        ("PROJECT-BRIEF.md", "myapi-main--PROJECT-BRIEF.md"),
        ("IMPLEMENTATION-PLAN.md", "myapi-main--IMPLEMENTATION-PLAN.md"),
        (
            "evals/golden_briefs/get_project_context_myapi_rebuild.md",
            "myapi-main--golden-myapi_rebuild.md",
        ),
        (
            "evals/golden_briefs/get_person_context_sab.md",
            "myapi-main--golden-person_sab.md",
        ),
    ]
    notes: list[str] = []
    for rel, out_name in tips:
        dest = STAGE_DIR / out_name
        # skip if already staged from working tree under similar name
        proc = subprocess.run(
            ["git", "-C", str(REPO), "show", f"main:{rel}"],
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            notes.append(f"git show main:{rel} unavailable")
            continue
        body = proc.stdout
        if len(body.encode("utf-8")) > MAX_FILE_BYTES:
            notes.append(f"skip large main:{rel}")
            continue
        dest.write_text(
            wrap_markdown(Path(f"git:main:{rel}"), body, out_name),
            encoding="utf-8",
        )
        staged.append(dest)
        notes.append(f"staged main:{rel}")
    return notes


def run(dry_run: bool = False) -> int:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    started = time.time()
    payload: dict = {
        "host": HOST_TAG,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "ok": False,
        "dry_run": dry_run,
    }
    try:
        staged, warnings = stage_all()
        tip_notes = git_export_main_tips(staged)
        payload["warnings"] = warnings + tip_notes
        payload["staged_count"] = len(staged)
        if len(staged) < 5:
            raise RuntimeError(f"too few staged files ({len(staged)}); allowlist empty or broken")

        manifest = load_manifest()
        to_upload: list[Path] = []
        skipped = 0
        for path in staged:
            digest = sha256_file(path)
            if manifest.get(path.name) == digest:
                skipped += 1
                continue
            to_upload.append(path)

        payload["skipped_unchanged"] = skipped
        payload["to_upload"] = len(to_upload)
        payload["files"] = [p.name for p in staged]

        if dry_run:
            payload["ok"] = True
            payload["message"] = "dry-run: staged only"
            write_receipt(True, payload)
            log(f"DRY-RUN staged={len(staged)} would_upload={len(to_upload)} skip={skipped}")
            return 0

        base = probe_khoj(DEFAULT_KHOJ_URLS)
        payload["khoj_url"] = base

        indexed = 0
        failed: list[str] = []
        for path in to_upload:
            code = put_file(base, path)
            if code in (200, 201, 204):
                manifest[path.name] = sha256_file(path)
                indexed += 1
                log(f"  OK {path.name} http={code}")
            else:
                failed.append(f"{path.name}:{code}")
                log(f"  FAIL {path.name} http={code}")

        payload["indexed"] = indexed
        payload["failed"] = failed
        if failed:
            raise RuntimeError(f"{len(failed)} file(s) failed to index: {failed[:5]}")

        save_manifest(manifest)
        payload["ok"] = True
        payload["elapsed_s"] = round(time.time() - started, 2)
        payload["finished_at"] = datetime.now(timezone.utc).isoformat()
        receipt = write_receipt(True, payload)
        log(f"OK indexed={indexed} skipped={skipped} receipt={receipt}")
        if indexed:
            notify("MyAPI daily corpus", f"OK: {indexed} file(s) → Khoj ({HOST_TAG})")
        return 0

    except Exception as exc:
        payload["ok"] = False
        payload["error"] = f"{type(exc).__name__}: {exc}"
        payload["elapsed_s"] = round(time.time() - started, 2)
        payload["finished_at"] = datetime.now(timezone.utc).isoformat()
        receipt = write_receipt(False, payload)
        log(f"FAIL {payload['error']} receipt={receipt}")
        notify("MyAPI daily corpus FAIL", str(exc)[:180])
        return 1


def status_cmd() -> int:
    if not LAST_PATH.exists():
        print("NO RECEIPT — daily corpus has never completed on this host")
        if FAIL_PATH.exists():
            print(FAIL_PATH.read_text(encoding="utf-8"))
        return 2
    data = json.loads(LAST_PATH.read_text(encoding="utf-8"))
    print(json.dumps(data, indent=2))
    # stale check: >26h
    finished = data.get("finished_at") or data.get("started_at")
    if finished:
        try:
            ts = datetime.fromisoformat(finished.replace("Z", "+00:00"))
            age_h = (datetime.now(timezone.utc) - ts).total_seconds() / 3600
            if age_h > 26:
                print(f"STALE: last run {age_h:.1f}h ago (>26h)", file=sys.stderr)
                return 1
        except ValueError:
            pass
    if not data.get("ok"):
        return 1
    if FAIL_PATH.exists():
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--status", action="store_true")
    args = parser.parse_args()
    if args.status:
        return status_cmd()
    return run(dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
