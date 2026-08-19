# myapi / SOURCES — merged v1

Date: 2026-07-29
Mini = repo/prod bias. Air = vault/operator bias. Both kept as evidence.

---

## From mini

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


---

## From air

# MyAPI — SOURCES (air)

Host: `sab-air.local` · Harvest: 2026-07-29 · Prefix `air:` = path on this machine.

**Clone note:** working tree is `feat/corpus-v1-normalization` @ `27b6821`, not `main` (`783c49b` local). Product tip files below marked **via main:** are readable with `git show main:…` but absent/stale on checked-out branch. Do not rewrite product tree.

| # | Path | Type | Freshness (approx) |
|---|------|------|--------------------|
| 1 | `air: git show main:PROJECT-BRIEF.md` (repo `~/repos/MyAPI`) | canon brief | on main tip; working tree missing file |
| 2 | `air: git show main:IMPLEMENTATION-PLAN.md` | implementation scaffold | on main; L0–L4 / corpus v2 / 2 MCP tools |
| 3 | `air: git show main:evals/golden_briefs/` — `get_project_context_myapi_rebuild.md`, `get_person_context_sab.md`, `get_project_context_pi_needle.md` | golden briefs | on main only |
| 4 | `air: ~/repos/MyAPI/handoffs/` (000–012 on branch) + `main:.handoffs/` (renumbered through 029) | durable handoffs | branch May–Jun 2026; main has 029 GDDP node 2026-07-17 |
| 5 | `air: ~/Obsidian/Corpus v1.0/` buckets: `00-index`…`90-raw-provenance`, `_manifests`, `_reports`, `dailys` | Corpus v1.0 vault substrate | structure Jun 2026; sample only — do not dump |
| 6 | `air: ~/Obsidian/SSD/What MyAPI v1 corpous normalization is really becoming.md` | operator note | 2026-06-01 |
| 7 | `air: ~/Obsidian/SSD/The 10 task checklist for the upgraded corpus v1 normalization path for MyAPI.md` | operator checklist | 2026-05-31 |
| 8 | `air: ~/Obsidian/SSD/02 Areas/Two Track Plan to Finishing GDD and MyAPI.md` | portfolio plan | 2026-05-01 (links MyAPI anchor) |
| 9 | `air: ~/Obsidian/SSD/02 Areas/Developer Infrastructure/AI/VM Codex Four Lanes Handoff 2026-07-02.md` | VM / lanes handoff | 2026-07-02 |
| 10 | `air: ~/repos/MyAPI/scratch/vertex_client.py` + upload/walkthrough scripts in `scratch/` | ADC/Vertex experiments (done on VM; local scripts remain) | Jul 2026 |
| 11 | `air: ~/.claude/projects/-Users-saboor-repos-MyAPI/` | Claude session project (legacy path encoding) | present; not active-cwd |
| 12 | `air: ~/.codex/memories/rollout_summaries/2026-05-21T08-50-35-ijdm-myapi_vertex_ai_search_chat_investigation.md` | Codex session summary | 2026-05-21 |
| 13 | `air: ~/.grok/sessions/%2FUsers%2Fsab-mini%2Frepos%2FMyAPI%2Fscratch%2Fcorpus-hot/` | Grok session (this harvest) | 2026-07-29 |
| 14 | `air: ~/repos/MyAPI/README.md`, `AGENTS.md`, `project-docs/`, `context_refinery/`, `graphify-out/` | live code + older docs on checkout | README 2026-06-08; graphify-out exists |
| 15 | `air: main:mcp/` (`mcp/server.py`, `mcp/README.md`) + `main:gddp/nodes/prove-first-durable-handoff.yaml` | MCP + first GDDP node | on main only |

**Env names only (no values):** `SENTRY_DSN`, `SENTRY_ENVIRONMENT`, `SENTRY_RELEASE`, `SENTRY_TRACES_SAMPLE_RATE`, `ENABLE_SENTRY_TEST_ENDPOINT` from `.env.example`. Vertex/GCP keys live outside tree (not listed as values).

**Missing on air checkout vs mini expectation:** root `.handoffs/` (dot), live `IMPLEMENTATION-PLAN`/`PROJECT-BRIEF` on working tree, `mcp/` package, `evals/golden_briefs/`. Truth for those = `main` objects or mini after pull.

