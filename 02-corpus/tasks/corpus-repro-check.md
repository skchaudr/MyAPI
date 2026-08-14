# corpus-repro-check

## Goal
Prove `02-corpus/output/corpus-snapshot/` regenerates identically from the same validated decision set. Record the check; do not hand-edit the snapshot to force a pass.

## Inputs
- `02-corpus/output/corpus-snapshot/BUILD.json`
- `02-corpus/output/corpus-snapshot/manifest.json`
- `02-corpus/output/corpus-snapshot/documents/`
- `01-decisions/output/decisions-validated.json`
- `02-corpus/tasks/build-corpus.md` (rebuild procedure pointer)

## Output
- **Path:** `02-corpus/output/repro-check.json`
- **Shape:**
```json
{
  "pass": true,
  "input": "01-decisions/output/decisions-validated.json",
  "input_checksum": "",
  "first_snapshot_checksum": "",
  "second_snapshot_checksum": "",
  "mismatched_paths": []
}
```
`mismatched_paths` lists relative paths whose checksums differ. Keep `pass` false when that list is non-empty.

Rebuild into a throwaway directory; do not clobber `corpus-snapshot/` until compare finishes. Discard the throwaway tree after writing the receipt.

## Verification
```sh
test -s 02-corpus/output/repro-check.json
python3 -c "import json; r=json.load(open('02-corpus/output/repro-check.json')); assert r.get('pass') is True; assert r.get('first_snapshot_checksum') and r['first_snapshot_checksum']==r.get('second_snapshot_checksum'); assert r.get('mismatched_paths')==[]"
```

## Authoritative sources
- `02-corpus/tasks/build-corpus.md`
- `01-decisions/output/decisions-validated.json`
- `02-corpus/CONTEXT.md`
- `docs/CONTEXT.md`

## Dependencies
- `build-corpus` → `02-corpus/output/corpus-snapshot/`

## Stop conditions
- Snapshot or validated set missing: stop and report.
- Rebuild command unknown / not recorded in `BUILD.json`: stop and report.
- Checksums differ: write failing receipt (`pass: false`) and stop; do not patch files.
