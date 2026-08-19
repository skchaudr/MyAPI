# myapi / GAPS — merged v1

Date: 2026-07-29
Mini = repo/prod bias. Air = vault/operator bias. Both kept as evidence.

---

## From mini

# MyAPI — GAPS (mini pass-1)

## Why graphify / semantic alone would fail

- Graph in PROJECT-BRIEF is a **plan snapshot** (2026-06-21 analysis), not live system state — agents treat nodes as implemented truth.
- `graphify-out/` present but **no reindex this pass**; labels lag code/docs.
- Corpus v1.0 bulk is volume-skewed (ChatGPT/Obsidian); semantic search without handoff priority re-creates v0 failure.
- Golden briefs and MCP fixtures live in small paths; full-vault retrieval buries them.
- Cross-repo edges (MyAPI ↔ GDDP node YAML ↔ .pi agents/myapi) need path joins files provide; empty graph query won’t.

## Still missing on mini (for pass-2 / air merge)

- Air vault notes + sessions last ~2 weeks (operator intent, not in this tree).
- Whether Khoj/VM live index matches active-corpus policy (out of scope to verify here).
- Full REBUILD-CONTEXT-ANCHOR / ARCHITECTURE deep extract (pointed, not copied this pass).
- Runtime proof that MCP tools are wired beyond fixture README (live wiring out of scope).
- Secret/env inventory names only — values never harvested.

## Pass-1 stop

Sources ≥5 · queries ≥8 · brief non-empty with real paths · gaps explicit. No commit / reindex.


---

## From air

# MyAPI — GAPS (air)

## Why graphify / semantic search would fail alone
- **MyAPI `graphify-out`** (present on air) labels functions/files (`split_paste…`, module names) — not product narrative, MCP tool contracts, or corpus admission rules.
- **Working tree ≠ main:** IMPLEMENTATION-PLAN, PROJECT-BRIEF, `evals/golden_briefs/`, `mcp/`, renumbered `.handoffs/` including 029 are not on current branch files; blind local index misses them.
- **Operator truth is vault-side** (Corpus v1.0 + SSD notes) outside the git graph; graphify of repo won’t see “what normalization is becoming.”
- **Volume-biased RAG** is the known failure mode this rebuild rejects; more Khoj reindex without handoff structure repeats v0.

## Still missing on air (for a complete brief)
- Checked-out `main` with live golden briefs + MCP package (or explicit multi-branch harvest procedure).
- Recent (~2 week) dense MyAPI agent sessions — air Claude path is legacy `-Users-saboor-repos-MyAPI`; few fresh MyAPI-titled rollouts vs GDDP/Needle.
- Mini’s freshest handoffs if air Sync/clone lags further (cross-host pass-2 merge).
- Active corpus tier policy / freshness audit files exist on main as `project-documents/*` — not verified content depth this pass.
- Live MCP wiring and Khoj “feel good” intentionally out of scope.

## What air uniquely contributes
- Full **Corpus v1.0** Obsidian substrate with numbered buckets.
- Operator simplification notes and 10-task normalization checklist.
- VM four-lanes / portfolio two-track notes tying MyAPI to GDDP.

