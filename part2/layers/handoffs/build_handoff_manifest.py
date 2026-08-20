#!/usr/bin/env python3
"""Build part2/layers/handoffs/handoff-manifest.jsonl — node-05 deliverable.

Deterministic: output depends only on .handoffs/ contents + git add-dates.
One entry per handoff artifact found; gaps recorded as explicit absences;
every exclusion carries a reason (inclusion-reproducible).
"""
import hashlib
import json
import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
HANDOFF_DIR = REPO / ".handoffs"
OUT = Path(__file__).resolve().parent / "handoff-manifest.jsonl"

DATE_LINE = re.compile(r"^Date:\s*(\d{4}-\d{2}-\d{2})", re.MULTILINE)
ISO_ANY = re.compile(r"20\d{2}-\d{2}-\d{2}")
NUM = re.compile(r"^(\d{3})-")


def git_added(path: Path) -> str:
    r = subprocess.run(
        ["git", "log", "--diff-filter=A", "--follow", "--format=%aI", "--", str(path)],
        cwd=REPO, capture_output=True, text=True,
    )
    lines = [l for l in r.stdout.splitlines() if l.strip()]
    return lines[-1] if lines else ""


def occurred_at(path: Path) -> tuple[str | None, str]:
    text = path.read_text(errors="replace")
    m = DATE_LINE.search(text)
    if m:
        return m.group(1), "header-date-line"
    b = ISO_ANY.search(text)
    if b:
        return b.group(0), "body-first-iso-mention"
    return None, "absent-in-document"


entries = []
present_nums = set()
for path in sorted(HANDOFF_DIR.glob("*.md")):
    m = NUM.match(path.name)
    num = m.group(1) if m else None
    if num:
        present_nums.add(int(num))
    body = path.read_text(errors="replace")
    is_template = path.name == "000-template.md"
    occ, occ_basis = occurred_at(path)
    entries.append({
        "artifact": f".handoffs/{path.name}",
        "number": int(num) if num else None,
        "title": body.splitlines()[0].lstrip("# ").strip() if body.splitlines() else "",
        "occurred_at": occ,
        "occurred_at_basis": occ_basis,
        "recorded_at": git_added(path),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "bytes": path.stat().st_size,
        "included": not is_template,
        "exclusion_reason": "canonical template, not a session record" if is_template else None,
        "vm_only": False,
    })

max_num = max(present_nums) if present_nums else 0
gaps = [n for n in range(1, max_num + 1) if n not in present_nums]

with OUT.open("w") as f:
    f.write(json.dumps({
        "manifest": "part2/layers/handoffs/handoff-manifest.jsonl",
        "generated_by": "build_handoff_manifest.py",
        "source_dir": ".handoffs/",
        "census": {
            "files_found": len(entries),
            "included": sum(1 for e in entries if e["included"]),
            "excluded": sum(1 for e in entries if not e["included"]),
            "number_range": [1, max_num],
            "missing_numbers": gaps,
            "missing_count": len(gaps),
        },
        "notes": [
            "Missing numbers were never committed to this repo on main; VM-era "
            "sessions may have produced handoffs recorded only there — not "
            "verifiable from this checkout and marked vm_only=false/unknown-here.",
            "occurred_at is null where no date exists in the document; "
            "occurred_at_basis records provenance (header-date-line | "
            "body-first-iso-mention | absent-in-document). recorded_at is the "
            "git add-date and is present for every entry, so chronology is "
            "preserved on the record axis regardless.",
        ],
    }, sort_keys=True) + "\n")
    for e in entries:
        f.write(json.dumps(e, sort_keys=True) + "\n")

print(f"wrote {OUT} — {len(entries)} entries, {sum(1 for e in entries if e['included'])} included, gaps: {gaps}")
