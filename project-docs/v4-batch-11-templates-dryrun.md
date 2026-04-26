# Vault Schema V4 Normalization Dry Run

Vault root: `/Users/saboor/Obsidian/SoloDeveloper`

## Summary

- Total files scanned: 32
- High confidence: 1
- Medium confidence: 0
- Needs review: 31

## Review Queue

### Templates/10-weekly-template.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/20-monthly-note-template.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: type conflict: current `periodic`, inferred `utility`; concepts need owner assignment
- Suggested:
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/21-monthly.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/30-quarterly.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/31-quartely-note-template.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: type conflict: current `periodic`, inferred `utility`; concepts need owner assignment
- Suggested:
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/40-yearly-note-template.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: type conflict: current `periodic`, inferred `utility`; concepts need owner assignment
- Suggested:
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/41-yearly.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/Daily Mobility Routine.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/Not So Roundtable {{date}}.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/Timestamp-Callout-Template.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/_code-problem-templater.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/_dataview-recent-template.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/callout-wrap.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/daily-note.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: type conflict: current `periodic`, inferred `utility`; concepts need owner assignment
- Suggested:
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/date-callout-datestamp-template.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/deep-work.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/default-note.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: type conflict: current `resource`, inferred `utility`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: original
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/docs-reading-template.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; unprefixed tag `learning`; unprefixed tag `docs/reading`; unprefixed tag `docs`; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/merge-periodic.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/miq-brainstorm.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/miq-callout.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/personal-note.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/primary-project-anchor-template.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/project-note.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: type conflict: current `project`, inferred `utility`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
status: active
source: original
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/research-note.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: type conflict: current `resource`, inferred `utility`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: article
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/task-note.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/time_and_datestamp-template.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/transcripts-template.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; unprefixed tag `transcript`; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/weekly-note-template.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: type conflict: current `periodic`, inferred `utility`; concepts need owner assignment
- Suggested:
```yaml
type: periodic
area: '[[Life]]'
tags:
- topic/log
source: original
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/weekly-project-anchors-templates.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

### Templates/workout-session.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
- Review needed: missing area/project/concept connection; unprefixed tag `workout`; concepts need owner assignment
- Suggested:
```yaml
type: utility
source: imported
folder_origin: Templates
migration_status: v4-dry-run
```

## High-Confidence Sample

### Templates/utility-note.md

- Destination: `system/`
- Reasons: top-level folder `Templates` maps to `system/`
```yaml
type: utility
area: '[[Vault]]'
source: original
folder_origin: Templates
migration_status: v4-dry-run
```
