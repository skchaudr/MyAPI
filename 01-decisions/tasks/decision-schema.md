# decision-schema

## Goal
Define the canonical decision-object shape for Part 1. Later decision tasks must conform to this schema and must not invent a second shape.

## Inputs
- `01-decisions/CONTEXT.md`
- `docs/CONTEXT.md`
- `PROJECT-BRIEF.md`
- `project-docs/` (read-only scan roots as needed)
- operator memo Part 1 (`GDDP v MyAPI Part 1 - the first slice.md`, operator repos)

## Output
- **Path:** `01-decisions/output/decision-schema.json`
- **Shape:** JSON schema document authored by the executing agent. Field names and constraints are **not** prescribed in this contract.

## Verification
```sh
test -s 01-decisions/output/decision-schema.json
python3 -c "import json; d=json.load(open('01-decisions/output/decision-schema.json')); assert isinstance(d, dict) and d"
```

## Authoritative sources
- `project-docs/`
- `PROJECT-BRIEF.md`
- operator memo Part 1
- `docs/CONTEXT.md`
- `01-decisions/CONTEXT.md`

## Dependencies
- None (first task in the decisions room; may run in parallel with `inventory-sources`).

## Stop conditions
- Required read roots missing: stop and report; do not invent a schema from memory alone.
- Sources conflict on more than one viable canonical shape: stop and report; do not guess.
- Write only the named output path.
