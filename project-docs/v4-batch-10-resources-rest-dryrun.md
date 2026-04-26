# Vault Schema V4 Normalization Dry Run

Vault root: `/Users/saboor/Obsidian/SoloDeveloper`

## Summary

- Total files scanned: 422
- High confidence: 274
- Medium confidence: 14
- Needs review: 134

## Review Queue

### 03 Resources/10 open source tools that feel illegal.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/2026 Dataview Queries Presets and Syntax.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; unprefixed tag `urgent`; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/ergonomics
- scope/finance
- scope/ops
- tool/obsidian
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/2026 New DevTools features from Chrome.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/2026 Tasks Queries Presets and Syntax.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- lang/js
- scope/communication
- scope/finance
- scope/ops
- scope/writing
- tool/obsidian
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/A repo-creating command line argument passing script for quick push&pull ready remote-connected repo.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/ops
- tool/git
- tool/terminal
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/A-shell turbo charges Apple Shortcuts.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- tool/obsidian
- tool/terminal
- topic/web-dev
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/AI/-cli-Claude-Code-and-the-Skills-known-as-Superpowers-~-engineering-methodology.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
- Review needed: status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/AGY-models.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
- Review needed: status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/Agents-Top-Agent-Ideas-for-Claude-or-OpenClaw.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
- Review needed: status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/Articles/X/Oliver Henry/2026-02-12 - How my OpenClaw agent Larry got millions of TikTok views in one week.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
- Review needed: status exists on non-project/event type; unprefixed tag `type/article`; unprefixed tag `source/x`; unprefixed tag `source/oliverhenry`; concepts need owner assignment; unknown source value `https://x.com/oliverhenry/status/2022011925903667547`
- Suggested:
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/openclaw
- topic/tiktok
- topic/marketing
- topic/ai
source: https://x.com/oliverhenry/status/2022011925903667547
folder_origin: 03 Resources/AI/Articles/X/Oliver Henry
migration_status: v4-dry-run
```

### 03 Resources/AI/Articles/X/Oliver Henry/2026-03-07 - How a personal AI agent will change your entire life in 1 day.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
- Review needed: status exists on non-project/event type; unprefixed tag `type/article`; unprefixed tag `source/x`; unprefixed tag `source/oliverhenry`; concepts need owner assignment; unknown source value `https://x.com/oliverhenry/status/2030394095399588145`
- Suggested:
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/openclaw
- topic/agents
- topic/skills
- topic/ai
source: https://x.com/oliverhenry/status/2030394095399588145
folder_origin: 03 Resources/AI/Articles/X/Oliver Henry
migration_status: v4-dry-run
```

### 03 Resources/AI/Combing-through-SmallPi-WhatsApp-thread-for-useful-BDR,-SCA,-Obsidian,-OC-config,-and-more,-info.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
- Review needed: status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/Jules-CLI-Completion-Commands-with-Examples-and-Explanations.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
- Review needed: status exists on non-project/event type; unprefixed tag `research`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/PicoClaw-OpenClaw-for-Android-and-encouragement-to-make-it.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
- Review needed: status exists on non-project/event type; unprefixed tag `DNS`; unprefixed tag `Find`; unprefixed tag `OR`; unprefixed tag `task`; unprefixed tag `TLS`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/agy-Antigravity-CLI-commands-to-avoid-chat-and-interactivity.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
- Review needed: status exists on non-project/event type; unprefixed tag `reference`; unprefixed tag `cli`; unprefixed tag `ai`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AMCC can be retrained and grown.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Active recall and near instant testing is the level up in learning you need to Implement.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; unprefixed tag `Learning`; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/learning
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/All fast actions should be done on the thumb keys.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
- tool/dygma
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Anthropic's 33 page presentation on how skills works.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Antigravity Agent Manager as all-purpose agent.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: type conflict: current `area`, inferred `resource`; missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
tags:
- tool/antigravity
- topic/agents
- tool/GoogleAI
- tool/howto
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Antigravity login to VM was failing because 10GB folder filled up.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- tool/terminal
- topic/ops
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Antigravity-Usage-Approach.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Asking deeply intelligent technical questions while remaining calm and non-emotional.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/BPI - Claude answering 2024, how AI mistakes are subtle but consequential.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/health
- topic/ai
- topic/web-dev
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Be positive of the direction you are going as 2026 begins.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Better Prompting through a Realistic understanding of what AI actually is.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Blink Shell and X-Callback-URL.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Brutal Claude 2026 Jan 29 callout more right than not.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/CPU & RAM Reductions and Optimizations on 8GB RAM Mac-M1 Machine.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- scope/ops
- tool/obsidian
- tool/terminal
- topic/ops
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/ChatGPT control prompts and custom instructions for no more word salad.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/finance
- scope/mindset
- scope/ops
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/China and the US differences on individual community and social obligation..md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
- topic/USvsChina
- topic/politics
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Cmux is workspaces Ghostty but with first-class agentic workflow support.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Complex systems can be broken down and understood simply.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Core Lazygit Loop.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Custom instructions for Claude on not wasting time confusing environment.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/mindset
- scope/writing
- tool/git
- tool/obsidian
- topic/ai
- topic/web-dev
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Cut to the chase by Eddie on session tokens.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Daily Tmux Cheatsheet of Commands.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- lang/js
- lang/py
- scope/communication
- scope/ops
- tool/neovim
- tool/terminal
- tool/tmux
- topic/web-dev
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Defining active workspaces.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Dissect and understand this nerve glide video.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Don't do X - requires both models and humans alike to recall X in order to not do it.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Dygma Refurbished are cheaper and are the 30-day-refund boards.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ergonomics
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/EPOMAKER K21 Macro Numpad Power Key.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- scope/communication
- scope/ergonomics
- scope/finance
- scope/fitness
- scope/mindset
- scope/ops
- tool/git
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Ergonomics - Nerve Safe Left Hand Typing Protocol.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: status exists on non-project/event type; unprefixed tag `ergonomics`; unprefixed tag `nerve`; unprefixed tag `typing`; unprefixed tag `workstation`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: ergonomics
tags:
- scope/ergonomics
- scope/health
- scope/mindset
- scope/ops
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Espanso how-to guide for adding matches.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Export tool general purpose use case is important.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Fastest way to grab something is cat, pipe, grep.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- tool/cat
- tool/commands
- tool/grep
- tool/pipe-operator
- tool/terminal
- tool/zsh
- topic/ai
- topic/terminal
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Find video tutorial of Swish's advanced usages (or make one).md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Finger Placement on Home Row Keys.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- scope/ergonomics
- tool/git
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Four rules for Nerve Glides.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Free VPS Google Collab collab vps sshx.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- topic/ops
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Ghostty Final Switch Plus Copilot for Terminal help and Aider to be dev-ready.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- scope/communication
- scope/finance
- scope/fitness
- scope/mindset
- scope/ops
- tool/ghostty
- tool/git
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Ghostty copy screen commands creates historical artifacts of your terminal session.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- lang/js
- lang/py
- scope/career
- tool/git
- tool/obsidian
- tool/terminal
- topic/ai
- topic/ops
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Ghostty master cheatsheet.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Git - there are TWO -m flags or none since BOTH represent that there is often a summary message AND a longer message.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Google AI Pro Recovery 2026-W12.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Google Collab and AI Coding Problem Sparring  is the GOAT pair.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Hack Your Brain with Powerlifting.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; unprefixed tag `content/video`; unprefixed tag `creator/noboilerplate`; unprefixed tag `transcript`; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/ergonomics
- scope/fitness
- scope/health
- scope/learning
- scope/mindset
- scope/sleep
- scope/writing
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Hand therapy appointment 2 -.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Hand therapy exercises packet 2026.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment; unknown source value `Hand-Therapy-Packet-2026.pdf`
- Suggested:
```yaml
type: resource
tags:
- scope/health
- scope/mindset
- scope/ops
- scope/writing
source: Hand-Therapy-Packet-2026.pdf
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Headless Obsidian Sync Commands.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- lang/js
- scope/writing
- tool/obsidian
- topic/ops
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Helping Mara find a new PC case.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Home row mods and then bottom row navigation with tabbing.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ergonomics
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Hook automation for shell command log for Claude Code configured.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/How to prove competence for job and try for fast cash in 2026.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- scope/finance
- scope/ops
- topic/web-dev
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/IBM & Anthropic hiring means those two Gemini-3-suggested projects are ne.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/IBM, Anthropic are hiring and I need to be ready tomorrow.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- scope/learning
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/IG reel - MIQ brain dump in morning + what you want done aat beginning, middle, and end of day.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Idea for Dygma raise keyboard - each thumb cluster is 7 distinct keys.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ergonomics
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Identify the smallest consistent action that moves your key project forward each day.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/In the middle of a git rebase when classic rebase conflict occurred.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Indexed Searches Accomplish Near-Zero Latency, Richer Matching Behavior, and Interactive Navigation Speed.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Instagram triage inbox for software, tech, and business.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Is the real value in the data going in or is the real value in layering retrieval and linking.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Jake Van Clief- building agents when it's going to be a feature by the big AI companies in weeks time.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Joanne • Mindset & Motherhood on Instagram.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Josh and Seed Tracer - do I have enough time to do this or should he move forward.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- scope/communication
- scope/finance
- scope/health
- scope/learning
- scope/ops
- scope/sleep
- tool/git
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Journaling to build keyboard inuition to complete the final layers.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ergonomics
- scope/mindset
- scope/writing
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Jul - Agent Dispatcher.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- lang/py
- scope/communication
- scope/finance
- scope/mindset
- scope/ops
- tool/obsidian
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Jul - Vault DOCTOR.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- lang/py
- scope/fitness
- scope/health
- scope/mindset
- scope/writing
- tool/obsidian
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/LLM Payload Idea between Mac and iPad.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Lovable-s plethora of integrations from Feb-April 2026.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/NeoVim/AI-augmented terminal power user primer.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `NeoVim`; area inferred from resource folder `NeoVim`
- Review needed: unprefixed tag `terminal`; unprefixed tag `notebookLM`; unprefixed tag `AI/agents`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- tool/neovim
source: imported
folder_origin: 03 Resources/NeoVim
migration_status: v4-dry-run
```

### 03 Resources/NeoVim/Daily Neogit workflow loop.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `NeoVim`; area inferred from resource folder `NeoVim`
- Review needed: unprefixed tag `neovim`; unprefixed tag `neogit`; unprefixed tag `git`; unprefixed tag `daily/workflow`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- tool/neovim
source: imported
folder_origin: 03 Resources/NeoVim
migration_status: v4-dry-run
```

### 03 Resources/NeoVim/NeoVim Anchor CPR.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `NeoVim`; area inferred from resource folder `NeoVim`; anchor-like filename adjusted structural type
- Review needed: unprefixed tag `tmux`; unprefixed tag `setup`; unprefixed tag `neovim`; unprefixed tag `IDE`; unprefixed tag `CPR`; unprefixed tag `config`; unprefixed tag `anchor`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- tool/neovim
source: imported
folder_origin: 03 Resources/NeoVim
migration_status: v4-dry-run
```

### 03 Resources/NeoVim/nvim - Useful beginner Neovim guide for daily coding.md

- Confidence: `medium`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `NeoVim`; area inferred from resource folder `NeoVim`
- Review needed: unprefixed tag `terminal`; unprefixed tag `neovim`; unprefixed tag `AI/terminal`; unprefixed tag `AI/claude`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- tool/neovim
source: imported
folder_origin: 03 Resources/NeoVim
migration_status: v4-dry-run
```

### 03 Resources/Obsidian Headless Sync on Raspberry Pi Runbook.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Obsidian vs GitHub Issues vs n8n vs systemd.path for Small Pi Control Plane.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Offload Compute Work With M1 and Raspberry Pi Devices.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/OpenClaw Gateway Restart SOP.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/OpenRouter vs OpenCode and how they compare vs differ.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Popular-readline-Keyboard-Shortcuts-for-the-GNU-Bash-Shell.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Power Pattern of OpenCode for active coding, Jules for background work, Gemini for thinking and routing..md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
- scope/ops
- tool/neovim
- tool/obsidian
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Prediction market trading bot or skill?.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Prime - We've love the tech.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- lang/js
- scope/career
- scope/communication
- scope/ergonomics
- scope/mindset
- scope/ops
- scope/writing
- tool/terminal
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Programming/Helix-flirting-begins-tutor,-projects,-minimal-config,-batteries-included.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `Programming`; area inferred from resource folder `Programming`
- Review needed: type conflict: current `project`, inferred `resource`; concepts need owner assignment
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

### 03 Resources/Prompt - Smart transcript prompt for avoiding opinionated reductions.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Quick JQ Cheatsheet.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/mindset
- scope/ops
- tool/git
- tool/neovim
- tool/terminal
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Remember to merge vaults via ultrai.pp.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Researching Skills for Codex reminds me to understand how LLMs and agentic AI works.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ops
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Saboor Docs - 11 Tailored Guides.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Shell vocabulary map for vars, prompt, env, path, RC files, completion, etc.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Steering AI to answering at or above the level of the question.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Stitch is apparently lovable but for developers.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Study and Learn tool by ChatGPT.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/TRAE's SOLO mode for rapid work.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Tables for Worldview Harness Creation.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Tasknotes Pomodoro Timer + any other timer are underexplored.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Tasks plugin docs with syntax explained and examples.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/finance
- tool/obsidian
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Terminal & iTerm2 Essential Shortcuts for Commands and Line Navigation.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- lang/py
- scope/career
- scope/communication
- scope/ergonomics
- scope/ops
- tool/commands
- tool/git
- tool/hotkeys
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Terminal command use upgrade with less, reactive output search, and recent command search.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- tool/terminal
- topic/ai
- topic/web-dev
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Terminal strings command extracts text from given file and have.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/mindset
- tool/ghostty
- tool/iterm2
- tool/terminal
- tool/zsh
- topic/commands
- topic/terminal
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Terminal substring or prefix command history depends on arrow keybindings.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ergonomics
- tool/terminal
- tool/zsh
- topic/terminal
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/The 2026 CLI agent sprawl compared and contrasted.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- scope/communication
- scope/ops
- tool/git
- tool/neovim
- tool/terminal
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/The goal is to breakdown your processes and map which features you should be using.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/The superpowers skills set for CLI agents.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Tmux Essential Shortcuts and Navigation.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/2026
- scope/communication
- scope/ergonomics
- scope/ops
- tool/neovim
- tool/terminal
- tool/tmux
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Type a full key test (online tester or VIA).md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- tool/obsidian
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Untitled.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- lang/py
- scope/ops
- tool/obsidian
- tool/terminal
- topic/ai
- topic/web-dev
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Use these 5 UI UX Components or services for beautiful design.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Uses and Benefits of Vertex AI.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Using external references in code blocks moving forward.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Using the Raspberry Pi in 2026.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Using trackpad gestures app Swish.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Vanta automates security and privacy compliance.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/What an OpenClaw Worldview Harness should answer.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/What is OpenRouter?.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/When to use OSM as a quick shift hold and tap versus double tap.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Why do smart lists in Reminders not be available in my terminal when other lists are.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; unprefixed tag `AI/API`; unprefixed tag `dashboard`; unprefixed tag `reminders`; unprefixed tag `reminders-cli`; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- tool/terminal
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Workflow portability via codifying your dev environment in dotfiles is a sign of advanced power user.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ops
- tool/git
- tool/neovim
- tool/terminal
- topic/ai
- topic/terminal
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Zed Day 1 basic keyboard workflows picking up quick.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ergonomics
- scope/ops
- tool/git
- tool/neovim
- tool/terminal
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/Zed Extensions Anchor.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/agents -- the pattern for agent creation is autonomaous processing and making reasonable assumptions, not unnecessary questions.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/andre Karpathy prompt for obsidian AI second brain.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `research`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/call harness leak and Elizabeth made Minecraft in space with open source models.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/dRs~ Base44 and the AI building landscape.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- lang/js
- lang/py
- scope/career
- scope/communication
- scope/ergonomics
- scope/finance
- scope/mindset
- scope/ops
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/data dog on tool hopping.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/declarative programming versus.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/dkbo- Super Layer - with superkey and more functionality.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- tool/neovim
- tool/obsidian
- tool/terminal
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/dr~ Bazeor to Kaleidoscope Report.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/ergonomics
- scope/health
- scope/ops
- tool/git
- tool/neovim
- tool/terminal
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/dygma hold timeout and overlap threshold.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/ergonomics
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/eg - Ek21 Numpad Hybrid Mac iPad Layout.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/writing
- tool/git
- tool/neovim
- tool/obsidian
- tool/terminal
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/grep - double grep piped for clean retrieval of searched info.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/mindset
- tool/terminal
- topic/ai
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/iTerm2 Core Essentials Quick Version.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- tool/terminal
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/iTerm2 Setup.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- tool/terminal
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/neovim-drills-day-1.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/tmux power move -- detaching > closing, keeps shell and processes alive.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- tool/terminal
- tool/tmux
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/unix -- useful ls piped to grep command like for tree.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- tool/obsidian
- tool/terminal
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

### 03 Resources/vi~ replacing $ with shift-6 or A or Ff or Tt or %.md

- Confidence: `review`
- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/writing
- tool/neovim
source: imported
folder_origin: 03 Resources
migration_status: v4-dry-run
```

## High-Confidence Sample

### 03 Resources/AI/17 Claude Code SubAgents examples with templates.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/API Keys vs Premium AI Pro Subscriptions.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/Automation/OpenClaw 2026- Updates.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI/Automation
migration_status: v4-dry-run
```

### 03 Resources/AI/Automation/Scripting is TMUX's Superpower.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI/Automation
migration_status: v4-dry-run
```

### 03 Resources/AI/CLI Fluency and IDE & AI Agent Integration.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/AI
- topic/10x-dev
- tool/geminiCLI
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/CLI OAuth vs Traditional API Keys.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/ChatGPT Switching from Analytical to Strategic Framing.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/Claude SC Automation Plan.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- tool/openclaw
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/Claude_Code_pipe-stdin-usage-command-examples.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/FREE API KEYS YOU CAN GET RIGHT NOW.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/First Jules workflow dispatch cycle 2026.01.31.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/Four node openclaw recovery plan, if I want it.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/Google Antigravity - Beginner to Power User Guide.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/JULES_MASTER_LAUNCHER_V2.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- tool/openclaw
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/Josh and Seed Tracer - b ability.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/Oliver Henry - How a personal AI agent will change your entire life in 1 day.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/Oliver Henry - How my OpenClaw agent, Larry, got millions of TikTok views in one week.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/OpenClaw architecture choice is unianimous.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/PROMPT_BOOK.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```

### 03 Resources/AI/Replace with README - Where the Pi pushes to.md

- Destination: `resources/`
- Reasons: top-level folder `03 Resources` maps to `resources/`; tag inferred from resource folder `AI`; area inferred from resource folder `AI`
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- tool/openclaw
- topic/ai
source: imported
folder_origin: 03 Resources/AI
migration_status: v4-dry-run
```
