# Thinnest v1 cold-start product loop

Type: grilling
Status: resolved
Blocked by: 01, 02

## Question

Smallest end-to-end loop that earns the north star using what already exists.

## Answer

**Loop:** Khoj → Context Refinery / MyAPI → agents hit **two MCP tools** + **`/query` (with args/examples)** → cold-start orientation in 30–90s.

**Entry (operator-locked):** Two MCP tools (`get_project_context`, `get_person_context` intent) + first-class `/query` with guidance; Khoj is the real engine underneath.

**Scope:** Prove on **MyAPI** first (project id in the API is fine; portfolio-wide v1 is not required). Same shape later for other projects.

**Response shape:** MCP tools return a **structured brief** (where we are / true / open / dangerous + evidence). `/query` returns **ranked grounded hits** for deeper dig. Both ship.

**Non-goals for v1:** Not a second Graphify AST. Not full life-graph ontology. Not multi-tenant SaaS. Not rewriting Khoj/refinery. Not “every trust-bank query green.” Not the old six-node GDDP graph as mandatory scaffold — **new graph** later from these decisions.

**Success bar:** The eight must-questions from research/02 for MyAPI cold-start, with grounded or explicitly weak/empty answers.

## Comments

- Entry locked live with operator; remaining cuts closed from north star + “stop re-covering ground.”
