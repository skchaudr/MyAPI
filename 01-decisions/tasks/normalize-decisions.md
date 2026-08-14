# normalize-decisions

## Goal
Normalize extracted decision candidates onto the canonical schema. Emit one schema-conforming object set for validation.

## Inputs
- `01-decisions/output/decision-schema.json`
- `01-decisions/output/decisions-raw.json`
- `01-decisions/CONTEXT.md`
- `docs/CONTEXT.md`

## Output
- **Path:** `01-decisions/output/decisions-normalized.json`
- **Shape:** JSON decision objects normalized to `decision-schema.json`. Values come from extract output; they are not prescribed here.

## Verification
```sh
test -s 01-decisions/output/decisions-normalized.json
python3 -c "import json; d=json.load(open('01-decisions/output/decisions-normalized.json')); assert d is not None"
```

## Authoritative sources
- `01-decisions/output/decision-schema.json`
- `01-decisions/output/decisions-raw.json`
- operator memo Part 1

## Dependencies
- `extract-decisions` → `01-decisions/output/decisions-raw.json`
- `decision-schema` → `01-decisions/output/decision-schema.json`

## Stop conditions
- Schema or raw-extract artifact missing: stop and report.
- A raw object cannot be mapped onto the schema: stop and report; do not drop it without record and do not invent values.
- Write only the named output path.
