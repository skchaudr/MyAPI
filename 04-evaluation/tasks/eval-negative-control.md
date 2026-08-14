# eval-negative-control

## Goal
Run memo intent 5 (negative control) against the ingested corpus. Record the raw answer and retrieval evidence. A confident unsupported answer is a first-class result.

## Inputs
- `03-ingestion/output/ingest-receipt.md`
- `03-ingestion/output/retrieval-smoke.md`
- `02-corpus/output/corpus-snapshot/`
- `02-corpus/output/khoj-ready/`
- `04-evaluation/results/eval-factual-rationale.md`
- `04-evaluation/results/eval-supersession-relationship.md`
- `04-evaluation/CONTEXT.md`
- `docs/CONTEXT.md`

## Output
- **Path:** `04-evaluation/results/eval-negative-control.md`
- **Shape:** One section — Intent 5 — Negative control — with:
  - Intent name
  - Intent meaning (one sentence): ask for a fact the ingested corpus cannot support; keep whatever the system returns
  - Query text (as executed)
  - Raw answer (verbatim system output)
  - Retrieved evidence (verbatim retrieval payload)
  - Run metadata: Khoj target id, receipt pointer, timestamp, executor
  - Quality notes (observation only)

Choose the query **at execution** after inspecting corpus content so the ask sits outside that support. Write executed query text only in this result file — not in this contract.

## Verification
```sh
test -s 04-evaluation/results/eval-negative-control.md
grep -q 'Intent 5 — Negative control' 04-evaluation/results/eval-negative-control.md
grep -q 'Query text (as executed)' 04-evaluation/results/eval-negative-control.md
grep -q 'Raw answer' 04-evaluation/results/eval-negative-control.md
grep -q 'Retrieved evidence' 04-evaluation/results/eval-negative-control.md
grep -q 'Run metadata' 04-evaluation/results/eval-negative-control.md
```
Pass = file present with intent 5 and required headings. Do not score answers. Do not treat an unsupported or confident-wrong answer as task failure.

## Authoritative sources
- `docs/CONTEXT.md`
- `04-evaluation/CONTEXT.md`
- `AGENTS.md`
- operator memo Part 1
- Khoj target named in `03-ingestion/output/ingest-receipt.md`
- Corpus under `02-corpus/output/`

## Dependencies
- `eval-factual-rationale` → `04-evaluation/results/eval-factual-rationale.md`
- `eval-supersession-relationship` → `04-evaluation/results/eval-supersession-relationship.md`
- `khoj-ingest` → `03-ingestion/output/ingest-receipt.md`
- `verify-retrieval` → `03-ingestion/output/retrieval-smoke.md`

## Stop conditions
- Any input missing: stop and report.
- Would pre-write the negative-control question into this contract or a query-canon file: stop.
- Target unreachable: write the failed run into the result and stop.
- Do not discard or rewrite a confident unsupported answer.
