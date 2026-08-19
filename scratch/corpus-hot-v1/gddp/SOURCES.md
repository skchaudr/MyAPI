# gddp / SOURCES — merged v1

Date: 2026-07-29
Mini = repo/prod bias. Air = vault/operator bias. Both kept as evidence.

---

## From mini

# GDDP — SOURCES (mini pass-1)

Host: sab-mini · harvest: 2026-07-29 · read-only

## Ownership split

| Repo | Owns | Does not |
|------|------|----------|
| `gddp-config` | Human graph truth: schemas, graphs/, templates, rules/workflows (future), validator/TUI scripts | Runtime jobs, SQLite state, silent graph writeback |
| `gddp-runtime` | Operating loop: dispatch, evidence, evaluators, adapters, SQLite, heartbeats | Canonical node YAML / project graph edits |

## Paths

| # | Path | Type | Freshness |
|---|------|------|-----------|
| 1 | `/Users/sab-mini/repos/gddp-runtime/PROJECT-BRIEF.md` | system narrative / canon model | 2026-07-18 |
| 2 | `/Users/sab-mini/repos/gddp-runtime/README.md` | runtime control-plane overview | live |
| 3 | `/Users/sab-mini/repos/gddp-runtime/AGENTS.md` | agent contract | live |
| 4 | `/Users/sab-mini/repos/gddp-runtime/TOPOLOGY.md` | topology | present |
| 5 | `/Users/sab-mini/repos/gddp-runtime/.handoffs/` | durable handoffs (e.g. 060 multi-project heartbeat 2026-07-29) | tip Jul 29 |
| 6 | `/Users/sab-mini/repos/gddp-config/README.md` | config repo map | live |
| 7 | `/Users/sab-mini/repos/gddp-config/AGENTS.md` | graph-truth rules; job vs node split | live |
| 8 | `/Users/sab-mini/repos/gddp-config/schemas/v1/` | Event/Node/Job/Result/… schemas | present |
| 9 | `/Users/sab-mini/repos/gddp-config/graphs/` | project graphs (per-project folders) | live |
| 10 | `/Users/sab-mini/repos/gddp-config/.handoffs/` | e.g. 033 TUI nav, 034 dispatch graph target (2026-07-29) | tip Jul 29 |
| 11 | `/Users/sab-mini/repos/gddp-config/scripts/` | validate.py, new_node.py, terminal TUI | live |
| 12 | graphify-out **label vocab only** | runtime: GRAPH_REPORT 2026-07-29 (2696 nodes…); config: graph.html/json | daily dated folders |

## Git tips (mini)

- runtime: `main` @ `5beb302` merge feat/rig1-scheduler
- config: `main` @ `58c6e8b` merge fix/gddp-tui-navigation · untracked `.pi-subagents/`

## Handoffs (1–2 named samples)

- Runtime: `060-multi-project-heartbeat-dispatch-hardening.md` (2026-07-29)
- Config: `033-gddp-tui-navigation.md`, `034-dispatch-graph-target-fix.md` (2026-07-29)

## Env names only

Job/runtime env and adapter tokens — names only if needed later; no values in corpus-hot.


---

## From air

# GDDP — SOURCES (air)

Host: `sab-air.local` · Harvest: 2026-07-29

Both clones present and on `main` tracking origin.

| # | Path | Type | Freshness |
|---|------|------|-----------|
| 1 | `air: ~/repos/gddp-runtime/PROJECT-BRIEF.md` | canon: purpose + runtime vs config ownership | 2026-07-19 |
| 2 | `air: ~/repos/gddp-runtime/TOPOLOGY.md` | production topology (sab-mini control plane) | verified note 2026-07-12 |
| 3 | `air: ~/repos/gddp-runtime/README.md`, `AGENTS.md`, `docs/current-mission-definition-of-done.md` | runtime ops docs | mid–late Jul 2026 |
| 4 | `air: ~/repos/gddp-runtime/.handoffs/059-scripted-pi-fleet-bridge.md` (+ 058, 057, …) | runtime handoffs | 2026-07-28 tip |
| 5 | `air: ~/repos/gddp-config/README.md` | config owns graphs/schemas/templates | 2026-07-09 |
| 6 | `air: ~/repos/gddp-config/.handoffs/034-dispatch-graph-target-fix.md`, `033-gddp-tui-navigation.md`, `025-config-owned-gddp-cli.md` | config handoffs | tip 2026-07-29 |
| 7 | `air: ~/repos/gddp-config/schemas/v1/`, `graphs/`, `templates/`, `scripts/` | config source-of-truth layout | live main `58c6e8b` |
| 8 | `air: ~/repos/gddp-runtime/graphify-out/{graph.json,manifest.json}` · `air: ~/repos/gddp-config/graphify-out/` | **label vocab only** (code graph; ~1723 / ~724 nodes) | present; not narrative canon |
| 9 | `air: ~/.claude/projects/-Users-sab-mini-repos-gddp-runtime/` · `…-gddp-config/` | Claude projects on air | active listings Jul 2026 |
| 10 | `air: ~/.codex/memories/rollout_summaries/*gddp*` (e.g. 2026-06-19, 06-29, 06-30, 07-22, 07-25) | Codex session summaries | Jun–Jul 2026 |
| 11 | `air: ~/Obsidian/SSD/03 Resources/Flashcards/GDDP_Protocol.md`, `GDDP Readiness Drills.md` | operator drills | vault |
| 12 | `air: ~/Obsidian/SSD/02 Areas/Two Track Plan to Finishing GDD and MyAPI.md` | portfolio link | 2026-05-01 |

**Env names only (from TOPOLOGY, no values):** queue/webhook host config references; secrets via password-store / GPG on **mini** production — air may not hold live production secrets. Names only if encountered: webhook shared secret env, `GDDP_RUNTIME_ROOT`.

**Also present:** `~/repos/gddp-config-stage1/` (stage1 sibling; not primary this pass).

