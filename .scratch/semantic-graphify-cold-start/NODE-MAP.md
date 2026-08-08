# MyAPI cold-start — executor node map

**Purpose:** Reasonable build nodes for executor agents. Not wayfinder Q&A.  
**Product:** Semantic Graphify for agent cold-start — first 30–90s orientation via MCP + `/query` over Khoj/MyAPI.  
**Constraint:** Reuse what exists. Prove on **MyAPI** first. Don’t invent a second AST Graphify.

**Machine notes for executors:**
- Working clone may be `feat/corpus-v1-normalization` with live `api/` + `context_refinery/`.
- GitHub `main` has `mcp/`, `evals/golden_briefs/`, `PROJECT-BRIEF.md`, `IMPLEMENTATION-PLAN.md` — pull or `git show` if missing on branch.
- Research: `.scratch/semantic-graphify-cold-start/research/01-inventory-existing-machinery.md`, `…/02-cold-start-question-bank.md`
- Draft YAML (drop into `gddp-config` when ready): `.scratch/semantic-graphify-cold-start/gddp-draft/myapi-cold-start/`

---

## Graph (order)

```
[1] bring-rebuild-surface-online
        ↓
[2] agent-query-contract          (can parallel with 3 after 1)
        ↓
[3] project-context-brief  ←──── depends on 1, uses /query
        ↓
[4] person-context-brief   ←──── depends on 3 (same envelope)
        ↓
[5] mcp-two-tools-live     ←──── depends on 3, 4, 2
        ↓
[6] prove-myapi-cold-start ←──── depends on 5
```

---

## Node 1 — `bring-rebuild-surface-online`

**Do:** Make the build tree have everything needed: live engine code + `mcp/` + golden briefs + product brief from `main` if missing. Document which branch/tip executors must use.

**Done when:**
- Executor can open `mcp/`, at least the golden brief paths named on main, and run or locate `/query` code without guessing hosts.
- Short `result-summary.md` lists tip SHA, paths present, and “run on Mac/VM” notes if relevant.

**Do not:** Redesign corpus. Reindex the world.

---

## Node 2 — `agent-query-contract`

**Do:** Make `/query` agent-usable: documented args, examples, and reasonable defaults for cold-start digs (project filter, n, sources). Point agents at Khoj-backed pipeline that already exists.

**Done when:**
- README or `docs/query-for-agents.md` (or MCP README section) has copy-paste examples.
- Schema/fields for request/response are accurate to current `api/schemas.py` + `query.py`.
- One smoke call documented (even if VM must be up).

**Do not:** Replace Khoj. Big retrieval rewrites.

---

## Node 3 — `project-context-brief`

**Do:** Implement the backend for **project cold-start brief** (what `get_project_context` will return): structured orientation for a project id (default **myapi**) — where we are, what’s true, what’s open/dangerous, key decisions, evidence paths. Compose from existing `/query` + anchors/handoffs/high-signal hits. If evidence is thin, say weak/missing — do not invent.

**Done when:**
- Callable path exists (function or HTTP) returning a stable brief shape.
- MyAPI-scoped call returns something usable for cold-start or explicit gaps.
- Evidence paths included when claims are made.
- Tests or a receipt with sample output.

**Do not:** Full portfolio multi-project perfection. AST graph.

---

## Node 4 — `person-context-brief`

**Do:** Same envelope as project brief, for **person** context (e.g. operator/sab) — thinner is fine. Reuse composer patterns from node 3.

**Done when:**
- Callable path + sample output or golden-aligned shape.
- Weak/empty allowed if corpus doesn’t support it yet (must be explicit).

**Do not:** Build a CRM. Scrape private stuff into git.

---

## Node 5 — `mcp-two-tools-live`

**Do:** Wire MCP server: **exactly two tools** — `get_project_context`, `get_person_context` — calling live MyAPI/brief path (not fixture-only as the end state). Keep `/query` documented as the dig tool.

**Done when:**
- Both tools callable via MCP.
- Live path works when API/Khoj are up; clear error if backend down (not a fake full brief).
- README: how to point Claude/Codex/Cursor at the server.

**Do not:** Large tool roster. Workflow engine. Graph traversal API.

---

## Node 6 — `prove-myapi-cold-start`

**Do:** Run the eight must cold-start questions for MyAPI (from research/02). Record pass / weak / empty / fail with evidence. This is the “agents can start” bar.

**Must-set (from research):**
1. What is this project and its current goal?
2. Who owns MyAPI vs MCP doorway / what may be written?
3. Current phase / north star / tip lag
4. What’s broken or blocked?
5. Where should I begin (entry paths)?
6. What decisions constrain this work?
7. What evidence paths back the above?
8. What does this code area mean in product terms (module narrative, not AST)?

**Done when:**
- Receipt lists all eight with outcome + sources or honest empty.
- Failures are diagnosed (corpus vs retrieval vs brief composer) — not silent.

**Do not:** Expand to full historical trust bank as the gate.

---

## Out of this graph

- New Graphify AST product  
- Full Corpus v1 rewrite as blocker  
- Multi-tenant SaaS  
- Old six-node myapi graph as required scaffold (loot only)  

---

## Hand to executors

Per node: give them this file + the matching YAML under `gddp-draft/myapi-cold-start/nodes/` + repo paths above. They write receipts; they do not invent new product direction.
