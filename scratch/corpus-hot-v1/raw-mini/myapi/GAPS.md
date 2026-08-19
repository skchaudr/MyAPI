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
