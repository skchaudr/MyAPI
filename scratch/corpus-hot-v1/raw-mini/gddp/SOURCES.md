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
