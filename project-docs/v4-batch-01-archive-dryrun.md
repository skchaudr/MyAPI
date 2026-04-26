# Vault Schema V4 Normalization Dry Run

Vault root: `/Users/saboor/Obsidian/SoloDeveloper`

## Summary

- Total files scanned: 22
- High confidence: 0
- Medium confidence: 0
- Needs review: 22

## Review Queue

### 05 Archive/Archive/Cleanup Log 2026-02-28.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 05 Archive/Archive
migration_status: v4-dry-run
```

### 05 Archive/Example-Note-Wiz-2.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 05 Archive
migration_status: v4-dry-run
```

### 05 Archive/Example-Note-Wiz.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 05 Archive
migration_status: v4-dry-run
```

### 05 Archive/Russian dude speaking to English audience trying to get them to probably sign up for a course but truth in what he says.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 05 Archive
migration_status: v4-dry-run
```

### 05 Archive/The Engineer's 5 W's of CIM and NUI Anchor.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- tool/git
- topic/web-dev
source: imported
folder_origin: 05 Archive
migration_status: v4-dry-run
```

### 05 Archive/Ty Conversation Call 4.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/finance
source: imported
folder_origin: 05 Archive
migration_status: v4-dry-run
```

### 05 Archive/Ty First Official Meeting After 7 Days of Processing.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
source: imported
folder_origin: 05 Archive
migration_status: v4-dry-run
```

### 05 Archive/Ty Zoom Meeting Day One.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- scope/communication
- scope/mindset
source: imported
folder_origin: 05 Archive
migration_status: v4-dry-run
```

### 05 Archive/_to-delete-after-30d/CIM-Ty-and-the-ownership-conversation.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 05 Archive/_to-delete-after-30d
migration_status: v4-dry-run
```

### 05 Archive/_to-delete-after-30d/End-of-Month Assessment.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `interview/sprint`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 05 Archive/_to-delete-after-30d
migration_status: v4-dry-run
```

### 05 Archive/_to-delete-after-30d/Hand Therapy Appt 1 Complete.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 05 Archive/_to-delete-after-30d
migration_status: v4-dry-run
```

### 05 Archive/_to-delete-after-30d/Ideal Typing Position Form.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; unprefixed tag `learning`; unprefixed tag `ergonomics`; unprefixed tag `workplace`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 05 Archive/_to-delete-after-30d
migration_status: v4-dry-run
```

### 05 Archive/_to-delete-after-30d/Important Ergonomics Tests .md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; unprefixed tag `None`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 05 Archive/_to-delete-after-30d
migration_status: v4-dry-run
```

### 05 Archive/_to-delete-after-30d/MUST USE health and nerve decompression protocols.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 05 Archive/_to-delete-after-30d
migration_status: v4-dry-run
```

### 05 Archive/_to-delete-after-30d/Mastering `make` is a hallmark of the advanced power user who values efficiency and reproducibility over manual execution..md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: type conflict: current `area`, inferred `resource`; missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
tags:
- topic/compilation
- topic/build
- tool/makefile
source: imported
folder_origin: 05 Archive/_to-delete-after-30d
migration_status: v4-dry-run
```

### 05 Archive/_to-delete-after-30d/Nerve Pain Log 2026.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 05 Archive/_to-delete-after-30d
migration_status: v4-dry-run
```

### 05 Archive/_to-delete-after-30d/Useful Git Commands.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 05 Archive/_to-delete-after-30d
migration_status: v4-dry-run
```

### 05 Archive/_to-delete-after-30d/VISION_B_PLAN.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 05 Archive/_to-delete-after-30d
migration_status: v4-dry-run
```

### 05 Archive/_to-delete-after-30d/Vincent Social Interactivity Meeting 3.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 05 Archive/_to-delete-after-30d
migration_status: v4-dry-run
```

### 05 Archive/_to-delete-after-30d/Vincent SocialXP Base44 with Co-Design 2 One Week Out.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 05 Archive/_to-delete-after-30d
migration_status: v4-dry-run
```

### 05 Archive/_to-delete-after-30d/Workplace Recovery Steps.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; unprefixed tag `ergonomics`; unprefixed tag `workplace`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 05 Archive/_to-delete-after-30d
migration_status: v4-dry-run
```

### 05 Archive/_to-delete-after-30d/zsh plugins.md

- Confidence: `review`
- Destination: `archive/`
- Reasons: top-level folder `05 Archive` maps to `archive/`; archive folder preserves inactive destination
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 05 Archive/_to-delete-after-30d
migration_status: v4-dry-run
```

## High-Confidence Sample
