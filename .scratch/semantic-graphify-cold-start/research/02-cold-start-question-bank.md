# 02 — Cold-start question bank (mined demand)

**Ticket:** semantic-graphify-cold-start / 02  
**Date:** 2026-08-04  
**Kind:** research findings only (no map/ticket edits)  
**Method:** harvest agent-shaped questions already present in corpus-hot, trust/acceptance banks, anchors, trust-threshold framing, and vault routing design — not invented from a blank page.

---

## 1. North-star frame (source-bound)

Cold-start success = an agent in the first **30–90s** can answer, with evidence paths or honest weak/no-evidence, the portfolio of:

| Cold-start axis | Phrase already in sources |
|---|---|
| Where we are | project identity + current goal / phase |
| What’s true | live tip, corpus policy, north star, branch lag |
| What’s open / dangerous | broken/blocked status; open workstreams |
| What’s decided | decision recall with authoritative sources preferred |
| What code *means* | narrative brief attached to symbols/files — not AST labels alone |

Primary product framing (agent as user):

> Agents call MyAPI on every cold start so they stop grepping for 30s. Return **answers**, not thread links. Quality bar = structured confidence, not vibes.

Sources: `project-docs/My-API-Trust-Threshold-Plan.md`; `README.md` (agent-facing cold-start); map north star in `.scratch/semantic-graphify-cold-start/map.md` (context only).

---

## 2. Ranked bank (~14 questions)

Rank = priority for **Semantic Graphify cold-start v1** (first session orientation), not full episodic memory coverage.  
Each item: **question** (as observed or lightly project-normalized from observed phrasing) · **intent** · **source path(s)** · **why cold-start** · **v1 must / defer**.

### A. Ownership

| Rank | Question | Source path | Why cold-start | v1 |
|---:|---|---|---|---|
| **1** | Who owns context engine vs doorway — **MyAPI vs MyMCP**? Is MyMCP a separate product or a thin paid doorway into MyAPI? | `/home/saboor/khoj-data/notes/corpus-hot-v1/myapi/QUERIES.md` (mini Q1; air Q3); `BRIEF-DRAFT.md` | Wrong owner → agent writes to wrong surface or invents MCP contracts | **must** |
| **2** | Who owns **durable handoff format** vs **MCP brief response shape**? Who may write graph/corpus truth vs who only reads/fixtures? | `QUERIES.md` (air Q1; mini Q3) | Prevents agents treating fixtures as write APIs or goldens as mutable truth | **must** (brief ownership answer) |
| **3** | Who owns **corpus admission** (vault normalize) vs **retrieval** (Khoj/VM vs local reader)? | `QUERIES.md` (air Q2) | Stops “just reindex Khoj” as the fix when admission policy is the lever | **defer** (important; not first 90s for every project) |

### B. Now-state

| Rank | Question | Source path | Why cold-start | v1 |
|---:|---|---|---|---|
| **4** | **What is MyAPI and what is its current goal?** | `scripts/acceptance.py` **A1**; `README.md` trust model; `myapi-status-anchor.md` (A1 references); corpus-hot `BRIEF-DRAFT.md` short answer | Canonical project-identity cold-start; acceptance gold | **must** |
| **5** | What is the **current phase** — planning/docs only, or implementation code live? What is the **north star** (corpus v1 vault substrate vs two MCP tools over durable handoffs)? | `QUERIES.md` (mini Q4; air Q6); `BRIEF-DRAFT.md` | Avoids agents “implementing” against plan-only trees or outdated north stars | **must** |
| **6** | What branch/tip is this clone on, and what is **missing vs `main`**? What did the last meaningful tip change? | `QUERIES.md` (mini Q5; air Q5); `GAPS.md` (working tree ≠ main); `SOURCES.md` | Air/mini lag is a proven failure mode for local-only reads | **must** (or honest “unknown / lagging clone”) |
| **7** | What is the **active corpus policy** (hot window vs Corpus v1.0 cold substrate)? | `QUERIES.md` (mini Q6); `BRIEF-DRAFT.md`; map “not yet specified” | Wrong corpus default re-creates volume-skewed v0 retrieval | **must** for MyAPI-scoped sessions; **defer** as generic multi-project default |
| **8** | What have I / we been working on **recently**? Has there been recent work on MyAPI? | `benchmark-v0.md` Q2; Trust-Threshold Category 2 (“Has there been recent work on MyAPI?”) | Resume without re-litigating origin | **must** (structured recent + evidence; not full timeline) |

### C. Danger / open (operational)

| Rank | Question | Source path | Why cold-start | v1 |
|---:|---|---|---|---|
| **9** | **What’s broken or blocked in MyAPI right now?** | `acceptance.py` **A7**; `source-of-truth-anchors/myapi-status-anchor.md` (explicit cold-start target); `STATUS_AND_NEXT_STEPS.md` | “What to avoid stepping on” before any edit | **must** |
| **10** | What is the **status of the API / Khoj deployment** (live endpoints, VM sleep, indexing)? | `acceptance.py` **A3**; `benchmark-v0.md` Q12; anchors `khoj-deployment-indexing-anchor.md`, `vm-tailscale-ssh-access-anchor.md` | Cold-start that pokes a sleeping VM looks like product failure | **must** for infra-touching work; optional otherwise |
| **11** | Which **golden briefs** exist and what intent do they encode (`get_project_context` / `get_person_context`)? | `QUERIES.md` (air Q7); `SOURCES.md` golden brief names; `BRIEF-DRAFT.md` | Eval contract for MCP-shaped answers | **must** if MCP surface is in scope for v1; else **defer** |

### D. Evidence

| Rank | Question | Source path | Why cold-start | v1 |
|---:|---|---|---|---|
| **12** | What **evidence paths** prove the two MCP tools and their fixture-backed answers? Where is the first **GDDP-linked** durable handoff node and what does acceptance require? | `QUERIES.md` (mini Q8–9; air Q9); `BRIEF-DRAFT.md` evidence lists; `SOURCES.md` | Grounds “what’s true” in paths, not chat | **must** (path list + honesty if fixtures-only) |
| **13** | What docs should I use to understand the **current system end to end**? Where should a cold-start agent **begin**? | `benchmark-v0.md` Q18; vault plan `00-index/` / project Index bundle; `STATUS_AND_NEXT_STEPS.md`; Trust-Threshold “answers not thread links” | Entry-point routing for the rest of the session | **must** |

### E. Decisions

| Rank | Question | Source path | Why cold-start | v1 |
|---:|---|---|---|---|
| **14** | **What did we decide about X?** (prototypes: vault schema; cwd-guard; packet schema; MyAPI rebuild direction / `myapi-db-plan` superseding prove-first-durable-handoff) | `benchmark-v0.md` Q8; Trust-Threshold Cat 2; `QUERIES.md` mini Q7; vault `40-decisions-and-trajectories/` question class | Prevents reopening settled choices | **must** for *project-scoped* decisions with handoff/anchor evidence; **defer** full decision-recovery / “paths not taken” (F4 — known corpus gap) |

### F. Meaning-of-code (Graphify-class steal)

| Rank | Question | Source path | Why cold-start | v1 |
|---:|---|---|---|---|
| **15** | Given a **symbol or file** from MyAPI `graphify-out`, what **project narrative** brief should attach (not just AST label)? Path from REBUILD-CONTEXT-ANCHOR / plan docs to MCP naming locks. | `QUERIES.md` mini Q15–16; air Q15 (steal-from-graphify shapes); `GAPS.md` (graphify labels ≠ product narrative); ticket 07 framing | Differentiates Semantic Graphify from AST Graphify | **must thin**: narrative for *project/module* level; **defer** full symbol-level dual graph |

---

## 3. Compact v1 “success set” (what defines done for thin cold-start)

If only **8** questions must pass with honest structured answers, sources converge on:

1. What is this project and its current goal? *(A1 / identity)*  
2. Who owns MyAPI vs MyMCP (and what may be written)? *(ownership)*  
3. What’s the current phase / north star / tip lag? *(now-state)*  
4. What’s broken or blocked right now? *(A7 / danger)*  
5. Where should I begin (index / handoff / anchor paths)? *(entry)*  
6. What was decided that constrains this work? *(decision, project-scoped)*  
7. What evidence backs the above (paths, not vibes)? *(evidence)*  
8. What does this code area *mean* in product terms (module/narrative, not AST)? *(meaning-of-code thin)*  

Human-find-thread queries (H1 “find the thread where…”, F5 exact-phrase) and failure probes (F1–F4 time/negation/cross-entity/paths-not-taken) are **trust-boundary probes**, not cold-start success criteria — already classified that way in anchors and STATUS.

---

## 4. Graphify / semantic failure modes (from GAPS + related)

Called out explicitly so v1 does **not** claim Graphify-out or raw semantic search is enough:

| Failure mode | Source | Implication for cold-start answers |
|---|---|---|
| Graph in PROJECT-BRIEF is a **plan snapshot** (e.g. 2026-06-21), not live system state — agents treat nodes as implemented truth | `GAPS.md` mini | Answers must distinguish plan vs live; stamp date/counts |
| `graphify-out/` labels **functions/files**, not product narrative, MCP contracts, or corpus admission rules | `GAPS.md` air + mini | Meaning-of-code must join narrative/handoffs, not return AST alone |
| **No reindex** / labels lag code/docs | `GAPS.md` mini | Prefer handoffs/anchors over stale graph cache |
| Corpus bulk **volume-skewed** (ChatGPT/Obsidian); semantic without handoff priority re-creates **v0 failure** | `GAPS.md` both; `BRIEF-DRAFT.md` | Handoff/anchor priority over blended RAG |
| Golden briefs / MCP fixtures are **small paths**; full-vault retrieval buries them | `GAPS.md` mini | Source-priority / subject-scope (A7 lesson) |
| **Working tree ≠ main** — blind local index misses goldens/MCP/handoffs | `GAPS.md` air; `BRIEF-DRAFT.md` risks | Branch/tip honesty is a first-class answer field |
| Operator truth is **vault-side** outside git graph | `GAPS.md` air | Sessions/notes substrate required; repo-only Graphify insufficient |
| Cross-repo edges need **path joins**; empty graph query won’t | `GAPS.md` mini | Evidence answers are path bundles, not single-node hits |
| Subject-scope dominates operational candidates (A7); reranker can’t fix missing candidates (F5) | `myapi-status-anchor.md` Failure Modes | Candidate-set + anchors before clever ranking |

---

## 5. Requirements signal → MCP surface (research implications, not decisions)

Observed demand already names tools, shapes, and call patterns. Mapping is **signal only**.

| Demand signal | Likely MCP / API surface agents would call | Notes from sources |
|---|---|---|
| Project identity + goal + phase | `get_project_context` (golden: `get_project_context_myapi_rebuild`) | Corpus-hot + SOURCES; fixture-backed until reader lands |
| Person / operator context | `get_person_context` (golden: `get_person_context_sab`) | Named in QUERIES + SOURCES |
| Broken/blocked / open issues | Operational slice of project context **or** dedicated status tool | A7 designed as status-anchor win, not raw eval notes |
| Evidence paths / handoffs | Brief response must include **paths + confidence**, not only prose | Trust-Threshold: structured confidence; agents hallucinate around bad retrieval |
| Recent work / leave-off | Prefer **handoff / current-state / work-queue** over chat volume | Vault bundle: Index / Current State / Work Queue / Timeline |
| Decision recall | Decision-level episodic object (vault `40-decisions…`) | Prefer authoritative notes over incidental mentions (benchmark Q8) |
| Meaning-of-code | Narrative attach to symbol/file **or** “ask Graphify for AST, MyAPI for why/current/broke” | Ticket 07; QUERIES steal shapes; GAPS |
| Infra/deploy readiness | Status anchors / operational recall (A3) | VM auto-shutdown called out as gotcha |
| Latency / caching | Agent loop wants fast structured answers | Trust-Threshold: human 2–3s OK; agent prefers &lt;500ms (aspiration; README cites &lt;3s live) |
| Empty / weak evidence | Honest no-evidence / weak-evidence contract (ticket 03) | Baseline candidate queries: evidence-absence checks are first-class |

**Not implied as v1 MCP tools:** human “find that ChatGPT export note,” full career episodic synthesis, negation/time-scoped failure probes — those are Category 1/3 trust work, not cold-start elimination.

---

## 6. Adjacent query inventories (harvested, mostly defer)

Kept for completeness so later tickets do not re-mine blindly.

### Trust acceptance set (mechanical)

From `scripts/acceptance.py` (bank file deleted as complexity layer; queries live here):

| ID | Query | Cold-start role |
|---|---|---|
| A1 | What is MyAPI and what is its current goal? | **core** |
| A3 | What is the status of the API deployment? | infra |
| A7 | What’s broken or blocked in MyAPI right now? | **core** |
| H1 | Find the thread where I set up the Khoj VM migration | human-find; defer |
| H4 | Find notes about the gold-mine Q1 fix | exact-term sentinel; defer |
| F5 | Find the note where I used the term "gold mine" | failure probe; defer |
| S1 | claude code session (source filter) | filter contract; defer |

A2 historically tied to end-to-end / system overview (`my-devinfra-system-anchor` win in 2026-04-25 blocker pass); Q18 still open for dedicated anchor.

### Trust-Threshold Category 2 agent examples

`My-API-Trust-Threshold-Plan.md`:

- What's the current state of the Bailey site deployment?  
- What were the recent decisions about cwd-guard?  
- What does our packet schema look like?  
- What's the status of GDDP runtime?  
- Has there been recent work on MyAPI?  

These define **answer-shape** (synthesized answers, not links) more than MyAPI-only content.

### Benchmark v0 (18 queries)

`project-docs/retrieval-benchmark-v0/Query/benchmark-v0.md` — broad human+agent mix (identity, temporal, source-specific, decision, operational, synthesis). Cold-start subset is Q1/A1-class, Q8, Q12, Q18, plus recency (Q2).

### Corpus v1 baseline candidates

`project-docs/corpus-v1-baseline-candidate-queries.md` — intentionally **GDDP-heavy** historical baseline (MyAPI cold-start questions removed as unfair). Useful for multi-project generalization later, not MyAPI v1 success definition.

### Vault folder → question class map

`project-docs/corpus-v1-vault-v1.0-implementation-plan.md`:

| Folder | Primary question class |
|---|---|
| `00-index/` | Where should a cold-start agent begin? |
| `10-current-state/` | What is true, active, blocked, or unresolved right now? |
| `20-projects/` | What is this project and how should an agent orient? |
| `40-decisions-and-trajectories/` | Why did this direction change / alternatives? |
| `50-timeline/` | What happened when? |
| `60-sessions-and-conversations/` | What happened in a specific session? |
| `70-artifacts-and-reference/` | Which durable artifact to load? |

Project bundle split: agent asking “what is MyAPI?” vs “where did we leave off?” must not load the same document — reinforces ranks 4 vs 8–9.

---

## 7. Source index (absolute paths)

| Path | Role in this harvest |
|---|---|
| `/home/saboor/khoj-data/notes/corpus-hot-v1/myapi/QUERIES.md` | Primary agent-shaped question list (mini + air) |
| `/home/saboor/khoj-data/notes/corpus-hot-v1/myapi/GAPS.md` | Graphify/semantic alone failure modes |
| `/home/saboor/khoj-data/notes/corpus-hot-v1/myapi/BRIEF-DRAFT.md` | Short answers + operator cold-start one-liner |
| `/home/saboor/khoj-data/notes/corpus-hot-v1/myapi/SOURCES.md` | Golden briefs, MCP, tip, host lag |
| `/home/saboor/MyAPI/project-docs/My-API-Trust-Threshold-Plan.md` | Agent cold-start product framing + Cat 2 queries |
| `/home/saboor/MyAPI/project-docs/retrieval-benchmark-v0/Query/benchmark-v0.md` | Canonical 18-query bank |
| `/home/saboor/MyAPI/scripts/acceptance.py` | Live A1/A3/A7 (etc.) acceptance queries |
| `/home/saboor/MyAPI/project-docs/source-of-truth-anchors/myapi-status-anchor.md` | A7 cold-start status contract + failure modes |
| `/home/saboor/MyAPI/project-docs/source-of-truth-anchors/my-devinfra-system-anchor.md` | Project identity / system overview |
| `/home/saboor/MyAPI/project-docs/source-of-truth-anchors/khoj-deployment-indexing-anchor.md` | Deploy/status evidence |
| `/home/saboor/MyAPI/project-docs/STATUS_AND_NEXT_STEPS.md` | A/H/F class queue + dual-audience framing |
| `/home/saboor/MyAPI/project-docs/corpus-v1-vault-v1.0-implementation-plan.md` | Folder → question class; project bundle cold-start |
| `/home/saboor/MyAPI/project-docs/corpus-v1-baseline-candidate-queries.md` | Adjacent multi-project queries (defer) |
| `/home/saboor/MyAPI/README.md` | Public cold-start framing + intent classes |
| `/home/saboor/MyAPI/handoffs/003-final-v0-benchmark-run.md` | Note: trust-categorized bank file deleted; acceptance.py remains |
| `/home/saboor/MyAPI/.scratch/semantic-graphify-cold-start/map.md` | Destination / path constraint (context only) |

**Note:** `project-docs/retrieval-benchmark-v0/Query/query-bank-trust-categorized-v1.md` is referenced widely but was **deleted** (handoff 003) as a complexity layer over `benchmark-v0.md`. A/H/F IDs survive in acceptance, anchors, STATUS, and harness run notes.

---

## 8. Research caveats

- This host’s MyAPI tree may lag mini `main` (corpus-hot air harvest; map clone note). Golden briefs / `mcp/` may be absent locally — questions still stand as demand signals.  
- Questions are **mined and lightly project-normalized**; no new product intents invented beyond combining observed phrasings.  
- v1 must/defer is a **research recommendation** for ticket 04+; not a build decision.
