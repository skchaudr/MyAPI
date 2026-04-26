# Vault Schema V4 Normalization Dry Run

Vault root: `/Users/saboor/Obsidian/SoloDeveloper`

## Summary

- Total files scanned: 782
- High confidence: 508
- Medium confidence: 91
- Needs review: 183

## Review Queue

### 02 Areas/AI code problem solving pipeline.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- topic/ai
- topic/workflow
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Atomic units of my 2026 development workflow.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- topic/workflow
- scope/career
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Awareness of and attentiveness to time passing increases chances of productivity.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/productivity
- topic/time
- tool/timers
- tool/watch
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Blink Build SSH Pathway to GitHub.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/CIM - Phase 0 mistake was hypothesis and marketing friendly not reality of API docs friendluy.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/writing
- tool/git
- topic/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/CIM - Ty response to agreement form v0.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Career/2026-the-emergeing-paradigm-the-next-2-years-of-software-development.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
- Review needed: status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Career]]'
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/Configuring LMN for Beiley in a way that actually serves him.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
- Review needed: status exists on non-project/event type; unprefixed tag `beiley`; unprefixed tag `project`; unprefixed tag `was`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Career]]'
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/Email Rules to Live By.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
- Review needed: status exists on non-project/event type; unprefixed tag `socialXP`; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Career]]'
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/Job Search 2026/** Technical Communication Practice.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
- Review needed: status exists on non-project/event type; unprefixed tag `card`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Career]]'
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career/Job Search 2026
migration_status: v4-dry-run
```

### 02 Areas/Career/Job Search 2026/2026-01 Interview Sprint/1-month Interview Sprint Jan 2026 Anchor.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`; anchor-like filename adjusted structural type
- Review needed: type conflict: current `project`, inferred `area`; unprefixed tag `interview/sprint`; unprefixed tag `interview/prep`; unprefixed tag `anchor`; concepts need owner assignment
- Suggested:
```yaml
type: project
area: '[[Career]]'
status: active
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career/Job Search 2026/2026-01 Interview Sprint
migration_status: v4-dry-run
```

### 02 Areas/Career/Job Search 2026/2026-01 Interview Sprint/Speedy Technical Mini Plan Jan 2026.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
- Review needed: type conflict: current `project`, inferred `resource`; concepts need owner assignment
- Suggested:
```yaml
type: project
area: '[[Career]]'
status: active
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career/Job Search 2026/2026-01 Interview Sprint
migration_status: v4-dry-run
```

### 02 Areas/Career/Job Search 2026/2026-01 Interview Sprint/Week 1 of Get Presentable Fast.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
- Review needed: type conflict: current `project`, inferred `resource`; concepts need owner assignment
- Suggested:
```yaml
type: project
area: '[[Career]]'
status: active
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career/Job Search 2026/2026-01 Interview Sprint
migration_status: v4-dry-run
```

### 02 Areas/Career/LinkedIn/Full-Audit-Action-Plan.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
- Review needed: type conflict: current `project`, inferred `resource`; concepts need owner assignment
- Suggested:
```yaml
type: project
area: '[[Career]]'
status: active
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career/LinkedIn
migration_status: v4-dry-run
```

### 02 Areas/Career/Mission 3 - Mac Portfolio + Networking Sprint.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
- Review needed: type conflict: current `project`, inferred `resource`; concepts need owner assignment
- Suggested:
```yaml
type: project
area: '[[Career]]'
status: active
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/Project Polish and Preparation/** Framing and work required to turn SocialXP into a win NOW.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
- Review needed: type conflict: current `project`, inferred `resource`; unprefixed tag `socialXP`; unprefixed tag `professional-profile`; unprefixed tag `interview-prep`; concepts need owner assignment
- Suggested:
```yaml
type: project
area: '[[Career]]'
status: active
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career/Project Polish and Preparation
migration_status: v4-dry-run
```

### 02 Areas/Career/Project Polish and Preparation/** Proper and impressive framing of projects.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
- Review needed: type conflict: current `project`, inferred `resource`; concepts need owner assignment
- Suggested:
```yaml
type: project
area: '[[Career]]'
status: active
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career/Project Polish and Preparation
migration_status: v4-dry-run
```

### 02 Areas/Career/SC Works New Tech Event 3-4-26.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
- Review needed: type conflict: current `project`, inferred `resource`; concepts need owner assignment
- Suggested:
```yaml
type: project
area: '[[Career]]'
status: active
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/SC-New-Works-Tech-Event-Sprint.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
- Review needed: type conflict: current `project`, inferred `resource`; concepts need owner assignment
- Suggested:
```yaml
type: project
area: '[[Career]]'
status: active
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Claude and Vertex AI save day by asking if Tailscale was installed and when it wasn't.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Claude in Chrome gets stuck for days over the wildest scenarios.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Clean up local Mac VS Code, offload to Pi's or VM😈.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/vscode
- topic/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Code Problem Solving/Code Problem Solving and NotetakingGuidelines.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Code Problem Solving`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Code Problem Solving]]'
tags:
- topic/problemsolving
source: imported
folder_origin: 02 Areas/Code Problem Solving
migration_status: v4-dry-run
```

### 02 Areas/Code Problem Solving/Problems Views.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Code Problem Solving`
- Review needed: type conflict: current `utility`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Code Problem Solving]]'
tags:
- topic/problemsolving
source: imported
folder_origin: 02 Areas/Code Problem Solving
migration_status: v4-dry-run
```

### 02 Areas/Code Problem Solving/Skill Tree - Code Problem Solving.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Code Problem Solving`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Code Problem Solving]]'
tags:
- topic/skill-tree
- topic/problemsolving
- topic/interview
- topic/systems-design
- topic/ai-coding
source: imported
folder_origin: 02 Areas/Code Problem Solving
migration_status: v4-dry-run
```

### 02 Areas/Code Problem Solving/problems.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Code Problem Solving`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Code Problem Solving]]'
tags:
- topic/problemsolving
source: imported
folder_origin: 02 Areas/Code Problem Solving
migration_status: v4-dry-run
```

### 02 Areas/Confidential/Relationships/Approaching Women.md

- Confidence: `medium`
- Destination: `_private/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; path contains private/confidential segment; area inferred from folder `Private`
- Review needed: unprefixed tag `to-process`; unprefixed tag `social-wellness`; unprefixed tag `relationships`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Private]]'
source: imported
folder_origin: 02 Areas/Confidential/Relationships
migration_status: v4-dry-run
```

### 02 Areas/Confidential/Relationships/Body Count.md

- Confidence: `medium`
- Destination: `_private/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; path contains private/confidential segment; area inferred from folder `Private`
- Review needed: unprefixed tag `relationships`; unprefixed tag `private`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Private]]'
source: imported
folder_origin: 02 Areas/Confidential/Relationships
migration_status: v4-dry-run
```

### 02 Areas/Confidential/Relationships/Ivy was right about the adderall.md

- Confidence: `medium`
- Destination: `_private/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; path contains private/confidential segment; area inferred from folder `Private`
- Review needed: unprefixed tag `relationships`; unprefixed tag `adderall`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Private]]'
source: imported
folder_origin: 02 Areas/Confidential/Relationships
migration_status: v4-dry-run
```

### 02 Areas/Confidential/Relationships/Looking for a safe, authentic, meaningful space to connect.md

- Confidence: `medium`
- Destination: `_private/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; path contains private/confidential segment; area inferred from folder `Private`
- Review needed: status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Private]]'
source: imported
folder_origin: 02 Areas/Confidential/Relationships
migration_status: v4-dry-run
```

### 02 Areas/Confidential/Relationships/Master Sab Feeld Profile Build Up.md

- Confidence: `medium`
- Destination: `_private/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; path contains private/confidential segment; area inferred from folder `Private`
- Review needed: unprefixed tag `feeld`; unprefixed tag `fantasy`; unprefixed tag `dating`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Private]]'
source: imported
folder_origin: 02 Areas/Confidential/Relationships
migration_status: v4-dry-run
```

### 02 Areas/Confidential/Relationships/Overcommunicating interest to women is Bilzerian’s biggest lesson from thousands of experiences on what not to do.md

- Confidence: `medium`
- Destination: `_private/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; path contains private/confidential segment; area inferred from folder `Private`
- Review needed: unprefixed tag `pickup`; unprefixed tag `mistakes`; unprefixed tag `game`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Private]]'
source: imported
folder_origin: 02 Areas/Confidential/Relationships
migration_status: v4-dry-run
```

### 02 Areas/Confidential/Relationships/Say No to Breadcrumbing!.md

- Confidence: `medium`
- Destination: `_private/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; path contains private/confidential segment; area inferred from folder `Private`
- Review needed: unprefixed tag `wellness`; unprefixed tag `relationships`; unprefixed tag `peace`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Private]]'
source: imported
folder_origin: 02 Areas/Confidential/Relationships
migration_status: v4-dry-run
```

### 02 Areas/Confidential/Relationships/She is no longer emotionally motivated for relationship because I would lust after outcomes while being routinely needy and affected.md

- Confidence: `medium`
- Destination: `_private/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; path contains private/confidential segment; area inferred from folder `Private`
- Review needed: unprefixed tag `relationships`; unprefixed tag `breakup`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Private]]'
source: imported
folder_origin: 02 Areas/Confidential/Relationships
migration_status: v4-dry-run
```

### 02 Areas/Confidential/Relationships/Why did that Noa dream be the one so vivid.md

- Confidence: `medium`
- Destination: `_private/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; path contains private/confidential segment; area inferred from folder `Private`
- Review needed: unprefixed tag `dream/journal`; unprefixed tag `dream`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Private]]'
source: imported
folder_origin: 02 Areas/Confidential/Relationships
migration_status: v4-dry-run
```

### 02 Areas/Confidential/SMW/General MW Element Delivery for Meetings Overview and Notes.md

- Confidence: `medium`
- Destination: `_private/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; path contains private/confidential segment; area inferred from folder `Private`
- Review needed: unprefixed tag `wildmen`; unprefixed tag `mens-weekend`; unprefixed tag `elements-calls`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Private]]'
source: imported
folder_origin: 02 Areas/Confidential/SMW
migration_status: v4-dry-run
```

### 02 Areas/Config history for ease of next time setup.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- tool/git
- tool/terminal
- tool/tmux
- topic/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Core Team Call 2026-W12.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Daily Workflow Execution.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- topic/workflow
- scope/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Exports/CLI/Codex and Claude log history + hooks.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas/Exports/CLI
migration_status: v4-dry-run
```

### 02 Areas/Exports/Kaleidoscope Dygma for custom firmware.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ergonomics
- tool/git
- tool/terminal
- topic/web-dev
source: imported
folder_origin: 02 Areas/Exports
migration_status: v4-dry-run
```

### 02 Areas/Exports/LLMs don't write code, compilers do (they fill structure).md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas/Exports
migration_status: v4-dry-run
```

### 02 Areas/Finances/Keystone Notes.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Finances`
- Review needed: unprefixed tag `Evergreen`; unprefixed tag `notes/evergreen`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Finances]]'
tags:
- scope/writing
source: imported
folder_origin: 02 Areas/Finances
migration_status: v4-dry-run
```

### 02 Areas/GDD - no mention of OpenClaw until it was forced.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/openclaw
- topic/ai
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Google first-vm compute engine setup workflow using gcloud aliases.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/gcp
- topic/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Health/Configure Swish's modifier keys.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
source: imported
folder_origin: 02 Areas/Health
migration_status: v4-dry-run
```

### 02 Areas/Health/Ergonomic & Nerve  Incident log.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health
migration_status: v4-dry-run
```

### 02 Areas/Health/Finger abductions and nerve glides are non-negotiables.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
source: imported
folder_origin: 02 Areas/Health
migration_status: v4-dry-run
```

### 02 Areas/Health/I am doing nerve glides and flosses and stretches more often now 2026-01.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health
migration_status: v4-dry-run
```

### 02 Areas/Health/MUST USE health and nerve decompression protocols.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health
migration_status: v4-dry-run
```

### 02 Areas/Health/MagSafe-Magnetic-Tenting-Kit-Hinges-and-Setup.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/Cognitive Benefits of Weightlifting for reminding me why I do it.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Health]]'
source: imported
folder_origin: 02 Areas/Health/Workouts
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/YB0/Day1-2026-03-14.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/YB0
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/YB0/Day2-2026-03-15.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/YB0
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/YB0/Day3-2026-03-15.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/YB0
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/YB1 Day 1.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `workout`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/YB1 Day 2.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `workout`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/YB1 Day 3.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `workout`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_archive/day-1.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `workout`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_archive
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_archive/day-2.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `workout`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_archive
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_archive/day-3.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `workout`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_archive
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_archive/day-4.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `workout`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_archive
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_archive/get-swole-2023-03-05-15.14.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `workout-record`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_archive
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_archive/get-swole.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `workout`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_archive
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_archive/leg-day-2023-03-05-15.06.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `workout-record`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_archive
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_archive/leg-day.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `workout`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_archive
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercise-records/bench-press-2023-03-05-15.15.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `exercise-record`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercise-records
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercise-records/bicep-curl-2023-03-05-15.16.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `exercise-record`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercise-records
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercise-records/calf-raises-2023-03-05-15.08.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `exercise-record`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercise-records
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercise-records/lat-pulldown-2023-03-05-15.16.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `exercise-record`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercise-records
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercise-records/leg-press-2023-03-05-15.09.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `exercise-record`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercise-records
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercise-records/lunges-2023-03-05-15.09.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `exercise-record`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercise-records
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercise-records/rowing-2023-03-05-15.09.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `exercise-record`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercise-records
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercise-records/rowing-2023-03-05-15.16.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; unprefixed tag `exercise-record`; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercise-records
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/Seated Neutral Grip Chest Press.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/back-braced-ez-curl.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/banded-45s.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/barbell-good-mornings.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/bayesian-curls.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/bench-press.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/bicep-curl.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/cable-crossovers.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/cable-tate-press.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/calf-press.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/calf-raises.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/clavicular-cable-flye.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/cross-body-tricep-extension.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/db-bench-press.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/dips.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/hack-squat-reverse-banded.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/hip-brace-cable-lat-rows.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/hip-thrust.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/incline-db-row.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/incline-press.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/lat-pulldown.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/leg-extension-unilateral.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/leg-extension.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/leg-press.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/lunges.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/machine-laterals.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/machine-rows.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/quad-leg-press.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/rowing.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/seated-leg-curl.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/smith-machine-kelso-shrugs.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/smith-press-behind-neck.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/supinated-grip-cable-rows.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/supinated-grip-chin-ups.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/supinated-grip-lat-pulldowns.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/trap-bar-rdl.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/exercises/upper-back-dumbbell-row.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: status exists on non-project/event type; unprefixed tag `exercise`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/exercises
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/workout-records/Iron Pulse - Lower - 2026-04-02.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/workout-records
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_database/workout-records/Iron Pulse - Upper - 2026-04-01.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_database/workout-records
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_templates/day-template.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `utility`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_templates
migration_status: v4-dry-run
```

### 02 Areas/Health/Workouts/_templates/program-template.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `utility`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: utility
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health/Workouts/_templates
migration_status: v4-dry-run
```

### 02 Areas/Health/YS7 Upper 1.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health
migration_status: v4-dry-run
```

### 02 Areas/Health/YS7 Upper 2.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Health`
- Review needed: type conflict: current `log`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: log
area: '[[Health]]'
tags:
- scope/health
source: imported
folder_origin: 02 Areas/Health
migration_status: v4-dry-run
```

### 02 Areas/Idea for Dygma raise keyboard - each thumb cluster is 7 distinct keys.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/dygma
- tool/keyboard
- scope/ergonomics
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Journaling to build keyboard inuition to complete the final layers.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/dygma
- tool/keyboard
- scope/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Jules Value Parsing  Method of a lot of Code.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- topic/ai
- tool/jules
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/LMN Official Zapier Integrations Article.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Lazygit Day 1 - creator video feature speedrun.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Learn Neovim Configuration via Plugins and their Docs.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Learning/A new AI&Code Muscle has emerged and it's time to lift.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `problems/solving`; unprefixed tag `interview/prep`; unprefixed tag `code/problems`; unprefixed tag `anchor`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/A powered up Second Brain style Obsidian fueled by NotebookLM.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `research`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- tool/obsidian
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Any system for personal use can be simplified .md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `learning`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
project: obsidian
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Carefully using AI in a smart notes system .md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `learning`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
project: obsidian
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Claude Code Filesystem MCP Tools.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `claude-code`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- tool/claude-code
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Claude Code Power User Primer.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `terminal`; unprefixed tag `primer`; unprefixed tag `learning`; unprefixed tag `claude-code`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- tool/claude-code
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Claude Skills are reusable components for specific tasks and specialized functions.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `claude-code`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Codex Creating Agents MD.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `terminal`; unprefixed tag `CLI`; unprefixed tag `AI/codex`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Creating a Claude Skills UI prompt library.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `claude-code`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Docs Patterns and Habits To Watch For.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `specs/reading`; unprefixed tag `learning`; unprefixed tag `docs/reading`; unprefixed tag `docs`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Gemini CLI commands and options.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `CLI`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- tool/gemini
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Gemini Gems are equivalent to Claude Skills.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `claude-code`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- tool/gemini
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/High quality, non-trivial, novel questions to answer instead of a summary.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `XY-problem`; unprefixed tag `questions`; unprefixed tag `learning`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Ideal Typing Position Form.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `workplace`; unprefixed tag `learning`; unprefixed tag `ergonomics`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/ergonomics
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Jules CLI is Google's asynchronous coding agent.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `CLI`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- topic/AI
- topic/agents
- topic/ai-coding
- topic/cli
- tool/jules
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Keyboard positioned split sides below my chair.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `learning`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/ergonomics
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Learning - Using AI in Complex Codebases.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `context-engineering`; unprefixed tag `complex-problems`; unprefixed tag `brownfield-problems`; unprefixed tag `AI-code`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/MCP Server setup for Obsidian vaults.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `terminal`; unprefixed tag `primer`; unprefixed tag `learning`; unprefixed tag `claude-code`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- tool/obsidian
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Obsidian Shortcuts for Quality of Life Workflows.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `automations`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- tool/obsidian
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Obsidian tasks terminal scripts in Python.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `terminal`; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- tool/obsidian
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/One NotebookLM notebook per theme or subject that you add sources to.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `notebookLM`; unprefixed tag `learning`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
project: notebookLM
tags:
- tool/obsidian
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/OpenCode CLI commands and options.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `CLI`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Quick vim survival guided commands .md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `learning`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
project: BDR
tags:
- tool/vim
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/STAR Summary of Claude Code + Obsidian Vault Integration 2025.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `project-management-system`; unprefixed tag `obsidian`; unprefixed tag `mcp-vault-integration`; unprefixed tag `MCP`; unprefixed tag `claude-code`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- tool/claude-code
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Ship Code while asleep using Ralph Wiggum technique.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `ralph-wiggum`; unprefixed tag `AI/technique/ralph`; unprefixed tag `AI/technique`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Styx-and-NeoOrg-as-per-document-language-exploration.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Syntax of commands for running scripts  (macOS zsh) step-by-step.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `zsh`; unprefixed tag `terminal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Terminal scripts for dashboard style views.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `terminal`; unprefixed tag `scripts`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/The purpose of anchor notes is to instantly restore context and answer what matters now.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`; anchor-like filename adjusted structural type
- Review needed: type conflict: current `resource`, inferred `area`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Transcript scraping using the YTT extension .md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `learning`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
project: terminal
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Video - 1 Habit for Productivity - Andrew Huberman.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `transcript`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Video - Big Tech Engineers are Idiots? Not actually but....md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `video`; unprefixed tag `learning`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Video - The #1 Habit for Productivity - Andrew Huberman.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `learning`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/learning
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Workplace Cue Hiearchy or Checklist.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `workplace`; unprefixed tag `ergonomics`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/ergonomics
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning/Workplace Recovery Steps.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Learning`
- Review needed: status exists on non-project/event type; unprefixed tag `workplace`; unprefixed tag `ergonomics`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[Learning]]'
tags:
- scope/ergonomics
source: imported
folder_origin: 02 Areas/Learning
migration_status: v4-dry-run
```

### 02 Areas/Learning Pi's Linux file system.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ergonomics
- scope/learning
- scope/ops
- tool/neovim
- tool/obsidian
- tool/terminal
- tool/tmux
- topic/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Lessons from the SC Works.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/LinkedIn Payload.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- lang/js
- scope/ergonomics
- scope/mindset
- scope/ops
- tool/neovim
- tool/terminal
- topic/ai
- topic/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Log workouts.csv.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/fitness
- scope/ops
- scope/writing
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Lovable trial.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- topic/web-dev
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Love's Canvassing Management Program.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Love's request for karoake for a cause.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/M1 Macs are GOAT.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: personal
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Make NeoVim Home -  Multi-Week Plan for 2026 proficiency.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: area
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Make NeoVim Home - One-Fix-Per-Session with copilot & co-config editing AI training wheels.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; status exists on non-project/event type
- Suggested:
```yaml
type: area
tags:
- tool/neovim
- topic/GDD
concepts:
- '[[Codebase Analysis]]'
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/March 2026 Element on Ego and Context.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/health
- scope/learning
- scope/mindset
- tool/git
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Matt Stein advice - get the real job, learn from within, do your thing on your time on your devices aka do it right, and build yourself.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Maximize Google AI Pro credits and finish them by.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/fitness
- scope/learning
- scope/ops
- tool/GoogleAI
- tool/gemini
- tool/git
- tool/roadmap
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Mayer Philosophy Digression.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Memorize a few nerve glide exercises in 2026-01.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Metacognition and higher order thinking.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Minimal Agent Infrastructure is a Work Contract.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Morgan NA Training.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/finance
- scope/ops
- scope/writing
- tool/git
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Multi-Device Git Workflow.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/git
- topic/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/My Obsidian Tasks Full Calendar synchronized with Apple apps setup.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/My Tmux config.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/ops
- tool/neovim
- tool/terminal
- tool/tmux
- topic/ai
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/My assets as a developer are my humanity and problem-solving logic.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/My shortcuts mapping system for keyboard shortcuts.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/ergonomics
- scope/mindset
- scope/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/My_DevInfra/Elegant terminal commands used to view periodic notes during the vault migrations.md

- Confidence: `medium`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `My_DevInfra`
- Review needed: unprefixed tag `bash`; unprefixed tag `scripts`; unprefixed tag `terminal`; unprefixed tag `vault/migration`; concepts need owner assignment
- Suggested:
```yaml
type: resource
area: '[[My_DevInfra]]'
tags:
- scope/writing
- tool/git
- tool/obsidian
- tool/terminal
source: imported
folder_origin: 02 Areas/My_DevInfra
migration_status: v4-dry-run
```

### 02 Areas/My_DevInfra/My_Neovim/Neovim-and-Obsidian-Integration-explained-by-Claude-CLI-since-Claude-desktop-is-2GB-RAM.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `My_DevInfra`
- Review needed: type conflict: current `area`, inferred `resource`
- Suggested:
```yaml
type: area
area: '[[My_DevInfra]]'
tags:
- topic/
- tool/
concepts:
- '[[AI Tooling]]'
- '[[Infrastructure]]'
source: imported
folder_origin: 02 Areas/My_DevInfra/My_Neovim
migration_status: v4-dry-run
```

### 02 Areas/My_DevInfra/My_Neovim/workflow-- 5  late 02.2026 Neovim workflows key commands only.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `My_DevInfra`
- Review needed: type conflict: current `area`, inferred `resource`
- Suggested:
```yaml
type: area
area: '[[My_DevInfra]]'
tags:
- scope/IDE
- tool/neovim
- tool/obsidian
concepts:
- '[[Keybindings]]'
- '[[lazyvim]]'
- '[[Developer Workflow]]'
source: imported
folder_origin: 02 Areas/My_DevInfra/My_Neovim
migration_status: v4-dry-run
```

### 02 Areas/My_DevInfra/OpenClaw/Informal excerpt of OpenClaw glossary or terminology explained and defined.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `My_DevInfra`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[My_DevInfra]]'
tags:
- topic/openclaw
- tool/hooks
- topic/config
- tool/openclaw
- topic/agents
- scope/learning
source: imported
folder_origin: 02 Areas/My_DevInfra/OpenClaw
migration_status: v4-dry-run
```

### 02 Areas/My_DevInfra/OpenClaw/OpenClaw broke again, exhaustion from running the same loop trying to fix it.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `My_DevInfra`
- Review needed: type conflict: current `project`, inferred `resource`
- Suggested:
```yaml
type: project
area: '[[My_DevInfra]]'
status: done
concepts:
- '[[Developer Workflow]]'
- '[[Infrastructure]]'
- '[[AI Tooling]]'
source: imported
folder_origin: 02 Areas/My_DevInfra/OpenClaw
migration_status: v4-dry-run
```

### 02 Areas/My_DevInfra/Terminal/Ghostty + tmux as the cockpit, Neovim as the workbench, and Obsidian as the memory layer.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `My_DevInfra`
- Review needed: type conflict: current `area`, inferred `resource`
- Suggested:
```yaml
type: area
area: '[[My_DevInfra]]'
concepts:
- '[[Developer Workflow]]'
- '[[IDE]]'
- '[[NeoVim]]'
source: imported
folder_origin: 02 Areas/My_DevInfra/Terminal
migration_status: v4-dry-run
```

### 02 Areas/My_DevInfra/Terminal/Terminal Browsing - Lynx Links and NotebookLM CLI.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `My_DevInfra`
- Review needed: type conflict: current `area`, inferred `resource`; unprefixed tag `workflow`; unprefixed tag `terminal`; unprefixed tag `browsing`; unprefixed tag `lynx`; unprefixed tag `links`; unprefixed tag `notebooklm`; unprefixed tag `zsh`
- Suggested:
```yaml
type: area
area: '[[My_DevInfra]]'
concepts:
- '[[Developer Workflow]]'
- '[[Infrastructure]]'
- '[[AI Tooling]]'
source: imported
folder_origin: 02 Areas/My_DevInfra/Terminal
migration_status: v4-dry-run
```

### 02 Areas/My_DevInfra/The generalized core pipeline for agentic workflow dispatching.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `My_DevInfra`
- Review needed: type conflict: current `project`, inferred `resource`
- Suggested:
```yaml
type: project
area: '[[My_DevInfra]]'
status: active
tags:
- scope/memory
- topic/ai
- scope/career
- topic/GDD
- scope/writing
- topic/ops
concepts:
- '[[Developer Workflow]]'
- '[[Infrastructure]]'
- '[[AI Tooling]]'
source: imported
folder_origin: 02 Areas/My_DevInfra
migration_status: v4-dry-run
```

### 02 Areas/My_DevInfra/Zed/Zed Search All Files and ripgrep Query Syntax.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `My_DevInfra`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; unprefixed tag `project`; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[My_DevInfra]]'
source: imported
folder_origin: 02 Areas/My_DevInfra/Zed
migration_status: v4-dry-run
```

### 02 Areas/My_DevInfra/myNeovim/Neovim-and-Obsidian-Integration-explained-by-Claude-CLI-since-Claude-desktop-is-2GB-RAM.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `My_DevInfra`
- Review needed: type conflict: current `area`, inferred `resource`
- Suggested:
```yaml
type: area
area: '[[My_DevInfra]]'
tags:
- topic/
- tool/
concepts:
- '[[CLI Workflow]]'
- '[[Terminal Workflow]]'
- '[[lazyvim]]'
- '[[NeoVim]]'
source: imported
folder_origin: 02 Areas/My_DevInfra/myNeovim
migration_status: v4-dry-run
```

### 02 Areas/My_DevInfra/myNeovim/wfl - 5  late 02.2026 Neovim workflows key commands only.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `My_DevInfra`
- Review needed: type conflict: current `area`, inferred `resource`
- Suggested:
```yaml
type: area
area: '[[My_DevInfra]]'
tags:
- scope/IDE
- tool/neovim
- tool/obsidian
concepts:
- '[[CLI Workflow]]'
- '[[Editor Workflow]]'
- '[[Developer Workflow]]'
source: imported
folder_origin: 02 Areas/My_DevInfra/myNeovim
migration_status: v4-dry-run
```

### 02 Areas/My_DevInfra/tmux glowup - session picker, status bar, scratchpad.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `My_DevInfra`
- Review needed: type conflict: current `area`, inferred `resource`
- Suggested:
```yaml
type: area
area: '[[My_DevInfra]]'
tags:
- scope/learning
- tool/terminal
- tool/openclaw
- tool/tmux
concepts:
- '[[CLI Workflow]]'
- '[[Editor Workflow]]'
- '[[Developer Workflow]]'
- '[[Terminal Workflow]]'
source: imported
folder_origin: 02 Areas/My_DevInfra
migration_status: v4-dry-run
```

### 02 Areas/New Dygma Raise Keyboard layout.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/ergonomics
- tool/git
- tool/neovim
- tool/obsidian
- tool/terminal
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/New Note Wiz v3.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
- scope/vault
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/New Tech SC Event Questions for Presenters.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- topic/ai
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/New-Note-Wiz-3.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/New-Note-Wiz-Test-1.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Not Overloaded,.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Not So Roundtable 2026-W16.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Not So Roundtable Week 6 Call 1.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Not So Week 11.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/NotebookLM CLI Power User Aliases and Text Expansion Macros.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- tool/notebookLM
- tool/terminal
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/NotebookLM for coding and engineering.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/NotebookLM must be done in stages.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- topic/ai
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/OpenClaw 2026- Updates.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- scope/communication
- scope/ergonomics
- scope/learning
- scope/ops
- scope/writing
- tool/git
- tool/obsidian
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/OpenClaw Raspberry Pi Setup Finally.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/openclaw
- tool/pi
- topic/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/OpenClaw and Antigravity Fusion Powerful.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- lang/py
- tool/git
- topic/ai
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/OpenClaw dual mac and pi setup.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/openclaw
- tool/pi
- topic/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/OpenClaw on browser could be better for me long term?.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- tool/terminal
- topic/ai
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/OpenClaw session lost and return.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- lang/js
- scope/communication
- tool/terminal
- topic/ai
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Openclaw Pairing Struggle Session with Commands and Explanation.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- topic/ai
- topic/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Owner review of Obsidian notes, normalized V4 schema, then back to ingestion.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
status: active
tags:
- scope/career
- topic/context
- tool/RAG
- lang/python
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Pen-Test Tool Zed Attack Proxy or ZAP finds issues in web apps.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Personal - going to start using this vault as my mostly personal one.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Personal - memorize motions of a few nerve and mobility exercises.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Phase 4 complete but the heart cannot update nodes or react accordingly.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- topic/web-dev
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Pi Coding Agent proves that minimal and constrained competes with overly-equipped and maintained.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Pi ~ Raspberry Pi Headless Setup 4GB and 8GB 2026.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Picking and choosing and pruning plugins to keep Obsidian lean and performant.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- tool/obsidian
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Plan Today.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/fitness
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Plan for Raspberry Pi Usage, OpenClaw, and Jules.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/openclaw
- tool/pi
- topic/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Portfolio site is Vercel-ready and shareable.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `interview/sprint`; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- topic/web-dev
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Portfolio website containing my current tech stack.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- topic/web-dev
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Process for Notetaking.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Question for Mastering Claude Code Primer for project mgmt automation.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Quotes on resilience and withstand adversity and winning.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/mindset
- scope/writing
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Qwen Meetup in South Korea had bangers.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/RGB lighting evolution indicating whether  a key ought to be pressed by the same side hand or not.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Raycast AI integration - PWA hotkeys, shortcuts to folders in Dock.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Raycast quick reference keyboard shortcuts.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ergonomics
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Reading the OpenClaw CLI Power User Guide.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/openclaw
- topic/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Review the Ghostty docs as a light workflow block.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/ghostty
- topic/workflow
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Session Card.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; unprefixed tag `context/session`; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- scope/meta
- tool/git
- tool/obsidian
- topic/ai
- topic/ops
- topic/web-dev
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Shortcuts Anchor for smart, evidence-driven, useful shortcuts and automations.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: area
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Showering twice a day gives time to reflect an process the subconscious.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/health
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Skill Tree Creation Day 1.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/ergonomics
- scope/fitness
- scope/ops
- scope/writing
- tool/git
- tool/neovim
- tool/obsidian
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Spaced Repetition iPad Workflow Idea.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ergonomics
- scope/learning
- scope/ops
- scope/writing
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Synopsis of Beiley Call revealed who am I emerging as a solo dev operator.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- scope/communication
- scope/health
- scope/learning
- scope/ops
- scope/solo
- scope/writing
- topic/ai
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/TRAE OpenClaw Architect Custom Agent.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/openclaw
- tool/trae
- topic/ai
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Tailored-Prompt-Book.md.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; unprefixed tag `1`; unprefixed tag `39`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/The 5 areas OpenClaw's "harness"  meaningfully is weak.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/The AMC in action to unfuck my life.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/The Pomodoro Work-Refine-Reflect Loop.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/The get back into it workflow 2026.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ops
- scope/writing
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/The moment I finally convinced myself I really am doing engineering.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/The non-linear solution to the big task list action plans and roadmaps.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; unprefixed tag `roadmap`; unprefixed tag `skilltree`; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/writing
- tool/obsidian
- topic/web-dev
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/The ultimate ergonomic hack is switching posture and sitting configurations two or three times per session.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; unprefixed tag `Evergreen`; unprefixed tag `MIQ`; unprefixed tag `ergonomics`; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/ergonomics
- scope/health
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Three node Openclaw recovery plan.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/openclaw
- topic/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Two Track Plan to Finishing GDD and MyAPI.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Understanding OpenClaw's cron, node loop and then a router and grep for Jules.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/openclaw
- topic/ops
- topic/ai
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Use Zed Search Files Once per Type.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Use the other MagSafe rings to create the necessary uniform levelness in reusing the original tenting kit.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/VS Code Power User Setup Era 2026.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/vscode
- topic/ops
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Vincent - You need to 1099 and start expensing your time and purchases.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
tags:
- scope/career
- scope/finance
- topic/consulting
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Warm burning Nerve irritation incident report.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `desksetup`; unprefixed tag `ergonomics`; unprefixed tag `rsirecovery`; unprefixed tag `trackpad`; unprefixed tag `ulnar_nerve`; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/career
- scope/communication
- scope/ergonomics
- scope/health
- scope/mindset
- scope/ops
- tool/git
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Welcome Back Triple Clean up overshadowed the new men.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Wenzels deal with Mark Stein.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Wildmen Point Program Code of Honor Card.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Writing in your own words is the real second Brain.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/mindset
- scope/ops
- scope/writing
- tool/obsidian
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Zarconi Photojournalism Men of Steel .md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `personal`; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Zed Day 1 basic keyboard workflows picking up quick.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/zed
- tool/keyboard
- topic/workflow
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Zed installed to MacOS, remote connection to SSD-BIG, new era begins.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/Zed new keymaps JSON table with dual use keys.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- tool/zed
- topic/keymaps
- scope/keyboard
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/classic rebase conflict with git diff, show, and reflog to visualize and show evidence of conflict and resolve.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/clipboard-to-Obsidian.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/dotfiles.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/fzf - Interactive X-Ray Mode is absurdly helpful.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- tool/neovim
- tool/terminal
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/hand therapy tools integration plan 2026.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/jDecontextualize ADHD as sleep disorder.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/communication
- scope/health
- scope/ops
- scope/sleep
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/john wicking it.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/learning
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/nvim - Neotree and File Explorer Workflow Loop.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/neovim
- topic/workflow
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/vi - deleting around and including curly brace code blocks.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: type conflict: current `area`, inferred `resource`; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: area
area: '[[Infrastructure]]'
tags:
- tool/neovim
- topic/workflow
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

### 02 Areas/zshrc ghostty & iterm2 failure incident reflections.md

- Confidence: `review`
- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
tags:
- scope/mindset
- tool/terminal
source: imported
folder_origin: 02 Areas
migration_status: v4-dry-run
```

## High-Confidence Sample

### 02 Areas/Career/2026-Deep-dive-into-Modern-System-Programming.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
```yaml
type: resource
area: '[[Career]]'
tags:
- scope/career
- topic/systems
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/Architecture Active Recall Cards.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
```yaml
type: resource
area: '[[Career]]'
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/FPSV - Mikael moving me to Sunday and Monday maybe.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
```yaml
type: resource
area: '[[Career]]'
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/First weekend new NA checklist and routine.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
```yaml
type: resource
area: '[[Career]]'
tags:
- scope/ops
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/Frictionless LinkedIn 2026 Update.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
```yaml
type: resource
area: '[[Career]]'
tags:
- scope/career
- scope/ops
- scope/writing
- tool/git
- topic/ai
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/Gold Thoughts.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
```yaml
type: resource
area: '[[Career]]'
tags:
- scope/ops
- tool/neovim
- tool/terminal
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/Justin Call - Revitalize website for mentorship and alumni and coaching.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
```yaml
type: resource
area: '[[Career]]'
tags:
- scope/career
- scope/communication
- topic/web-dev
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/Justin call 2 conversation.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
```yaml
type: resource
area: '[[Career]]'
tags:
- scope/communication
- topic/ai
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/Networking Pitch Cards - Project Set.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
```yaml
type: resource
area: '[[Career]]'
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/Networking Talking Points - Paradigm Shift.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
```yaml
type: resource
area: '[[Career]]'
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/Non-technical-professionals-on-AI-making-things-easier-but-its-the-tools-that-got-smarter.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
```yaml
type: resource
area: '[[Career]]'
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/Portfolio Websites of Peer or Near Peer Developers.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
```yaml
type: resource
area: '[[Career]]'
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/TODAY_SPRINT.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
```yaml
type: resource
area: '[[Career]]'
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Career/There's hope again - be uncompromisingly you and you will make it.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Career`
```yaml
type: resource
area: '[[Career]]'
tags:
- scope/career
source: imported
folder_origin: 02 Areas/Career
migration_status: v4-dry-run
```

### 02 Areas/Code Problem Solving/Avoiding shadow work when my big boy job win is so close.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Code Problem Solving`
```yaml
type: resource
area: '[[Code Problem Solving]]'
source: imported
folder_origin: 02 Areas/Code Problem Solving
migration_status: v4-dry-run
```

### 02 Areas/Code Problem Solving/Code Problem Solving Anchor.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Code Problem Solving`; anchor-like filename adjusted structural type
```yaml
type: area
area: '[[Code Problem Solving]]'
tags:
- scope/career
- topic/interview
- topic/problemsolving
source: imported
folder_origin: 02 Areas/Code Problem Solving
migration_status: v4-dry-run
```

### 02 Areas/Code Problem Solving/easy/Count Vowels in String.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Code Problem Solving`
```yaml
type: resource
area: '[[Code Problem Solving]]'
tags:
- topic/algorithms
- topic/problemsolving
source: imported
folder_origin: 02 Areas/Code Problem Solving/easy
migration_status: v4-dry-run
```

### 02 Areas/Code Problem Solving/easy/Easy Problems Anchor.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Code Problem Solving`; anchor-like filename adjusted structural type
```yaml
type: area
area: '[[Code Problem Solving]]'
tags:
- topic/algorithms
- topic/problemsolving
source: imported
folder_origin: 02 Areas/Code Problem Solving/easy
migration_status: v4-dry-run
```

### 02 Areas/Code Problem Solving/easy/Find Max Element in Array.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Code Problem Solving`
```yaml
type: resource
area: '[[Code Problem Solving]]'
tags:
- topic/algorithms
- topic/problemsolving
source: imported
folder_origin: 02 Areas/Code Problem Solving/easy
migration_status: v4-dry-run
```

### 02 Areas/Code Problem Solving/easy/Reverse a String.md

- Destination: `areas/`
- Reasons: top-level folder `02 Areas` maps to `areas/`; area inferred from folder `Code Problem Solving`
```yaml
type: resource
area: '[[Code Problem Solving]]'
tags:
- topic/algorithms
- topic/problemsolving
source: imported
folder_origin: 02 Areas/Code Problem Solving/easy
migration_status: v4-dry-run
```
