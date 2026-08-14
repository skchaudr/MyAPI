# khoj-transform

## Goal
Transform the reproducible corpus snapshot into the exact Khoj-ingestible tree that `03-ingestion` loads. No live Khoj writes.

## Inputs
- `02-corpus/output/corpus-snapshot/` (`BUILD.json`, `manifest.json`, `documents/`)
- `02-corpus/output/repro-check.json` (must have `"pass": true`)
- `docs/02-target-output.md`
- `docs/01-taxonomy.md`
- `02-corpus/CONTEXT.md`
- `03-ingestion/CONTEXT.md`

## Output
- **Path:** `02-corpus/output/khoj-ready/`
- **Shape:**
```text
02-corpus/output/khoj-ready/
  TRANSFORM.json
  manifest.json
  notes/
```
- `TRANSFORM.json` — source snapshot checksum, UTC timestamp, transform id/command, output checksum.
- `manifest.json` — one entry per ingestible file: relative path, checksum, source document path under `corpus-snapshot/documents/`.
- `notes/` — Khoj-ingestible files only; membership equals the snapshot; format follows `docs/02-target-output.md`.

Do not add, drop, or author new decision text.

## Verification
```sh
test -s 02-corpus/output/repro-check.json
python3 -c "import json; assert json.load(open('02-corpus/output/repro-check.json')).get('pass') is True"
test -s 02-corpus/output/khoj-ready/TRANSFORM.json
test -s 02-corpus/output/khoj-ready/manifest.json
test -d 02-corpus/output/khoj-ready/notes
```
Also confirm note count equals snapshot document count and taxonomy strings, when present, come from `docs/01-taxonomy.md`.

## Authoritative sources
- `docs/02-target-output.md`
- `docs/01-taxonomy.md`
- `02-corpus/output/corpus-snapshot/`
- `03-ingestion/CONTEXT.md`
- `02-corpus/CONTEXT.md`

## Dependencies
- `build-corpus` → `02-corpus/output/corpus-snapshot/`
- `corpus-repro-check` → `02-corpus/output/repro-check.json`

## Stop conditions
- Snapshot or passing repro-check missing: stop and report.
- Target format / taxonomy docs missing: stop and report.
- Transform would invent members or rewrite decision content: stop.
- Write only under `02-corpus/output/khoj-ready/`.
