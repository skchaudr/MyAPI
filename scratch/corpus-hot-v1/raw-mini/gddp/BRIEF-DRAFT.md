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
