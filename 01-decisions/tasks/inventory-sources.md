# inventory-sources

## Goal
Inventory authoritative sources that may contain Part 1 decisions. Produce a structured inventory for extraction; do not extract decision bodies here.

## Inputs
- `01-decisions/CONTEXT.md`
- `docs/CONTEXT.md`
- `PROJECT-BRIEF.md`
- `project-docs/`
- `01-decisions/inputs/`
- operator memo Part 1 (`GDDP v MyAPI Part 1 - the first slice.md`, operator repos)

## Output
- **Path:** `01-decisions/output/sources-inventory.md`
- **Shape:** Structured markdown inventory. Columns/entry format are chosen at execution; this contract does **not** pre-list sources.

## Verification
```sh
test -s 01-decisions/output/sources-inventory.md
grep -qE '^#{1,3} |^- ' 01-decisions/output/sources-inventory.md
```

## Authoritative sources
- `project-docs/`
- `PROJECT-BRIEF.md`
- operator memo Part 1
- `docs/CONTEXT.md`
- `01-decisions/CONTEXT.md`

## Dependencies
- None (may run in parallel with `decision-schema`).

## Stop conditions
- No authoritative source can be inventoried: stop and report; do not fabricate entries.
- Write only the named output path. Do not extract decisions or author schema fields.
