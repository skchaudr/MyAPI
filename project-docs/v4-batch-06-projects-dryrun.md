# Vault Schema V4 Normalization Dry Run

Vault root: `/Users/saboor/Obsidian/SoloDeveloper`

## Summary

- Total files scanned: 174
- High confidence: 0
- Medium confidence: 0
- Needs review: 174

## Review Queue

### 01 Projects/01 Projects.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `01 Projects.md`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--01 Projects.md]]'
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/2026 ~ dotfiles repo must be made.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `2026 ~ dotfiles repo must be made.md`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--2026 ~ dotfiles repo must be made.md]]'
tags:
- tool/git
- tool/terminal
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/2026-W06 Anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `2026-W06 Anchor.md`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--2026-W06 Anchor.md]]'
status: active
tags:
- scope/career
- scope/mindset
- scope/ops
- scope/writing
- tool/neovim
- tool/terminal
- topic/ai
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/BDR/BDR Kanban.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `BDR`
- Review needed: missing area/project/concept connection; unprefixed tag `medium`; unprefixed tag `high`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--BDR]]'
source: imported
folder_origin: 01 Projects/BDR
migration_status: v4-dry-run
```

### 01 Projects/BDR/BDR Project Anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `BDR`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; unprefixed tag `project`; unprefixed tag `development`; unprefixed tag `bdr`; unprefixed tag `anchor`; concepts need owner assignment
- Suggested:
```yaml
type: project
project: BDR
status: active
source: imported
folder_origin: 01 Projects/BDR
migration_status: v4-dry-run
```

### 01 Projects/BDR/BDR Project Brief.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `BDR`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `project`; unprefixed tag `development`; unprefixed tag `context-management`; unprefixed tag `context-engineering`; unprefixed tag `code-agent`; unprefixed tag `bdr`; unprefixed tag `AI-code`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: BDR
source: imported
folder_origin: 01 Projects/BDR
migration_status: v4-dry-run
```

### 01 Projects/BDR/BDR Q4 Action Plan v1.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `BDR`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `project`; unprefixed tag `development`; unprefixed tag `bdr`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: BDR
source: imported
folder_origin: 01 Projects/BDR
migration_status: v4-dry-run
```

### 01 Projects/BDR/BDR-anchor-v2.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `BDR`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--BDR]]'
status: active
source: imported
folder_origin: 01 Projects/BDR
migration_status: v4-dry-run
```

### 01 Projects/BDR/Create an AGENTS.md for BDR.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `BDR`
- Review needed: missing area/project/concept connection; unprefixed tag `project`; unprefixed tag `bdr`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: BDR
source: imported
folder_origin: 01 Projects/BDR
migration_status: v4-dry-run
```

### 01 Projects/BDR/Understand how BDR works front to back.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `BDR`
- Review needed: missing area/project/concept connection; unprefixed tag `bdr`; unprefixed tag `interview-prep`; unprefixed tag `projects`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--BDR]]'
source: imported
folder_origin: 01 Projects/BDR
migration_status: v4-dry-run
```

### 01 Projects/BDR/Water Stone Sprint.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `BDR`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--BDR]]'
tags:
- scope/career
- scope/communication
- scope/finance
- scope/health
- scope/mindset
- scope/ops
- scope/writing
- tool/git
source: imported
folder_origin: 01 Projects/BDR
migration_status: v4-dry-run
```

### 01 Projects/Codex 5.4 CLI Thread Summary 3.7.26.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Codex 5.4 CLI Thread Summary 3.7.26.md`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Codex 5.4 CLI Thread Summary 3.7.26.md]]'
tags:
- scope/writing
- tool/git
- tool/obsidian
- tool/terminal
- tool/tmux
- topic/ai
- topic/ops
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/Daily Loop Solves One Problem.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Daily Loop Solves One Problem.md`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Daily Loop Solves One Problem.md]]'
tags:
- scope/learning
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/GDDP/ChatGPT 5.4 thinking played a significant role in crafting the GDAD Pipeline system.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- scope/career
- scope/communication
- scope/ops
- scope/writing
- tool/git
- tool/obsidian
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD - Definition of a good project graph of nodes for GDD.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD - GDDP commitment to understanding the system I am creating.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD - OpenClaw v1 begins.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[GDDP]]'
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD - Point of manual runs is to answer these questions.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--GDDP]]'
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD - Return router implementation since forward lane already proven.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- scope/learning
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD - Toy operator loop run with baby task, simple project,.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD - agentic or autonomous dispatch pipeline anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD - freezing system state for manual operator node runs.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[GDDP]]'
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD - just start and FAFO.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD - pivot return route and directory map.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[GDDP]]'
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD Main Thread Summary.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- scope/career
- scope/ops
- scope/writing
- tool/git
- tool/obsidian
- topic/ai
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD Tour by Claude Haiku and next steps forward.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD pivot - return loop fixed to prevent modification of project graph truth.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
- tool/GDDP
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD step back, scale back, simplify 3..28.26.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/Foundational-Context/Detailed-Big-Picture.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/Foundational-Context
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/Foundational-Context/GDD-Naming-and-Glossary.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/Foundational-Context
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/docs/architecture.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/docs
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/docs/capability-matrix.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/docs
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/docs/execution_model.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/docs
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/docs/safety_model.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/docs
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/docs/system_roles.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/docs
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/missions/mission_001_control_plane_bootstrap.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/missions
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/openclaw/AGENTS.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/openclaw
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/openclaw/HEARTBEAT.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/openclaw
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/openclaw/MEMORY.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/openclaw
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/openclaw/POLICIES.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/openclaw
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/openclaw/TOOLS.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/openclaw
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/prompts/claude_bootstrap.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/prompts
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/prompts/codex_bootstrap.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/GDAD-Control-Plane/prompts
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/architecture.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/capability-matrix.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/execution_model.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/roadmap.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/safety_model.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/system_roles.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/three-layer-model.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/v1/00-pipeline-overview.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs/v1
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/v1/01-event-schema.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs/v1
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/v1/02-job-schema.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs/v1
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/v1/03-queue-design.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs/v1
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/v1/04-classifier.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs/v1
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/v1/05-scope-check.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs/v1
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/v1/06-executor-routing.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs/v1
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/v1/07-jules-dispatch.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs/v1
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/v1/08-result-schema.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs/v1
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/v1/09-artifact-contract.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs/v1
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/v1/10-project-graph.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs/v1
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/v1/11-schema-versioning.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs/v1
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/v1/12-transcript-event-type.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs/v1
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/v1/13-artifact-verification.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs/v1
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/docs/v1/README.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/docs/v1
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/missions/mission_001_control_plane_bootstrap.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/missions
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/openclaw/AGENTS.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/openclaw
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/openclaw/HEARTBEAT.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/openclaw
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/openclaw/MEMORY.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/openclaw
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/openclaw/POLICIES.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/openclaw
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/openclaw/TOOLS.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/openclaw
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/prompts/claude_bootstrap.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/prompts
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/prompts/codex_bootstrap.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/prompts
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-Control-Center/prompts/openclaw-hardening-handoff.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
tags:
- topic/GDD
source: imported
folder_origin: 01 Projects/GDDP/GDD-Control-Center/prompts
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDD-ran-my-first-supervised-rep-and-succeded-to-dispatch.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `task`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[GDDP]]'
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/GDDO - operator practice manual run checklist.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--GDDP]]'
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/GDDP/Phase 4 Complete.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `GDDP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; unprefixed tag `11`; unprefixed tag `12`; unprefixed tag `13`; unprefixed tag `2`; unprefixed tag `5`; unprefixed tag `6`; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[GDDP]]'
status: active
source: imported
folder_origin: 01 Projects/GDDP
migration_status: v4-dry-run
```

### 01 Projects/Jules Prompts for SC Automation.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Jules Prompts for SC Automation.md`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Jules Prompts for SC Automation.md]]'
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/MyAPI Anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--MyAPI]]'
status: active
tags:
- topic/GDD
- tool/GDDP
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/MyAPI-UI-Anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--MyAPI]]'
status: active
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/README.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--MyAPI]]'
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/context-refinery anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--MyAPI]]'
status: active
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/myapi - first pass normalization of obsidian vault .md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--MyAPI]]'
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/refinement-queue-2026-04-20.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--MyAPI]]'
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/rubric.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--MyAPI]]'
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-15-anchor-pass-2.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--MyAPI]]'
status: active
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-15-anchor-tuned.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--MyAPI]]'
status: active
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-15-post-anchor-rerun.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--MyAPI]]'
status: active
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-15-tuned.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--MyAPI]]'
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-15.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--MyAPI]]'
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-16-canonical-anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--MyAPI]]'
status: active
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-16-narrow-anchors.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--MyAPI]]'
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-18-new-vm-baseline.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--MyAPI]]'
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-19-clean-index-dedup-normalized.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--MyAPI]]'
status: active
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-19-clean-index-no-clickbait-after-khoj-restart.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--MyAPI]]'
status: active
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-19-clean-index-no-clickbait-after-refinery-restart.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--MyAPI]]'
status: active
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-19-clean-index-no-clickbait.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--MyAPI]]'
status: active
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-19-clean-index.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--MyAPI]]'
status: active
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-19-daily-note-penalty.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--MyAPI]]'
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-19-source-aware-priors.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--MyAPI]]'
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-23-post-anchor-v2.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--MyAPI]]'
status: active
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/MyAPI/run-2026-04-25-blocker-pass.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `MyAPI`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--MyAPI]]'
source: imported
folder_origin: 01 Projects/MyAPI
migration_status: v4-dry-run
```

### 01 Projects/Phase 0 -- CIM & NUI Domain Selection and NotebookLM Workflow.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Phase 0 -- CIM & NUI Domain Selection and NotebookLM Workflow.md`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Phase 0 -- CIM & NUI Domain Selection and NotebookLM Workflow.md]]'
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/Portfolio/LinkedIn Sprint V2 for 2026 is arc-defining.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Portfolio`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Portfolio]]'
source: imported
folder_origin: 01 Projects/Portfolio
migration_status: v4-dry-run
```

### 01 Projects/Portfolio/Portfolio website planning and design.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Portfolio`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Portfolio]]'
tags:
- lang/js
- scope/career
- scope/health
- scope/writing
- tool/obsidian
- tool/terminal
- topic/ai
- topic/web-dev
source: imported
folder_origin: 01 Projects/Portfolio
migration_status: v4-dry-run
```

### 01 Projects/Portfolio/skc-2-anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Portfolio`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--Portfolio]]'
status: active
source: imported
folder_origin: 01 Projects/Portfolio
migration_status: v4-dry-run
```

### 01 Projects/Portfolio/skc-anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Portfolio`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--Portfolio]]'
status: active
source: imported
folder_origin: 01 Projects/Portfolio
migration_status: v4-dry-run
```

### 01 Projects/Santa Cruz Smart Automations.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Santa Cruz Smart Automations.md`
- Review needed: type conflict: current `project`, inferred `resource`; unprefixed tag `next-js`; unprefixed tag `lead-gen`; unprefixed tag `client-work`; concepts need owner assignment
- Suggested:
```yaml
type: project
area: freelance
project: '[[--Santa Cruz Smart Automations.md]]'
status: active
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/Semantic complexity around "already existing user profile" is why Zapier stays deliberately dumb.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Semantic complexity around "already existing user profile" is why Zapier stays deliberately dumb.md`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Semantic complexity around "already existing user profile" is why Zapier
  stays deliberately dumb.md]]'
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/SocialXP/Co-Design Group 1.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `SocialXP`
- Review needed: type conflict: current `log`, inferred `resource`; missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `socialXP`; concepts need owner assignment
- Suggested:
```yaml
type: log
project: '[[SocialXP Anchor]]'
source: imported
folder_origin: 01 Projects/SocialXP
migration_status: v4-dry-run
```

### 01 Projects/SocialXP/Co-Design Group Prep.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `SocialXP`
- Review needed: type conflict: current `log`, inferred `resource`; missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `socialXP`; concepts need owner assignment
- Suggested:
```yaml
type: log
project: '[[SocialXP Anchor]]'
source: imported
folder_origin: 01 Projects/SocialXP
migration_status: v4-dry-run
```

### 01 Projects/SocialXP/Co-Design-Group-2.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `SocialXP`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; unprefixed tag `socialXP`; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[SocialXP Anchor]]'
status: active
source: imported
folder_origin: 01 Projects/SocialXP
migration_status: v4-dry-run
```

### 01 Projects/SocialXP/Notion Collaborating Tips, Guidelines, etc.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `SocialXP`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `socialXP`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[SocialXP Anchor]]'
source: imported
folder_origin: 01 Projects/SocialXP
migration_status: v4-dry-run
```

### 01 Projects/SocialXP/SocialXP Anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `SocialXP`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; unprefixed tag `socialXP`; unprefixed tag `project`; unprefixed tag `anchor`; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[SocialXP Anchor]]'
status: active
source: imported
folder_origin: 01 Projects/SocialXP
migration_status: v4-dry-run
```

### 01 Projects/SocialXP/SocialXP Pre-Codesign Group 2026-01-21.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `SocialXP`
- Review needed: type conflict: current `log`, inferred `resource`; missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `socialXP`; concepts need owner assignment
- Suggested:
```yaml
type: log
project: '[[SocialXP Anchor]]'
source: imported
folder_origin: 01 Projects/SocialXP
migration_status: v4-dry-run
```

### 01 Projects/SocialXP/UX Reusable Automation Workflows.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `SocialXP`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `UI-UX`; unprefixed tag `socialXP`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[SocialXP Anchor]]'
source: imported
folder_origin: 01 Projects/SocialXP
migration_status: v4-dry-run
```

### 01 Projects/SocialXP/Vincent Social Interactivity App Meeting 1.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `SocialXP`
- Review needed: type conflict: current `log`, inferred `resource`; missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `social`; concepts need owner assignment
- Suggested:
```yaml
type: log
project: '[[SocialXP Anchor]]'
source: imported
folder_origin: 01 Projects/SocialXP
migration_status: v4-dry-run
```

### 01 Projects/SocialXP/Vincent Social Interactivity Meeting 2.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `SocialXP`
- Review needed: type conflict: current `log`, inferred `resource`; missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `social`; concepts need owner assignment
- Suggested:
```yaml
type: log
project: '[[SocialXP Anchor]]'
source: imported
folder_origin: 01 Projects/SocialXP
migration_status: v4-dry-run
```

### 01 Projects/SocialXP/Vincent Social Interactivity Meeting 3.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `SocialXP`
- Review needed: type conflict: current `log`, inferred `resource`; missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `social`; concepts need owner assignment
- Suggested:
```yaml
type: log
project: '[[SocialXP Anchor]]'
source: imported
folder_origin: 01 Projects/SocialXP
migration_status: v4-dry-run
```

### 01 Projects/SocialXP/Vincent’s Week 1 Suggested Work.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `SocialXP`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--SocialXP]]'
source: imported
folder_origin: 01 Projects/SocialXP
migration_status: v4-dry-run
```

### 01 Projects/SocialXP/Wireframes Day 1.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `SocialXP`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `socialXP`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[SocialXP Anchor]]'
source: imported
folder_origin: 01 Projects/SocialXP
migration_status: v4-dry-run
```

### 01 Projects/SocialXP Part 2.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `SocialXP Part 2.md`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--SocialXP Part 2.md]]'
tags:
- topic/ai
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/Solve-Bench/AI Sparring Loop.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Solve-Bench`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Solve Bench]]'
tags:
- topic/ai
source: imported
folder_origin: 01 Projects/Solve-Bench
migration_status: v4-dry-run
```

### 01 Projects/Solve-Bench/Solve-Bench-Anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Solve-Bench`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--Solve Bench]]'
status: active
source: imported
folder_origin: 01 Projects/Solve-Bench
migration_status: v4-dry-run
```

### 01 Projects/Universal Router/USR-Anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Universal Router`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--Universal Router]]'
status: active
source: imported
folder_origin: 01 Projects/Universal Router
migration_status: v4-dry-run
```

### 01 Projects/Vault Doctor practice opening soon.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Vault Doctor practice opening soon.md`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Vault Doctor practice opening soon.md]]'
tags:
- lang/py
- scope/ops
- tool/obsidian
- tool/terminal
- topic/ai
- topic/web-dev
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/Vault Keeper TIME.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Vault Keeper TIME.md`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Vault Keeper TIME.md]]'
tags:
- lang/py
- scope/communication
- tool/git
- tool/obsidian
- tool/terminal
- topic/ops
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/VaultDr/VaultDr-Anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `VaultDr`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--Vault Doctor]]'
status: active
source: imported
folder_origin: 01 Projects/VaultDr
migration_status: v4-dry-run
```

### 01 Projects/Vertex AI finally used day 1.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Vertex AI finally used day 1.md`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Vertex AI finally used day 1.md]]'
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/WAS/Beiley QuickBooks - cleaning books, re-categorizing transactions.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `WAS`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--Water and Stone]]'
status: active
source: imported
folder_origin: 01 Projects/WAS
migration_status: v4-dry-run
```

### 01 Projects/WAS/Beiley-Meeting-Prep-3.19.26.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `WAS`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Water and Stone]]'
source: imported
folder_origin: 01 Projects/WAS
migration_status: v4-dry-run
```

### 01 Projects/WAS/Beiley-Water-and-Stone-Landscaper-Part-Time-Job-Meeting.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `WAS`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Water and Stone]]'
source: imported
folder_origin: 01 Projects/WAS
migration_status: v4-dry-run
```

### 01 Projects/WAS/Creating a new website for Beiley using React and Vite.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `WAS`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--Water and Stone]]'
status: active
tags:
- topic/web-dev
- tool/lovable
- topic/react
- topic/vite
- topic/frontend
source: imported
folder_origin: 01 Projects/WAS
migration_status: v4-dry-run
```

### 01 Projects/WAS/LMN-QBO field discovery checklist.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `WAS`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Water and Stone]]'
source: imported
folder_origin: 01 Projects/WAS
migration_status: v4-dry-run
```

### 01 Projects/WAS/LMN-QBO first-flow discovery.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `WAS`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Water and Stone]]'
source: imported
folder_origin: 01 Projects/WAS
migration_status: v4-dry-run
```

### 01 Projects/WAS/WAS - Claude LMN QBO Manual Pre-Automation Sync.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `WAS`
- Review needed: missing area/project/concept connection; unprefixed tag `OFFICE`; unprefixed tag `SHOP`; unprefixed tag `1`; unprefixed tag `2`; unprefixed tag `3`; unprefixed tag `4`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Water and Stone]]'
source: imported
folder_origin: 01 Projects/WAS
migration_status: v4-dry-run
```

### 01 Projects/WAS/WAS - The core Zapier automations for Water and Stone.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `WAS`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; unprefixed tag `project`; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--Water and Stone]]'
status: active
source: imported
folder_origin: 01 Projects/WAS
migration_status: v4-dry-run
```

### 01 Projects/WAS/WAS-website-anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `WAS`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--Water and Stone]]'
status: active
source: imported
folder_origin: 01 Projects/WAS
migration_status: v4-dry-run
```

### 01 Projects/WAS/Water Stone Ops Infra Kickoff Plan.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `WAS`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Water and Stone]]'
tags:
- scope/career
- scope/communication
- scope/finance
- scope/ops
- tool/git
- topic/ops
- topic/web-dev
source: imported
folder_origin: 01 Projects/WAS
migration_status: v4-dry-run
```

### 01 Projects/Water and Stone Ride Along.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Water and Stone Ride Along.md`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Water and Stone Ride Along.md]]'
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/Zapier's Zaps are background listeners waiting to take action on a specified a trigger event.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `Zapier's Zaps are background listeners waiting to take action on a specified a trigger event.md`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--Zapier''s Zaps are background listeners waiting to take action on a
  specified a trigger event.md]]'
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/-- The Engineer's 5 W's of CIM and NUI - CRITICAL Anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--_Projects Archive]]'
status: active
tags:
- scope/career
- scope/communication
- scope/mindset
- scope/ops
- scope/writing
- tool/git
- topic/ops
- topic/web-dev
source: imported
folder_origin: 01 Projects/_Projects Archive
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/Asking Ty for a deposit or a retainer.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--_Projects Archive]]'
status: active
tags:
- scope/learning
source: imported
folder_origin: 01 Projects/_Projects Archive
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/API Evidence/github-about-dependency-graph.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM/API Evidence
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/API Evidence/github-change-used-by-data.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM/API Evidence
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/API Evidence/github-rest-dependency-graph.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM/API Evidence
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/API Evidence/github-rest-get-repository.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM/API Evidence
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/API Evidence/github-rest-issues.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM/API Evidence
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/API Evidence/github-rest-pulls.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM/API Evidence
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/API Evidence/github-rest-traffic.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM/API Evidence
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/API Evidence/github-webhooks-repositories.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM/API Evidence
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/API Evidence/hackernews-api.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM/API Evidence
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/CIM - Begin Ingestion, spin up the pipeline.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[Cultural Intel Monitor & NUI Anchor]]'
status: active
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/CIM - Google Vertex AI and Phase 0.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: type conflict: current `log`, inferred `resource`; missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `workout`; unprefixed tag `training`; concepts need owner assignment
- Suggested:
```yaml
type: log
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/CIM Anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--_Projects Archive]]'
status: active
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/CIM-Ty-and-the-ownership-conversation.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[Cultural Intel Monitor & NUI Anchor]]'
status: active
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/Cultural Intel Monitor & NUI Anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--_Projects Archive]]'
status: active
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/Deploy Phase 0 on GCP VM.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `gcp`; unprefixed tag `vm`; unprefixed tag `phase-0`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/LETTER OF UNDERSTANDING.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/Phase 0 -- NotebookLM Domain & Data Feasibility Research.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; unprefixed tag `phase-0`; unprefixed tag `data-strategy`; unprefixed tag `domain-selection`; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[Cultural Intel Monitor & NUI Anchor]]'
status: active
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/Phase 0 API Evidence Pack.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `phase-0`; unprefixed tag `api`; unprefixed tag `evidence`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/Phase-0-Domain-Selection.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `research`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/Zed + Pi Phase 0 Workflow.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[Cultural Intel Monitor & NUI Anchor]]'
status: active
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/hypotheses.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/let's build the GCP VM and ingestion scripts.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/phase 0 validation session explained, contested H4.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `project`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/phase-0-domain-candidates.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; unprefixed tag `phase-0`; unprefixed tag `domain-candidates`; unprefixed tag `data-feasibility`; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/CIM/signal_dictionary.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; status exists on non-project/event type; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[Cultural Intel Monitor & NUI Anchor]]'
tags:
- topic/cim
source: imported
folder_origin: 01 Projects/_Projects Archive/CIM
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/Cultulral Intel/Phase 0 -- NotebookLM Domain & Data Feasibility Research.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; unprefixed tag `phase-0`; unprefixed tag `data-strategy`; unprefixed tag `domain-selection`; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--_Projects Archive]]'
status: active
source: imported
folder_origin: 01 Projects/_Projects Archive/Cultulral Intel
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/First VM SSH CIMToken.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--_Projects Archive]]'
tags:
- topic/dsa
- topic/ops
source: imported
folder_origin: 01 Projects/_Projects Archive
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/Market-Sentinel/market-sentinel-anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--_Projects Archive]]'
status: active
source: imported
folder_origin: 01 Projects/_Projects Archive/Market-Sentinel
migration_status: v4-dry-run
```

### 01 Projects/_Projects Archive/SC Automations/SC Automations Update after AGY foundation with OpenClaw critique.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `_Projects Archive`
- Review needed: type conflict: current `project`, inferred `resource`; missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--_Projects Archive]]'
status: active
tags:
- topic/
source: imported
folder_origin: 01 Projects/_Projects Archive/SC Automations
migration_status: v4-dry-run
```

### 01 Projects/agy> SocialXP Browser Demo looks clean 2.22.26.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `agy> SocialXP Browser Demo looks clean 2.22.26.md`
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: resource
project: '[[--agy> SocialXP Browser Demo looks clean 2.22.26.md]]'
tags:
- scope/learning
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

### 01 Projects/smb-ops-hub-anchor.md

- Confidence: `review`
- Destination: `projects/`
- Reasons: top-level folder `01 Projects` maps to `projects/`; project inferred from folder `smb-ops-hub-anchor.md`; anchor-like filename adjusted structural type
- Review needed: missing area/project/concept connection; concepts need owner assignment
- Suggested:
```yaml
type: project
project: '[[--smb-ops-hub-anchor.md]]'
status: active
source: imported
folder_origin: 01 Projects
migration_status: v4-dry-run
```

## High-Confidence Sample
