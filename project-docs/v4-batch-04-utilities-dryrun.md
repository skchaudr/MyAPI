# Vault Schema V4 Normalization Dry Run

Vault root: `/Users/saboor/Obsidian/SoloDeveloper`

## Summary

- Total files scanned: 100
- High confidence: 85
- Medium confidence: 13
- Needs review: 2

## Review Queue

### 09 Utilities/AI-Handoff-TaskSystem-Integration.md

- Confidence: `medium`
- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
- Review needed: status exists on non-project/event type; unprefixed tag `handoff`; unprefixed tag `task-system`; unprefixed tag `obsidian`; unprefixed tag `PARA`; unprefixed tag `agent-context`; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities
migration_status: v4-dry-run
```

### 09 Utilities/Home Hub 2026.md

- Confidence: `medium`
- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area; anchor-like filename adjusted structural type
- Review needed: status exists on non-project/event type; unprefixed tag `dashboard`; unprefixed tag `homepage`; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities
migration_status: v4-dry-run
```

### 09 Utilities/Hybrid-Task-System-Architecture.md

- Confidence: `medium`
- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
- Review needed: status exists on non-project/event type; unprefixed tag `task-system`; unprefixed tag `architecture`; unprefixed tag `hybrid`; unprefixed tag `taskforge`; unprefixed tag `tasknotes`; unprefixed tag `obsidian-tasks`; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities
migration_status: v4-dry-run
```

### 09 Utilities/Sweep.md

- Confidence: `medium`
- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
- Review needed: status exists on non-project/event type; unprefixed tag `workflow`; unprefixed tag `sweep`; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities
migration_status: v4-dry-run
```

### 09 Utilities/_Vault System/Broken-aspects-of-properties-wiz.md

- Confidence: `medium`
- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; vault-system utility gets reference tag
- Review needed: status exists on non-project/event type; unprefixed tag `vault`; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Vault]]'
tags:
- topic/quickadd
- topic/automation
- topic/reference
source: imported
folder_origin: 09 Utilities/_Vault System
migration_status: v4-dry-run
```

### 09 Utilities/_Vault System/Creating strong visual feedback and metadeta driven vault.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; vault-system utility gets reference tag
- Review needed: type conflict: current `resource`, inferred `utility`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Vault]]'
tags:
- topic/reference
source: imported
folder_origin: 09 Utilities/_Vault System
migration_status: v4-dry-run
```

### 09 Utilities/_Vault System/Daily Note Template Tags.md

- Confidence: `medium`
- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; vault-system utility gets reference tag
- Review needed: unprefixed tag `sleep/good`; unprefixed tag `signal/loop`; unprefixed tag `signal/insight`; unprefixed tag `mood/ok`; unprefixed tag `mood/low`; unprefixed tag `mood/high`; unprefixed tag `focus/deep`; unprefixed tag `energy/low`; unprefixed tag `ego/high`; unprefixed tag `ego/low`; unprefixed tag `ego/3D`; unprefixed tag `ego/balanced`; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Vault]]'
tags:
- topic/reference
source: imported
folder_origin: 09 Utilities/_Vault System
migration_status: v4-dry-run
```

### 09 Utilities/_Vault System/How to filter notes through the vault System Inbox.md

- Confidence: `medium`
- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; vault-system utility gets reference tag
- Review needed: unprefixed tag `vault/migration`; unprefixed tag `vault/howto`; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Vault]]'
tags:
- topic/reference
source: imported
folder_origin: 09 Utilities/_Vault System
migration_status: v4-dry-run
```

### 09 Utilities/_Vault System/Obsidian_Vault_Situation_Report.md

- Confidence: `medium`
- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; vault-system utility gets reference tag
- Review needed: unprefixed tag `4`; unprefixed tag `3`; unprefixed tag `2`; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Vault]]'
tags:
- topic/reference
source: imported
folder_origin: 09 Utilities/_Vault System
migration_status: v4-dry-run
```

### 09 Utilities/_Vault System/Review current callouts and custom callouts.md

- Confidence: `medium`
- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; vault-system utility gets reference tag
- Review needed: status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Vault]]'
tags:
- topic/reference
source: imported
folder_origin: 09 Utilities/_Vault System
migration_status: v4-dry-run
```

### 09 Utilities/_Vault System/VLT_ Vault Schema V2.md

- Confidence: `medium`
- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; vault-system utility gets reference tag
- Review needed: unprefixed tag `active`; unprefixed tag `tags`; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Vault]]'
tags:
- topic/reference
source: imported
folder_origin: 09 Utilities/_Vault System
migration_status: v4-dry-run
```

### 09 Utilities/_Vault System/Vault Schema V4 Reference.md

- Confidence: `review`
- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; vault-system utility gets reference tag
- Review needed: type conflict: current `resource`, inferred `utility`
- Suggested:
```yaml
type: resource
area:
- - Vault
tags:
- topic/reference
concepts:
- - Knowledge Management
source: imported
folder_origin: 09 Utilities/_Vault System
migration_status: v4-dry-run
```

### 09 Utilities/transcripts/Can we test it? Yes we can!.md

- Confidence: `medium`
- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
- Review needed: unprefixed tag `transcript`; unprefixed tag `testing`; unprefixed tag `testability`; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/transcripts
migration_status: v4-dry-run
```

### 09 Utilities/transcripts/IOB - AI coming for your mind, not your life .md

- Confidence: `medium`
- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
- Review needed: unprefixed tag `internet-of-bugs`; unprefixed tag `content/video`; unprefixed tag `AI`; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Vault]]'
project: AI
source: imported
folder_origin: 09 Utilities/transcripts
migration_status: v4-dry-run
```

### 09 Utilities/transcripts/transcript-Danger-Illusion-of-AI-Code.md

- Confidence: `medium`
- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
- Review needed: status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/transcripts
migration_status: v4-dry-run
```

## High-Confidence Sample

### 09 Utilities/Attachments/_from_coding-tech/media-lib/url-AI-vs-ML-Engineer.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Attachments/_from_coding-tech/media-lib
migration_status: v4-dry-run
```

### 09 Utilities/Attachments/_from_coding-tech/media-lib/url-Prime-one-year-unemployed.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Attachments/_from_coding-tech/media-lib
migration_status: v4-dry-run
```

### 09 Utilities/Attachments/_from_coding-tech/media-lib/url-how-git-works.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Attachments/_from_coding-tech/media-lib
migration_status: v4-dry-run
```

### 09 Utilities/Attachments/_from_coding-tech/media-lib/url-no-vibes-allowed.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Attachments/_from_coding-tech/media-lib
migration_status: v4-dry-run
```

### 09 Utilities/Attachments/_from_coding-tech/media-lib/url-ypzlg8q9.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Attachments/_from_coding-tech/media-lib
migration_status: v4-dry-run
```

### 09 Utilities/Custom Callouts Reference.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities
migration_status: v4-dry-run
```

### 09 Utilities/Obsidian-Neovim-Setup/01-Neovim-Workflows.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Obsidian-Neovim-Setup
migration_status: v4-dry-run
```

### 09 Utilities/Obsidian-Neovim-Setup/02-Obsidian-CLI-Capture.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Obsidian-Neovim-Setup
migration_status: v4-dry-run
```

### 09 Utilities/Obsidian-Neovim-Setup/03-Apple-Shortcuts-Setup.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Obsidian-Neovim-Setup
migration_status: v4-dry-run
```

### 09 Utilities/Obsidian-Neovim-Setup/README.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Obsidian-Neovim-Setup
migration_status: v4-dry-run
```

### 09 Utilities/Reminders-CLI.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities
migration_status: v4-dry-run
```

### 09 Utilities/Reports/Hardened_Configuration_Vision.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Reports
migration_status: v4-dry-run
```

### 09 Utilities/Reports/OpenClaw_Known_Good_State.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Reports
migration_status: v4-dry-run
```

### 09 Utilities/Reports/PR_add-jules-mcp-case-study-2336253627227224160_Decision.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Reports
migration_status: v4-dry-run
```

### 09 Utilities/Reports/PR_dispatch-queue_Decision.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Reports
migration_status: v4-dry-run
```

### 09 Utilities/Reports/PR_feat-add-cn-utility-tests-12605712029049757920_Decision.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Reports
migration_status: v4-dry-run
```

### 09 Utilities/Reports/PR_feat-add-jules-case-study-12239587449017906312_Decision.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Reports
migration_status: v4-dry-run
```

### 09 Utilities/Reports/PR_feat-add-pathfinder-case-study-4226522165892727140_Decision.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Reports
migration_status: v4-dry-run
```

### 09 Utilities/Reports/PR_feat-expand-agentic-workflow-post-17722960923824425775_Decision.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Reports
migration_status: v4-dry-run
```

### 09 Utilities/Reports/PR_feat-expand-agentic-workflow-post-6509006787236807011_Decision.md

- Destination: `system/`
- Reasons: top-level folder `09 Utilities` maps to `system/`; utilities note gets vault area
```yaml
type: utility
area: '[[Vault]]'
source: imported
folder_origin: 09 Utilities/Reports
migration_status: v4-dry-run
```
