# MyAPI-Rebuild — Architecture

> **Reframe (from Codex, agreed):** This is not "universal data ingestion as a product."
> It is a **personal context engine** where MCP is one interface. The output is a
> **context brief** — human-legible by default, with structured metadata alongside.
> The engine should teach you your own corpus back.

---

## 0. The one-sentence thesis

Given this corpus and this intent, return **what matters, why it matters, what the
evidence is, and what to think about next** — in a shape that serves both an agent
runtime and a human study session.

Everything below is plumbing to produce that shape reliably.

---

## 0.1 Cost posture

MyMCP is the paid doorway into MyAPI, so the public MCP surface stays tiny and
budget-aware. Tool schemas are standing prompt overhead; a large roster of tools
charges every conversation before the first useful retrieval happens. The design
therefore keeps the exposed surface to two tools and moves routing into compact
arguments.

Public tools:

- `get_project_context`
- `get_person_context`

Those tools accept structured arguments instead of spawning more public tools:

```json
{
  "subject": "MyAPI-rebuild",
  "intent": "next_action",
  "budget": "tiny",
  "max_tokens": 1200,
  "include_evidence": false
}
```

The default answer returns a small brief with evidence paths. Excerpts and full
packets are opt-in. Every response reports the requested budget, returned size,
estimated tokens, and freshness metadata.

---

## 1. What already exists (do not rebuild from zero)

| Asset | Location | Status | Reuse decision |
|---|---|---|---|
| PARA corpus | `~/repos/MyAPI/Corpus v1.0/` | 22 buckets, rich frontmatter | **Baseline/reference.** Keep its schema lessons and durable anchors; avoid treating stale volume as current truth. |
| Graphify graph | `graphify-out/graph.json` | 862 nodes, 2186 links, mostly code/rationale | Reuse existing graph; add note/project relationships. |
| Old schemas | `api/schemas.py` | `QueryIntent`, `AnswerMode`, `CanonicalDocument` | **Carry the taxonomy forward.** It is battle-tested. |
| Retrieval pipeline | `context_refinery/retrieval.py` | Khoj client + metadata inference | Concept survives; rewrite thinner. |
| Obsidian export spec | `AGENTS.md` (root) | FSRS-migratable frontmatter | **Hard requirement** — briefs must render to this. |

**Three gaps the rebuild must close:**

1. **Note/project relationships are missing.** `graph.json` already has links, mostly
   from code and rationale extraction. The whole "context brief" promise depends on
   *traversal*, which depends on relationships from the corpus notes too.
2. **The prose corpus is not graphified.** Code + rationale were extracted, but
   `20-projects`, `40-decisions`, `60-sessions` — the actual knowledge — is ungraphed.
3. **No context-brief output type exists.** Old code returned `RetrievedDocument`
   lists. The rebuild returns *briefs*.

---

## 2. The four layers (Codex's frame, made concrete)

```
┌─────────────────────────────────────────────────────────────┐
│  L4  STUDY / EXPORT LAYER   (human)                          │
│       Obsidian Markdown · review cards · recall prompts      │
│       FSRS-migratable frontmatter (see AGENTS.md)            │
├─────────────────────────────────────────────────────────────┤
│  L3  MCP LAYER               (interface)                     │
│       2 tools · budgeted ContextBrief envelopes               │
├─────────────────────────────────────────────────────────────┤
│  L2  CONTEXT-PACK LAYER      (synthesis)                     │
│       graph traversal + retrieval → brief assembly           │
│       intent → which brief template → which sections         │
├─────────────────────────────────────────────────────────────┤
│  L1  GRAPHIFY LAYER          (extraction)                    │
│       entities · relations · evidence · provenance           │
│       code (AST) + prose (LLM) → unified graph               │
├─────────────────────────────────────────────────────────────┤
│  L0  CORPUS                  (source of truth)               │
│       fresh window + durable/canonical promoted anchors       │
└─────────────────────────────────────────────────────────────┘
```

The rebuild moves **bottom-up**: you cannot pack context (L2) without a graph (L1),
and you cannot expose MCP (L3) without packs (L2). L4 falls out of the brief shape.

### 2.1 MyAPI vs MyMCP

| Layer | Responsibility | Cost rule |
|---|---|---|
| MyAPI | Corpus refresh, source manifests, retrieval, freshness checks, cached briefs, evidence policy. | Spend work here because it is offline, cacheable, testable, and inspectable. |
| MyMCP | Two public tool schemas, compact arguments, budgeted return envelopes. | Keep the standing prompt cost tiny; return references first and content only on request. |

MyAPI can keep using the existing Khoj RAG engine on the Google Cloud VM as a
retrieval backend while the rebuild experiments with a radically fresher corpus.
MyMCP should not know whether the answer came from Khoj, local search, cached
briefs, or a future graph traversal. It asks MyAPI for a bounded brief and receives
the smallest useful envelope.

---

## 3. The unified graph model (L1) — the keystone

The current graph has two universes that never met:

- **Code universe** (690 nodes): `api_main_health`, `routers_enrich_enrich_content`…
- **Rationale universe** (152 nodes): design rationale attached to code lines.
- **Prose universe** (ungraphed): projects, decisions, sessions, the *meaning*.

The rebuild's first real job is **one graph with cross-universe edges.**

### 3.1 Node types (unified)

```
Entity        person, project, system, decision, claim, artifact, concept
CodeSymbol    function, class, module, file          (from AST, reuse graphify)
Rationale     design note attached to code           (from AST, reuse graphify)
Document      corpus note                            (from vault frontmatter)
Evidence      a quote + location pointing at a source
```

Every node carries `source_file`, `source_location`, `_origin` (carried from existing
graph), **plus** a `provenance` field: `code-backed` vs `inferred`. This is what makes
the AGENTS.md recall prompt *"Which relationships are code-backed vs inferred?"*
answerable — it must be a first-class field on edges, not a guess.

### 3.2 Edge types (the missing piece)

```
depends_on        A needs B to function          (code-backed: import/call)
depended_by       inverse of depends_on
implements        CodeSymbol implements Decision/Claim
evidences         Evidence supports Claim
derived_from      Document derived_from Document  (already in vault frontmatter!)
mentions          loose co-occurrence             (inferred — mark confidence)
decided_by        Artifact decided_by Decision
part_of           Entity part_of Project/System
```

**Key insight:** `derived_from` already exists in the corpus frontmatter
(see `MyAPI Anchor.md`). Edge extraction for prose is partly *already done* —
the vault authors declared relationships explicitly. Mine those first; LLM-infer the rest.

### 3.3 Confidence + degree + community

These three fields appear in the AGENTS.md export frontmatter:

```yaml
graphify:
  degree:        # how many edges touch this node — centrality
  community:     # Louvain/label-propagation cluster id
  confidence:    # 0.0–1.0 — how trustworthy the node's relationships are
```

- `degree` is free (count edges).
- `community` is a one-shot clustering pass over the graph.
- `confidence` = ratio of `code-backed` edges to total edges. A node with all inferred
  edges is low-confidence; a node wired by imports is high. This is the "God Node"
  detector — high-degree + low-confidence = review candidate.

---

## 4. The Context Brief (L2) — the output contract

This is the single most important design object. **Everything returns one of these.**

### 4.1 Dual representation

```
ContextBrief
├── metadata   (machine-readable, for agent runtime)
│   ├── brief_id, intent, context_type, generated_at
│   ├── anchors: [node ids the brief is about]
│   ├── evidence: [{node_id, source_file, source_location, quote, confidence}]
│   └── graph_slice: {nodes, edges}  ← the subgraph that produced this brief
└── markdown   (human-readable, renders to Obsidian)
    └── see §4.2
```

An agent reads `metadata`. A human reads `markdown`. **Same call, both consumers.**
This is Codex's "not machine-only, not prose-only, both" principle made literal.

### 4.2 Markdown brief template

```markdown
# Context Brief: <subject>

## Short Answer
<2–4 sentences. The answer an agent could act on directly.>

## Why This Matters
<why a reader should care, tied to intent>

## Key Relationships
- <node> →<edge type>→ <node>   (code-backed | inferred, conf 0.8)

## Evidence
- [<quote>] — `source_file:L##` (confidence 0.9)

## Open Risks / Unknowns
<what the graph does not know, low-confidence nodes, missing edges>

## Useful Next Questions
<suggested follow-up tool calls or study directions>
```

The **Open Risks** section is what makes this honest: it surfaces *what the engine
does not know*, which is where the study layer earns its keep.

### 4.3 Intent → brief template mapping

Carry the old taxonomy forward (it is proven):

| `intent` (from old schemas) | Brief emphasis | Sections prioritized |
|---|---|---|
| `project_overview` | What is this, what's the state | Short Answer, Relationships, Risks |
| `decision` | Why was X chosen | Evidence, derived_from chain |
| `operational` | How do I do X | Short Answer, step artifacts |
| `cross_source` | What do A and B share | Relationships, Evidence (multi) |
| `synthesis` | Pattern across corpus | Relationships, Next Questions |
| `temporal` | How did this evolve | Evidence (time-ordered) |
---

## 5. The two MCP tools (L3)

The MCP surface is intentionally smaller than the internal capability set. Public
tool count is a cost decision, not just an API-design decision.

### 5.1 Tool roster

| # | Tool | Required inputs | Optional inputs | Returns | Why it exists |
|---|---|---|---|---|---|
| 1 | `get_project_context` | `project` | `intent`, `budget`, `max_tokens`, `include_evidence` | Budgeted `ContextBrief` envelope | The first vertical slice and default project-continuity call. |
| 2 | `get_person_context` | `subject` | `intent`, `budget`, `max_tokens`, `include_evidence` | Budgeted `ContextBrief` envelope | The user/operator continuity call. Name stays `person`, not a second `user`/`operator` fork. |

### 5.2 Argument-driven routing

Fine-grained behavior belongs in arguments, not a large public tool roster.

| Argument | Values | Effect |
|---|---|---|
| `intent` | `status`, `next_action`, `handoff`, `architecture`, `verification`, `history` | Selects the internal route and brief template. |
| `budget` | `tiny`, `normal`, `deep` | Chooses evidence depth, excerpt policy, and compression target. |
| `max_tokens` | integer | Hard cap for returned content. The response may stop early with a partial-but-valid envelope. |
| `include_evidence` | boolean | `false` returns evidence paths; `true` includes bounded excerpts. |

Internal routes can still exist for claim evidence, review queues, source freshness,
or study cards. They live behind MyAPI where they can be versioned, tested, cached,
and called by scripts without increasing MCP prompt overhead.

### 5.3 Budgeted return envelope

```json
{
  "answer": "...",
  "evidence_paths": ["..."],
  "freshness": {
    "generated_at": "2026-07-02T00:00:00Z",
    "source_manifest_hash": "..."
  },
  "budget": {
    "requested": "tiny",
    "returned_chars": 3200,
    "estimated_tokens": 800,
    "max_tokens": 1200
  },
  "expand_with": {
    "same_tool_args": {
      "budget": "deep",
      "include_evidence": true
    }
  }
}
```

The default path is references-first: short answer, state, next action, evidence
paths, and freshness. Full packets are for handoff, planning, evals, and agent
bootstrapping.

---

## 5.4 Fresh corpus policy

MyAPI v0 proved that a large cold corpus can drown the active truth. The rebuild
uses a fresh active window by default:

- Include current live sources and daily refreshes from the active vault, agent
  sessions, repo docs, `.pi` traces, and handoffs.
- Prefer a 15–30 day active window for ordinary retrieval.
- Promote durable/canonical items out of the expiry window with an explicit stamp.
- Treat Corpus v1.0 as baseline, evaluation substrate, and cold reference material.
- Cache compiled briefs and invalidate them when the source manifest changes.

Khoj on the Google Cloud VM can remain a retrievable backend with embeddings. The
new corpus policy changes what MyAPI feeds and trusts by default: fresh, lean,
promoted when durable, and visibly stale when old.

---

## 6. The study / export layer (L4) — wiring to AGENTS.md

The root `AGENTS.md` already specifies the exact frontmatter and body shape for
review cards. The rebuild's job is to **generate those cards from graph nodes**,
not build a separate flashcard app.

### 6.1 Card generation rule

A review card = a graph node rendered through the AGENTS.md template. Specifically:

- `graphify_id` ← node `id`
- `source_file`, `source_location` ← node provenance
- `graphify.degree` ← edge count
- `graphify.community` ← cluster id
- `graphify.confidence` ← code-backed edge ratio
- `review.state` ← from the internal study/review scheduler (simple-v1)
- Body `## Incoming Links` / `## Outgoing Links` ← the node's edges (finally useful
  now that edges exist)

**The recall prompt is auto-generated from the node's role:**
a `Decision` node asks "What would break if this changed?"; a `CodeSymbol` node asks
"What depends on it?". This is the AGENTS.md spec made algorithmic.

### 6.2 Scheduler: simple-v1 (per constraints)

```
due       = last_reviewed + interval
interval  = base (1d) × 2^reps, capped, reset on lapse
```

Deliberately dumb. The frontmatter is FSRS-shaped so a future migration swaps the
scheduler function without touching storage. **Do not implement FSRS now** — the
constraint is explicit and correct.

### 6.3 God Node Review mode

The internal review route returns high-degree + low-confidence nodes. This is the
batch queue. Single-card review can use either public context tool with
`intent: "verification"` or `intent: "next_action"` depending on the subject.

---

## 7. Repository layout (proposed)

Mirrors the scaffold that already exists, with the layers made explicit:

```
MyAPI-rebuild/
├── AGENTS.md                  # exists — study/export spec (the L4 contract)
├── ARCHITECTURE.md            # this file
├── ingest/                    # L0→L1: vault → unified graph
│   ├── vault_reader.py        #   walk Corpus v1.0, parse frontmatter
│   ├── code_graphifier.py     #   AST extraction (port from old graphify)
│   ├── prose_graphifier.py    #   LLM extraction for notes/decisions/sessions
│   └── edge_miner.py          #   derived_from, mentions, implements
├── rag-pipeline/
│   ├── graph/                 # L1 store: nodes + edges + community
│   │   ├── store.py           #   load/save graph.json (now WITH edges)
│   │   └── community.py       #   degree/community/confidence computation
│   ├── retrieval/             # L2a: hybrid retrieval
│   │   ├── traverse.py        #   graph walk from anchors (the new core)
│   │   ├── vector.py          #   embedding search (replace Khoj dependency?)
│   │   └── rank.py            #   fuse graph + vector scores
│   └── packs/                 # L2b: brief assembly
│       ├── brief.py           #   ContextBrief model + dual repr
│       └── templates.py       #   intent → section mapping (§4.3)
├── mcp/                       # L3: the 2 public tools
│   ├── server.py              #   MCP server entry
│   └── tools/
│       ├── get_project_context.py
│       └── get_person_context.py
├── export/                    # L4: Obsidian rendering + scheduler
│   ├── obsidian_card.py       #   node → AGENTS.md template
│   └── scheduler.py           #   simple-v1, FSRS-migratable
└── evals/                     # query suite defines the quality bar
    └── golden_briefs/         #   expected briefs for known queries
```

---

## 8. Build order — the critical path

The dependency is strictly bottom-up. Do not skip ahead; each layer blocks the next.

```
Step 1  L0→L1  vault_reader + code_graphifier port
        └─ get graph.json back to current node count (862) in the new schema
Step 2  L1     edge_miner: mine derived_from from frontmatter (free wins first)
        └─ this alone produces real edges without any LLM cost
Step 3  L1     prose_graphifier: graphify 20-projects, 40-decisions, 60-sessions
        └─ now the graph has meaning, not just code shape
Step 4  L1     community.py: degree + community + confidence
        └─ God Nodes become visible; review queue becomes possible
Step 5  L2     brief.py + templates.py: the ContextBrief contract
        └─ this is the make-or-break artifact; evals anchor here
Step 6  L2     traverse.py + rank.py: graph walk fuses with vector search
        └─ hybrid retrieval lives; briefs stop being empty
Step 7  L3     get_project_context FIRST (the vertical slice)
        └─ demoable, testable, exercises the whole stack
Step 8  L3     get_person_context with the same budgeted envelope
        └─ user/operator continuity without a second public naming fork
Step 9  L4     obsidian_card + scheduler (simple-v1)
        └─ the study loop closes; AGENTS.md spec satisfied
Step 10 evals  golden briefs + a quality gate
        └─ "benchmark-driven quality, not vibes" — carried from old principles
```

**The portfolio vertical slice is Steps 1–7.** Steps 8–10 round it out. Anything
beyond that (FSRS, LinkedIn/WhatsApp corpora, person/thread tools) is explicitly
deferred per the constraints.

---

## 9. Decisions to confirm before coding

1. **Vector store:** Use Khoj on the Google Cloud VM as the established retrieval
   backend, with a local fallback later if demo independence becomes important.
   *Lean: reuse Khoj while making the corpus fresher and smaller.*
2. **Prose graphifier model:** Gemini (you have a key) vs local. *Lean: Gemini for
   extraction quality, cache aggressively, mark all such edges `inferred`.*
3. **Graph store format:** Single `graph.json` (current) vs sqlite. *Lean: sqlite
   once node count grows past prose graphification; json until then for diffability.*
4. **MCP runtime:** Python MCP SDK (matches existing stack) vs TypeScript.
   *Lean: Python — the old pipeline, schemas, and your muscle memory are all Python.*

---

## 10. What this is NOT (guardrails, from AGENTS.md + your instincts)

- Not a generic flashcard app. Cards come from graph nodes only.
- Not full spaced repetition. simple-v1 only; FSRS-shaped but unimplemented.
- Not universal ingestion. The active corpus is fresh by default; older material
  earns durable/canonical status before it shapes ordinary answers.
- Not agent-plumbing-only. Every tool returns a human-legible brief.
- Not metadata inspection. Clicking a node invites active recall, not a properties panel.
