# Vault Schema V4 Normalization Dry Run

Vault root: `/Users/saboor/Obsidian/SoloDeveloper`

## Summary

- Total files scanned: 17
- High confidence: 14
- Medium confidence: 2
- Needs review: 1

## Review Queue

### 03 Resources/Programming/Helix-flirting-begins-tutor,-projects,-minimal-config,-batteries-included.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
- Review needed: type conflict: current `project`, inferred `resource`; unprefixed tag `project`; concepts need owner assignment
- Suggested:
```yaml
type: project
area: '[[Programming]]'
status: active
tags:
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

### 03 Resources/Programming/Key CS Knowledge of the Books DDIA, SICP, and CSAPP.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
- Review needed: unprefixed tag `books`; unprefixed tag `learning`; unprefixed tag `resources`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Programming]]'
tags:
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

### 03 Resources/Programming/git - the git trinity and navigational workflow of status, diff, log - show.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
- Review needed: status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Programming]]'
tags:
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

## High-Confidence Sample

### 03 Resources/Programming/-fzf-example-commands-for-its-dope-features.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
```yaml
type: resource
area: '[[Programming]]'
tags:
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

### 03 Resources/Programming/Blink & a-Shell for iPad file editing and Raspberry Pi connecting.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
```yaml
type: resource
area: '[[Programming]]'
tags:
- tool/terminal
- tool/tmux
- topic/ops
- scope/ops
- topic/ai
- tool/git
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

### 03 Resources/Programming/Blink Shell and Blink Code Features from Home Page.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`; anchor-like filename adjusted structural type
```yaml
type: resource
area: '[[Programming]]'
tags:
- tool/terminal
- tool/git
- topic/ai
- topic/dsa
- tool/neovim
- topic/ops
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

### 03 Resources/Programming/Blink Shell for VS Code Tunneling on iPad or iPhone.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
```yaml
type: resource
area: '[[Programming]]'
tags:
- tool/terminal
- topic/ai
- tool/tmux
- lang/py
- topic/ops
- scope/communication
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

### 03 Resources/Programming/For the incoming future plan on iPad A-Shell or Blink Shell to up my game.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
```yaml
type: resource
area: '[[Programming]]'
tags:
- tool/terminal
- topic/ai
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

### 03 Resources/Programming/Gemini CLI Cheat Sheet.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
```yaml
type: resource
area: '[[Programming]]'
tags:
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

### 03 Resources/Programming/Gemini CLI commands and options.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
```yaml
type: resource
area: '[[Programming]]'
tags:
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

### 03 Resources/Programming/Pi Terminal Color and Visual Feedback.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
```yaml
type: resource
area: '[[Programming]]'
tags:
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

### 03 Resources/Programming/TMUX muscle memory starter confidence pack.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
```yaml
type: resource
area: '[[Programming]]'
tags:
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

### 03 Resources/Programming/The pipe syntax is fundamental to Unix's terminal power.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
```yaml
type: resource
area: '[[Programming]]'
tags:
- topic/terminal
- topic/scripting
- tool/zsh
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

### 03 Resources/Programming/Ultimate GitHub Repo Skills Usages and Downloads.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
```yaml
type: resource
area: '[[Programming]]'
tags:
- tool/git
- tool/terminal
- topic/ai
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

### 03 Resources/Programming/When to use git diff and when to use git rebase.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
```yaml
type: resource
area: '[[Programming]]'
tags:
- scope/communication
- tool/git
- topic/ai
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

### 03 Resources/Programming/bsb - Blink Shell Build Up Commands.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
```yaml
type: resource
area: '[[Programming]]'
tags:
- tool/terminal
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```

### 03 Resources/Programming/fzf-newly-discovered-functionality-make-fzf-a-game-changer.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
```yaml
type: resource
area: '[[Programming]]'
tags:
- topic/programming
source: imported
folder_origin: 03 Resources/Programming
migration_status: v4-dry-run
```
