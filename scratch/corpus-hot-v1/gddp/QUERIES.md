# gddp / QUERIES — merged v1

Date: 2026-07-29
Mini = repo/prod bias. Air = vault/operator bias. Both kept as evidence.

---

## From mini

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


---

## From air

# GDDP — QUERIES (air)

## Ownership (runtime vs config) — required pair
1. What does **gddp-config** own that runtime must never invent? (graphs, schemas, acceptance criteria)
2. What does **gddp-runtime** own that config does not? (jobs, queue, evidence, evaluator loop, topology)
3. Who is allowed to **mutate graph truth** after a successful agent run? (human acceptance only — per PROJECT-BRIEF)

## Now-state
4. Where is production control plane (host, intake port, queue DB path) documented?
5. What is the newest runtime handoff number/topic on air?
6. What is the newest config handoff number/topic on air?
7. Is pi-big still a GDDP queue host or disarmed?

## Evidence
8. Where is the four-truth model (canon / graph / evidence / human acceptance) written?
9. What handoff proves **config-owned CLI** vs runtime boundary?
10. What runtime handoff covers concurrent evaluator / fleet bridge with Pi?

## Connect
11. How does a **node** in config `graphs/` relate to a **job** / executor session in runtime?
12. How should graphify-out labels be used (vocab) without confusing them for project nodes?
13. How does MyAPI’s `prove-first-durable-handoff` node validate against gddp-config schema?
14. Where do operator flashcards (GDDP_Protocol) sit relative to repo canon — teaching layer or authority?

