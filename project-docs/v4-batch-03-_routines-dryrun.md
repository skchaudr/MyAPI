# Vault Schema V4 Normalization Dry Run

Vault root: `/Users/saboor/Obsidian/SoloDeveloper`

## Summary

- Total files scanned: 2
- High confidence: 0
- Medium confidence: 0
- Needs review: 2

## Review Queue

### _routines/jobs-seen.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `_routines` maps to `resources/`
- Review needed: missing area/project/concept connection; unprefixed tag `routine`; unprefixed tag `jobs-scout`; unprefixed tag `ledger`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: _routines
migration_status: v4-dry-run
```

### _routines/lessons-covered.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `_routines` maps to `resources/`
- Review needed: missing area/project/concept connection; unprefixed tag `routine`; unprefixed tag `codebase-lesson`; unprefixed tag `ledger`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: _routines
migration_status: v4-dry-run
```

## High-Confidence Sample
