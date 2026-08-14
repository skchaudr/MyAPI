# eval-factual-rationale

## Goal
Run memo intents 1 and 2 (factual decision, rationale) against the ingested corpus on the Khoj target named by ingest. Record raw answers and retrieval evidence; quality is observed, not gated.

## Inputs
- `03-ingestion/output/ingest-receipt.md`
- `03-ingestion/output/retrieval-smoke.md`
- `02-corpus/output/corpus-snapshot/`
- `02-corpus/output/khoj-ready/`
- `04-evaluation/CONTEXT.md`
- `docs/CONTEXT.md`

## Output
- **Path:** `04-evaluation/results/eval-factual-rationale.md`
- **Shape:** One file, two sections, in order:
  1. Intent 1 — Factual decision
  2. Intent 2 — Rationale

Each section must contain:
- Intent name
- Query text (as executed)
- Raw answer (verbatim system output)
- Retrieved evidence (verbatim retrieval payload)
- Run metadata: Khoj target id, receipt pointer, timestamp, executor
- Quality notes (observation only)

Choose one query per intent **at execution** from corpus content. Write executed query text only in this result file — not in this contract.

## Verification
```sh
test -s 04-evaluation/results/eval-factual-rationale.md
grep -q 'Intent 1 — Factual decision' 04-evaluation/results/eval-factual-rationale.md
grep -q 'Intent 2 — Rationale' 04-evaluation/results/eval-factual-rationale.md
grep -q 'Query text (as executed)' 04-evaluation/results/eval-factual-rationale.md
grep -q 'Raw answer' 04-evaluation/results/eval-factual-rationale.md
grep -q 'Retrieved evidence' 04-evaluation/results/eval-factual-rationale.md
grep -q 'Run metadata' 04-evaluation/results/eval-factual-rationale.md
```
Pass = file present with both intents and required headings. Do not score answers.

## Authoritative sources
- `docs/CONTEXT.md`
- `04-evaluation/CONTEXT.md`
- `AGENTS.md`
- operator memo Part 1
- Khoj target named in `03-ingestion/output/ingest-receipt.md`
- Corpus under `02-corpus/output/`

## Dependencies
- `khoj-ingest` → `03-ingestion/output/ingest-receipt.md`
- `verify-retrieval` → `03-ingestion/output/retrieval-smoke.md`

## Stop conditions
- Any input missing: stop and report.
- Ingest receipt does not name a target: stop and report.
- Retrieval smoke absent/failed: stop; do not start the five-intent set.
- Would pre-write query strings into this contract or a query-canon file: stop.
- Target unreachable: write the failed run into the result and stop further intents in this task.
