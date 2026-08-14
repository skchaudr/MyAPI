# 03-ingestion — Room Map

Stage F–G of Part 1: ingest the Khoj-ready corpus into a clean target and verify basic retrieval behavior.

## Purpose

Load the snapshot produced by `02-corpus/` into Khoj (or the designated Khoj target) and confirm presence plus smoke-level retrieval — not the fixed evaluation set.

## Layout

| Path | Role |
|---|---|
| `tasks/` | Per-node task contracts |
| `output/` | Ingest receipts, target ids, retrieval smoke evidence |

## Task contracts (GDDP node → file)

| Node theme | Contract |
|---|---|
| khoj ingest | `tasks/khoj-ingest.md` |
| verify retrieval | `tasks/verify-retrieval.md` |

## Upstream / downstream

- **In:** Khoj transform / corpus bundle from `02-corpus/output/`.
- **Out:** ingest + verification evidence under `output/` for `04-evaluation/`.

## Rules

- Prefer a clean target corpus for Part 1; record target identity in the ingest receipt.
- Verification here is presence and basic retrieve-ability, not the five eval intents.
- Do not modify graph truth databases; only the designated Khoj target named by the contract.
