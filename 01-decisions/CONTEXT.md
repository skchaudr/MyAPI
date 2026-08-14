# 01-decisions — Room Map

Stage A–C of Part 1: establish decision schema, extract/normalize from authoritative sources, validate the decision set.

## Purpose

Produce a canonical, validated decision-object snapshot. Later rooms consume only this room’s outputs — not raw upstream notes.

## Layout

| Path | Role |
|---|---|
| `inputs/` | Staged pointers or copies of source material for extraction |
| `tasks/` | Per-node task contracts |
| `output/` | Durable decision artifacts for `02-corpus/` |

## Task contracts (GDDP node → file)

| Node theme | Contract |
|---|---|
| decision schema | `tasks/decision-schema.md` |
| inventory sources | `tasks/inventory-sources.md` |
| extract decisions | `tasks/extract-decisions.md` |
| normalize decisions | `tasks/normalize-decisions.md` |
| validate decision set | `tasks/validate-decision-set.md` |

## Downstream

Validated decision set under `output/` is the sole decision input to `02-corpus/`.

## Rules

- Contracts name inputs, exact output paths/shapes, and verification — they do not pre-answer schema fields or source lists.
- Prefer authoritative project sources over reconstructed memory.
- Keep artifacts machine-checkable where the contract requires it.
