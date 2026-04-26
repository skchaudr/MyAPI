# Vault Schema V4 Normalization Dry Run

Vault root: `/Users/saboor/Obsidian/SoloDeveloper`

## Summary

- Total files scanned: 29
- High confidence: 26
- Medium confidence: 0
- Needs review: 3

## Review Queue

### 00 Inbox/skc -- steps towards building my portfolio website with insightful posting from recent experiences.md

- Confidence: `review`
- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; unprefixed tag `use/howto`; unprefixed tag `use/reference`; concepts need owner assignment
- Suggested:
```yaml
type: area
tags:
- lang/js
- lang/py
- scope/career
- scope/communication
- scope/ergonomics
- scope/finance
- scope/learning
- scope/ops
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/vlt_ Vault Schema V3 -- introduces Concepts.md

- Confidence: `review`
- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
- Review needed: type conflict: current `utility`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: utility
tags:
- scope/obsidian
- tool/schema
- topic/normalization
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/vlt_ Vault Schema V3 with concept fix.md

- Confidence: `review`
- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
- Review needed: type conflict: current `utility`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: utility
tags:
- scope/obsidian
- topic/normalization
- tool/schema
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

## High-Confidence Sample

### 00 Inbox/Instagram-Triage/Brain chooses cheap dopamine to cover for stress, pain, rather than running this neurologically-sound process.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
source: imported
folder_origin: 00 Inbox/Instagram-Triage
migration_status: v4-dry-run
```

### 00 Inbox/LLM Payload Mailbox/LLM Payload Workflow.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
source: imported
folder_origin: 00 Inbox/LLM Payload Mailbox
migration_status: v4-dry-run
```

### 00 Inbox/Quick reference of prefixes in my vault ecosystem for fast retrieval.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
tags:
- tool/obsidian
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/Review the Med students wildly impresive. valuabe Obsidian setup.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
tags:
- scope/vault
- tool/schema
- topic/obsidian
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/Untitled V4 Test Note.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/keyboard idea.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
tags:
- scope/communication
- scope/ergonomics
- tool/neovim
- tool/terminal
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/landing pages and AB testing shows simple text message wins.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/lc_1004 — Max Consecutive Ones III.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/nlm - Mobile SSH and Remote Dev Guide for iOS.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
tags:
- lang/js
- lang/py
- scope/communication
- scope/ergonomics
- scope/ops
- tool/neovim
- tool/terminal
- topic/ops
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/nlm - powerful CLI for full use of NotebookLM.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/nvim - Quick calls to some agent CLI using terminal commands.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
tags:
- scope/communication
- scope/ergonomics
- tool/neovim
- tool/terminal
- topic/ai
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/nvim - q enters macro recording mode and only q exits.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
tags:
- scope/ergonomics
- tool/neovim
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/nvimt - di" is goto deleting within surrounding quotes.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
tags:
- scope/mindset
- tool/neovim
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/obsidian.neovim comprehensive command list and breakdown.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/quickbooks.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
tags:
- scope/finance
- scope/ops
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/skc__ How PWAs liberated me and taught me about available software.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/skc__ Portfolio Website Ready to be Deployed.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
tags:
- lang/js
- scope/career
- scope/communication
- scope/ops
- tool/git
- topic/web-dev
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/solve-bench index.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`; anchor-like filename adjusted structural type
```yaml
type: resource
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/solve-bench is coding problem solving and AI sparring partner.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```

### 00 Inbox/terminal keys like ctrl d and ctrl c.md

- Destination: `inbox/`
- Reasons: top-level folder `00 Inbox` maps to `inbox/`
```yaml
type: resource
tags:
- tool/terminal
source: imported
folder_origin: 00 Inbox
migration_status: v4-dry-run
```
