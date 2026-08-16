# GDDP — QUERIES (mini pass-1)

## Ownership (runtime vs config) — required pair

1. What does **gddp-config** own that **gddp-runtime** must only read?
2. What does **gddp-runtime** own that must never rewrite node YAML / graph status?

## Now-state

3. What is the canonical operating loop (Authored → Ready → … → Human acceptance)?
4. What is the four-way truth split (Canon / Graph / Evidence / Human acceptance)?
5. Where do ready nodes and acceptance criteria live on disk?
6. What is the current mini tip of runtime vs config?

## Evidence

7. Which handoff documents multi-project heartbeat / dispatch hardening on runtime?
8. Which handoff documents TUI navigation or dispatch graph target on config?
9. What schemas define Node vs Job vs Result vs Event?

## Connect A→B

10. How does a human-marked ready node become a job packet and then `awaiting_review` without graph writeback?
11. How do Jules (or other) adapters attach without changing graph authorship?
12. How does MyAPI’s first durable-handoff node relate across MyAPI repo and GDDP graphs?

## Graphify-class (labels only)

13. What community hubs does GRAPH_REPORT list for gddp-runtime (reconciler, SemanticToolbox, cli…)?
14. When is the graph stale relative to `git rev-parse HEAD` vs built-from commit in GRAPH_REPORT?
