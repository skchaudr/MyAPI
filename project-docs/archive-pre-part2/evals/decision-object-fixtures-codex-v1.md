# MYAPI — Decision Objects Day 1

Related: [[2026.08.10]]

## Purpose

Manually construct expected canonical `Decision` objects for five strong MyAPI cold-start candidates. These are **evaluation fixtures only**. They are not automatically ingested production data, accepted production IDs, or a substitute for the future M2 schema.

The fixtures use the current vocabulary in `CONTEXT.md`: `EvidenceRef`, `Decision`, `DecisionRelation`, `AcceptanceReceipt`, `DecisionCodeDivergence`, `CodeRef`, `DecisionAnswer`, and `ContextBrief`.

## Selection

Each retained query requires project intent, rationale, history, or implementation provenance. Each also has a real recorded query source and enough current evidence to construct an expected answer without inventing the missing links.

| Fixture | Existing candidate | Decision dimension | Why it is strong |
|---|---|---|---|
| F01 | M03 | Historical evolution / current intent | The correct answer changed from durable-handoff product framing to a Decision-centered provenance graph. |
| F02 | M02 | Product ownership boundary | The answer depends on the deliberate MyAPI engine / MyMCP doorway split. |
| F03 | M04 | Public architectural constraint | The two stable tools are a chosen public contract and already have matching code symbols. |
| F04 | M10 | Corpus policy / implementation provenance | The hot/durable/cold rule has source rationale, commits, and current implementing code. |
| F05 | M08 | Historical rationale / code divergence | The answer requires the v0 failure record and comparison with the current document-retrieval implementation. |

## Fixture conventions

- IDs beginning with `fixture_` are local fixture identifiers, not production IDs.
- `EvidenceRef.locator` uses a repository-relative path plus line range when available.
- `commit_refs` contain verified commits from the current MyAPI Git history.
- `CodeRef` names only files and symbols inspected in the current worktree.
- `AcceptanceReceipt` is an expected fixture record grounded in `IMPLEMENTATION-PLAN.md:3-7`. The exact accepting session turn has no stable Evidence ID yet and remains a provenance gap.
- `DecisionCodeDivergence` distinguishes an accepted target from the current material implementation. `target_not_yet_implemented` means the code still reflects the pre-Decision substrate.

## F01 — Current MyAPI north star

Source query: **“What is the current north star: corpus v1 vault substrate, or two MCP tools over v2 durable handoffs?”**

Query origin: `/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:13`; normalized candidate M03 at `evals/eval-bank-v0.md:53`.

```yaml
fixture:
  id: fixture_f01_myapi_north_star
  kind: expected_canonical_decision
  production_ingestion: false
  review_state: manually_constructed

decision:
  type: Decision
  id: fixture_dec_myapi_decision_graph_north_star
  project: myapi-rebuild
  statement: >-
    MyAPI is a continuously maintained semantic provenance graph whose canonical
    knowledge unit is the Decision; it serves current and historical project intent
    through DecisionAnswers wrapped in ContextBriefs.
  rationale: >-
    Durable handoffs remain evidence and continuity substrate, but handoffs alone do
    not model current intent, rationale, supersession, commits, or code provenance.
    The Decision unit gives those relationships a canonical home.
  status: active
  decided_at: 2026-08-10
  time_precision: day

  evidence_refs:
    - type: EvidenceRef
      id: fixture_ev_f01_query
      source_type: document
      locator: /Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:13
      role: source_query
    - type: EvidenceRef
      id: fixture_ev_f01_predecessor
      source_type: project_brief
      locator: PROJECT-BRIEF.md:18-24
      role: historical_predecessor
    - type: EvidenceRef
      id: fixture_ev_f01_design
      source_type: design_document
      locator: docs/decision-object-is-born-8.10.26.md:1-47
      role: supports_statement_and_rationale
    - type: EvidenceRef
      id: fixture_ev_f01_current
      source_type: implementation_plan
      locator: IMPLEMENTATION-PLAN.md:5-23
      role: current_canonical_direction
    - type: EvidenceRef
      id: fixture_ev_f01_truth_boundary
      source_type: implementation_plan
      locator: IMPLEMENTATION-PLAN.md:37-73
      role: supports_truth_model

  commit_refs:
    - commit: 281c056
      role: introduced_durable_handoff_and_context_brief_predecessor
    - commit: 220496c
      role: introduced_decision_object_design
    - commit: 0b28418
      role: accepted_and_planned_decision_graph_direction

  code_refs:
    - type: CodeRef
      path: context_refinery/context_packets.py
      symbols: [ContextBrief]
      lines: 131-219
      role: current_answer_envelope_substrate
    - type: CodeRef
      path: api/routers/query.py
      symbols: [query]
      lines: 11-29
      role: current_query_entrypoint
    - type: CodeRef
      path: context_refinery/retrieval.py
      symbols: [RetrievalPipeline.execute]
      lines: 1113-1263
      role: current_document_retrieval_substrate

  relations:
    - type: DecisionRelation
      relation: refines
      target_decision_id: null
      target_locator: PROJECT-BRIEF.md:18-24
      note: The historical durable-handoff north-star decision has no canonical Decision ID yet.

  acceptance_receipt:
    type: AcceptanceReceipt
    id: fixture_receipt_f01
    accepted_by: Sab
    accepted_at: 2026-08-10
    time_precision: day
    source_evidence_ref: fixture_ev_f01_current
    provenance_gap: Exact accepting session turn has not been assigned a stable Evidence ID.

  decision_code_divergence:
    type: DecisionCodeDivergence
    state: open
    classification: target_not_yet_implemented
    expected: Retrieval returns a DecisionAnswer with rationale, history, evidence, relations, commits, and code context.
    observed: The live /query path still returns ranked document results and groups.
    observed_at:
      - api/routers/query.py:11-29
      - context_refinery/retrieval.py:1204-1263

  provenance_gaps:
    - The predecessor Decision needs a canonical production ID before the refines edge can resolve.
    - No context_refinery/decisions implementation exists yet; this is the planned M2 surface.
    - The exact user-session acceptance locator is still unresolved.
```

Expected `DecisionAnswer`: name the Decision graph as current truth, preserve durable handoffs as a predecessor/substrate, and surface the open implementation gap.

## F02 — MyAPI engine / MyMCP doorway boundary

Source query: **“Is MyMCP a separate product surface or a thin paid doorway into MyAPI?”**

Query origin: `/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:8`; normalized candidate M02 at `evals/eval-bank-v0.md:52`.

```yaml
fixture:
  id: fixture_f02_myapi_mymcp_boundary
  kind: expected_canonical_decision
  production_ingestion: false
  review_state: manually_constructed

decision:
  type: Decision
  id: fixture_dec_myapi_engine_mymcp_doorway
  project: myapi-rebuild
  statement: >-
    MyAPI owns evidence collection, Decision graph maintenance, retrieval, manifests,
    caching, and backend integration; MyMCP is the small public doorway into MyAPI.
  rationale: >-
    Keeping engine responsibilities behind a small doorway prevents transport and
    token-budget concerns from becoming a second retrieval product or duplicating
    MyAPI's truth and corpus ownership.
  status: active
  decided_at: 2026-08-10
  time_precision: day

  evidence_refs:
    - type: EvidenceRef
      id: fixture_ev_f02_query
      source_type: document
      locator: /Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:8
      role: source_query
    - type: EvidenceRef
      id: fixture_ev_f02_origin
      source_type: project_brief
      locator: PROJECT-BRIEF.md:26-31
      role: first_verified_architecture_statement
    - type: EvidenceRef
      id: fixture_ev_f02_handoff
      source_type: handoff
      locator: .handoffs/026-cost-aware-mymcp-corpus-tiers.md:12-15
      role: implementation_handoff_confirmation
    - type: EvidenceRef
      id: fixture_ev_f02_language
      source_type: canonical_language
      locator: CONTEXT.md:56-63
      role: current_ownership_definition
    - type: EvidenceRef
      id: fixture_ev_f02_current
      source_type: implementation_plan
      locator: IMPLEMENTATION-PLAN.md:25-35
      role: current_execution_boundary

  commit_refs:
    - commit: 79cfdf2
      role: introduced_cost_aware_engine_doorway_split
    - commit: 11d50fc
      role: implemented_fixture_backed_mymcp_foundation
    - commit: 0b28418
      role: carried_boundary_into_accepted_decision_graph_plan

  code_refs:
    - type: CodeRef
      path: mcp/server.py
      symbols: [get_project_context, get_person_context, _context_envelope]
      lines: 1-59
      role: current_public_doorway_foundation
    - type: CodeRef
      path: scripts/source_manifest.py
      symbols: [build_manifest, build_corpus_manifest]
      lines: 135-250
      role: current_myapi_owned_corpus_manifest_surface

  relations: []

  acceptance_receipt:
    type: AcceptanceReceipt
    id: fixture_receipt_f02
    accepted_by: Sab
    accepted_at: 2026-08-10
    time_precision: day
    source_evidence_ref: fixture_ev_f02_current
    provenance_gap: Exact accepting session turn has not been assigned a stable Evidence ID.

  decision_code_divergence:
    type: DecisionCodeDivergence
    state: open
    classification: partial_implementation
    expected: MyMCP transports ContextBriefs produced by the MyAPI Decision engine.
    observed: mcp/server.py reads golden Markdown fixtures directly and no Decision engine exists yet.
    observed_at: mcp/server.py:17-59

  provenance_gaps:
    - The exact session that originated the paid-doorway framing has not been linked.
    - There is no production MyMCP transport registration or Decision engine integration yet.
```

Expected `DecisionAnswer`: answer “thin doorway into MyAPI,” then show the ownership boundary, its July commits, and the current fixture-backed implementation gap.

## F03 — Two stable public MCP tools

Source query: **“What are the two MCP tools and what intents do they encode?”**

Query origin: normalized candidate M04 at `evals/eval-bank-v0.md:54`; the underlying cold-start question appears at `/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:14`.

```yaml
fixture:
  id: fixture_f03_two_public_tools
  kind: expected_canonical_decision
  production_ingestion: false
  review_state: manually_constructed

decision:
  type: Decision
  id: fixture_dec_myapi_two_public_tools
  project: myapi-rebuild
  statement: >-
    MyAPI exposes exactly two stable public context operations through MyMCP:
    get_project_context for project intent and get_person_context for person/operator
    continuity. Granular Decision operations remain internal.
  rationale: >-
    A small stable surface reduces MCP tool and token cost while allowing intent,
    budget, evidence depth, and answer size to vary through arguments and ContextBriefs.
  status: active
  decided_at: 2026-08-10
  time_precision: day

  evidence_refs:
    - type: EvidenceRef
      id: fixture_ev_f03_query
      source_type: evaluation_bank
      locator: evals/eval-bank-v0.md:54
      role: source_query
    - type: EvidenceRef
      id: fixture_ev_f03_origin
      source_type: project_brief
      locator: PROJECT-BRIEF.md:18-31
      role: names_tools_and_cost_constraint
    - type: EvidenceRef
      id: fixture_ev_f03_current
      source_type: implementation_plan
      locator: IMPLEMENTATION-PLAN.md:30-35
      role: current_public_contract
    - type: EvidenceRef
      id: fixture_ev_f03_language
      source_type: canonical_language
      locator: CONTEXT.md:51-63
      role: defines_contextbrief_myapi_and_mymcp

  commit_refs:
    - commit: 281c056
      role: introduced_two_tool_context_brief_direction
    - commit: 11d50fc
      role: implemented_both_tool_functions
    - commit: f35059c
      role: added_golden_context_brief_fixtures
    - commit: 0b28418
      role: preserved_two_tool_surface_in_accepted_plan

  code_refs:
    - type: CodeRef
      path: mcp/server.py
      symbols: [get_project_context]
      lines: 17-25
      role: project_intent_tool
    - type: CodeRef
      path: mcp/server.py
      symbols: [get_person_context]
      lines: 28-36
      role: person_continuity_tool
    - type: CodeRef
      path: context_refinery/context_packets.py
      symbols: [ContextBrief]
      lines: 131-219
      role: intended_answer_envelope
    - type: CodeRef
      path: evals/golden_briefs/get_project_context_myapi_rebuild.md
      symbols: []
      lines: 1-44
      role: project_tool_expected_output
    - type: CodeRef
      path: evals/golden_briefs/get_person_context_sab.md
      symbols: []
      lines: 1-44
      role: person_tool_expected_output

  relations:
    - type: DecisionRelation
      relation: constrains
      target_decision_id: fixture_dec_myapi_engine_mymcp_doorway
      note: The two-tool public contract is a constraint on the MyMCP doorway decision.

  acceptance_receipt:
    type: AcceptanceReceipt
    id: fixture_receipt_f03
    accepted_by: Sab
    accepted_at: 2026-08-10
    time_precision: day
    source_evidence_ref: fixture_ev_f03_current
    provenance_gap: Exact accepting session turn has not been assigned a stable Evidence ID.

  decision_code_divergence: null

  provenance_gaps:
    - The two Python functions are verified; actual MCP transport registration remains a future implementation surface.
    - The final argument contract for intent, budget, max_tokens, and evidence inclusion is not implemented.
```

Expected `DecisionAnswer`: name both tools and their intents, then distinguish verified function names from the still-future transport/argument contract.

## F04 — Active corpus tier policy

Source query: **“What is the active corpus policy (hot window vs Corpus v1.0 cold)?”**

Query origin: normalized candidate M10 at `evals/eval-bank-v0.md:60`; its underlying ownership/current-state questions are recorded at `/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:7,13`.

```yaml
fixture:
  id: fixture_f04_active_corpus_policy
  kind: expected_canonical_decision
  production_ingestion: false
  review_state: manually_constructed

decision:
  type: Decision
  id: fixture_dec_myapi_active_corpus_tiers
  project: myapi-rebuild
  statement: >-
    The existing MyAPI corpus policy classifies sources as hot, durable, or cold:
    recent material defaults to a 30-day hot window, canonical anchors and handoffs
    remain durable, and Corpus v1 baseline material remains cold and outside the
    active bundle. The Decision MVP further narrows initial ingestion to recent
    MyAPI sessions, Git history, MyAPI handoffs, and one golden project brief.
  rationale: >-
    Daily context should stay fresh and bounded while durable sources remain
    available and the old bulk corpus serves as evaluation/reference substrate
    instead of overwhelming active project intent.
  status: active
  decided_at: 2026-08-10
  time_precision: day

  evidence_refs:
    - type: EvidenceRef
      id: fixture_ev_f04_query
      source_type: evaluation_bank
      locator: evals/eval-bank-v0.md:60
      role: source_query
    - type: EvidenceRef
      id: fixture_ev_f04_policy_origin
      source_type: project_brief
      locator: PROJECT-BRIEF.md:33-37
      role: policy_rationale
    - type: EvidenceRef
      id: fixture_ev_f04_handoff
      source_type: handoff
      locator: .handoffs/027-active-corpus-manifest.md:10-34
      role: implementation_confirmation
    - type: EvidenceRef
      id: fixture_ev_f04_mvp_refinement
      source_type: implementation_plan
      locator: IMPLEMENTATION-PLAN.md:25-33
      role: decision_mvp_scope_refinement

  commit_refs:
    - commit: 79cfdf2
      role: recorded_recent_active_window_and_cold_baseline_policy
    - commit: 389f026
      role: implemented_hot_durable_cold_classification
    - commit: cfd0c74
      role: added_source_manifest_output_overrides
    - commit: 6177b13
      role: added_daily_hot_corpus_build_and_delivery_pipeline
    - commit: 0b28418
      role: narrowed_decision_mvp_initial_evidence_sources

  code_refs:
    - type: CodeRef
      path: scripts/source_manifest.py
      symbols: [DURABLE_BASENAMES, COLD_SOURCE_FAMILIES, DEFAULT_HOT_DAYS]
      lines: 50-64
      role: tier_constants
    - type: CodeRef
      path: scripts/source_manifest.py
      symbols: [TierDecision, classify_corpus_tier]
      lines: 67-170
      role: tier_classification
    - type: CodeRef
      path: scripts/source_manifest.py
      symbols: [build_corpus_manifest]
      lines: 205-250
      role: active_bundle_manifest

  relations:
    - type: DecisionRelation
      relation: refines
      target_decision_id: null
      target_locator: PROJECT-BRIEF.md:33-37
      note: The Decision MVP source restriction refines the broader active-corpus policy; the predecessor has no canonical ID yet.

  acceptance_receipt:
    type: AcceptanceReceipt
    id: fixture_receipt_f04
    accepted_by: Sab
    accepted_at: 2026-08-10
    time_precision: day
    source_evidence_ref: fixture_ev_f04_mvp_refinement
    provenance_gap: Exact accepting session turn has not been assigned a stable Evidence ID.

  decision_code_divergence:
    type: DecisionCodeDivergence
    state: open
    classification: scope_refinement_pending
    expected: Decision MVP ingestion admits only the four initial MyAPI evidence classes.
    observed: Existing source_manifest.py still implements the broader hot/durable/cold corpus mechanism.
    observed_at: scripts/source_manifest.py:205-250

  provenance_gaps:
    - The broader July corpus-tier Decision needs a canonical production ID.
    - The four-source Decision MVP collector does not exist yet.
```

Expected `DecisionAnswer`: return both layers of truth—implemented corpus tiers and the newer, narrower Decision-MVP source boundary—without treating either as the whole history.

## F05 — v0 failure forces Decision-centered redesign

Source query: **“How does Corpus v1.0 failure mode force handoff-first redesign?”**

Query origin: normalized candidate M08 at `evals/eval-bank-v0.md:58`; the underlying evidence question is `/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:19`.

```yaml
fixture:
  id: fixture_f05_v0_failure_redesign
  kind: expected_canonical_decision
  production_ingestion: false
  review_state: manually_constructed

decision:
  type: Decision
  id: fixture_dec_myapi_reject_blended_pool_as_canonical_model
  project: myapi-rebuild
  statement: >-
    MyAPI does not treat a blended document retrieval pool as its canonical
    knowledge model. Documents, sessions, handoffs, commits, and code are Evidence;
    accepted Decisions are the canonical unit used to preserve current intent,
    rationale, history, and implementation provenance.
  rationale: >-
    In v0, ChatGPT exports dominated by volume, roughly 579 ingested CLI sessions
    failed to surface, and retrieval produced disconnected meta-narratives rather
    than trustworthy project intent. Better ranking alone could not represent why
    a choice existed, what replaced it, or which code realized it.
  status: active
  decided_at: 2026-08-10
  time_precision: day

  evidence_refs:
    - type: EvidenceRef
      id: fixture_ev_f05_query
      source_type: document
      locator: /Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:19
      role: source_query
    - type: EvidenceRef
      id: fixture_ev_f05_failure
      source_type: project_brief
      locator: PROJECT-BRIEF.md:7-15
      role: observed_v0_failure_and_rationale
    - type: EvidenceRef
      id: fixture_ev_f05_field_test
      source_type: handoff
      locator: .handoffs/015-corpus-v1-field-test-realization.md:35-85
      role: retrieval_field_test_and_honest_routing_constraints
    - type: EvidenceRef
      id: fixture_ev_f05_design
      source_type: design_document
      locator: docs/decision-object-is-born-8.10.26.md:1-47
      role: decision_centered_replacement
    - type: EvidenceRef
      id: fixture_ev_f05_current
      source_type: implementation_plan
      locator: IMPLEMENTATION-PLAN.md:9-23
      role: accepted_current_model

  commit_refs:
    - commit: 281c056
      role: recorded_v0_failure_and_handoff_inversion
    - commit: 832960e
      role: expanded_failure_and_active_context_narrative
    - commit: e86c440
      role: preserved_corpus_field_test_realization
    - commit: 220496c
      role: proposed_decision_as_canonical_unit
    - commit: 0b28418
      role: accepted_decision_graph_implementation_direction

  code_refs:
    - type: CodeRef
      path: context_refinery/retrieval.py
      symbols: [RetrievalPipeline.execute]
      lines: 1113-1263
      role: current_pre_decision_retrieval_path
    - type: CodeRef
      path: api/routers/query.py
      symbols: [query]
      lines: 11-29
      role: current_document_result_api
    - type: CodeRef
      path: context_refinery/context_packets.py
      symbols: [ContextBrief]
      lines: 131-219
      role: preserved_future_answer_envelope

  relations:
    - type: DecisionRelation
      relation: supersedes
      target_decision_id: null
      target_locator: PROJECT-BRIEF.md:7-13
      note: The v0 blended-pool architecture has no canonical historical Decision ID yet.

  acceptance_receipt:
    type: AcceptanceReceipt
    id: fixture_receipt_f05
    accepted_by: Sab
    accepted_at: 2026-08-10
    time_precision: day
    source_evidence_ref: fixture_ev_f05_current
    provenance_gap: Exact accepting session turn has not been assigned a stable Evidence ID.

  decision_code_divergence:
    type: DecisionCodeDivergence
    state: open
    classification: target_not_yet_implemented
    expected: Query results are DecisionAnswers expanded through evidence, relations, commits, and code.
    observed: The current pipeline classifies, searches, filters, reranks, groups, and returns document results.
    observed_at:
      - context_refinery/retrieval.py:1125-1263
      - api/routers/query.py:11-29

  provenance_gaps:
    - The raw benchmark run that produced the “~579 sessions ingested but never surfaced” count has not been linked to a stable artifact in this pass.
    - The v0 architecture needs a canonical historical Decision ID before the supersedes edge can resolve.
    - Decision models, persistence, resolution, and retrieval are planned but absent from current code.
```

Expected `DecisionAnswer`: explain the failure as rationale for the accepted redesign, cite the historical record, and make the current implementation divergence visible.

## Review findings

1. **F01 and F05 are the best hypothesis tests.** They force the answer to distinguish historical intent, current accepted intent, and current code instead of returning a project summary.
2. **F02 and F03 prove that one project can hold related but non-identical Decisions.** Product ownership and public tool surface should be connected, not collapsed into one blob.
3. **F04 is the cleanest end-to-end provenance fixture.** It has a real query, rationale, two policy stages, concrete commits, and current implementing symbols.
4. **The biggest shared gap is acceptance provenance.** `IMPLEMENTATION-PLAN.md` records the accepted date, but the accepting session turn does not yet have a stable `EvidenceRef`.
5. **Historical relation targets lack canonical IDs.** The fixtures preserve their source locators and leave `target_decision_id` null rather than inventing production identity.
6. **Current code truth must remain visible.** The existing API is still document retrieval plus fixture-backed context output; the Decision architecture is accepted and planned, with implementation beginning at M2.

## Recommended fixture order

Use F04 first to validate object shape against the strongest complete provenance chain. Use F03 second to validate a no-divergence case. Then use F01 and F05 to validate refinement, supersession, and `DecisionCodeDivergence`. Use F02 to validate connected Decisions and product boundary reasoning.

## Sources inspected

- `/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md`
- `/Users/sab-mini/repos/MyAPI-rebuild/evals/eval-bank-v0.md`
- `/Users/sab-mini/repos/MyAPI-rebuild/PROJECT-BRIEF.md`
- `/Users/sab-mini/repos/MyAPI-rebuild/CONTEXT.md`
- `/Users/sab-mini/repos/MyAPI-rebuild/IMPLEMENTATION-PLAN.md`
- `/Users/sab-mini/repos/MyAPI-rebuild/docs/decision-object-is-born-8.10.26.md`
- `/Users/sab-mini/repos/MyAPI-rebuild/.handoffs/015-corpus-v1-field-test-realization.md`
- `/Users/sab-mini/repos/MyAPI-rebuild/.handoffs/026-cost-aware-mymcp-corpus-tiers.md`
- `/Users/sab-mini/repos/MyAPI-rebuild/.handoffs/027-active-corpus-manifest.md`
- `/Users/sab-mini/repos/MyAPI-rebuild/mcp/server.py`
- `/Users/sab-mini/repos/MyAPI-rebuild/context_refinery/context_packets.py`
- `/Users/sab-mini/repos/MyAPI-rebuild/context_refinery/retrieval.py`
- `/Users/sab-mini/repos/MyAPI-rebuild/scripts/source_manifest.py`
