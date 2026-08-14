# build-corpus

## Goal
Build a fresh, regenerable corpus snapshot from the validated decision set only.

## Inputs
- `01-decisions/output/decisions-validated.json` (from `validate-decision-set`; require `validation-report.md` first line `status: pass`)
- `01-decisions/output/validation-report.md`
- `02-corpus/CONTEXT.md`
- `docs/CONTEXT.md`

## Output
- **Path:** `02-corpus/output/corpus-snapshot/`
- **Shape:**
```text
02-corpus/output/corpus-snapshot/
  BUILD.json
  manifest.json
  documents/
```
- `BUILD.json` — input path, UTC timestamp, builder id/command, snapshot checksum.
- `manifest.json` — source artifact path + checksum; document count; one entry per file under `documents/` (relative path + checksum).
- `documents/` — one file per validated decision, derived only from the input set.

Overwrite this tree on each run. No live Khoj writes.

## Verification
```sh
test -s 01-decisions/output/validation-report.md
grep -q '^status: pass$' 01-decisions/output/validation-report.md
test -s 01-decisions/output/decisions-validated.json
test -s 02-corpus/output/corpus-snapshot/BUILD.json
test -s 02-corpus/output/corpus-snapshot/manifest.json
test -d 02-corpus/output/corpus-snapshot/documents
```
Also confirm manifest source checksum matches `decisions-validated.json`, and document count equals validated-set size with every manifest path present.

## Authoritative sources
- `01-decisions/output/decisions-validated.json`
- `02-corpus/CONTEXT.md`
- `docs/CONTEXT.md`
- `project-docs/corpus-work-2026-08/CORPUS-TARGET-SHAPE.md` (scope pointer only)

## Dependencies
- `validate-decision-set` → `01-decisions/output/decisions-validated.json`

## Stop conditions
- Validated set or passing validation report missing: stop and report.
- About to invent members, bodies, or substitute another source tree: stop.
- Write only under `02-corpus/output/corpus-snapshot/`.
