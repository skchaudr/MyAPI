# preserve-results

## Goal
Bundle the three eval artifacts, raw answers, retrieved evidence, and run metadata into the final Part 1 results package. Part 1 ends when this package verifies.

## Inputs
- `04-evaluation/results/eval-factual-rationale.md`
- `04-evaluation/results/eval-supersession-relationship.md`
- `04-evaluation/results/eval-negative-control.md`
- `03-ingestion/output/ingest-receipt.md`
- `03-ingestion/output/retrieval-smoke.md`
- `04-evaluation/CONTEXT.md`
- `docs/CONTEXT.md`

## Output
- **Path:** `04-evaluation/results/part1-package/`
- **Shape:**
  - `manifest.md` — package identity; Khoj target from ingest receipt; index of all five memo intents; pointers to bundled files
  - `eval-factual-rationale.md` — copy of intent 1–2 result
  - `eval-supersession-relationship.md` — copy of intent 3–4 result
  - `eval-negative-control.md` — copy of intent 5 result
  - `run-metadata.md` — ingest target id, receipt pointer, eval timestamps, executor, source paths

Copy raw answers and retrieved evidence without cleansing failures. Manifest must list intents 1–5 by name: factual decision, rationale, supersession, relationship, negative control.

## Verification
```sh
test -s 04-evaluation/results/part1-package/manifest.md
test -s 04-evaluation/results/part1-package/eval-factual-rationale.md
test -s 04-evaluation/results/part1-package/eval-supersession-relationship.md
test -s 04-evaluation/results/part1-package/eval-negative-control.md
test -s 04-evaluation/results/part1-package/run-metadata.md
grep -qi 'Factual decision' 04-evaluation/results/part1-package/manifest.md
grep -qi 'Rationale' 04-evaluation/results/part1-package/manifest.md
grep -qi 'Supersession' 04-evaluation/results/part1-package/manifest.md
grep -qi 'Relationship' 04-evaluation/results/part1-package/manifest.md
grep -qi 'Negative control' 04-evaluation/results/part1-package/manifest.md
```
Pass = package files exist and the manifest indexes all five memo intents. Do not score answers.

## Authoritative sources
- `docs/CONTEXT.md`
- `04-evaluation/CONTEXT.md`
- `AGENTS.md`
- operator memo Part 1
- Eval results under `04-evaluation/results/`
- Khoj target named in `03-ingestion/output/ingest-receipt.md`

## Dependencies
- `eval-factual-rationale` → `04-evaluation/results/eval-factual-rationale.md`
- `eval-supersession-relationship` → `04-evaluation/results/eval-supersession-relationship.md`
- `eval-negative-control` → `04-evaluation/results/eval-negative-control.md`
- `khoj-ingest` → `03-ingestion/output/ingest-receipt.md`
- `verify-retrieval` → `03-ingestion/output/retrieval-smoke.md`

## Stop conditions
- Any input eval result missing: stop and report; do not invent answers or evidence.
- Would add an intent beyond the memo five, or rewrite/cleanse raw answers: stop.
- Package written and verification passes: Part 1 ends. Do not start another stage.
