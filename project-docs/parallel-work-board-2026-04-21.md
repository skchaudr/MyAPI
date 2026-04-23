# Parallel Work Board — 2026-04-21

Primary live lane: V4 CLI owner pass for My_DevInfra medium/review notes.

This board tracks useful sidecar work that can happen while the interactive CLI is waiting on human input.

## Lane 1 — CLI Triage Owner Pass

Status: active / primary

Current target:

- `02 Areas/My_DevInfra`
- 26 medium/review notes from `project-docs/pilot-devinfra.json`

Run on Mac:

```bash
/Users/saboor/repos/MyAPI/project-docs/run-devinfra-owner-pass.sh
```

Goal:

- resolve type conflicts
- clear stale status on non-project/event notes
- assign concepts
- clean tags
- add project links where useful

After pass:

Run on Mac:

```bash
python3 scripts/normalize_vault_schema_v4.py --subdir "02 Areas/My_DevInfra" --report project-docs/devinfra-owner-pass-after-trial.md --json project-docs/devinfra-owner-pass-after-trial.json
```

## Lane 2 — BigPi / Harness Work

Status: good sidecar candidate

Signals found:

- `Job Class Matrix (Mac + Big Pi + Small Pi)`
- `Mission - BigPi SmallPi Stabilization`
- OpenClaw harness references
- distributed ops runbooks in My_DevInfra/OpenClaw backups
- retrieval tests already mention `openclaw harness leak`

Useful next artifacts:

- BigPi harness health checklist
- BigPi job-class routing note
- one canonical `BigPi Harness Anchor`
- one benchmark query for BigPi/OpenClaw harness retrieval

Suggested sidecar output:

- `project-docs/source-of-truth-anchors/bigpi-harness-anchor.md`

## Lane 3 — Neovim Workflow Training

Status: already normalized structurally

Signals found:

- 24 NeoVim notes normalized successfully
- multiple indexed notes on LazyVim, macros, terminal workflow, Obsidian integration, and Neovim drills
- active Antigravity lane is already focused here

Useful next artifacts:

- Neovim training map
- daily drill sequence
- "survive a full day in Neovim" checklist
- link Antigravity training outputs back into V4 concepts

Suggested sidecar output:

- `project-docs/neovim-training-map.md`

## Lane 4 — Zapier / SMB Ops Hub

Status: planning sidecar candidate

Signals found:

- indexed notes mention Zapier integrations
- `obsidian-smb-ops-hub-anchor.md` exists in the Khoj-ready bundle
- Water & Stone / SMB ops material appears in project context

Useful next artifacts:

- SMB Ops Hub anchor
- Zapier integration inventory
- "manual process -> automation candidate" table
- first two integration specs only, not a giant automation sweep

Suggested sidecar output:

- `project-docs/source-of-truth-anchors/smb-ops-hub-anchor.md`
- `project-docs/zapier-integration-inventory.md`

## Priority Rule

If the user is actively in the CLI:

1. Keep CLI triage primary.
2. Use sidecar time for read-only mapping, anchors, and planning docs.
3. Avoid changing Obsidian files outside the active owner-pass lane.
4. Avoid touching another agent's active tmux/session work unless explicitly handed off.

## Best Next Sidecar Pick

BigPi harness anchor is the safest sidecar:

- it supports the active My_DevInfra area
- it helps retrieval
- it does not conflict with Neovim training
- it turns scattered OpenClaw/BigPi notes into one source-of-truth target
