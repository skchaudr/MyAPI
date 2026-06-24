# MyAPI-rebuild — Implementation Plan

Sequel to [`PROJECT-BRIEF.md`](PROJECT-BRIEF.md). Direction + ground state live
there. This is an implementation scaffold, not a complete execution plan: it
sequences the work into phases a lesser model can decompose into
native units — **Python module** (context_refinery / ingest / MCP) · **eval suite**
(golden briefs + benchmarks) · **docs commit** (handoffs + traces). **Link, don't
restate:** the architecture (4 layers L0–L4, 10-step build order), context anchor
(paradigm + glossary + integrated plan), and event trace template already exist.
This overlay adds phase shape, DoD, and risk.

## Canonical direction

Update corpus v1.0 into corpus v2.0. Get the necessary data aggregated so that two
MCP tool calls can be made to that data (`get_project_context`, `get_person_context`).
**Lots of build, some understand, audit is a continual process.**

The loop is: determine what goes into the corpus → get it raw → normalize → test.
Then: normalize → test → normalize → test → run benchmarks → run on live agents.
Test on agents who think they're making real MCP calls before wiring. Test what
agents actually look for. Build → audit → understand, in any order, continuously.

## Mental model (how the pieces fit)

MyAPI-rebuild is a 4-layer stack built bottom-up:

```
L4  Study/Export   — human review cards from graph nodes (FSRS-shaped, not FSRS)
L3  MCP Surface   — 2 tools: get_project_context, get_person_context
L2  Context Packs — graph traversal + retrieval → context brief assembly
L1  Graphify      — entities, relations, evidence, provenance → unified graph
L0  Corpus        — Obsidian vault, PARA-structured, frontmatter-typed
```

You can't pack context (L2) without a graph (L1). You can't expose MCP (L3) without
briefs (L2). The portfolio vertical slice is L0 → L1 → L2 → L3: corpus → graph →
brief → MCP tool. L4 falls out of the brief shape. The architecture doc
(`ARCHITECTURE.md`) has the 10-step build order — this plan sequences it into
phases with build/audit/understand dimensions.

## Source docs (read before decomposing any phase)
- Direction + paradigm: [`PROJECT-BRIEF.md`](PROJECT-BRIEF.md)
- Context anchor (read first in cold session): [`project-documents/REBUILD-CONTEXT-ANCHOR.md`](project-documents/REBUILD-CONTEXT-ANCHOR.md)
- Architecture (4 layers, 10-step build, graph model, MCP tools, brief contract): [`project-documents/ARCHITECTURE.md`](project-documents/ARCHITECTURE.md)
- Handoffs: [`.handoffs/012-rebuild-narrative-recapture.md`](.handoffs/012-rebuild-narrative-recapture.md)
- Old substrate: [`../MyAPI/Corpus v1.0/`](../MyAPI/) (22 PARA buckets), `../MyAPI/graphify-out/graph.json` (862 nodes, 2186 links)

## Phase summary
| # | Phase | Build | Audit | Understand | Native unit |
|---|---|---|---|---|---|
| 1 | Corpus v2.0: determine + raw | scope what goes in, extract raw | scope review, raw completeness check | learn the corpus landscape | docs + raw extraction |
| 2 | Corpus v2.0: normalize | vault reader, frontmatter parser, handoff shaper | normalize tests (schema validation, provenance check) | learn the normalization surface | Python modules |
| 3 | Graph: unify + edges | code graphifier port, edge miner, prose graphifier | graph schema tests, node/edge counts, confidence distribution | learn the unified graph shape | Python modules |
| 4 | Briefs: the output contract | ContextBrief model, template engine, brief assembly | golden briefs (expected output for known inputs), brief quality tests | learn what a good brief looks like | Python modules + eval suite |
| 5 | MCP: the two tools | get_project_context, get_person_context MCP server | MCP integration tests, tool-call contract tests | learn the agent-facing surface | MCP server |
| 6 | Live agent testing | wire MCP to live agents, run on real sessions | agent usage tests (do agents actually use it? what do they ask?), benchmark runs | learn what agents need | integration tests + benchmarks |

## Phases
Each phase carries all 3 dimensions: **build** (expansion/actualization), **audit**
(build + run testing infrastructure), **understand** (docs, learning artifacts,
competence demonstration).

### Phase 1 — Corpus v2.0: determine what goes in + get it raw
- **Scope:** determine what data goes into the new corpus. Walk `Corpus v1.0/` (22 PARA buckets), inventory what's there, what's stale, what's missing. Extract raw material into the v2.0 structure. The goal: a raw corpus that can be normalized — not a final product.
- **Build:** scope document (what goes in, what's excluded, why); raw extraction scripts (walk v1.0, pull into v2.0 directory structure); event trace template instances (the first durable handoffs — the MyAPI v0 derail trace and the rebuild-night Codex derail trace per the context anchor's integrated plan).
- **Audit:** completeness check — does the raw corpus cover the intended scope? Are there gaps (missing project contexts, missing person data)? Schema validation on raw frontmatter (PARA structure, required fields). The completeness check is a test script that runs against the raw corpus and reports gaps.
- **Understand:** scoping teaches the corpus landscape — what v1.0 has (579 CLI sessions ingested but never surfaced, ChatGPT exports dominating by volume, no presentable narratives), what's missing, what the v2.0 shape needs to be. The event traces teach the handoff format by doing it — writing the first two traces teaches what a durable handoff looks like.
- **DoD:** raw corpus in v2.0 directory structure; completeness check script built and run; 2 event traces written; scope document committed.
- **Dependency:** none (first).
- **Risk:** v1.0 has 22 buckets — inventory is manual work. Don't try to normalize in this phase — raw extraction only.
- **Native unit:** raw extraction scripts + event traces + completeness check script + scope doc.

### Phase 2 — Corpus v2.0: normalize
- **Scope:** normalize the raw corpus into the handoff vault shape. Build the vault reader and frontmatter parser. The vault reader walks the normalized corpus, parses frontmatter, and produces structured records. The handoff shaper transforms raw notes into event traces (the handoff shape from the context anchor).
- **Build:** `vault_reader.py` (walk vault, parse frontmatter, produce records); `frontmatter_schema.py` (validation rules for PARA structure + custom fields); handoff shaper (raw note → event trace template). These are the L0→L1 pipeline's input stage.
- **Audit:** schema validation tests (frontmatter has required fields, types are correct, provenance is present); normalization regression tests (normalize a known raw note, assert output matches expected structure); vault walk test (walk the full corpus, assert zero parse errors).
- **Understand:** normalization teaches the data quality surface — what frontmatter is clean, what's inconsistent, what needs manual intervention. The vault reader teaches the corpus's actual structure vs the assumed structure.
- **DoD:** vault reader walks full corpus without errors; schema tests pass; handoff shaper produces valid event traces from raw notes.
- **Dependency:** Phase 1 (raw corpus exists).
- **Native unit:** Python modules (vault_reader, frontmatter_schema, handoff_shaper) + test suite.

### Phase 3 — Graph: unify + edges
- **Scope:** build the unified graph (L1). Port the code graphifier from old graphify (AST extraction → CodeSymbol + Rationale nodes). Build the edge miner (extract `derived_from` from frontmatter — free wins first, no LLM cost). Build the prose graphifier (LLM extraction for projects, decisions, sessions — the meaning layer that v1.0 never had). Compute degree + community + confidence.
- **Build:** `code_graphifier.py` (AST extraction, reuse existing graphify logic); `edge_miner.py` (derived_from from frontmatter, mentions, implements); `prose_graphifier.py` (LLM extraction for prose notes → Entity + Document nodes); `community.py` (degree + community + confidence computation). The unified graph merges code universe (690 nodes), rationale universe (152 nodes), and the new prose universe.
- **Audit:** graph schema tests (node types valid, edge types valid, provenance field present on every node); node count regression (≥862 from code graph alone after port); edge count regression (≥2186 from existing graph); confidence distribution report (how many nodes are high-confidence vs inferred); God Node detector (high-degree + low-confidence = review candidate).
- **Understand:** the unified graph teaches the cross-universe connections — what code relates to what decisions, what projects share what artifacts. The confidence distribution teaches where the graph is solid (code-backed imports) and where it's speculative (LLM-inferred relationships). God Nodes teach the review targets.
- **DoD:** unified graph with all three universes; edge miner extracts derived_from from frontmatter; prose graphifier produces Entity + Document nodes for projects/decisions/sessions; community.py computes degree + community + confidence; all tests pass.
- **Dependency:** Phase 2 (normalized corpus as input for prose graphifier).
- **Native unit:** Python modules (code_graphifier, edge_miner, prose_graphifier, community) + test suite + confidence report.

### Phase 4 — Briefs: the output contract
- **Scope:** build the ContextBrief model — the single most important design object (ARCHITECTURE.md §4). Dual representation (machine-readable metadata + human-readable markdown). Intent → template mapping. Brief assembly from graph traversal.
- **Build:** `ContextBrief` model (metadata + markdown, dual repr); template engine (intent → section mapping per ARCHITECTURE.md §4.3); `brief.py` (graph traversal → brief assembly); `templates.py` (Short Answer, Why This Matters, Key Relationships, Evidence, Open Risks, Next Questions per intent type).
- **Audit:** golden briefs — write expected briefs for 3-5 known inputs (a project overview, a decision, a cross-source query). Build a brief quality eval suite that compares generated briefs against goldens (not string match — structural: does the brief have all sections? does it cite evidence? does it surface open risks?). Brief regression tests (same input always produces structurally valid output).
- **Understand:** writing golden briefs teaches what a good brief looks like — the right level of detail, the right evidence density, the right risk surfacing. The eval suite teaches the quality bar — what's acceptable vs what needs work.
- **DoD:** ContextBrief model with dual repr; template engine maps all 6 intents; 3-5 golden briefs written; eval suite passes on goldens.
- **Dependency:** Phase 3 (graph with edges + confidence needed for traversal).
- **Native unit:** Python modules (brief, templates) + golden briefs + eval suite.

### Phase 5 — MCP: the two tools
- **Scope:** build the MCP server with `get_project_context` and `get_person_context`. These are the two tools the canonical direction calls for. Build them as the vertical slice that exercises the full stack: L0 (corpus) → L1 (graph) → L2 (brief) → L3 (MCP).
- **Build:** MCP server (`mcp/server.py`); `get_project_context` tool (query → brief assembly → ContextBrief return); `get_person_context` tool (same stack, person context). Python MCP SDK (matches existing stack per ARCHITECTURE.md decision).
- **Audit:** MCP integration tests — call `get_project_context` with a known project, assert brief structure matches golden; call `get_person_context`, assert person data surfaces correctly. Tool-call contract tests — verify input validation, error handling, empty-result behavior. Build a mock MCP client that simulates an agent making tool calls.
- **Understand:** the MCP tools teach the agent-facing surface — what an agent sees when it calls these tools, whether the output is actionable, whether the brief shape serves both agent runtime and human reading. The mock client teaches what a real agent experience would be.
- **DoD:** MCP server starts; both tools return valid ContextBriefs; integration tests pass; mock client works.
- **Dependency:** Phase 4 (ContextBrief model + brief assembly).
- **Native unit:** MCP server + 2 tool implementations + mock client + integration tests.

### Phase 6 — Live agent testing
- **Scope:** wire the MCP server to live agents. Run it on real coding sessions. Test on agents who think they're making real MCP calls (before full wiring — simulate the tool-call path). Test what agents actually look for — do they reach for `get_project_context`? What do they ask? What's missing from the responses? Run benchmarks (latency, accuracy, coverage). This is the continual audit loop: normalize → test → normalize → test.
- **Build:** live agent integration (wire MCP server to a test agent session); benchmark harness (latency, brief accuracy, coverage metrics); agent behavior logger (what queries agents make, what they do with the responses).
- **Audit:** live agent tests — run agents on real sessions with MCP wired, log their queries, evaluate whether the briefs were useful. Benchmark runs — latency budget met? brief accuracy matches golden quality? coverage (did the corpus have answers for what agents asked?). Agent adoption test — do agents actually call `get_project_context` / `get_person_context` without being forced?
- **Understand:** live testing teaches what agents actually need from a context engine — not what we assume they need. The behavior log teaches the query patterns, the failure modes, the gaps in the corpus. The benchmark teaches the performance baseline. This is the operator getting first-hand exposure to the domain problem: "I built a context engine — here's what agents actually do with it."
- **DoD:** MCP wired to live agent; benchmark harness built and run; behavior log analyzed; adoption confirmed (agents use the tools without prompting); coverage gaps documented.
- **Dependency:** Phase 5 (MCP tools working).
- **Risk:** agents may not use the tools if the briefs aren't useful — that's valid feedback, not a bug. Document it and iterate.
- **Native unit:** integration wiring + benchmark harness + behavior logger + analysis.

## Execution + commit policy
- Order: 1 → 2 → 3 → 4 → 5 → 6. Bottom-up (L0 → L1 → L2 → L3). Phase 6 is the continual audit loop — it can run in parallel with earlier phases' later work (e.g., normalizing more corpus while testing MCP tools).
- Branch: this scaffold is now on `main`; `rebuild` is historical. New phase
  work should branch from `main` unless Sab chooses otherwise. **No push** until
  Sab signs off.
- Audit is a continual process — every phase builds test infrastructure, every phase runs it. The eval suite grows with each phase.
- Two MCP tools: `get_project_context` + `get_person_context`. The anchor locks these names. Do not fork.
- Before each phase, classify inherited local state. Preserve unknown edits as
  context evidence unless they are proven generated noise; do not normalize a
  clean worktree by discarding unclassified work.

## Open (Sab decides)
- **Corpus v2.0 scope:** what exactly goes in? All 22 v1.0 buckets, or a subset? Which projects, which decisions, which sessions are the priority?
- **Prose graphifier model:** Gemini (external, extraction quality) or local (self-contained)? ARCHITECTURE.md leans Gemini. Confirm.
- **Vector store:** local (sqlite-vss / lancedb) or keep Khoj dependency? ARCHITECTURE.md leans local. Confirm.
- **`get_person_context` data source:** Obsidian-primary (projects, decisions, preferences) per context anchor — no LinkedIn/WhatsApp dependency. Confirm scope.
- **Event traces:** Sab writes the first two (MyAPI v0 derail + rebuild-night Codex derail) per context anchor's integrated plan. When?
- **Live agent selection:** which agents to test against? Pi? Claude? Both?
