# Pi / Needle / Gemma — SOURCES (air)

Host: `sab-air.local` · Harvest: 2026-07-29  
**Scoped inventory only** — do not full-ingest `~/.pi`.

| # | Path | Type | Freshness |
|---|------|------|-----------|
| 1 | `air: ~/.pi/PROJECT-BRIEF.md`, `AGENTS.md`, `README.md` | pi root canon | PROJECT-BRIEF ~2026-06-24 |
| 2 | `air: ~/.pi/needle/README.md`, `router.py`, `serve.py`, `tools.json` | Needle router/serve surface | README 2026-07-18 |
| 3 | `air: ~/.pi/needle/needle-gemma-v1/` (`manifest.json`, `schemas/`, `configs/`, `evals/`) | local Needle-Gemma v1 bundle | 2026-07-26 |
| 4 | `air: ~/.pi/needle/docs/needle-gemma-v1-execution-ledger.md` | Camber Part 1 ledger (gates) | 2026-07-26 |
| 5 | `air: ~/.pi/docs/needle_gemma_pi_harness_implementation_plan.md` | harness implementation plan | 2026-07-10 |
| 6 | `air: ~/.pi/harness/` (`NEEDLE-HANDOFF.md`, `HARNESS-CHOICE-CONTRACT.md`, `machines.json`, `packets/`, `pi-hub-rs/`) | harness / session / hub | present Jul 2026 |
| 7 | `air: ~/.pi/agent/models.json`, `models-store.json`, `auto-mode.json` | **model settings paths** (not weights) | models.json 2026-07-25 |
| 8 | `air: ~/.pi/needle/models/{july-v5,june-baseline}/` · `air: ~/.ollama/models/functiongemma/` | model **dirs/tags** (no weight dump) | functiongemma dir present |
| 9 | `air: ~/.pi/needle/gemma-cli.py`, `scripts/build_needle_gemma_v1.py`, `scripts/needle_gemma_v1/` | build/CLI tooling | Jul 2026 |
| 10 | `air: ~/.pi/.handoffs/` (incl. needle-gemma camber notes) | pi handoffs | many; tree active |
| 11 | `air: ~/.pi/gddp/`, `graphify-out/` | pi-local GDDP + graphify | present |
| 12 | `air: ~/Obsidian/SSD/00 Inbox/Needle Gemma Execution Plan.md` · `Needle Gemma Pi Postmortem.md` | operator vault | plan 2026-07-16; postmortem 2026-07-15 |
| 13 | `air: ~/.claude/projects/-Users-sab-mini--pi/` · `…--pi-needle/` | Claude projects | listed |
| 14 | `air: ~/.codex/memories/rollout_summaries/2026-07-10T08-16-29-bvLm-needle_gemma_harness_design_and_routing_inventory.md` | Codex design session | 2026-07-10 |
| 15 | `air: ~/repos/needle/`, `~/repos/mac-needle/` | related repos (siblings; not deep-read) | exist |

**Env / secret names only:** `auth.json` exists under `~/.pi/agent/` — do not copy values; use `auth.json.example` pattern. `auto-mode.json` keys include `classifierModel`, `allowlistedTools`, `denyRules` (names only).

**Ingest risk callout:** `~/.pi` contains agent data, auth, training jsonl, quarantine backups, shadow/, graphify-out, hf-datasets — **full ingest is wrong**. Prefer handoffs, PROJECT-BRIEF, needle README, ledger, vault notes, schemas/manifests.
