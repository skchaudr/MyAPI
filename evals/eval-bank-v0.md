# eval-bank-v0 (DRAFT — Sab edits before freeze)

Status: **draft**  
Purpose: score wave1 / MyAPI generations without optimizing the wrong thing  
Location: mini `scratch/corpus-hot-v1/eval-bank-v0.md` (copy to VM pack when frozen)

## Rules (do not skip)

1. Every row needs **gold** (path and/or fact) **or** `OOD`.
2. Prefer questions agents already asked (graphify history) or pass-1 QUERIES shapes.
3. **Surface** says where a correct system should get the answer:
   - `brief` = wave1 pack / MyAPI narrative (indexed on :42111 today)
   - `graphify` = live or day-old graphify-out (NOT in wave1 Khoj yet)
   - `both` = narrative + code-connect
   - `env` = person/operator/topology (pack or live env — mark gold carefully)
4. HIT for retrieval smoke: gold path (or filename stem) appears in top-k **or** answer states the gold fact with cite.
5. Do **not** count “any corpus-hot-v1 filename” as enough once this bank freezes — must match **that row’s gold**.
6. Sab cuts anything soft. Target after edit: **20–28 live rows**.

## Column legend

| Col | Meaning |
|-----|---------|
| id | stable id |
| project | myapi / gddp / pi-needle-gemma / cross |
| family | own / orient / now / contract / connect / person-env |
| surface | brief / graphify / both / env |
| q | question text |
| gold | path(s) and/or required fact |
| source | where the Q came from |
| status | draft / keep / kill / needs-graphify-refresh |

---

## A. From real graphify / agent history (seed truth)

| id | project | family | surface | q | gold | source | status |
|----|---------|--------|---------|---|------|--------|--------|
| H01 | gddp | own | brief | *What is the purpose of gddp-config compared to gddp-runtime?* | Fact: config owns graph/schemas/acceptance; runtime owns jobs/queue/evidence/loop. Paths: wave1 `corpus-hot-v1-gddp-BRIEF-DRAFT.md`, `…-gddp-SOURCES.md` (and/or repo PROJECT-BRIEF/AGENTS when promoted) | zsh `graphify query` history | draft |
| H02 | gddp | own | brief | What does this repo own vs what runtime owns? | Same ownership split as H01; must not say runtime writes node YAML | zsh graphify history | draft |
| H03 | gddp | orient | brief | What is gddp-runtime? | Short identity: operating loop / dispatch / evidence / evaluators; not graph authorship. Gold file: `…-gddp-BRIEF-DRAFT.md` | zsh `graphify query "what is gddp-runtime"` | draft |
| H04 | gddp | now | both | What does the local executor do as of right now to trigger the evaluator? | Gold fact from pack or runtime docs: executor completes work → evidence/git → human/evaluator path — **not** “executor directly calls evaluator” unless docs say so. Prefer handoff/BRIEF; mark **needs-graphify-refresh** for code path | zsh multi-turn graphify queries | draft |
| H05 | gddp | contract | both | What exact intent, criteria, implementation surfaces, and evidence establish neutral-executor-contract Node 1 (incl. handoffs 047/048/050 and branch tips)? | Gold: handoff IDs + node intent/criteria paths under gddp-config/MyAPI as cited in harvest; **partial until graphify+handoffs in pack** | zsh required graphify pre-gate | draft |

---

## B. MyAPI (from pass-1 QUERIES + product canon)

| id | project | family | surface | q | gold | source | status |
|----|---------|--------|---------|---|------|--------|--------|
| M01 | myapi | own | brief | Who owns the context engine vs the doorway — MyAPI vs MyMCP? | Fact: MyAPI = engine; MyMCP = lean doorway. File: `corpus-hot-v1-myapi-BRIEF-DRAFT.md` | mini QUERIES | draft |
| M02 | myapi | own | brief | Is MyMCP a separate product or a thin paid doorway into MyAPI? | Same as M01 / PROJECT-BRIEF framing in BRIEF-DRAFT | air QUERIES | draft |
| M03 | myapi | orient | brief | What is MyAPI-rebuild’s north star in one short answer? | Durable handoffs + two MCP tools / context briefs — not single RAG pool. `…-myapi-BRIEF-DRAFT.md` | BRIEF + PROJECT-BRIEF via harvest | draft |
| M04 | myapi | contract | brief | What are the two MCP tools and what intents do they encode? | `get_project_context`, `get_person_context`. Files: BRIEF-DRAFT, QUERIES, (goldens named in SOURCES) | QUERIES + prior smoke | draft |
| M05 | myapi | evidence | brief | What evidence paths prove the two MCP tools / golden briefs? | Must cite golden brief names or `evals/golden_briefs/…` as listed in `…-myapi-SOURCES.md` | mini QUERIES | draft |
| M06 | myapi | evidence | brief | Which handoff documents the GDDP first durable handoff node for MyAPI? | `.handoffs/029-…` / prove-first-durable-handoff named in SOURCES/BRIEF | mini QUERIES | draft |
| M07 | myapi | connect | brief | How does L0 corpus → L1 graphify → L2 packs → L3 MCP chain? | Layers named in IMPLEMENTATION-PLAN framing inside BRIEF/SOURCES | mini QUERIES | draft |
| M08 | myapi | connect | brief | How does Corpus v1.0 failure mode force handoff-first redesign? | ChatGPT volume / CLI sessions not surfaced — in BRIEF GAPS/SOURCES | mini QUERIES | draft |
| M09 | myapi | connect | graphify | Path from a MyAPI code symbol in graphify-out to the project narrative (not just AST label)? | **OOD for wave1 Khoj until graphify artifacts in pack**; gold later: graphify report + BRIEF | air QUERIES steal-shape | draft |
| M10 | myapi | now | brief | What is the active corpus policy (hot window vs Corpus v1.0 cold)? | Hot short window + durable handoffs; v1.0 cold — as stated in BRIEF/SOURCES | mini QUERIES | draft |

---

## C. GDDP (ownership is non-negotiable)

| id | project | family | surface | q | gold | source | status |
|----|---------|--------|---------|---|------|--------|--------|
| G01 | gddp | own | brief | What does gddp-config own that gddp-runtime must only read? | graphs/, schemas, acceptance criteria; runtime must not invent graph truth. `…-gddp-BRIEF-DRAFT.md` / SOURCES | mini+air QUERIES | draft |
| G02 | gddp | own | brief | What does gddp-runtime own that must never rewrite node YAML / graph status? | jobs, queue, evidence, evaluator loop; human acceptance advances graph. BRIEF | mini QUERIES | draft |
| G03 | gddp | own | brief | Who may mutate graph truth after a successful agent run? | Human acceptance only | air QUERIES / PROJECT-BRIEF | draft |
| G04 | gddp | now | brief | What is the four-way truth split (canon / graph / evidence / human acceptance)? | Named four-way model in BRIEF/SOURCES | mini QUERIES | draft |
| G05 | gddp | evidence | brief | Which handoff documents multi-project heartbeat / dispatch hardening on runtime? | handoff `060-…` named in SOURCES | mini SOURCES | draft |
| G06 | gddp | evidence | brief | What schemas define Node vs Job vs Result vs Event? | `gddp-config/schemas/v1/` cited in SOURCES | mini QUERIES | draft |
| G07 | gddp | connect | brief | How does a human-marked ready node become a job then awaiting_review without graph writeback? | Loop described in BRIEF; no silent graph writeback | mini QUERIES | draft |
| G08 | gddp | connect | graphify | What community hubs does GRAPH_REPORT list for gddp-runtime? | **needs-graphify-refresh**; gold = GRAPH_REPORT.md after refresh | mini QUERIES graphify-class | draft |
| G09 | gddp | now | env | Where is production control plane (host, intake, queue) documented? | TOPOLOGY / BRIEF “prod on mini” — `…-gddp-BRIEF-DRAFT.md` or SOURCES TOPOLOGY path | air QUERIES | draft |

---

## D. Pi / Needle / Gemma

| id | project | family | surface | q | gold | source | status |
|----|---------|--------|---------|---|------|--------|--------|
| P01 | pi-needle-gemma | own | brief | What does Needle own vs Pi agent vs harness? | Needle route/serve; agent; harness — split in BRIEF/SOURCES | air+mini QUERIES | draft |
| P02 | pi-needle-gemma | own | brief | Where do model provider settings live vs weights/checkpoints? | models.json / settings vs checkpoints path-only; never ingest weights. BRIEF + DENYLIST | mini QUERIES | draft |
| P03 | pi-needle-gemma | now | brief | What are the five verbs in tools.json? | edit_file, run_shell, search_code, read_file, delegate (as in SOURCES/BRIEF) | mini QUERIES | draft |
| P04 | pi-needle-gemma | now | brief | Is Needle observe-only or active until eval gates clear? | observe-only / prefer Mac routing — as stated in harvest | mini QUERIES | draft |
| P05 | pi-needle-gemma | evidence | brief | What must never be ingested from ~/.pi into Khoj/corpus? | auth, weights, full sessions, quarantine, etc. `corpus-hot-v1-DENYLIST.md` + GAPS | air QUERIES + DENYLIST | draft |
| P06 | pi-needle-gemma | evidence | brief | Where is the Camber / needle-gemma execution ledger or approval gate described? | ledger path in SOURCES (`needle-gemma-v1-execution-ledger` or equiv) | air QUERIES | draft |
| P07 | pi-needle-gemma | connect | brief | How should get_project_context_pi_needle attach to these paths? | golden brief name + pi paths in SOURCES | air QUERIES | draft |
| P08 | pi-needle-gemma | connect | graphify | Path tools.json → router.route → shadow/eval before promotion? | **needs-graphify-refresh** on ~/.pi/needle | mini QUERIES | draft |

---

## E. Person / environment (second tool surface)

| id | project | family | surface | q | gold | source | status |
|----|---------|--------|---------|---|------|--------|--------|
| E01 | cross | person-env | brief | Who is Sab in the sense of get_person_context (operator continuity, not LinkedIn dump)? | Person-brief framing in myapi BRIEF / person golden named in SOURCES | golden get_person_context_sab | draft |
| E02 | cross | person-env | env | Where does GDDP production control plane run (which machine)? | sab-mini / TOPOLOGY — pack BRIEF says mini-primary | topology + gddp harvest | draft |
| E03 | cross | person-env | brief | For agent retrieval, which Khoj backend is the lean snapshot vs full archive? | wave1 :42111 vs archive :42110 — **only gold if this fact is in pack or ops note**; else add to pack before scoring | ops (khoj-backend) — may need pack line | draft |

---

## Freeze checklist (Sab)

- [ ] Kill any row that is soft, double, or un-goldable
- [ ] Confirm five-verb list and ownership one-liners against live files once
- [ ] Tag final **keep** set (aim 20–28)
- [ ] Split scoring: `brief` rows → :42111 now; `graphify` rows → after graphify refresh lands in generation
- [ ] Copy frozen bank to VM `/data/corpus-hot/v1/eval-bank-v0.md` and changelog it

## Explicitly NOT in v0

- “Does search return something?” without gold
- Full Corpus v1.0 trivia
- Weight/checkpoint contents
- Secret/env values

---

## Suggested first cut if impatient

**Must-keep candidates:** H01–H03, M01, M03, M04, M08, G01–G04, P01, P03, P05, E01–E02  

**Park until graphify refresh:** H04–H05, M09, G08, P08  

**Park until pack mentions khoj-backend:** E03
