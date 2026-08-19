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
