# Task: Implement Modular Triage Package (Fill-in-the-Blanks)

## What this is
The CLI triage tool at `context_refinery/triage/` is fully scaffolded — 13 files with function signatures, docstrings, imports, and `raise NotImplementedError(...)` placeholders. Your job is to **replace every `NotImplementedError` with working code** by porting logic from the monolithic `context_refinery/triage.py` (681 lines).

## Quick orientation
```
context_refinery/
├── triage.py              ← MONOLITH (read this first, delete when done)
└── triage/                ← SCAFFOLD (fill these in)
    ├── __init__.py        ✅ complete — do not touch
    ├── __main__.py        ✅ complete — do not touch
    ├── terminal.py        ❌ 3 functions stubbed
    ├── writers.py         ❌ 6 functions stubbed
    ├── review.py          ❌ 2 functions stubbed
    ├── runner.py          ❌ 3 functions stubbed
    └── passes/
        ├── __init__.py    ✅ complete — do not touch
        ├── base.py        ✅ complete — do not touch
        ├── status.py      ❌ 2 methods stubbed
        ├── doctype.py     ❌ 2 methods stubbed
        ├── tags.py        ❌ 2 methods stubbed
        ├── projects.py    ❌ 2 methods stubbed
        └── links.py       ❌ 2 methods stubbed (NEW feature, see spec)
```

## How to work
1. **Read `context_refinery/triage.py` first** — every stub has a comment like `"JULES: Copy from triage.py lines 89-117"` telling you exactly where to look.
2. **Read the full spec** at `project-docs/jules-spec-modular-triage-system.md` — it has a file-by-file table with source line ranges and implementation notes.
3. Implement bottom-up: `terminal.py` → `writers.py` → `passes/*.py` → `review.py` → `runner.py`
4. **Delete `context_refinery/triage.py`** after everything works.

## Rules
- **DO NOT** create new files (except `tests/test_triage_modular.py`)
- **DO NOT** change function signatures, class names, or import structure
- **DO NOT** modify files marked ✅ above
- **DO NOT** add dependencies beyond `rich`, `pyyaml`, and stdlib
- **DO NOT** use async/await — this is a synchronous terminal tool
- **DO NOT** modify files outside `context_refinery/triage/` and `tests/`

## One thing the spec doesn't mention
The Obsidian triage inbox script (separate project) uses `0-9` then `a-z` for single-keypress selection when there are 10+ options. Apply the same pattern here — in `terminal.py`, add a constant:
```python
import string
KEYS = list(string.digits) + list(string.ascii_lowercase)  # 36 single-keypress slots
```
Use `KEYS` anywhere a pass needs to map numbered options to keypresses (tags, projects, links). This avoids the double-digit input problem entirely.

## Verification
```bash
# 1. No stubs remain
grep -r "NotImplementedError" context_refinery/triage/ && echo "FAIL: stubs remain" || echo "PASS"

# 2. Import works
python3 -c "from context_refinery.triage import main" && echo "PASS"

# 3. Monolith deleted
[ ! -f context_refinery/triage.py ] && echo "PASS: monolith deleted" || echo "FAIL"

# 4. Tests pass
python3 -m pytest tests/test_triage_modular.py -v

# 5. Smoke test (needs a directory with .md files)
python3 -m context_refinery.triage --help
```

## Key references
- `project-docs/jules-spec-modular-triage-system.md` — detailed file-by-file spec
- `context_refinery/triage.py` — monolith source (lines referenced in all stubs)
- `context_refinery/triage/passes/base.py` — abstract base class contract
- `docs/01-taxonomy.md` — valid status/doc_type values
