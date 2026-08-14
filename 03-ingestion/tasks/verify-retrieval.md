# verify-retrieval

## Goal
Confirm the ingested Part 1 corpus is present on the target named by the ingest receipt and that basic retrieval smoke works. Do **not** run the five memo evaluation intents.

## Inputs
- `03-ingestion/output/ingest-receipt.md`
- The Khoj target named in that receipt’s **Target identity**
- `02-corpus/output/khoj-ready/` (presence cross-check only)
- `03-ingestion/CONTEXT.md`
- `docs/CONTEXT.md`

## Output
- **Path:** `03-ingestion/output/retrieval-smoke.md`
- **Shape:** Markdown evidence with these sections, in order:
  1. **Status** — `success` or `failed`
  2. **Target identity** — copied from the ingest receipt
  3. **Presence** — document/index count observed; whether it matches receipt source file count
  4. **Smoke** — one presence/identity probe (probe text as run, raw response, timestamp)
  5. **Errors** — verbatim failures, or `none`

Do not embed hostnames, credentials, tokens, or connection strings.

## Verification
```sh
test -s 03-ingestion/output/ingest-receipt.md
test -s 03-ingestion/output/retrieval-smoke.md
grep -qi 'Target identity' 03-ingestion/output/retrieval-smoke.md
grep -qi 'Presence' 03-ingestion/output/retrieval-smoke.md
grep -qi 'Smoke' 03-ingestion/output/retrieval-smoke.md
```
Confirm smoke target identity matches the ingest receipt, presence count is non-zero on success, and the smoke probe is not one of the five memo intents (factual decision, rationale, supersession, relationship, negative control).

## Authoritative sources
- `03-ingestion/CONTEXT.md`
- `04-evaluation/CONTEXT.md` (boundary only: five intents belong downstream)
- `docs/CONTEXT.md`
- `deploy_to_khoj.sh`
- `scripts/reindex_khoj_safe.py`
- `scripts/khoj_index_diff.py`

## Dependencies
- `khoj-ingest` → `03-ingestion/output/ingest-receipt.md`

## Stop conditions
- Ingest receipt missing or not success: stop and report.
- Target identity unreadable: stop and report; do not pick another corpus.
- Work would run the five memo intents: stop (those belong to `04-evaluation/`).
- Target unreachable: write **Status** `failed` plus verbatim errors, then stop.
