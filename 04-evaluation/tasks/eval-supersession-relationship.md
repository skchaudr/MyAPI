# eval-supersession-relationship

## Goal
Run memo intents 3 and 4 (supersession, relationship) against the ingested corpus on the Khoj target named by ingest. Record raw answers and retrieval evidence; quality is observed, not gated.

## Inputs
- `03-ingestion/output/ingest-receipt.md`
- `03-ingestion/output/retrieval-smoke.md`
- `02-corpus/output/corpus-snapshot/`
- `02-corpus/output/khoj-ready/`
- `04-evaluation/results/eval-factual-rationale.md`
- `04-evaluation/CONTEXT.md`
- `docs/CONTEXT.md`

## Output
- **Path:** `04-evaluation/results/eval-supersession-relationship.md`
- **Shape:** One file, two sections, in order:
  1. Intent 3 — Supersession
  2. Intent 4 — Relationship

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
test -s 04-evaluation/results/eval-supersession-relationship.md
grep -q 'Intent 3 — Supersession' 04-evaluation/results/eval-supersession-relationship.md
grep -q 'Intent 4 — Relationship' 04-evaluation/results/eval-supersession-relationship.md
grep -q 'Query text (as executed)' 04-evaluation/results/eval-supersession-relationship.md
grep -q 'Raw answer' 04-evaluation/results/eval-supersession-relationship.md
grep -q 'Retrieved evidence' 04-evaluation/results/eval-supersession-relationship.md
grep -q 'Run metadata' 04-evaluation/results/eval-supersession-relationship.md
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
- `eval-factual-rationale` → `04-evaluation/results/eval-factual-rationale.md`
- `khoj-ingest` → `03-ingestion/output/ingest-receipt.md`
- `verify-retrieval` → `03-ingestion/output/retrieval-smoke.md`

## Stop conditions
- Any input missing: stop and report.
- Would pre-write query strings into this contract or a query-canon file: stop.
- Target unreachable: write the failed run into the result and stop further intents in this task.
