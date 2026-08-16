# MyAPI-rebuild — Decision Graph Implementation Plan

Status: active

Accepted direction: 2026-08-10

Canonical design input: [`docs/decision-object-is-born-8.10.26.md`](docs/decision-object-is-born-8.10.26.md)

## Outcome

MyAPI becomes a continuously maintained semantic provenance graph for software
projects. Its canonical unit is the **Decision**: a current or historical statement
of intent linked to rationale, evidence, commits, code, and the Decisions it
supersedes or refines.

The MVP proves one hypothesis:

> Given a natural cold-start question about MyAPI-rebuild, can MyAPI return the
> current Decision, rationale, evidence, implementation history, and code location
> with enough trust that an agent can continue without repository archaeology?

MyAPI-rebuild is the first subject corpus. The system dogfoods its own project
history before another project enters the evaluation gate.

## Execution boundary

- All implementation work lands in `MyAPI-rebuild`.
- Execution begins directly in this repository; GDDP orchestration can adopt the
  graph later.
- The initial evidence set is limited to recent MyAPI agent sessions, MyAPI Git
  history, MyAPI handoffs, and one golden MyAPI project brief.
- Existing Obsidian, broad corpus, person-context, and cross-project ingestion
  become later expansion surfaces.
- The public MCP surface remains `get_project_context` and `get_person_context`.
  Granular Decision operations remain internal MyAPI capabilities.

## Canonical architecture

```text
Evidence sources
    ↓
Addressable Evidence records + Source cursors
    ↓
DecisionCandidate extraction
    ↓
Deterministic resolution and Git/code linking
    ↓
Human acceptance
    ↓
Canonical Decision graph
    ↓
Semantic + lexical retrieval and graph expansion
    ↓
DecisionAnswer
    ↓
ContextBrief / MyMCP
```

The separation between `DecisionCandidate` and `Decision` is the central truth
boundary. Model extraction proposes. Deterministic resolution gathers and
classifies evidence. Human acceptance advances canonical project intent.

## Truth hierarchy

- **Golden project brief:** project identity, invariants, and major systems.
- **Accepted Decision:** declared intent, rationale, and current status.
- **Git:** historical implementation evidence and temporal spine.
- **Current code:** present material state.
- **Sessions and handoffs:** rationale, alternatives, and operational context.
- **DecisionCandidate:** a proposed interpretation awaiting resolution.

Disagreement between these layers is a first-class result named
`DecisionCodeDivergence`.

## Existing substrate to preserve

| Existing surface | Role in the Decision architecture |
|---|---|
| `context_refinery/adapters/` | Session and document evidence parsing |
| `scripts/source_manifest.py` | Source inventory, hashes, and freshness metadata |
| `context_refinery/services.py` | Gemini extraction client and structured-output seam |
| `context_refinery/retrieval.py` | Semantic/lexical retrieval, filtering, and reranking substrate |
| `context_refinery/context_packets.py` | `ContextBrief` answer envelope |
| `mcp/server.py` | Two-tool public doorway |
| `api/db.py` and migration `001` | Postgres connection and migration foundation |
| `evals/eval-bank-v0.md` | Historical cold-start question seed bank |

`CanonicalDoc` remains a normalized source-document envelope. `Decision` becomes
the canonical knowledge unit. `ContextBrief` remains the rendered agent and human
answer envelope.

## Implementation graph

| ID | Node | Depends on | Accepted outcome |
|---|---|---|---|
| M1 | Freeze the MyAPI Decision evaluation set | — | Twenty answerable cold-start questions with verified gold |
| M2 | Model Decision provenance | M1 | Domain models and lifecycle invariants pass unit tests |
| M3 | Persist the Decision graph | M2 | Canonical Decisions round-trip with evidence and relations |
| M4 | Ingest four source deltas | M3 | Changed evidence imports through source cursors |
| M5 | Extract DecisionCandidates | M4 | Structured candidates preserve exact evidence locators |
| M6 | Resolve and link Decisions | M5 | Candidates classify, link to Git/code, and enter human review |
| M7 | Retrieve current Decision state | M6 | One question returns current truth plus provenance graph |
| M8 | Serve, evaluate, and update | M7 | One, five, then twenty questions pass; daily delta update runs |

## M1 — Freeze the MyAPI Decision evaluation set

### Objective

Turn real MyAPI cold-start failures into the contract that controls the build.

### Ground-truth inputs

- `evals/eval-bank-v0.md`
- historical MyAPI Graphify and agent questions
- `docs/decision-object-is-born-8.10.26.md`
- MyAPI Git history and handoffs
- `evals/golden_briefs/get_project_context_myapi_rebuild.md`

### Artifact

`evals/decision-mvp-v0.yaml`, containing exactly twenty questions. Every case
records:

- stable case ID and question
- expected current Decision statement and status
- expected rationale
- required evidence locators
- expected commit and code references when applicable
- expected supersession or divergence result
- scoring rubric

### Verification

- Every evidence locator resolves.
- Every required fact has a verified source.
- The set includes orientation, rationale, history, supersession, implementation,
  and divergence questions.
- A current agent can score every row deterministically.

### Stop condition

The twenty-question set is frozen before retrieval or prompt tuning begins.

## M2 — Model Decision provenance

### Objective

Create the domain contract shared by ingestion, resolution, storage, retrieval,
API, and evaluation.

### Build

- `context_refinery/decisions/models.py`
- `tests/test_decision_models.py`

The contract defines:

- `EvidenceRef`
- `SourceCursor`
- `DecisionCandidate`
- `Decision`
- `DecisionRelation`
- `CodeRef`
- `AcceptanceReceipt`
- `DecisionAnswer`
- `DecisionCodeDivergence`

### Verification

- Stable IDs and timestamps validate.
- Evidence provenance is required.
- Candidate and canonical status spaces remain distinct.
- Accepted Decisions carry an acceptance receipt.
- Supersession and contradiction relations preserve direction.
- Models serialize and deserialize without information loss.

### Stop condition

This node defines contracts only. Extraction, storage, and retrieval begin in
their own nodes.

## M3 — Persist the Decision graph

### Objective

Extend the existing Postgres persistence seam with canonical Decision records and
their provenance graph.

### Build

- migration `002_decision_graph.sql`
- `context_refinery/decisions/repository.py`
- repository unit and Postgres integration tests

The schema contains evidence records, source cursors, candidates, Decisions,
Decision-evidence links, Decision relations, code references, and acceptance
receipts.

### Verification

- Migration applies idempotently.
- A complete Decision graph round-trips.
- Evidence deletion policy preserves accepted Decision provenance.
- One active Decision can link to multiple historical Decisions and evidence
  sources.
- Repository calls use parameterized SQL and preserve transaction boundaries.

### Stop condition

Storage exposes a repository interface. API and extraction logic remain outside
the persistence layer.

## M4 — Ingest four source deltas

### Objective

Collect only evidence changed since each source cursor.

### Initial sources

1. Recent MyAPI agent sessions
2. MyAPI Git commits and diffs
3. MyAPI handoffs
4. One golden MyAPI project brief

### Build

- source-specific evidence adapters
- universal evidence normalization
- cursor read/write and changed-source collection
- deterministic source hashing

### Verification

- Every record has a stable ID, project, source type, timestamp, locator, hash,
  and bounded content.
- A second unchanged run imports zero records.
- A changed source imports only its delta.
- Raw private session content stays outside committed fixtures; tests use bounded,
  approved excerpts.

### Stop condition

The node outputs addressable Evidence records. Decision interpretation begins in
M5.

## M5 — Extract DecisionCandidates

### Objective

Extract structured candidate intent and rationale while preserving the exact
evidence that produced each proposal.

### Build

- candidate extraction prompt and schema
- Gemini-backed extractor through the existing service seam
- deterministic fixture extractor for tests
- candidate review payload

### Verification

- Every candidate cites at least one resolvable `EvidenceRef`.
- Extracted text, rationale, project, time window, and possible relations validate.
- Repeated extraction deduplicates by evidence and normalized statement.
- Model output cannot create a canonical Decision directly.

### Stop condition

Candidates enter resolution with provenance intact.

## M6 — Resolve and link Decisions

### Objective

Classify each candidate against project history and assemble the evidence required
for human acceptance.

### Resolution classes

- new
- duplicate
- refinement
- supersession
- contradiction
- unsupported

### Signals

- temporal distance from commits
- changed files and referenced paths
- code-symbol overlap
- semantic and lexical similarity
- handoff confirmation
- relationship to active Decisions

### Verification

- Deterministic fixtures exercise every resolution class.
- Git and code links include exact commit, file, and symbol references.
- Confidence exposes its contributing signals.
- Human acceptance produces an `AcceptanceReceipt` and canonical Decision.
- Rejection preserves the candidate and rationale for audit.

### Stop condition

The canonical graph contains accepted Decisions only; unresolved candidates remain
visible in the review queue.

## M7 — Retrieve current Decision state

### Objective

Answer a natural question by retrieving Decisions first, then expanding through
their provenance graph.

### Query path

```text
question
    ↓
semantic + lexical Decision retrieval
    ↓
candidate Decision ranking
    ↓
graph expansion
    ├── supporting evidence
    ├── superseding Decisions
    ├── implementation commits
    └── current code references
    ↓
current-truth ranking
    ↓
DecisionAnswer
```

### Verification

- The first frozen question returns its expected Decision.
- The answer includes rationale, evidence, status, and current code references.
- Supersession follows the active chain.
- A fixture mismatch between accepted intent and current code returns
  `DecisionCodeDivergence`.
- Retrieval remains inspectable through scores and traversed relations.

### Stop condition

One Decision question passes end to end before the public surface changes.

## M8 — Serve, evaluate, and update

### Objective

Expose Decision retrieval through MyAPI, prove the cold-start hypothesis, and keep
the graph fresh through deltas.

### Internal operations

| Operation | Purpose |
|---|---|
| `project(project)` | Project identity, invariants, and active Decisions |
| `ask(project, question)` | Current evidence-backed answer |
| `decision(decision_id)` | One Decision and direct provenance |
| `history(topic)` | Ordered Decision and supersession history |
| `evidence(decision_id)` | Supporting and conflicting evidence |
| `code_context(decision_id)` | Commits, files, symbols, and divergence |

The two public MCP tools route to these operations through intent arguments and
return a budgeted `ContextBrief`.

### Evaluation ladder

1. One fully verified question
2. Five representative questions
3. All twenty frozen questions
4. One cold agent using only the returned brief
5. One incremental update followed by a changed answer

### MVP acceptance

- Current Decision accuracy meets the frozen rubric.
- Required evidence locators resolve.
- Supersession and divergence cases classify correctly.
- The cold agent identifies the project direction and next action without a repo
  scan.
- A daily updater advances source cursors and imports only changed evidence.
- Evaluation and update runs write inspectable receipts.

## Implementation policy

- One node, one objective, one bounded verification gate.
- Tests and fixtures land with the behavior they verify.
- Model outputs remain proposals until accepted.
- Canonical truth changes through explicit acceptance receipts.
- Exact evidence paths, commits, and code symbols remain visible.
- Resource-heavy corpus refreshes wait until the twenty-question MVP proves value.
- Graphify contributes code structure and references; MyAPI owns Decision truth.
- ContextBrief stays the output contract; Decision stays the knowledge contract.

## Immediate next packet

Begin M1 in `evals/decision-mvp-v0.yaml`. Freeze the first five MyAPI questions
with verified gold, validate the case schema, then expand the same artifact to
twenty before M2 begins.
