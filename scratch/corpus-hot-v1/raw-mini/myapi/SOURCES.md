# MyAPI — SOURCES (mini pass-1)

Host: sab-mini · harvest: 2026-07-29 · read-only

| # | Path | Type | Freshness (mtime-ish) |
|---|------|------|------------------------|
| 1 | `/Users/sab-mini/repos/MyAPI/PROJECT-BRIEF.md` | portfolio brief / direction | 2026-07-11 |
| 2 | `/Users/sab-mini/repos/MyAPI/IMPLEMENTATION-PLAN.md` | phase scaffold L0–L4 | 2026-07-11 |
| 3 | `/Users/sab-mini/repos/MyAPI/AGENTS.md` | agent contract / work order | 2026-07-11 |
| 4 | `/Users/sab-mini/repos/MyAPI/myapi-db-plan.md` | six-node execution graph plan | 2026-07-28 |
| 5 | `/Users/sab-mini/repos/MyAPI/mcp/` (`server.py`, `README.md`) | MyMCP doorway (2 tools) | 2026-07-11 |
| 6 | `/Users/sab-mini/repos/MyAPI/evals/golden_briefs/` | golden briefs (3 files) | present under evals |
| 7 | `/Users/sab-mini/repos/MyAPI/.handoffs/` | durable handoffs 000–029 | bulk 2026-07-11; **029** 2026-07-28 |
| 8 | `/Users/sab-mini/repos/MyAPI/project-docs/` | ARCHITECTURE, REBUILD-CONTEXT-ANCHOR, corpus plans | live tree |
| 9 | `/Users/sab-mini/repos/MyAPI/Corpus v1.0/` | PARA substrate (buckets only below) | vault build ~2026-06-01; tree present |
| 10 | `/Users/sab-mini/repos/MyAPI/context_refinery/` | Python package (adapters, models, triage) | present |
| 11 | `/Users/sab-mini/repos/MyAPI/graphify-out/` | graph labels / prior analysis | cache + graph.json present |
| 12 | `/Users/sab-mini/repos/MyAPI/gddp/nodes/` | first durable-handoff GDDP node YAML | linked via handoff 029 |
| 13 | git tip `main` @ `b56e47a` | repo truth | `docs: add myapi-db-plan…` |

## Corpus v1.0 buckets (sample list — no dump)

`00-index` · `10-current-state` · `20-projects` · `30-systems-and-workflows` · `40-decisions-and-trajectories` · `50-timeline` · `60-sessions-and-conversations` · `70-artifacts-and-reference` · `80-candidates` · `90-raw-provenance` + `_manifests/` `_reports/`

README counts (build report): ~2675 inventory rows, ~579 CLI sessions role, ChatGPT/Claude/Codex/Obsidian mixes — cold substrate, not active corpus default.

## Golden briefs (names only)

- `evals/golden_briefs/get_project_context_myapi_rebuild.md`
- `evals/golden_briefs/get_project_context_pi_needle.md`
- `evals/golden_briefs/get_person_context_sab.md`

## Env / secret names only (no values)

Expect names like `KHOJ_*`, corpus path overrides, MCP budget args — never paste values. `.env` out of scope for this harvest.

## mini vs air

Mini owns repo truth (main tip, handoffs, plans, mcp package, corpus tree). Air expected to own vault notes + agent sessions about MyAPI.
