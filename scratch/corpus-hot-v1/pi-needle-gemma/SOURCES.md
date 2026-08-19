# pi-needle-gemma / SOURCES — merged v1

Date: 2026-07-29
Mini = repo/prod bias. Air = vault/operator bias. Both kept as evidence.

---

## From mini

# Pi / Needle / Gemma — SOURCES (mini pass-1)

Host: sab-mini · harvest: 2026-07-29 · **scoped inventory only** (do not swallow all of `~/.pi`)

## Core paths

| # | Path | Type | Freshness |
|---|------|------|-----------|
| 1 | `/Users/sab-mini/.pi/PROJECT-BRIEF.md` | Pi portfolio brief | 2026-06-24 |
| 2 | `/Users/sab-mini/.pi/README.md` | repo readme | 2026-07-11 |
| 3 | `/Users/sab-mini/.pi/AGENTS.md` | agent contract | 2026-07-29 |
| 4 | `/Users/sab-mini/.pi/needle/README.md` | Needle integration map | 2026-07-22 |
| 5 | `/Users/sab-mini/.pi/needle/router.py` · `serve.py` · `tools.json` · `pi-route` | route daemon surface | present |
| 6 | `/Users/sab-mini/.pi/needle/gemma-cli.py` + `scripts/build_*gemma*` · `docs/needle-gemma-v1-execution-ledger.md` | Gemma train/cli paths (no weights) | present |
| 7 | `/Users/sab-mini/.pi/harness/` | packet runner, config examples, pi-hub-rs | present |
| 8 | `/Users/sab-mini/.pi/agent/models.json` | provider/model **settings** (keys redacted in harvest) | present |
| 9 | `/Users/sab-mini/.pi/agent/sessions/` | session dirs (names only sampled) | live |
| 10 | `/Users/sab-mini/.pi/.handoffs/` | e.g. needle routing, gemma camber bundle 032 | present |
| 11 | `/Users/sab-mini/.pi/docs/needle_gemma_pi_harness_implementation_plan.md` | joint plan | present |
| 12 | `/Users/sab-mini/repos/mac-needle/` | Cactus Needle training package clone; `checkpoints/` (path only) | mini training home |

## Needle layout notes (from README)

- Integration: `~/.pi/needle` · training package: `~/repos/mac-needle`
- 5 verbs in `tools.json`: edit_file, run_shell, search_code, read_file, delegate
- Prefer **Mac** neural routing; VM daemon fallback; observe-only until eval gate
- launchd: `com.needle.serve.plist`

## Gemma — path + config, not weights

- CLI/scripts under `~/.pi/needle/` and `scripts/needle_gemma_v1`
- Checkpoints dir exists at `~/repos/mac-needle/checkpoints` — **do not ingest weights**
- HF-related datasets under `~/.pi/agent/data/hf-datasets/functiongemma-*` (path labels only)
- `agent/models.json` lists frontier providers (deepseek, zai/glm, …) — **apiKey names redacted**; Gemma local not dumped as binary

## Env names only (no values)

`NEEDLE_URL` · harness vars from `harness/config.sh.example` · provider `apiKey` fields in models.json · Vertex/ADC names if referenced in Needle README (values never stored here)

## mini-only vs missing

| Present on mini | Missing / air may differ |
|-----------------|---------------------------|
| Full `~/.pi` tree, needle, harness, agent sessions, mac-needle clone | Air clone lag of `.pi` / needle; air Vertex operator path stronger historically |
| models.json local providers | Air-only session transcripts about Pi |
| launchd plist path for needle serve | Whether air runs same launchd job |

## Ingest risks (do not full-ingest `~/.pi`)

- `agent/sessions/` volume + PII/operator paths
- `private/`, `auth.json`, models-store secrets
- `checkpoints/` / weights / training blobs
- `archive/incident_reports/` host leaks (brief already warns)
- Nested `.worktrees/` duplicates
- Entire graphify-out rebuild of `.pi` (out of scope)


---

## From air

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

