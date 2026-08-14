# 02-corpus — Room Map

Stage D–E of Part 1: build a fresh corpus snapshot from validated decisions, then transform it into the exact Khoj-ingestible representation.

## Purpose

Turn the canonical decision set into a reproducible corpus bundle and a Khoj-ready transform. No live Khoj writes happen here.

## Layout

| Path | Role |
|---|---|
| `inputs/` | Optional staged copies or manifests pulled from `01-decisions/output/` |
| `tasks/` | Per-node task contracts |
| `output/` | Corpus snapshot + Khoj transform artifacts for `03-ingestion/` |

## Task contracts (GDDP node → file)

| Node theme | Contract |
|---|---|
| build corpus | `tasks/build-corpus.md` |
| corpus repro check | `tasks/corpus-repro-check.md` |
| khoj transform | `tasks/khoj-transform.md` |

## Upstream / downstream

- **In:** validated decision artifacts from `01-decisions/output/` (paths fixed in each task contract).
- **Out:** reproducible corpus + transform under `output/` for `03-ingestion/`.

## Rules

- Corpus must be regenerable from the validated decision set alone.
- Do not pre-list document bodies or invent corpus membership beyond contract inputs.
- Transform output must match what the ingestion room expects to load.
