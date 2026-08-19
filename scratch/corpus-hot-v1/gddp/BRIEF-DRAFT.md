# gddp / BRIEF-DRAFT — merged v1

Date: 2026-07-29
Mini = repo/prod bias. Air = vault/operator bias. Both kept as evidence.

---

## From mini

# GDDP — BRIEF-DRAFT (mini pass-1)

## Short Answer

GDDP is a **graph-driven control plane**: humans author intent as nodes (deps, constraints, acceptance); agents execute **jobs** and return **evidence**; only human acceptance advances graph truth. **gddp-config** = declarative truth (schemas, graphs/, templates, validator/TUI). **gddp-runtime** = loop engine (dispatch, adapters, SQLite, evaluators, heartbeats) that **reads** config and **never** writes node YAML. On mini both repos are on `main` with Jul 29 handoffs (runtime multi-project heartbeat; config TUI/dispatch). Infrastructure completion is never the destination — the node round trip is.

## Evidence paths (exist on mini)

1. `/Users/sab-mini/repos/gddp-runtime/PROJECT-BRIEF.md`
2. `/Users/sab-mini/repos/gddp-runtime/README.md`
3. `/Users/sab-mini/repos/gddp-config/README.md`
4. `/Users/sab-mini/repos/gddp-config/AGENTS.md`
5. `/Users/sab-mini/repos/gddp-config/schemas/v1/` (dir)
6. `/Users/sab-mini/repos/gddp-runtime/.handoffs/060-multi-project-heartbeat-dispatch-hardening.md`
7. `/Users/sab-mini/repos/gddp-config/.handoffs/033-gddp-tui-navigation.md`

## Operator one-liner

Config for *what*; runtime for *how attempts are recorded*; human for *truth*.


---

## From air

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

