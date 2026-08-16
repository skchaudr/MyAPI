# MyAPI Decision Fixture Review — F01–F10

Status: reviewer pass; non-canonical  
Date: 2026-08-10  
Reviewer: Codex  

Reviewed immutable first-pass checkpoints:

- `6b58429` — Grok independent F06–F10 worker pass
- `b5105ab` — verbatim Codex F01–F05 snapshot

This document critiques the fixtures as they stand. It does not promote any
fixture to production truth, rewrite either first-pass artifact, or freeze M1.

## Review gates

1. The source query must require a project Decision, rationale, architectural
   constraint, historical evolution, or implementation provenance.
2. A canonical `Decision` must be accepted project intent, not merely a proposed
   plan, ready task, document location, or reviewer inference.
3. Acceptance must resolve through an `AcceptanceReceipt`; a missing receipt is
   a material provenance gap, not an accepted boolean.
4. Evidence paths, line ranges, commits, files, and symbols must resolve in the
   live worktree.
5. Historical intent, current accepted intent, and current code must remain
   distinguishable.
6. `DecisionCodeDivergence` must describe disagreement between the Decision under
   review and current implementation, not merely unfinished adjacent work.

## Verdicts

| Fixture | Origin | Verdict | Core finding |
|---|---|---|---|
| F01 | Codex | Retain after receipt repair | Strong current-intent/history fixture; exact acceptance Evidence ID and predecessor Decision ID remain unresolved. |
| F02 | Codex | Retain after receipt repair | Strong ownership Decision with real code boundary; exact acceptance provenance remains unresolved. |
| F03 | Codex | Retain after divergence correction | Strong public-contract Decision; `decision_code_divergence: null` conflicts with the documented missing transport and argument contract. |
| F04 | Codex | Split or narrow before gold freeze | Excellent provenance, but one object combines the July corpus-tier Decision with the August four-source MVP refinement. |
| F05 | Codex | Retain after receipt repair | Strong failure-rationale/history fixture; raw benchmark evidence for the approximately 579-session result remains missing. |
| F06 | Grok | Reclassify or replace | The query is primarily artifact lookup, and the node is explicitly `ready` pending Sab review; it is a `DecisionCandidate`, not an accepted `Decision`. |
| F07 | Grok | Retain after narrowing | Implementation-provenance query is admissible, but the quality-bar Decision needs direct plan/architecture evidence and a narrower divergence. |
| F08 | Grok | Retain as historical/refined | Strong historical architecture fixture; the L0–L3 Graphify-first chain is no longer sufficient as active current truth after the accepted Decision Graph plan. |
| F09 | Grok | Retain after receipt resolution | Strong human-acceptance constraint with a real runtime-enforcement gap; canonical acceptance provenance is still unresolved. |
| F10 | Grok | Retain after receipt and relation repair | Strong handoff/ContextBrief ownership Decision; inverse relation vocabulary and acceptance provenance need normalization. |

## Cross-set findings

### 1. The evidence is real; canonicality is still open

Mechanical review found ten parseable YAML fixtures, ten
`production_ingestion: false` flags, resolvable evidence files and line ranges,
resolvable Git commit objects, and existing code paths for every `CodeRef`.

That proves the fixtures are evidence-backed evaluation material. It does not
prove that their statements are accepted project truth.

### 2. Acceptance is the shared blocking invariant

F01–F05 synthesize expected `AcceptanceReceipt` records from the accepted
2026-08-10 implementation plan. Their own provenance gaps correctly state that
the exact accepting session turn has no stable `EvidenceRef`. In particular,
`accepted_by: Sab` is not independently resolvable from the plan file alone.

F06–F10 take the safer factual position that no receipt was found, but still type
the records as `Decision`. That violates the proposed contract:

- `CONTEXT.md:22-24` defines a `Decision` as accepted intent.
- `IMPLEMENTATION-PLAN.md:59-61` makes human acceptance the truth boundary.
- `IMPLEMENTATION-PLAN.md:170-174` requires accepted Decisions to carry an
  acceptance receipt.

Before gold freeze, each record needs either a resolvable receipt or
reclassification as `DecisionCandidate`. F06 is the clearest mandatory
reclassification because `.handoffs/029-gddp-first-durable-handoff-node.md:32-34`
explicitly says Sab review is still next and the node remains `status: ready`.

### 3. Relationship direction needs one vocabulary

The Grok pass uses `refined_by` in F06, F08, and F10. Current canonical examples
name directed relations with active labels such as `refines`, `supersedes`, and
`contradicts`. M1 must freeze direction and allowed values before these become
gold.

F06 also describes F09 as `refined_by`, while F09 correctly describes the
relationship as `constrains`. Human acceptance constrains the node; it does not
refine the node definition.

### 4. Divergence must stay attached to the reviewed Decision

- F03 declares no divergence while separately acknowledging that the public MCP
  transport and final argument contract are absent. The correct fixture state is
  an open partial-implementation divergence.
- F06 treats an unexecuted ready node as code divergence. Pending task execution
  is not disagreement with an accepted Decision, especially while acceptance is
  still pending.
- F07 attaches the missing live Decision retrieval pipeline to the golden-brief
  quality-bar Decision. That broader gap belongs to the MyMCP/Decision-engine
  integration Decision; F07 should limit divergence to how goldens are currently
  used and whether their evidence pointers remain valid.
- F08 presents the gap mainly as incomplete implementation. The deeper result is
  historical intent change: the accepted 2026-08-10 architecture centers an
  Evidence → DecisionCandidate → acceptance → Decision graph pipeline and does
  not require the older Graphify-first L1 chain as the current canonical path.

### 5. One Decision per object

F04 combines two independently useful Decisions:

1. the July hot/durable/cold corpus-tier policy, already represented in
   `scripts/source_manifest.py`; and
2. the August Decision-MVP restriction to four evidence classes.

The current object should either state only the August refinement and point to a
historical July Decision, or split into two connected fixtures. Keeping both in
one statement hides the exact supersession/refinement behavior the MVP is meant
to evaluate.

F08 has a related temporal issue. The old L0–L4 architecture is valuable
historical intent, but `status: active` overstates it. Its expected answer should
identify the older chain, then explain how the accepted Decision Graph plan
refines the internal model while preserving `ContextBrief` and the two-tool
surface.

## Per-fixture review

### F01 — Current MyAPI north star

- **Query gate:** Pass. Correctness requires historical evolution and current
  accepted intent.
- **Evidence gate:** Pass. The design document, implementation plan, commits, and
  current retrieval path form a real chain.
- **Required repair:** Resolve the accepting session Evidence ID and predecessor
  Decision ID. Until then, keep the receipt explicitly provisional.

### F02 — MyAPI engine / MyMCP doorway

- **Query gate:** Pass. This is a deliberate product-ownership boundary.
- **Evidence gate:** Pass. `CONTEXT.md`, the accepted plan, July commits, and
  `mcp/server.py` support the answer and current partial implementation.
- **Required repair:** Resolve the acceptance receipt rather than treating the
  plan date alone as proof of `accepted_by`.

### F03 — Two stable public tools

- **Query gate:** Pass. The two-tool limit is a chosen public contract.
- **Evidence gate:** Pass. Both symbols and golden outputs exist.
- **Required repair:** Replace `decision_code_divergence: null` with an open
  partial-implementation record for missing transport registration and the final
  intent/budget/token/evidence argument contract.

### F04 — Corpus tier policy

- **Query gate:** Pass. The answer requires policy evolution and implementation
  provenance.
- **Evidence gate:** Pass; this is the strongest complete source → commits → code
  chain in the set.
- **Required repair:** Split the July implemented tier policy from the August
  four-source MVP refinement, or narrow this object to the current refinement.

### F05 — v0 failure and Decision-centered redesign

- **Query gate:** Pass. The rationale cannot be recovered from current code
  navigation alone.
- **Evidence gate:** Pass with one explicit raw-artifact gap. The project brief
  records the approximately 579-session result, but the underlying benchmark run
  was not located in this pass.
- **Required repair:** Resolve the acceptance receipt and historical target ID;
  retain the raw benchmark gap until an artifact is found.

### F06 — First GDDP-linked durable handoff node

- **Query gate:** Weak. M06 asks which handoff documents the node, which can be
  answered as artifact navigation. The expanded QUERIES wording adds a real
  acceptance-constraint dimension.
- **Evidence gate:** Pass. The node, handoff, project graph, and commits resolve.
- **Required repair:** Reclassify as `DecisionCandidate` or use it as a negative
  acceptance-boundary fixture. The repo explicitly records pending Sab review,
  so it cannot be an expected canonical `Decision` today.

### F07 — Golden briefs as tool evidence

- **Query gate:** Pass narrowly as implementation provenance; it becomes generic
  inventory if the answer stops at filenames.
- **Evidence gate:** Pass. The golden files, loader, and commits resolve, including
  the stale `project-documents/` evidence pointers.
- **Required repair:** Cite `project-docs/ARCHITECTURE.md:416-417` and
  `IMPLEMENTATION-PLAN.md:111-120` for the quality-gate policy. Narrow divergence
  to golden usage and stale evidence pointers; keep the broader live Decision
  pipeline gap with the engine-integration Decision.

### F08 — L0–L3 layer chain

- **Query gate:** Pass. This is architectural history and current-vs-prior intent.
- **Evidence gate:** Pass. The old architecture and partial L0/L2/L3 substrates
  are real.
- **Required repair:** Mark it historical/refined, not unqualified active truth.
  The expected answer must include the accepted 2026-08-10 Decision Graph pipeline
  and explain which older layer responsibilities survive.

### F09 — Human acceptance owns graph truth

- **Query gate:** Pass. This is a core architectural constraint.
- **Evidence gate:** Pass. Node policy and the accepted Decision-plan truth
  boundary agree; runtime enforcement is genuinely absent.
- **Required repair:** Resolve an acceptance receipt for the policy Decision. Keep
  the runtime-enforcement divergence and cross-repo ownership gap explicit.

### F10 — Handoff format vs ContextBrief shape

- **Query gate:** Pass. This is an ownership and representation Decision.
- **Evidence gate:** Pass. Template, anchor, packet contract, code, and current
  vocabulary all support the distinction.
- **Required repair:** Resolve acceptance provenance and normalize the inverse
  `refined_by` relation. Preserve the current-plan distinction: handoffs are
  Evidence, Decisions are canonical knowledge, and ContextBrief is delivery.

## Freeze recommendation

The current ten objects are a useful comparative fixture corpus, not M1 gold.

Recommended next states:

- Gold candidates after bounded repair: F01, F02, F03, F05, F09, F10.
- Provenance candidate after narrowing: F07.
- Historical/refinement candidate: F08.
- Split before freeze: F04.
- Negative boundary fixture or replacement candidate: F06.

Preserve both first-pass files unchanged. Apply any schema or semantic corrections
in a later commit only after the fixture review is accepted.

## Verification performed

- Parsed all ten YAML blocks with Ruby/Psych.
- Confirmed all ten use `production_ingestion: false`.
- Confirmed every referenced Evidence file and line range exists.
- Confirmed every referenced Git hash resolves to a commit object.
- Confirmed every `CodeRef.path` exists and the named Python symbols used by the
  fixtures exist in the live AST/source.
- Re-read the current vocabulary and accepted implementation plan before judging
  canonical status.

