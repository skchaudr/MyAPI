---
type: utility
title: V4 Tag Prefix Audit
area: '[[Vault]]'
source: original
---

# V4 Tag Prefix Audit

Vault root: `/Users/saboor/Obsidian/SoloDeveloper`

## Summary

- Total notes scanned: **1721**
- Notes with `tags:` field: **1460**
- Notes with at least one unprefixed tag: **92**
- Distinct unprefixed tag values: **100**
- Distinct prefixed tag values (already V4-clean): **142**

## Tier 2 Worklist — Unprefixed → Suggested Prefix

Each row is one tag value to migrate via the owner-pass CLI. The suggested prefix
is a heuristic; override during owner-pass when the meaning is wrong.

### Suggested DROP — structural noise (V4 uses `type:` for these)

| Tag | Files | Sample |
| --- | ----- | ------ |
| `task` | 9 | `09 Utilities/transcripts/transcript-Danger-Illusion-of-AI-Code.md`, `02 Areas/Blink Build SSH Pathway to GitHub.md`, `02 Areas/Health/Configure Swish's modifier keys.md`, `_tasks/Finish-GDDP-and-Khoj-project-audit.md`, `01 Projects/GDDP/GDD - pivot return route and directory map.md` |
| `project` | 8 | `02 Areas/Career/Configuring LMN for Beiley in a way that actually serves him.md`, `02 Areas/My_DevInfra/Zed/Zed Search All Files and ripgrep Query Syntax.md`, `01 Projects/SocialXP/SocialXP Anchor.md`, `01 Projects/BDR/BDR Project Anchor.md`, `01 Projects/BDR/Create an AGENTS.md for BDR.md` |

### → `lang/zsh`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `zsh` | 1 | `02 Areas/My_DevInfra/Terminal/Terminal Browsing - Lynx Links and NotebookLM CLI.md` |

### → `scope/ergonomics`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `ergonomics` | 2 | `05 Archive/_to-delete-after-30d/Ideal Typing Position Form.md`, `05 Archive/_to-delete-after-30d/Workplace Recovery Steps.md` |

### → `scope/learning`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `learning` | 2 | `05 Archive/_to-delete-after-30d/Ideal Typing Position Form.md`, `Templates/docs-reading-template.md` |

### → `scope/relationships`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `relationships` | 10 | `02 Areas/Confidential/Relationships/Women with critical parents.md`, `02 Areas/Confidential/Relationships/Body Count.md`, `02 Areas/Confidential/Relationships/Ivy OF Tips.md`, `02 Areas/Confidential/Relationships/She is no longer emotionally motivated for relationship because I would lust after outcomes while being routinely needy and affected.md`, `02 Areas/Confidential/Relationships/Approaching Women.md` |

### → `tool/neovim`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `neovim` | 1 | `_inbox/friction-log.md` |

### → `tool/notebooklm`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `notebooklm` | 1 | `02 Areas/My_DevInfra/Terminal/Terminal Browsing - Lynx Links and NotebookLM CLI.md` |

### → `tool/obsidian`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `obsidian` | 1 | `09 Utilities/AI-Handoff-TaskSystem-Integration.md` |

### → `tool/tasknotes`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `tasknotes` | 1 | `09 Utilities/Hybrid-Task-System-Architecture.md` |

### → `topic/1`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `1` | 3 | `02 Areas/Tailored-Prompt-Book.md.md`, `02 Areas/Confidential/SMW/March Element 2025 Addictions, Consequences, and Formula.md`, `01 Projects/WAS/WAS - Claude LMN QBO Manual Pre-Automation Sync.md` |

### → `topic/11`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `11` | 1 | `01 Projects/GDDP/Phase 4 Complete.md` |

### → `topic/12`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `12` | 1 | `01 Projects/GDDP/Phase 4 Complete.md` |

### → `topic/13`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `13` | 1 | `01 Projects/GDDP/Phase 4 Complete.md` |

### → `topic/2`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `2` | 3 | `02 Areas/My_DevInfra/Automation/Phase_3_Bootstrap.md`, `01 Projects/GDDP/Phase 4 Complete.md`, `01 Projects/WAS/WAS - Claude LMN QBO Manual Pre-Automation Sync.md` |

### → `topic/3`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `3` | 1 | `01 Projects/WAS/WAS - Claude LMN QBO Manual Pre-Automation Sync.md` |

### → `topic/39`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `39` | 1 | `02 Areas/Tailored-Prompt-Book.md.md` |

### → `topic/4`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `4` | 1 | `01 Projects/WAS/WAS - Claude LMN QBO Manual Pre-Automation Sync.md` |

### → `topic/5`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `5` | 1 | `01 Projects/GDDP/Phase 4 Complete.md` |

### → `topic/6`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `6` | 1 | `01 Projects/GDDP/Phase 4 Complete.md` |

### → `topic/adderall`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `adderall` | 1 | `02 Areas/Confidential/Relationships/Ivy was right about the adderall.md` |

### → `topic/ai`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `agent-context` | 1 | `09 Utilities/AI-Handoff-TaskSystem-Integration.md` |
| `AI` | 1 | `09 Utilities/transcripts/IOB - AI coming for your mind, not your life .md` |
| `AI-code` | 1 | `01 Projects/BDR/BDR Project Brief.md` |
| `code-agent` | 1 | `01 Projects/BDR/BDR Project Brief.md` |
| `domain-selection` | 1 | `01 Projects/_Projects Archive/Cultulral Intel/Phase 0 -- NotebookLM Domain & Data Feasibility Research.md` |

### → `topic/anchor`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `anchor` | 2 | `01 Projects/SocialXP/SocialXP Anchor.md`, `01 Projects/BDR/BDR Project Anchor.md` |

### → `topic/apple`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `apple` | 1 | `09 Utilities/transcripts/Apple M1 Macs were revolutionary according to one guy online.md` |

### → `topic/architecture`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `architecture` | 1 | `09 Utilities/Hybrid-Task-System-Architecture.md` |

### → `topic/bdr`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `bdr` | 5 | `01 Projects/BDR/BDR Project Anchor.md`, `01 Projects/BDR/Create an AGENTS.md for BDR.md`, `01 Projects/BDR/Understand how BDR works front to back.md`, `01 Projects/BDR/BDR Q4 Action Plan v1.md`, `01 Projects/BDR/BDR Project Brief.md` |

### → `topic/beiley`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `beiley` | 1 | `02 Areas/Career/Configuring LMN for Beiley in a way that actually serves him.md` |

### → `topic/breakup`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `breakup` | 1 | `02 Areas/Confidential/Relationships/She is no longer emotionally motivated for relationship because I would lust after outcomes while being routinely needy and affected.md` |

### → `topic/browsing`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `browsing` | 1 | `02 Areas/My_DevInfra/Terminal/Terminal Browsing - Lynx Links and NotebookLM CLI.md` |

### → `topic/client-work`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `client-work` | 1 | `01 Projects/Santa Cruz Smart Automations.md` |

### → `topic/codebase-lesson`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `codebase-lesson` | 1 | `_routines/lessons-covered.md` |

### → `topic/content-video`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `content/video` | 1 | `09 Utilities/transcripts/IOB - AI coming for your mind, not your life .md` |

### → `topic/context-engineering`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `context-engineering` | 1 | `01 Projects/BDR/BDR Project Brief.md` |

### → `topic/context-management`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `context-management` | 1 | `01 Projects/BDR/BDR Project Brief.md` |

### → `topic/dashboard`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `dashboard` | 1 | `09 Utilities/Home Hub 2026.md` |

### → `topic/data-strategy`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `data-strategy` | 1 | `01 Projects/_Projects Archive/Cultulral Intel/Phase 0 -- NotebookLM Domain & Data Feasibility Research.md` |

### → `topic/dating`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `dating` | 1 | `02 Areas/Confidential/Relationships/Master Sab Feeld Profile Build Up.md` |

### → `topic/design`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `UI-UX` | 1 | `01 Projects/SocialXP/UX Reusable Automation Workflows.md` |

### → `topic/development`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `development` | 3 | `01 Projects/BDR/BDR Project Anchor.md`, `01 Projects/BDR/BDR Q4 Action Plan v1.md`, `01 Projects/BDR/BDR Project Brief.md` |

### → `topic/docs`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `docs` | 1 | `Templates/docs-reading-template.md` |
| `docs/reading` | 1 | `Templates/docs-reading-template.md` |

### → `topic/dream`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `dream` | 1 | `02 Areas/Confidential/Relationships/Why did that Noa dream be the one so vivid.md` |

### → `topic/dream-journal`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `dream/journal` | 1 | `02 Areas/Confidential/Relationships/Why did that Noa dream be the one so vivid.md` |

### → `topic/dsa`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `interview/sprint` | 3 | `05 Archive/_to-delete-after-30d/End-of-Month Assessment.md`, `_tasks/Select the 3 easy problem to solve.md`, `_tasks/End-of-Month Assessment.md` |
| `interview-prep` | 1 | `01 Projects/BDR/Understand how BDR works front to back.md` |
| `interview/prep` | 1 | `_tasks/Select the 3 easy problem to solve.md` |

### → `topic/elements-calls`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `elements-calls` | 1 | `02 Areas/Confidential/SMW/General MW Element Delivery for Meetings Overview and Notes.md` |

### → `topic/fantasy`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `fantasy` | 1 | `02 Areas/Confidential/Relationships/Master Sab Feeld Profile Build Up.md` |

### → `topic/feeld`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `feeld` | 1 | `02 Areas/Confidential/Relationships/Master Sab Feeld Profile Build Up.md` |

### → `topic/friction`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `friction` | 1 | `_inbox/friction-log.md` |

### → `topic/game`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `game` | 1 | `02 Areas/Confidential/Relationships/Overcommunicating interest to women is Bilzerian’s biggest lesson from thousands of experiences on what not to do.md` |

### → `topic/handoff`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `handoff` | 1 | `09 Utilities/AI-Handoff-TaskSystem-Integration.md` |

### → `topic/high`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `high` | 1 | `01 Projects/BDR/BDR Kanban.md` |

### → `topic/homepage`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `homepage` | 1 | `09 Utilities/Home Hub 2026.md` |

### → `topic/hybrid`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `hybrid` | 1 | `09 Utilities/Hybrid-Task-System-Architecture.md` |

### → `topic/internet-of-bugs`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `internet-of-bugs` | 1 | `09 Utilities/transcripts/IOB - AI coming for your mind, not your life .md` |

### → `topic/jobs-scout`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `jobs-scout` | 1 | `_routines/jobs-seen.md` |

### → `topic/lead-gen`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `lead-gen` | 1 | `01 Projects/Santa Cruz Smart Automations.md` |

### → `topic/ledger`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `ledger` | 2 | `_routines/jobs-seen.md`, `_routines/lessons-covered.md` |

### → `topic/links`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `links` | 1 | `02 Areas/My_DevInfra/Terminal/Terminal Browsing - Lynx Links and NotebookLM CLI.md` |

### → `topic/log`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `workout` | 1 | `Templates/workout-session.md` |

### → `topic/lynx`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `lynx` | 1 | `02 Areas/My_DevInfra/Terminal/Terminal Browsing - Lynx Links and NotebookLM CLI.md` |

### → `topic/medium`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `medium` | 1 | `01 Projects/BDR/BDR Kanban.md` |

### → `topic/mens-weekend`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `mens-weekend` | 1 | `02 Areas/Confidential/SMW/General MW Element Delivery for Meetings Overview and Notes.md` |

### → `topic/mistakes`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `mistakes` | 1 | `02 Areas/Confidential/Relationships/Overcommunicating interest to women is Bilzerian’s biggest lesson from thousands of experiences on what not to do.md` |

### → `topic/next-js`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `next-js` | 1 | `01 Projects/Santa Cruz Smart Automations.md` |

### → `topic/none`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `None` | 1 | `05 Archive/_to-delete-after-30d/Important Ergonomics Tests .md` |

### → `topic/obsidian-tasks`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `obsidian-tasks` | 1 | `09 Utilities/Hybrid-Task-System-Architecture.md` |

### → `topic/office`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `OFFICE` | 1 | `01 Projects/WAS/WAS - Claude LMN QBO Manual Pre-Automation Sync.md` |

### → `topic/para`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `PARA` | 1 | `09 Utilities/AI-Handoff-TaskSystem-Integration.md` |

### → `topic/peace`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `peace` | 1 | `02 Areas/Confidential/Relationships/Say No to Breadcrumbing!.md` |

### → `topic/personal`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `personal` | 18 | `05 Archive/_to-delete-after-30d/MUST USE health and nerve decompression protocols.md`, `02 Areas/My Obsidian Tasks Full Calendar synchronized with Apple apps setup.md`, `02 Areas/Question for Mastering Claude Code Primer for project mgmt automation.md`, `02 Areas/Metacognition and higher order thinking.md`, `02 Areas/My assets as a developer are my humanity and problem-solving logic.md` |

### → `topic/phase-0`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `phase-0` | 1 | `01 Projects/_Projects Archive/Cultulral Intel/Phase 0 -- NotebookLM Domain & Data Feasibility Research.md` |

### → `topic/pickup`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `pickup` | 1 | `02 Areas/Confidential/Relationships/Overcommunicating interest to women is Bilzerian’s biggest lesson from thousands of experiences on what not to do.md` |

### → `topic/private`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `private` | 1 | `02 Areas/Confidential/Relationships/Body Count.md` |

### → `topic/projects`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `projects` | 1 | `01 Projects/BDR/Understand how BDR works front to back.md` |

### → `topic/research`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `research` | 1 | `03 Resources/andre Karpathy prompt for obsidian AI second brain.md` |

### → `topic/routine`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `routine` | 2 | `_routines/jobs-seen.md`, `_routines/lessons-covered.md` |

### → `topic/shop`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `SHOP` | 1 | `01 Projects/WAS/WAS - Claude LMN QBO Manual Pre-Automation Sync.md` |

### → `topic/social`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `social` | 3 | `01 Projects/SocialXP/Vincent Social Interactivity App Meeting 1.md`, `01 Projects/SocialXP/Vincent Social Interactivity Meeting 2.md`, `01 Projects/SocialXP/Vincent Social Interactivity Meeting 3.md` |

### → `topic/social-wellness`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `social-wellness` | 1 | `02 Areas/Confidential/Relationships/Approaching Women.md` |

### → `topic/socialxp`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `socialXP` | 9 | `02 Areas/Career/Email Rules to Live By.md`, `01 Projects/SocialXP/UX Reusable Automation Workflows.md`, `01 Projects/SocialXP/Wireframes Day 1.md`, `01 Projects/SocialXP/Co-Design Group 1.md`, `01 Projects/SocialXP/Co-Design-Group-2.md` |

### → `topic/sprint`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `sprint` | 1 | `_inbox/friction-log.md` |

### → `topic/sweep`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `sweep` | 1 | `09 Utilities/Sweep.md` |

### → `topic/task-system`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `task-system` | 2 | `09 Utilities/Hybrid-Task-System-Architecture.md`, `09 Utilities/AI-Handoff-TaskSystem-Integration.md` |

### → `topic/taskforge`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `taskforge` | 1 | `09 Utilities/Hybrid-Task-System-Architecture.md` |

### → `topic/terminal`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `terminal` | 1 | `02 Areas/My_DevInfra/Terminal/Terminal Browsing - Lynx Links and NotebookLM CLI.md` |

### → `topic/testability`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `testability` | 1 | `09 Utilities/transcripts/Can we test it? Yes we can!.md` |

### → `topic/testing`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `testing` | 1 | `09 Utilities/transcripts/Can we test it? Yes we can!.md` |

### → `topic/to-process`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `to-process` | 1 | `02 Areas/Confidential/Relationships/Approaching Women.md` |

### → `topic/transcript`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `transcript` | 4 | `09 Utilities/transcripts/Transcript for The One Habit of Productivity Huberman Video.md`, `09 Utilities/transcripts/Untitled.md`, `09 Utilities/transcripts/Can we test it? Yes we can!.md`, `Templates/transcripts-template.md` |

### → `topic/was`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `was` | 1 | `02 Areas/Career/Configuring LMN for Beiley in a way that actually serves him.md` |

### → `topic/wellness`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `wellness` | 1 | `02 Areas/Confidential/Relationships/Say No to Breadcrumbing!.md` |

### → `topic/wildmen`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `wildmen` | 2 | `02 Areas/Confidential/SMW/General MW Element Delivery for Meetings Overview and Notes.md`, `02 Areas/Confidential/SMW/Love Phone Call Beginning of March.md` |

### → `topic/workflow`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `workflow` | 2 | `09 Utilities/Sweep.md`, `02 Areas/My_DevInfra/Terminal/Terminal Browsing - Lynx Links and NotebookLM CLI.md` |

### → `topic/workplace`

| Tag | Files | Sample (up to 5) |
| --- | ----- | ---------------- |
| `workplace` | 2 | `05 Archive/_to-delete-after-30d/Ideal Typing Position Form.md`, `05 Archive/_to-delete-after-30d/Workplace Recovery Steps.md` |

## Existing Prefixed Tags (V4-clean — informational)

| Tag | Files |
| --- | ----- |
| `topic/workflow` | 175 |
| `topic/ai` | 132 |
| `topic/log` | 115 |
| `scope/health` | 96 |
| `scope/learning` | 95 |
| `tool/neovim` | 69 |
| `scope/career` | 66 |
| `tool/terminal` | 64 |
| `scope/ops` | 63 |
| `scope/communication` | 62 |
| `topic/GDD` | 59 |
| `scope/ergonomics` | 54 |
| `tool/git` | 53 |
| `tool/obsidian` | 46 |
| `topic/ops` | 36 |
| `scope/writing` | 35 |
| `scope/mindset` | 30 |
| `topic/cim` | 25 |
| `tool/openclaw` | 23 |
| `topic/web-dev` | 22 |
| `topic/reference` | 22 |
| `scope/finance` | 19 |
| `topic/programming` | 19 |
| `lang/py` | 16 |
| `tool/tmux` | 13 |
| `lang/js` | 13 |
| `topic/problemsolving` | 11 |
| `scope/fitness` | 8 |
| `topic/agents` | 7 |
| `topic/terminal` | 6 |
| `tool/claude-code` | 5 |
| `tool/zed` | 4 |
| `tool/jules` | 4 |
| `tool/keyboard` | 4 |
| `topic/algorithms` | 4 |
| `topic/openclaw` | 4 |
| `tool/zsh` | 4 |
| `tool/macos` | 4 |
| `tool/schema` | 3 |
| `tool/dygma` | 3 |
| `scope/sleep` | 3 |
| `tool/gemini` | 3 |
| `tool/pi` | 3 |
| `tool/ghostty` | 3 |
| `topic/dsa` | 3 |
| `topic/` | 3 |
| `topic/commands` | 3 |
| `scope/obsidian` | 2 |
| `topic/normalization` | 2 |
| `scope/vault` | 2 |
| `tool/vscode` | 2 |
| `tool/GoogleAI` | 2 |
| `tool/roadmap` | 2 |
| `topic/keymaps` | 2 |
| `topic/interview` | 2 |
| `topic/ai-coding` | 2 |
| `topic/AI` | 2 |
| `topic/cli` | 2 |
| `topic/config` | 2 |
| `scope/infrastructure` | 2 |
| `tool/` | 2 |
| `scope/IDE` | 2 |
| `topic/lazyvim` | 2 |
| `tool/GDDP` | 2 |
| `tool/commands` | 2 |
| `tool/google` | 2 |
| `topic/mindfulness` | 2 |
| `tool/geminiCLI` | 2 |
| `tool/notebooklm` | 1 |
| `topic/obsidian` | 1 |
| `topic/quickadd` | 1 |
| `topic/automation` | 1 |
| `topic/knowledge-management` | 1 |
| `topic/compilation` | 1 |
| `topic/build` | 1 |
| `tool/makefile` | 1 |
| `topic/learning` | 1 |
| `scope/productivity` | 1 |
| `topic/time` | 1 |
| `tool/timers` | 1 |
| `tool/watch` | 1 |
| `scope/solo` | 1 |
| `scope/meta` | 1 |
| `topic/context` | 1 |
| `tool/RAG` | 1 |
| `lang/python` | 1 |
| `tool/notebookLM` | 1 |
| `topic/consulting` | 1 |
| `tool/trae` | 1 |
| `tool/gcp` | 1 |
| `scope/keyboard` | 1 |
| `topic/skill-tree` | 1 |
| `topic/systems-design` | 1 |
| `topic/systems` | 1 |
| `tool/vim` | 1 |
| `tool/IDE` | 1 |
| `tool/CLI` | 1 |
| `scope/agents` | 1 |
| `scope/memory` | 1 |
| `scope/CLI` | 1 |
| `tool/AIzaSyDvfxytmyisi3JzmWNrwyBVHRdvw2iS6uo` | 1 |
| `scope/shell` | 1 |
| `scope/AI` | 1 |
| `topic/hallucination` | 1 |
| `tool/agents/frontier` | 1 |
| `tool/ipad` | 1 |
| `tool/blink` | 1 |
| `topic/keybindings` | 1 |
| `topic/hotkeys` | 1 |
| `topic/harness` | 1 |
| `topic/memory` | 1 |
| `tool/hooks` | 1 |
| `tool/skills` | 1 |
| `topic/portfolio` | 1 |
| `tool/lovable` | 1 |
| `topic/react` | 1 |
| `topic/vite` | 1 |
| `topic/frontend` | 1 |
| `tool/cat` | 1 |
| `tool/grep` | 1 |
| `tool/pipe-operator` | 1 |
| `tool/docker` | 1 |
| `tool/iterm2` | 1 |
| `tool/hotkeys` | 1 |
| `tool/antigravity` | 1 |
| `tool/howto` | 1 |
| `topic/USvsChina` | 1 |
| `topic/politics` | 1 |
| `tool/cline` | 1 |
| `tool/raycast` | 1 |
| `scope/2026` | 1 |
| `topic/quickadd/bug` | 1 |
| `topic/templates/bug` | 1 |
| `topic/security` | 1 |
| `topic/scripting` | 1 |
| `topic/10x-dev` | 1 |
| `topic/skills` | 1 |
| `topic/tiktok` | 1 |
| `topic/marketing` | 1 |
| `topic/setup` | 1 |
| `topic/IDE` | 1 |
| `topic/shortcuts` | 1 |
