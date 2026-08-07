# Canonical intent — foundation for Factory Droid mission planning → GDDP graph

**Use this file when:** running a Factory Droid (or other) mission-planning session to author the **canonical** MyAPI cold-start graph in `gddp-config`.  
**Role of this pack:** Wayfinder-class **intent capture**. GDDP will **preserve** intent in nodes; it will not invent it. Factory Droid may re-grill shape/acceptance — this is the non-negotiable product intent underneath.

**Sibling refs:**
- Full thread capture (tickets ↔ nodes): `THREAD-CAPTURE-MAP.md`
- Executor node prose: `NODE-MAP.md`
- Draft YAML: `gddp-draft/myapi-cold-start/`
- Handoff rule: `WAYFINDER-TO-GDDP.md`
- Research: `research/01-inventory-existing-machinery.md`, `research/02-cold-start-question-bank.md`

---

## 1. Intent (what must not get lost)

### End state that counts as “usable”
An agent, on cold start for **MyAPI** (prove path first), can in **30–90 seconds**:

1. Call **MCP** like they call Graphify — specifically **`get_project_context`** and **`get_person_context`**
2. Optionally dig with **`/query`** (Khoj-backed MyAPI) using **documented args/examples**
3. Get **orientation**, not file archaeology: where we are, what’s true, what’s open, what’s dangerous
4. Get **meaning** (intent, decisions, drivers, history) from sessions / notes / docs — **not** AST structure
5. See **grounded** claims with evidence paths, or **explicit weak/empty** — never Graphify-style confident bogus

If those five are true, the graph followed through. If MCP exists but briefs invent, or `/query` works but agents can’t find it, or only fixtures work forever — **intent failed** even if nodes are “green.”

### Product name for the intent
**Semantic Graphify for agent cold-start** — same hammer pattern as Graphify, substrate = personal + project knowledge + meaning-behind-code.

### Architecture intent (roles)
| Piece | Owns |
|---|---|
| **Khoj** | Search engine / index |
| **MyAPI / Context Refinery** | Retrieval engine, `/query`, brief composition |
| **MCP** | Thin doorway: two tools only for cold-start hammers |
| **Graphify / repo tools** | Structure only (symbols, imports) — **out of this product** |

### Path intent
- Reuse what exists; near-term; not a multi-month rewrite  
- **MyAPI first** as prove project; multi-project later with same contract  
- **New** canonical graph; old six-node `graphs/myapi` is **loot/reference only**  
- Executors dig the corpus; humans/mission planning capture intent — operator is not the corpus index  

---

## 2. Why order matters (usable follow-through)

Wrong order ships “tools” that nothing real backs, or “retrieval” nothing can call.

**Critical path to usable outcome:**

```
N1  Rebuild surface online
    (engine + mcp package + goldens on one tip — no host guessing)
         │
         ├──────────────────────┐
         ▼                      ▼
N2  /query agent contract    N3  Project context brief
    (dig tool usable)            (orientation payload exists)
         │                      │
         │                      ▼
         │                   N4  Person context brief
         │                      (second tool payload; thin OK)
         │                      │
         └──────────┬───────────┘
                    ▼
N5  MCP two tools LIVE
    (agents’ actual entry — must call real path, not fixture-as-end-state)
                    │
                    ▼
N6  Prove eight must questions
    (usable bar — not vibes)
```

**Ordering rules for mission planning / canonical graph:**

1. **N1 before everything** — otherwise executors invent paths or build against half a tree.  
2. **N3 before N5** — MCP without a real brief is a hollow Graphify.  
3. **N2 before or with N5** — `/query` must be a documented first-class dig; not an afterthought README.  
4. **N4 after N3** — same envelope; don’t redesign twice.  
5. **N5 before N6** — prove the path agents will actually hit.  
6. **N6 is the definition of done for v1** — eight questions, honest outcomes. Do not mark the graph “product complete” on N5 alone.

**Parallelism allowed:** N2 ∥ N3 after N1.  
**Not allowed:** N5 before N3; N6 before N5; skipping N1 because “main has it somewhere.”

**Trap to avoid (from thread + old graph):** shipping `serve-context-via-mcp` style nodes while corpus/brief/prove order is wrong — or running heavy corpus assembly as a blocker when the intent was a **thin cold-start loop**.

---

## 3. Intent → node `why` (paste into canonical graph)

When authoring `gddp-config` nodes, every node `why` should still point at the end state in §1.

| Node | Intent one-liner for `why` |
|---|---|
| **N1** bring-rebuild-surface-online | Executors cannot deliver cold-start if engine and doorway assets live on different tips/hosts. |
| **N2** agent-query-contract | Agents freestyle retrieval unless `/query` has args/examples and a real Khoj-backed path. |
| **N3** project-context-brief | Cold-start needs a structured orientation brief (status/true/open/danger/decisions/evidence), not hits alone. |
| **N4** person-context-brief | Second hammer needs the same envelope; weak/empty OK if corpus is thin — no invented person story. |
| **N5** mcp-two-tools-live | Agents already hammer Graphify-class tools; the product is two live MCP tools on MyAPI, not fixtures forever. |
| **N6** prove-myapi-cold-start | Usable means the eight must questions work with grounded or honest empty answers. |

**Acceptance intent (every build node should respect):**
- No invention of project truth  
- Evidence paths when claiming  
- Backend down → clear failure, not a fake full brief  
- Meaning over AST  
- MyAPI prove-first  

---

## 4. Tickets (intent layer) vs nodes (execution layer)

| Tickets (Wayfinder captured) | Nodes (GDDP executes) |
|---|---|
| T01 inventory | N1 |
| T02 eight must questions | N6 (+ shapes N3/N5) |
| T03 no fake confidence | N3–N6 acceptance |
| T04 thin loop | whole chain N1–N6 |
| T05 episodic levels | N3/N4 brief shape |
| T06 sources high-signal | N3 inputs |
| T07 meaning vs AST | N3 scope; bans AST clone |
| T08 engine vs MCP | N2, N5 |

Full matrix: `THREAD-CAPTURE-MAP.md`.

**Division of labor going forward:**
- **Wayfinder / this pack / Factory mission grilling:** capture and sharpen intent, order, acceptance language  
- **GDDP graph:** durable nodes + depends_on + acceptance + constraints  
- **Factory Droid (executor):** build within node bounds; its grilling should refine *how*, not replace *why*  
- **Runtime:** dispatch + receipts; does not rewrite intent  

---

## 5. Eight must questions (N6 bar — do not drop)

1. What is this project and its current goal?  
2. Who owns MyAPI vs MCP doorway / what may be written?  
3. Current phase / north star / tip lag  
4. What’s broken or blocked?  
5. Where should I begin (entry paths)?  
6. What decisions constrain this work?  
7. What evidence paths back the above?  
8. What does this code area mean (module narrative, not AST)?  

---

## 6. Suggested mission-planning agenda (Factory Droid)

1. Load **this file** as non-negotiable intent.  
2. Load `NODE-MAP.md` + draft YAML as starting graph, not final law.  
3. Re-grill only where acceptance is fuzzy (field shapes, hosts, fixture vs live policy) — not re-litigate north star.  
4. Emit **canonical** `gddp-config/graphs/<id>/` with:
   - depends_on matching §2 order  
   - `why` language from §3  
   - N6 as the usability gate  
5. Mark old `graphs/myapi` six-node set as superseded/loot in project notes if needed.  
6. Only then queue Factory Droid (or other) **execution** runs node-by-node.

---

## 7. Current operational note (external to this pack)

Operator note (session context): first five-node execution runs are already in flight under a **second executor type (Factory Droid)**. When promoting **this** cold-start graph to canonical, keep:

- Intent and order from this file as the target product path  
- Live Droid runs as a separate execution stream unless intentionally merged  
- Do not let a different graph’s node order redefine “usable” for Semantic Graphify cold-start  

---

## 8. One sentence for the top of the canonical `project.yaml`

> Agents cold-start on MyAPI in 30–90s via two live MCP tools plus documented `/query` on Khoj-backed MyAPI, receiving grounded orientation (where / true / open / dangerous / meaning) or explicit empty — not AST Graphify and not confident invention.
