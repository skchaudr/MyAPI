# extract-decisions

## Goal
Extract decision candidates from inventoried sources into raw objects. Capture candidates as found; do not normalize to the schema in this task.

## Inputs
- `01-decisions/output/decision-schema.json`
- `01-decisions/output/sources-inventory.md`
- Source paths recorded in `01-decisions/output/sources-inventory.md`
- `01-decisions/inputs/`
- `01-decisions/CONTEXT.md`
- `docs/CONTEXT.md`

## Output
- **Path:** `01-decisions/output/decisions-raw.json`
- **Shape:** JSON document of raw decision-candidate objects. Bodies/fields are not prescribed here.

## Verification
```sh
test -s 01-decisions/output/decisions-raw.json
python3 -c "import json; d=json.load(open('01-decisions/output/decisions-raw.json')); assert d is not None"
```

## Authoritative sources
- Paths named by `01-decisions/output/sources-inventory.md`
- `01-decisions/output/decision-schema.json` (shape reference only)
- operator memo Part 1

## Dependencies
- `decision-schema` → `01-decisions/output/decision-schema.json`
- `inventory-sources` → `01-decisions/output/sources-inventory.md`

## Stop conditions
- Schema or inventory missing: stop and report.
- An inventoried source path is missing: stop and report; skip nothing silently.
- Zero candidates found: stop and report; do not fabricate objects.
- Write only the named output path.
