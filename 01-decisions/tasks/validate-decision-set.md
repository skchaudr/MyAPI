# validate-decision-set

## Goal
Validate the normalized set for completeness, structure, and canonical status. Emit the validated decision set that `02-corpus/` consumes.

## Inputs
- `01-decisions/output/decision-schema.json`
- `01-decisions/output/decisions-normalized.json`
- `01-decisions/output/sources-inventory.md`
- `01-decisions/CONTEXT.md`
- `docs/CONTEXT.md`

## Output
- **Path:** `01-decisions/output/decisions-validated.json`
  - **Shape:** Validated canonical decision set — sole decision input to `02-corpus/`. Object bodies follow the schema; not prescribed here.
- **Path:** `01-decisions/output/validation-report.md`
  - **Shape:** Report of completeness, structure, and canonical-status checks. First line MUST be `status: pass` or `status: fail`.

## Verification
```sh
test -s 01-decisions/output/validation-report.md
grep -qE '^status: (pass|fail)$' 01-decisions/output/validation-report.md
if grep -q '^status: pass$' 01-decisions/output/validation-report.md; then
  test -s 01-decisions/output/decisions-validated.json
  python3 -c "import json; d=json.load(open('01-decisions/output/decisions-validated.json')); assert d is not None"
else
  test ! -e 01-decisions/output/decisions-validated.json
fi
```

## Authoritative sources
- `01-decisions/output/decision-schema.json`
- `01-decisions/output/decisions-normalized.json`
- `01-decisions/output/sources-inventory.md`
- operator memo Part 1

## Dependencies
- `normalize-decisions` → `01-decisions/output/decisions-normalized.json`
- `decision-schema` → `01-decisions/output/decision-schema.json`
- `inventory-sources` → `01-decisions/output/sources-inventory.md`

## Stop conditions
- Required input missing: stop and report.
- Any completeness/structure/canonical check fails: write `status: fail`, omit `decisions-validated.json`, stop. Do not hand a failed set to `02-corpus/`.
- Write only the named output paths. Do not start corpus, ingestion, or evaluation work.
