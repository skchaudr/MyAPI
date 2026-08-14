# 04-evaluation — Room Map

Stage H–I of Part 1: run the fixed evaluation intents against the ingested corpus and preserve raw answers plus evidence.

## Purpose

Execute the predetermined five-intent set and capture results. Part 1 stops after preservation — quality is measured, not gated.

## Layout

| Path | Role |
|---|---|
| `queries/` | Query stubs or runners bound to the five fixed intents |
| `tasks/` | Per-node task contracts |
| `results/` | Raw answers, retrieved evidence, run metadata |

## Task contracts (GDDP node → file)

| Node theme | Contract |
|---|---|
| factual + rationale | `tasks/eval-factual-rationale.md` |
| supersession + relationship | `tasks/eval-supersession-relationship.md` |
| negative control | `tasks/eval-negative-control.md` |
| preserve results | `tasks/preserve-results.md` |

## Fixed intents (from Part 1 memo only)

1. Factual decision  
2. Rationale  
3. Supersession  
4. Relationship  
5. Negative control — confident unsupported answers are first-class results  

## Upstream

Ingest/verify evidence from `03-ingestion/output/` and the live Khoj target named there.

## Rules

- Do not invent additional eval queries beyond the five memo intents.
- Preserve raw system output and retrieval evidence; do not silently cleanse failures.
- After `preserve-results`, Part 1 ends.
