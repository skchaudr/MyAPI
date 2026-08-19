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
