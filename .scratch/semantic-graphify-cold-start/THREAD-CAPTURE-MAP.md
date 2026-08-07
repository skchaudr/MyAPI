# Thread capture map — MyAPI Semantic Graphify cold-start

**Source:** Full wayfinder / product conversation (destination through executor handoff).  
**Purpose:** Capture important information even where process was incomplete or abandoned mid-grill.  
**Not:** A claim that every ticket was “properly” wayfinder-resolved.  
**Also:** Side-by-side **tickets** (decide / clarify / track) vs **nodes** (build / prove).

**Artifacts in this effort folder:**
- `map.md` — wayfinder destination + decisions so far  
- `issues/01–08` — decision tickets  
- `research/01`, `research/02` — inventory + question bank  
- `WAYFINDER-TO-GDDP.md` — handoff rule  
- `NODE-MAP.md` — executor-oriented node list  
- `gddp-draft/myapi-cold-start/` — draft GDDP YAML  

---

## 1. Product north star (from the thread)

### One line
Agent cold-start that returns structured, leveled, grounded orientation over work + life knowledge — including semantic meaning of project code — via an API/MCP agents can hammer like Graphify.

### What you optimized for most
**First 30–90 seconds of an agent session:** where we are, what’s true, what’s open, what’s dangerous — without file archaeology.

### What the product is
**Semantic Graphify** that can *supplant* normal Graphify for orientation because it includes:
- agent sessions  
- project notes not only in repo `docs/`  
- chats, project docs  
- other sources that establish **objective reality** of a project/feature/code: intentions, who drives it, decisions made  

### Graphify comparison (thread table, kept)

| Graphify-ish tools give | MyAPI/MCP adds |
|---|---|
| Code structure (symbols, imports, call graph) | Meaning of that code — intent, decisions, constraints, history |
| Repo-local graph | Life + work corpus — chats, sessions, vault, operator state |
| “Where is X defined?” | “Why is X this way, what’s current, what broke last time?” |

Same **interaction pattern** (agents hammer a query/graph tool). Different **substrate**.

### Fixed principles (thread)
- Cold-start first  
- Semantic graph over life/work corpus — not AST modules/imports  
- Prefer no evidence / weak evidence over confident bogus answers  
- Agent questions (including failed Graphify queries) are product signal  
- Episodic levels: not one blob of “relevant docs” (raw → summary → decision → current status)  
- **Near-term path:** much already exists; not a multi-month greenfield  

### Explicit non-goals (thread)
- Replacing Graphify for pure code structure  
- Multi-tenant SaaS  
- Perfect total recall of all history as v1 bar  
- Greenfield rewrite of Context Refinery or Khoj  
- Auto-writing graph truth without human trust gates  
- “Every Phase-2 trust-bank query green” as definition of done  
- Old six-node `gddp-config/graphs/myapi` as mandatory scaffold (loot only; **new graph**)  

---

## 2. Process / meta (what this thread also decided)

| Insight | Implication |
|---|---|
| Wayfinder = reveal path / lock decisions | Good for fog; bad if re-asking what’s already known |
| GDDP = execution surface | Nodes for executor agents; receipts; human accepts graph truth |
| Tickets → foundation for nodes | After decisions (or after capturing them), nodes get `why` + acceptance |
| Operator not committed to skill-to-the-T | Prefer usable node/ticket map over pure wayfinder ritual |
| Operator does not hold entire corpus in head | Executors research; tickets/nodes carry enough context to dig |
| Two MCP tools + `/query` + Khoj | Entry surface locked mid-thread |
| New MyAPI graph | Author fresh graph from this capture; don’t only reconcile old nodes |

**Handoff rule (short):** Open questions ≠ nodes. Buildable capabilities with acceptance = nodes. Runtime stops at receipts. Full writeup: `WAYFINDER-TO-GDDP.md`.

**Workflows compared early in thread (context only):**
1. Matt main flow: grill → to-spec → to-tickets → implement  
2. Wayfinder: decision map → then join main flow  
3. GDDP: human graph → runtime dispatch → receipts → human review  

---

## 3. Side-by-side: tickets vs nodes

Tickets = “what we had to surface / decide / remember.”  
Nodes = “what an executor builds or proves.”  
Not 1:1. One ticket can feed many nodes; one node can absorb many tickets.

### A. Research / inventory tickets

| Ticket | Status in process | What it captured | Related node(s) |
|---|---|---|---|
| **T01 Inventory existing machinery** | Resolved (research) | Live engine on feat trees (`/query`, refinery, adapters, anchors, benchmarks). Rebuild surface on GitHub `main` (`mcp/`, golden briefs, PROJECT-BRIEF, IMPLEMENTATION-PLAN, …). Local `origin/main` can be stale. Thin paths: anchors+query, corpus-hot, MCP glued to `/query`. | **N1** bring-rebuild-surface-online |
| **T02 Cold-start question bank** | Resolved (research) | Eight **must** questions for v1 success; Graphify failure modes; MCP surface signal (`get_project_context` / `get_person_context`). Full list in research/02. | **N6** prove-myapi-cold-start; shapes **N3/N5** success criteria |

### B. Product / decision tickets (thread + collapse)

| Ticket | Status in process | What it captured (even if closed roughly) | Related node(s) |
|---|---|---|---|
| **T03 Don’t fake confidence** (“honest answer contract”) | Resolved as *already in north star* | When system doesn’t know → say weak/missing; don’t invent. Field names = build detail. Jargon was poorly framed mid-thread. | **N3, N4, N5, N6** (acceptance: no invention; backend-down honest) |
| **T04 Thinnest v1 loop** | Resolved (entry locked live; rest closed from north star) | Khoj → MyAPI → **2 MCP tools + `/query` (args/examples)**; prove MyAPI first; MCP brief + ranked hits; new GDDP graph. | **N1–N6** entire graph |
| **T05 Episodic levels** | Resolved from north star | Prefer status/open/danger + decisions in brief; summaries support; raw as evidence links. | **N3, N4** brief shape |
| **T06 Source priority** | Resolved from north star | Sessions, project notes (incl. outside `docs/`), chats, docs, anchors/handoffs; prefer high-signal over bulk chat spam; live Khoj path. | **N3** composer inputs; corpus work if later nodes added |
| **T07 Code-meaning boundary** | Resolved from operator | MyAPI owns **meaning**; Graphify/repo owns **structure**; knowledge-primary; no dual AST product in v1. | **N3** (narrative, not AST); out-of-scope for Graphify clone nodes |
| **T08 MyAPI vs MCP ownership** | Resolved from entry surface | MyAPI/Khoj = engine; MCP = thin doorway; `/query` stays first-class. | **N2, N5** |

### C. Execution nodes (draft graph `myapi-cold-start`)

| Node | Builds / proves | Fed by tickets | Depends on |
|---|---|---|---|
| **N1** `bring-rebuild-surface-online` | One build tip with engine + mcp + goldens; host/run notes | T01, T04 | — |
| **N2** `agent-query-contract` | `/query` docs, args, examples for agents | T04, T08 | N1 |
| **N3** `project-context-brief` | Project cold-start brief composer (MyAPI first) | T02–T07 | N1 |
| **N4** `person-context-brief` | Person brief, same envelope | T04, T03, T08 | N3 |
| **N5** `mcp-two-tools-live` | Live `get_project_context` + `get_person_context` | T04, T08, T03 | N2, N3, N4 |
| **N6** `prove-myapi-cold-start` | Eight must-questions eval receipt | T02, T03 | N5 |

### D. Dependency picture (both layers)

```
TICKETS (already surfaced)              NODES (executor work)
─────────────────────────               ────────────────────
T01 inventory ───────────────────────► N1 rebuild surface
T02 question bank ───────────────┐       │
T03 no fake confidence ──────────┤       ▼
T04 thin loop (entry+loop) ──────┼──► N2 query contract
T05 levels ──────────────────────┤       │
T06 sources ─────────────────────┤       ▼
T07 meaning vs AST ──────────────┼──► N3 project brief ──► N4 person brief
T08 engine vs MCP ───────────────┘       │
                                         ▼
                                      N5 MCP two tools
                                         │
                                         ▼
                                      N6 prove 8 questions
```

---

## 4. Eight must questions (ticket T02 → node N6)

These are the v1 cold-start success set mined in research (not invented blank-page):

1. What is this project and its current goal?  
2. Who owns MyAPI vs MCP doorway / what may be written?  
3. Current phase / north star / tip lag  
4. What’s broken or blocked?  
5. Where should I begin (entry paths)?  
6. What decisions constrain this work?  
7. What evidence paths back the above?  
8. What does this code area *mean* in product terms (module narrative, not AST)?  

**Deferred from full trust bank as cold-start gates:** human find-thread, exact-phrase probes, F1–F4 failure classes, full decision-recovery, symbol-level dual graph.

---

## 5. Important facts surfaced (inventory) — keep for executors

- **This host / feat branch:** live `api/` + `context_refinery/` + adapters + anchors + benchmarks + deploy scripts.  
- **GitHub `main`:** `mcp/`, `evals/golden_briefs/`, `PROJECT-BRIEF`, `IMPLEMENTATION-PLAN`, `myapi-db-plan`, `graphify-out`, rebuild handoffs — may be missing on feat checkout.  
- **Corpus-hot pack:** `/home/saboor/khoj-data/notes/corpus-hot-v1/myapi/` (SOURCES, QUERIES, GAPS, BRIEF-DRAFT).  
- **Old GDDP graph (loot):** `/home/sab-mini/gddp-config/graphs/myapi/` — six nodes (vertex baseline, assemble corpus, mine queries, prove retrieval, serve MCP, incremental refresh). Reference language only; **new** graph is `myapi-cold-start` draft.  
- **Known failure modes:** Graphify plan-as-live; AST ≠ narrative; working tree ≠ main; volume RAG / ChatGPT dominance; vault truth outside git.  

---

## 6. Tickets that were *process pain* (capture the lesson)

| What went wrong | Capture |
|---|---|
| Re-grilling already-answered north star as “T03–T08” | Don’t require operator to re-state corpus ontology; collapse into destination |
| “Honest answer contract” jargon | Means: don’t invent when weak/empty; say so |
| Tables / multi-option theater | Operator wanted flat questions or just nodes |
| Assuming operator holds full active corpus | Executors dig; nodes include paths and research pointers |

These are meta-tickets for *how* to run the next effort — not product nodes.

---

## 7. Optional later tickets/nodes (fog — not in the six)

Surfaced as “not yet” / out of path for thin v1; keep so they aren’t lost:

| ID | Idea | Ticket or node later? |
|---|---|---|
| F1 | Full life-graph entity/edge ontology | Ticket → then nodes |
| F2 | Live join Graphify AST symbol → narrative brief | Node after N3/N6 |
| F3 | Multi-project portfolio cold-start | Nodes after MyAPI prove |
| F4 | Active hot window vs Corpus v1 cold default | Ticket + corpus node |
| F5 | MCP install UX across all agent hosts | Node polish after N5 |
| F6 | Obsidian human UI as product surface | Out of cold-start graph |
| F7 | Port useful acceptance from old six-node graph (baseline freeze, incremental refresh) | Optional nodes if still needed |
| F8 | Copy `gddp-draft/myapi-cold-start` into official `gddp-config` | Operator/task node |

---

## 8. Master index (everything numbered)

### Tickets (T)
| ID | Title |
|---|---|
| T01 | Inventory existing machinery |
| T02 | Cold-start question bank (8 must) |
| T03 | Don’t fake confidence / grounded or empty |
| T04 | Thinnest v1 loop (MCP + /query + Khoj, MyAPI first) |
| T05 | Episodic levels in brief |
| T06 | Source priority / high-signal substrate |
| T07 | Code-meaning vs Graphify AST |
| T08 | MyAPI engine vs MCP doorway |
| T-meta-1 | Wayfinder → GDDP handoff rule |
| T-meta-2 | New graph not old six-node scaffold |
| T-meta-3 | Process: collapse known answers; executors dig corpus |

### Nodes (N)
| ID | node_id |
|---|---|
| N1 | bring-rebuild-surface-online |
| N2 | agent-query-contract |
| N3 | project-context-brief |
| N4 | person-context-brief |
| N5 | mcp-two-tools-live |
| N6 | prove-myapi-cold-start |

### Side-by-side one-pager

| Ticket | Node |
|---|---|
| T01 | N1 |
| T02 | N6 (criteria); N3/N5 (shape) |
| T03 | N3, N4, N5, N6 |
| T04 | N1–N6 (whole chain) |
| T05 | N3, N4 |
| T06 | N3 (+ future corpus nodes) |
| T07 | N3 (narrative only); bans Graphify-clone node |
| T08 | N2, N5 |
| T-meta-1/2 | How to place YAML in gddp-config |
| T-meta-3 | How to brief executors (NODE-MAP + research paths) |

---

## 9. Where to go next (no more clarification required)

1. Hand executors **NODE-MAP.md** + `gddp-draft/myapi-cold-start/nodes/*.yaml` + this file.  
2. Optionally copy draft graph into `/home/sab-mini/gddp-config/graphs/myapi-cold-start/`.  
3. Start **N1**.  

Wayfinder ritual is optional from here; the map of what the thread produced is this document.
