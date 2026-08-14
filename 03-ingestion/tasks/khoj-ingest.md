# khoj-ingest

## Goal
Load the Khoj-ready transform from `02-corpus/output/khoj-ready/` into a clean Part 1 target corpus. Write an ingest receipt that names the target actually used.

## Inputs
- `02-corpus/output/khoj-ready/`
- `02-corpus/output/khoj-ready/TRANSFORM.json`
- `02-corpus/output/khoj-ready/manifest.json`
- `03-ingestion/CONTEXT.md`
- `docs/CONTEXT.md`

## Output
- **Path:** `03-ingestion/output/ingest-receipt.md`
- **Shape:** Markdown receipt with these sections, in order:
  1. **Status** — `success` or `failed`
  2. **Source** — transform path, file count, content hash of `02-corpus/output/khoj-ready/`
  3. **Target identity** — corpus/index/collection name or id actually written
  4. **Method** — script or API entrypoint used (name only)
  5. **Timing** — started and finished timestamps
  6. **Errors** — verbatim failures, or `none`

Do not embed hostnames, credentials, tokens, or connection strings.

## Verification
```sh
test -d 02-corpus/output/khoj-ready
test -s 02-corpus/output/khoj-ready/TRANSFORM.json
test -s 03-ingestion/output/ingest-receipt.md
grep -qE '^\*\*Status\*\* — success$' 03-ingestion/output/ingest-receipt.md || grep -qE '^## Status$|Status.*success' 03-ingestion/output/ingest-receipt.md
grep -qi 'Target identity' 03-ingestion/output/ingest-receipt.md
```
Confirm source file count in the receipt matches `find 02-corpus/output/khoj-ready -type f | wc -l`.

## Authoritative sources
- `03-ingestion/CONTEXT.md`
- `docs/CONTEXT.md`
- `docs/02-target-output.md`
- `deploy_to_khoj.sh`
- `scripts/reindex_khoj_safe.py`
- `scripts/khoj_reindex_resume_index.py`
- `scripts/khoj_index_diff.py`
- `project-docs/source-of-truth-anchors/` (Khoj/deploy anchors if present)

Read for procedure only. Do not copy live credentials or hostnames into artifacts.

## Dependencies
- `khoj-transform` → `02-corpus/output/khoj-ready/`

## Stop conditions
- Input transform missing/empty: stop and report; do not invent a bundle.
- No clean Part 1 target can be named without guessing: stop and report.
- Write would hit graph truth or a non-Khoj runtime database: stop and report.
- Ingest fails: write **Status** `failed` plus verbatim errors, then stop.
