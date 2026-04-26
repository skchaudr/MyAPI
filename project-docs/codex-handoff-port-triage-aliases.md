---
type: utility
title: Codex Handoff — Port Vault Triage Aliases to MyAPI CLI
area: "[[My_DevInfra]]"
source: original
created: 2026-04-26
---

# Codex Handoff — Port Vault Triage Aliases to MyAPI CLI

## Why this exists

After the V4 migration (see `~/Repos/MyAPI/project-docs/v4-batch-*-manifest.json` + `v4-owner-pass-queue.md`), Saboor's two terminal aliases — `triage` and `triage pick` — still invoke pre-V4 in-vault Python scripts. Those scripts only know the V3 schema (4-folder routing, no `area`/`source`/`concepts` awareness). Meanwhile MyAPI has a much more capable owner-pass tool that already knows V4. Time to wire the aliases to the better tool.

## Current state — pre-V4 in-vault scripts

Location: `~/Obsidian/SoloDeveloper/09 Utilities/Scripts/`

| Script | Purpose | V4 status |
| ------ | ------- | --------- |
| `triage_inbox.py` | Interactive 4-folder routing (1=Projects, 2=Areas, 3=Resources, 4=Archive, s=Skip). Two-phase UI: routing → sub-folder selection. Uses `rich` for table preview. | **Pre-V4.** Only moves files; doesn't write any frontmatter. No type/area/source/concepts awareness. |
| `inbox_sweep.py` | Reads each inbox file's `move_to:` frontmatter field, moves the file there. Bulk operation. | **Pre-V4.** Knows only the four old destinations. `move_to:` is itself a deprecated convention. |
| `sweep.py` | Generates a morning sweep note from yesterday's daily + tasks + inbox. **Not a triage tool — different purpose.** | Out of scope for this port. Leave alone. |

## Target state — MyAPI CLI as the triage backend

Location: `~/Repos/MyAPI/context_refinery/triage/`

Entry: `python3 -m context_refinery.triage [files...] [--queue-json <path>] [--vault-root <path>] [--confidence medium,review]`

Capabilities you'd be unlocking for the alias:
- 8 passes: `V4SchemaPass` (full owner-pass: type → project/status → area → concepts → tags → related), plus single-pass variants for `TypePass`, `StatusPass`, `ConceptsPass`, `TagsPass`, `LinksPass`, `ProjectPass`.
- Reads suggestions from the bulk normalizer's `--json` output (the `v4-batch-NN-*-dryrun.json` files in `project-docs/`). Pre-fills V4-known fields, asks the human only for judgment-heavy ones (concepts, tags, related).
- Writes frontmatter directly via `triage/writers.py:write_frontmatter`. Field order matches V4 schema. Body is preserved exactly.
- Concept suggester pulls from existing vault concept stubs in `03 Resources/Concepts/` (21 seeded on 2026-04-26) plus a hardcoded `CONCEPT_PRESETS` list at `triage/passes/v4schema.py:38`.
- Stateless — no progress ledger inside the tool. The file's own `migration_status` is the truth.

## Goal

`triage` and `triage pick` should invoke the MyAPI CLI in two ergonomic flavors, fast enough for Saboor to clear a note in 10–20 seconds when in flow.

## What you'll have to figure out

These are decisions the brief intentionally leaves open so you can pick the cleanest path:

1. **Where do the aliases currently live?** Codex: search `~/.zshrc`, `~/.zshenv`, `~/.zprofile`, `~/.config/zsh/`, `~/AGENTS.md`, plus any `~/Repos/dev_infra/` or `~/Repos/My_DevInfra/` shell config. The earlier grep here turned up nothing in the obvious files — likely in a sourced fragment.
2. **Install path for the MyAPI CLI** — three options:
   - **(a)** `pip install -e ~/Repos/MyAPI` so `python3 -m context_refinery.triage` works from any cwd.
   - **(b)** Wrapper script at `~/bin/triage` that activates a venv + cds + invokes.
   - **(c)** Direct alias `alias triage='cd ~/Repos/MyAPI && python3 -m context_refinery.triage'` (cwd-changing, ugly but simple).
   Pick the one that matches Saboor's existing patterns (he uses `nvm`, `pip`, `brew`; resource-conscious 8GB Mac).
3. **What does `triage pick` mean semantically?** Three plausible reads:
   - Pick a single file from a fuzzy list, run owner-pass on just that one.
   - Pick a sub-folder, run owner-pass on all files in it.
   - Pick from the medium/review-confidence files in the most recent dryrun JSON.
   Confirm with Saboor or pick the one most useful given Phase 4 just produced a stack of `v4-batch-NN-*-dryrun.json` files he could pick a batch from.
4. **Fate of the old in-vault scripts:**
   - `triage_inbox.py` — retire or keep as a fast V3-style folder-only mover for files that *only* need a move?
   - `inbox_sweep.py` — same question; `move_to:` is genuinely dead, so this can probably go.
   - `sweep.py` — keep, unrelated.

## Constraints

- **Don't break the V4 frontmatter writer contract.** The MyAPI writer (`triage/writers.py:write_frontmatter`) already enforces field order and preserves body. Don't add a parallel write path.
- **No new schema fields.** V4 is the closed set: `type / status / area / project / concepts / tags / source / title / aliases / created / modified / folder_origin / migration_status`.
- **Preserve `rich` UI quality.** The current `triage_inbox.py` has a polished color-coded table. The MyAPI runner already uses `rich.console`; just make sure it's not regressed by the alias plumbing.
- **Speed.** Saboor's target is 10–20 sec per note in flow. Don't add a startup tax (e.g., spinning up a venv every invocation). If using a venv, source-once-and-stay-warm patterns are fair game.
- **Resource-conscious.** 8GB M1 Mac. No daemons. No watchers.
- **Don't auto-commit.** The triage tool writes to vault files; user commits when *they* decide. Phase 4 batches already showed the pattern: pre-tag, apply, post-tag, then let the user inspect before pushing.

## Files Codex should read first

1. `~/Obsidian/SoloDeveloper/09 Utilities/Scripts/triage_inbox.py` (full file — current UX you're matching/replacing)
2. `~/Obsidian/SoloDeveloper/09 Utilities/Scripts/inbox_sweep.py` (move_to-frontmatter pattern for context)
3. `~/Repos/MyAPI/context_refinery/triage/__main__.py` and `runner.py` (entry point + CLI surface)
4. `~/Repos/MyAPI/context_refinery/triage/passes/v4schema.py` (the V4 owner-pass — what `triage` should invoke)
5. `~/Repos/MyAPI/context_refinery/triage/writers.py` (the frontmatter writer)
6. `~/Repos/MyAPI/scripts/normalize_vault_schema_v4.py` (just for context on the bulk-pass that produces the queue JSONs)
7. `~/Repos/MyAPI/project-docs/v4-owner-pass-queue.md` (the actual worklist the aliases will be addressing)

## Acceptance criteria

The port is done when:

1. `triage` from any cwd kicks Saboor into MyAPI's V4 owner-pass against the inbox (or whatever default scope makes sense given decision #3).
2. `triage pick` provides the chosen narrowing flavor from decision #3.
3. The old in-vault `triage_inbox.py` and `inbox_sweep.py` are either deleted or relocated/renamed so they can't be invoked accidentally.
4. A short `~/Obsidian/SoloDeveloper/09 Utilities/_Vault System/triage-aliases.md` doc explains the new aliases for future-Saboor.
5. Saboor can clear a 10-file owner-pass batch in ~3 minutes total without any "wait, what command was that again?" friction.

## Out of scope

- Don't touch `sweep.py` (different purpose).
- Don't redesign the MyAPI passes themselves — they're V4-correct.
- Don't add new normalizer fields; that's a Phase 6 conversation if it ever happens.
- Don't migrate the vault again — Phase 4 is done, 99.5% v4-applied. Leave the floor work alone.

## Reporting back

When you're done, drop a summary at `~/Repos/MyAPI/project-docs/codex-handoff-port-triage-aliases-results.md`:
- Which decisions you made on items 1–4.
- Final alias definitions (paste them).
- Whether the old in-vault scripts were deleted, archived, or renamed.
- Any quirks or follow-ups for Saboor.
