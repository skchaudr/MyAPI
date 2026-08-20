#!/usr/bin/env python3
"""Build part2/layers/git/git-export.jsonl — node-06 deliverable.

Deterministic export of the full MyAPI git history: commits, absolute
ISO-8601 UTC dates, parents, messages, affected files + change evidence
(numstat). Output depends only on immutable git objects; reruns are
byte-identical (verified defaa...-style: script prints sha256; a git repo
is append-only, so the export is stable until new commits land).
"""
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
OUT_DIR = Path(__file__).resolve().parent
OUT = OUT_DIR / "git-export.jsonl"
REC_SEP = "\x1e"  # field separator inside format
END_SEP = "\x1f"   # record terminator (allows multi-line full message)
COMMIT_FMT = REC_SEP.join(["%H", "%P", "%at", "%ct", "%aN", "%cN"]) + REC_SEP + "%B" + END_SEP


def git(*args: str) -> str:
    r = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout


def iso_utc(unix: str) -> str:
    return datetime.fromtimestamp(int(unix), tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


head = git("rev-parse", "HEAD").strip()
total = int(git("rev-list", "--count", "HEAD").strip())

# Pass 1: metadata + full messages, topo-order oldest-first.
meta_raw = git("log", "--reverse", "--topo-order", f"--format={COMMIT_FMT}")
entries = []
by_sha = {}
for rec in meta_raw.split(END_SEP):
    rec = rec.strip("\n")
    if not rec.strip():
        continue
    sha, parents, at, ct, an, cn, body = rec.split(REC_SEP)
    entry = {
        "commit": sha,
        "parents": parents.split() if parents else [],
        "authored_at": iso_utc(at),
        "committed_at": iso_utc(ct),
        "author": an,
        "committer": cn,
        "message": body.strip("\n"),
        "files": [],
    }
    entries.append(entry)
    by_sha[sha] = entry

# Pass 2: change evidence (numstat), same order.
raw = git("log", "--reverse", "--topo-order", "--numstat", "--format=%H")
current = None
for line in raw.splitlines():
    if not line.strip():
        continue
    if len(line) == 40 and all(c in "0123456789abcdef" for c in line):
        current = by_sha[line]
    elif current is not None:
        parts = line.split("\t")
        if len(parts) == 3:
            added, deleted, path = parts
            current["files"].append({
                "path": path,
                "status": "binary" if added == "-" else "text",
                "lines_added": None if added == "-" else int(added),
                "lines_deleted": None if deleted == "-" else int(deleted),
            })

assert len(entries) == total, f"parsed {len(entries)} commits, expected {total}"

with OUT.open("w") as f:
    f.write(json.dumps({
        "manifest": "part2/layers/git/git-export.jsonl",
        "generated_by": "build_git_export.py",
        "repo": "skchaudr/MyAPI",
        "head_commit": head,
        "commit_count": total,
        "scope": "full history, topo-order oldest-first",
        "date_convention": "all dates absolute ISO-8601 UTC",
    }, sort_keys=True) + "\n")
    for e in entries:
        f.write(json.dumps(e, sort_keys=True) + "\n")

digest = hashlib.sha256(OUT.read_bytes()).hexdigest()
print(f"wrote {OUT} — {total} commits, head {head[:12]}, sha256 {digest}")
