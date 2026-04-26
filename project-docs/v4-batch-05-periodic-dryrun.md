# Vault Schema V4 Normalization Dry Run

Vault root: `/Users/saboor/Obsidian/SoloDeveloper`

## Summary

- Total files scanned: 109
- High confidence: 101
- Medium confidence: 7
- Needs review: 1

## Review Queue

### 04 Periodic/00 Dailys/2026.02.23.md

- Confidence: `medium`
- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
- Review needed: status exists on non-project/event type; unprefixed tag `neovim`; unprefixed tag `obsidian`; unprefixed tag `setup`; unprefixed tag `dev-environment`; unprefixed tag `voice`; unprefixed tag `copilot`; concepts need owner assignment
- Suggested:
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.02.26.md

- Confidence: `medium`
- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
- Review needed: status exists on non-project/event type; unprefixed tag `daily-notes`; concepts need owner assignment
- Suggested:
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.03.07.md

- Confidence: `medium`
- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
- Review needed: status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.03.14.md

- Confidence: `review`
- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
- Review needed: type conflict: current `area`, inferred `periodic`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.03.18.md

- Confidence: `medium`
- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
- Review needed: status exists on non-project/event type; unprefixed tag `task`; unprefixed tag `reflection`; concepts need owner assignment
- Suggested:
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.03.27.md

- Confidence: `medium`
- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
- Review needed: status exists on non-project/event type; unprefixed tag `daily-notes`; concepts need owner assignment
- Suggested:
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.04.03.md

- Confidence: `medium`
- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
- Review needed: status exists on non-project/event type; unprefixed tag `daily-notes`; concepts need owner assignment
- Suggested:
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.04.23.md

- Confidence: `medium`
- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
- Review needed: status exists on non-project/event type; unprefixed tag `credits`; concepts need owner assignment
- Suggested:
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

## High-Confidence Sample

### 04 Periodic/00 Dailys/2026.01.23.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.01.25.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.01.26.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.01.27.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.01.28.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.01.29.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.01.30.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.02.01.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.02.02.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.02.03.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.02.04.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.02.05.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.02.06.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.02.07.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.02.08.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.02.09.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.02.10.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.02.11.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.02.12.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```

### 04 Periodic/00 Dailys/2026.02.13.md

- Destination: `periodics/`
- Reasons: top-level folder `04 Periodic` maps to `periodics/`; periodic note gets life area and log tag
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: 04 Periodic/00 Dailys
migration_status: v4-dry-run
```
