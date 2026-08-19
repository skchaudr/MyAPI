# pi-needle-gemma / BRIEF-DRAFT — merged v1

Date: 2026-07-29
Mini = repo/prod bias. Air = vault/operator bias. Both kept as evidence.

---

## From mini

# Pi / Needle / Gemma — BRIEF-DRAFT (mini pass-1)

## Short Answer

**Pi** is a personal coding agent + packet harness (verify peer claims; interactive/non-interactive). **Needle** is the on-device tool router (5 verbs; local vs `delegate`) living at `~/.pi/needle`, with training package at `~/repos/mac-needle`. Prefer Mac neural routing; VM is fallback/health. **Gemma** appears as multirole/train CLI and scripts under needle + datasets paths — config and ledgers only for this harvest; checkpoints stay path-only. Mini has the full tree; full `~/.pi` ingest is unsafe (sessions, secrets, weights, worktrees).

## Evidence paths (exist on mini)

1. `/Users/sab-mini/.pi/PROJECT-BRIEF.md`
2. `/Users/sab-mini/.pi/needle/README.md`
3. `/Users/sab-mini/.pi/needle/tools.json`
4. `/Users/sab-mini/.pi/harness/` (dir)
5. `/Users/sab-mini/.pi/agent/models.json` (settings; secrets not copied)
6. `/Users/sab-mini/.pi/docs/needle_gemma_pi_harness_implementation_plan.md`
7. `/Users/sab-mini/repos/mac-needle/` (dir; checkpoints path only)

## Operator one-liner

Pi runs work; Needle cheap-routes tools; Gemma is local-model tooling — never dump all of `~/.pi` into a corpus.


---

## From air

# Pi / Needle / Gemma — BRIEF-DRAFT (air)

## Short Answer
On air, **`~/.pi` is a full working tree**: Pi agent + **Needle** (router/serve/shadow/training tooling) + **needle-gemma-v1** local bundle (schemas, receipts, evals) aimed at a leak-free Camber Part 1 upload — **not** automatic train/launch. Gemma surfaces as **config/CLI/schemas + ollama functiongemma path**, not as a weight dump for corpus. Operator notes in Obsidian (execution plan, postmortem) and Codex/Claude projects reinforce design; **full `~/.pi` ingest is an anti-goal**.

## Why
Needle routes/assembles agent work; Gemma path is a bounded local bundle + model settings for controlled training/serve experiments; Pi harness ties multi-machine sessions.

## Relationships
- Ledger gates: local build (worker) → stash upload (Sab) → Camber compute (Sab per-run).
- Multi-host routing inventory stages reports for sab-air / pi-big / pi-small / old-air.
- MyAPI golden brief for pi_needle is on MyAPI `main`, not inside `~/.pi`.

## Evidence (exist on air)
1. `air: ~/.pi/needle/README.md`
2. `air: ~/.pi/needle/docs/needle-gemma-v1-execution-ledger.md`
3. `air: ~/.pi/needle/needle-gemma-v1/manifest.json`
4. `air: ~/.pi/docs/needle_gemma_pi_harness_implementation_plan.md`
5. `air: ~/Obsidian/SSD/00 Inbox/Needle Gemma Execution Plan.md`

## Risks
- Ingesting `auth.json`, training jsonl, quarantine backups, or ollama blobs into MyAPI/Khoj.
- Treating Camber approval as granted because local bundle validates.
- Confusing air-present pi tree with “mini-only” production for other services.

## Next
- Pass-2 brief: three-layer map (agent / needle / harness) + explicit deny-list for ingest.
- Diff mini vs air only if mini paths available later; this pass lists air inventory as primary.

