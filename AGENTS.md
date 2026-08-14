# AGENTS.md — Part 1 ICM Routing Map

Fresh agent entrypoint for MyAPI Part 1. GDDP schedules; this map routes.

## Load order

1. This file (where to go)
2. `docs/CONTEXT.md` (slice boundary)
3. Room `CONTEXT.md` (what the stage means)
4. Exactly one `tasks/<task>.md` named by the node (what to do)

## Node id → room → contract

Match the GDDP `node_id` / task slug against the table. One hop from this map reaches the room; the room CONTEXT names the contract file.

### 01-decisions/

| Task slug | Contract |
|---|---|
| `decision-schema` | `01-decisions/tasks/decision-schema.md` |
| `inventory-sources` | `01-decisions/tasks/inventory-sources.md` |
| `extract-decisions` | `01-decisions/tasks/extract-decisions.md` |
| `normalize-decisions` | `01-decisions/tasks/normalize-decisions.md` |
| `validate-decision-set` | `01-decisions/tasks/validate-decision-set.md` |

Room map: `01-decisions/CONTEXT.md`

### 02-corpus/

| Task slug | Contract |
|---|---|
| `build-corpus` | `02-corpus/tasks/build-corpus.md` |
| `corpus-repro-check` | `02-corpus/tasks/corpus-repro-check.md` |
| `khoj-transform` | `02-corpus/tasks/khoj-transform.md` |

Room map: `02-corpus/CONTEXT.md`

### 03-ingestion/

| Task slug | Contract |
|---|---|
| `khoj-ingest` | `03-ingestion/tasks/khoj-ingest.md` |
| `verify-retrieval` | `03-ingestion/tasks/verify-retrieval.md` |

Room map: `03-ingestion/CONTEXT.md`

### 04-evaluation/

| Task slug | Contract |
|---|---|
| `eval-factual-rationale` | `04-evaluation/tasks/eval-factual-rationale.md` |
| `eval-supersession-relationship` | `04-evaluation/tasks/eval-supersession-relationship.md` |
| `eval-negative-control` | `04-evaluation/tasks/eval-negative-control.md` |
| `preserve-results` | `04-evaluation/tasks/preserve-results.md` |

Room map: `04-evaluation/CONTEXT.md`

## Stage sequence

`01-decisions → 02-corpus → 03-ingestion → 04-evaluation → stop`

Do not skip upstream artifacts. If a required input path is missing, stop and report; do not invent replacements.

## Contract shape (every task file)

Each `tasks/*.md` must state:

- **Inputs** — exact paths
- **Output** — exact artifact path and shape
- **Verification** — command or check
- **Authoritative sources** — pointers only (no pre-answered schema/sources/queries)

## Global constraints (Part 1)

- Scaffold and stage agents create markdown/artifacts only where contracts allow.
- Never modify graph truth or runtime databases unless a later contract explicitly names a Khoj target.
- Evaluation uses only the memo’s five fixed intents.
- Answer quality is recorded; it is not a completion gate.

## Rebuild / project docs

Broader rebuild operating notes live under `project-docs/`, `PROJECT-BRIEF.md`, and related trees. Part 1 execution stays inside the four rooms above unless a task contract points elsewhere for read-only authoritative input.
