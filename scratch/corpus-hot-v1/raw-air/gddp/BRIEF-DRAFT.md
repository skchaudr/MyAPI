# GDDP — BRIEF-DRAFT (air)

## Short Answer
**GDDP** (Graph-Driven Agentic Development) keeps agent work **economically small and intent-preserving**: project work is a graph of **nodes** with dependencies and acceptance criteria; agents execute **jobs** that produce **evidence**; only **human acceptance** advances graph truth. On air: full clones of **gddp-config** (schemas, graphs, templates — source of truth agents read, do not write) and **gddp-runtime** (operating loop, queue, evaluator, topology — production documented as **sab-mini**). Air is strong for docs/handoffs/sessions; live intake/queue secrets and production launchd are mini-primary.

## Why
Without GDDP, agent success silently becomes “project truth.” GDDP separates canon, graph, evidence, and human gate.

## Relationships
- **config** defines; **runtime** observes/dispatches/evaluates.
- Portfolio with MyAPI (context continue) and Pi/Needle (executors/fleet).
- graphify-out = code label inventory, not the GDDP project graph.

## Evidence (exist on air)
1. `air: ~/repos/gddp-runtime/PROJECT-BRIEF.md`
2. `air: ~/repos/gddp-config/README.md`
3. `air: ~/repos/gddp-runtime/TOPOLOGY.md`
4. `air: ~/repos/gddp-runtime/.handoffs/059-scripted-pi-fleet-bridge.md`
5. `air: ~/repos/gddp-config/.handoffs/034-dispatch-graph-target-fix.md`

## Risks
- Confusing graphify AST nodes with GDDP project nodes.
- Treating air clone as production control plane (TOPOLOGY says mini).
- Reading only one repo and missing ownership split.

## Next
- Pass-2: golden brief with explicit ownership matrix + one worked example node→job→evidence→accept.
- Keep production ops changes on mini.
