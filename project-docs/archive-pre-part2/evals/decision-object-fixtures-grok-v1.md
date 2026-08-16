# Decision Object Fixtures — Grok independent first pass (F06–F10)

Status: worker first pass  
Date: 2026-08-10  
Branch: `codex/myapi-decision-plan`  
Worker: grok-cli  

These are **evaluation fixtures only**. They are not production ingestion data,
accepted production IDs, or frozen M1 gold. Every object uses fixture-prefixed
IDs, `production_ingestion: false`, and `review_state: worker_first_pass`.

Vocabulary follows `CONTEXT.md` and the M1/M2 contract list in
`IMPLEMENTATION-PLAN.md`: `EvidenceRef`, `Decision`, `DecisionRelation`,
`CodeRef`, `AcceptanceReceipt`, `DecisionCodeDivergence`, `DecisionAnswer`,
and `ContextBrief`.

Independence note: F01–F05 (other agent / Day-1 packaging) are untrusted
comparison material only. Occupied candidate IDs M02, M03, M04, M08, and M10
were excluded. Evidence chains were derived from primary repo sources and Git
history on this branch.

## Selection / rejection rationale

Selected five (strong real cold-start queries with resolvable provenance):

| Fixture | Source candidate | Query (short) | Why retained |
|---|---|---|---|
| F06 | M06 / QUERIES #9 | First GDDP-linked MyAPI handoff node | Handoff + node YAML + two verified commits + current files |
| F07 | M05 / QUERIES #7 | Golden briefs prove two MCP tools | Eval-bank + three golden fixtures + `mcp/server.py` load path |
| F08 | M07 / QUERIES #12 | L0→L1→L2→L3 layer chain | Architecture layer contract with current code substrates |
| F09 | QUERIES #4 | Who advances GDDP graph truth | Explicit human-acceptance constraint on the ready node |
| F10 | QUERIES #1 | Handoff format vs MCP brief shape | Separate ownership of durable handoff template vs `ContextBrief` |

Rejected (this pass):

| Candidate | Reason |
|---|---|
| M02, M03, M04, M08, M10 | Occupied by the other Day-1 fixture set (F01–F05 mapping) |
| M01 | Near-duplicate of occupied M02 ownership boundary |
| M09 | Marked OOD / needs-graphify-refresh; incomplete evidence chain for a Decision fixture |
| H\*, G\*, P\*, E\* | Outside the MyAPI-rebuild Decision subject corpus for this first pass |

## Fixture conventions

- IDs beginning with `fixture_` are local fixture identifiers, not production IDs.
- `EvidenceRef.locator` uses a repository-relative path plus line range when the
  source lives in this repo; absolute path only for the external QUERIES harvest
  file under sibling `MyAPI/scratch/`.
- `commit_refs` contain verified commit objects from this Git history.
- `CodeRef` names only files and symbols inspected in the current worktree.
- `AcceptanceReceipt` appears only when an acceptance source is resolvable.
  Historical product choices landed as docs/code without a durable receipt are
  recorded under `acceptance_gap`.
- Dates use day precision when only commit/handoff dates are known.
- `DecisionCodeDivergence` records accepted/historical intent vs present material
  state when they disagree.

---

## F06 — First GDDP-linked durable handoff node

Source query: **“Which handoff documents the GDDP first durable handoff node for MyAPI?”** / **“Where is the first GDDP-linked MyAPI handoff node defined, and what does acceptance require?”**

Query origin: `evals/eval-bank-v0.md:56` (M06); harvest phrasing at
`/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:18`.

```yaml
fixture:
  id: fixture_f06_gddp_first_durable_handoff_node
  kind: expected_canonical_decision
  production_ingestion: false
  review_state: worker_first_pass

decision:
  type: Decision
  id: fixture_dec_gddp_first_durable_handoff_node
  project: myapi-rebuild
  statement: >-
    MyAPI's first project-local GDDP capability node is
    prove-first-durable-handoff: prove the first durable handoff and golden
    project brief before reader or MCP implementation, with acceptance criteria
    for two event traces, source verification, golden brief production, and
    cold-agent continuation.
  rationale: >-
    MyAPI earns trust when verified event history becomes a compact brief a cold
    agent can use correctly; more ingestion or retrieval machinery before that
    proof risks rebuilding the noisy single-pool failure mode from v0.
  status: active
  decided_at: 2026-07-17
  time_precision: day

  evidence_refs:
    - type: EvidenceRef
      id: fixture_ev_f06_query_eval
      source_type: evaluation_bank
      locator: evals/eval-bank-v0.md:56
      role: source_query
    - type: EvidenceRef
      id: fixture_ev_f06_query_harvest
      source_type: document
      locator: /Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:18
      role: source_query_phrasing
    - type: EvidenceRef
      id: fixture_ev_f06_handoff
      source_type: handoff
      locator: .handoffs/029-gddp-first-durable-handoff-node.md:9-34
      role: session_confirmation_and_resume
    - type: EvidenceRef
      id: fixture_ev_f06_node
      source_type: document
      locator: gddp/nodes/prove-first-durable-handoff.yaml:1-67
      role: supports_statement_and_acceptance_criteria
    - type: EvidenceRef
      id: fixture_ev_f06_project_graph
      source_type: document
      locator: gddp/project.yaml:1-44
      role: indexes_ready_node_and_locked_order

  commit_refs:
    - commit: f004101
      role: introduced_gddp_project_and_prove_first_node
    - commit: d799360
      role: aligned_node_artifacts_with_schema
    - commit: 783c49b
      role: documented_gddp_graph_handoff_029

  code_refs:
    - type: CodeRef
      path: gddp/nodes/prove-first-durable-handoff.yaml
      symbols: [prove-first-durable-handoff, acceptance_criteria, constraints]
      lines: 1-67
      role: current_node_definition
    - type: CodeRef
      path: gddp/project.yaml
      symbols: [project_id, nodes, execution_policy]
      lines: 1-44
      role: current_project_graph_index

  relations:
    - type: DecisionRelation
      relation: refined_by
      target_decision_id: fixture_dec_gddp_human_acceptance_owns_graph_truth
      note: Fixture-local link to F09; not a production DecisionRelation.

  acceptance_receipt: null
  acceptance_gap: >-
    Handoff 029 resume point still asks for Sab review of node language before
    execution; no durable AcceptanceReceipt EvidenceRef for promoting this
    DecisionCandidate to accepted project intent was found. Node status remains
    ready, not accepted/completed.

  decision_code_divergence:
    type: DecisionCodeDivergence
    state: open
    classification: target_not_yet_implemented
    expected: >-
      Two human-legible event traces, a source-verified golden project brief, and
      a cold-agent continuation pass exist before reader/MCP expansion.
    observed: >-
      The GDDP node and handoff exist; required event-trace artifacts and
      cold-agent acceptance run are not present as completed graph results in-repo.
    observed_at:
      - gddp/nodes/prove-first-durable-handoff.yaml:14-45
      - .handoffs/029-gddp-first-durable-handoff-node.md:32-34

  provenance_gaps:
    - Exact originating agent session turn ID for authoring the node is not linked.
    - required_artifacts listed on the node (decision.md, result-summary.md, etc.) are not present as completed node outputs in this worktree.
```

Expected `DecisionAnswer`: name `prove-first-durable-handoff` as the first
GDDP-linked MyAPI node, cite handoff `029` and commits `f004101`/`d799360`,
list acceptance criteria, and surface that human acceptance of the node work is
still pending.

---

## F07 — Golden briefs as evidence for the two public tools

Source query: **“What evidence paths prove the two MCP tools / golden briefs?”** / **“Which golden briefs exist and what intent do they encode?”**

Query origin: `evals/eval-bank-v0.md:55` (M05); harvest phrasing at
`/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:14`.

```yaml
fixture:
  id: fixture_f07_golden_briefs_evidence_paths
  kind: expected_canonical_decision
  production_ingestion: false
  review_state: worker_first_pass

decision:
  type: Decision
  id: fixture_dec_golden_briefs_are_tool_quality_bar
  project: myapi-rebuild
  statement: >-
    Expected outputs for the two public MCP tools are committed golden brief
    fixtures under evals/golden_briefs/: get_project_context_myapi_rebuild.md,
    get_project_context_pi_needle.md, and get_person_context_sab.md; the current
    MyMCP foundation loads those fixtures by tool name and selector slug.
  rationale: >-
    Golden briefs define the quality bar for ContextBrief returns before live
    assembly exists, so cold agents and tests can score known inputs without
    depending on retrieval luck.
  status: active
  decided_at: 2026-07-01
  time_precision: day

  evidence_refs:
    - type: EvidenceRef
      id: fixture_ev_f07_query_eval
      source_type: evaluation_bank
      locator: evals/eval-bank-v0.md:55
      role: source_query
    - type: EvidenceRef
      id: fixture_ev_f07_query_harvest
      source_type: document
      locator: /Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:14
      role: source_query_phrasing
    - type: EvidenceRef
      id: fixture_ev_f07_myapi_brief
      source_type: golden_brief
      locator: evals/golden_briefs/get_project_context_myapi_rebuild.md:1-44
      role: expected_project_tool_output
    - type: EvidenceRef
      id: fixture_ev_f07_person_brief
      source_type: golden_brief
      locator: evals/golden_briefs/get_person_context_sab.md:1-44
      role: expected_person_tool_output
    - type: EvidenceRef
      id: fixture_ev_f07_pi_brief
      source_type: golden_brief
      locator: evals/golden_briefs/get_project_context_pi_needle.md:1-43
      role: expected_second_project_fixture
    - type: EvidenceRef
      id: fixture_ev_f07_handoff
      source_type: handoff
      locator: .handoffs/026-cost-aware-mymcp-corpus-tiers.md:12-50
      role: session_confirms_golden_fixtures_landed

  commit_refs:
    - commit: f35059c
      role: introduced_three_golden_brief_fixtures
    - commit: 11d50fc
      role: wired_mcp_server_to_load_golden_fixtures

  code_refs:
    - type: CodeRef
      path: mcp/server.py
      symbols: [get_project_context, get_person_context, _context_envelope, _slug, GOLDEN_BRIEFS_DIR]
      lines: 1-63
      role: current_fixture_backed_doorway
    - type: CodeRef
      path: evals/golden_briefs/get_project_context_myapi_rebuild.md
      symbols: []
      lines: 1-44
      role: project_tool_expected_markdown
    - type: CodeRef
      path: evals/golden_briefs/get_person_context_sab.md
      symbols: []
      lines: 1-44
      role: person_tool_expected_markdown

  relations: []

  acceptance_receipt: null
  acceptance_gap: >-
    Fixtures were committed as expected outputs; no AcceptanceReceipt EvidenceRef
    records human promotion of a DecisionCandidate for this policy. Handoff 026
    is itself marked non-canonical until Sab verifies.

  decision_code_divergence:
    type: DecisionCodeDivergence
    state: open
    classification: partial_implementation
    expected: >-
      MCP tools return budgeted ContextBrief envelopes assembled from live Decision
      or corpus retrieval, scored against golden briefs.
    observed: >-
      mcp/server.py returns raw golden Markdown from disk; several golden brief
      evidence paths still point at removed project-documents/ paths rather than
      current project-docs/ locations.
    observed_at:
      - mcp/server.py:17-59
      - evals/golden_briefs/get_project_context_myapi_rebuild.md:25-30

  provenance_gaps:
    - Absolute path rewrite from project-documents/ to project-docs/ (commit 3b510d9) is not reflected inside golden brief evidence lines.
    - No stable session Evidence ID for the original golden-brief authoring turn.
```

Expected `DecisionAnswer`: list the three golden brief paths, map them to
`get_project_context` / `get_person_context`, cite `f35059c` and `11d50fc`, and
note the fixture-backed implementation gap.

---

## F08 — Portfolio layer chain L0 → L1 → L2 → L3

Source query: **“How does L0 corpus → L1 graphify → L2 packs → L3 MCP chain?”**

Query origin: `evals/eval-bank-v0.md:57` (M07); related harvest at
`/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:23`.

```yaml
fixture:
  id: fixture_f08_l0_l3_layer_chain
  kind: expected_canonical_decision
  production_ingestion: false
  review_state: worker_first_pass

decision:
  type: Decision
  id: fixture_dec_bottom_up_l0_l3_stack
  project: myapi-rebuild
  statement: >-
    The rebuild stack is strictly bottom-up: L0 corpus, L1 graphify extraction,
    L2 context-pack / ContextBrief synthesis, L3 two-tool MCP interface, with L4
    study/export as the human layer; the portfolio vertical slice is steps through
    get_project_context (L0→L3).
  rationale: >-
    Packs cannot assemble without a graph, and MCP cannot expose packs that do not
    exist; enforcing bottom-up dependency prevents another retrieval-first detour
    that skips durable structure.
  status: active
  decided_at: 2026-06-21
  time_precision: day

  evidence_refs:
    - type: EvidenceRef
      id: fixture_ev_f08_query_eval
      source_type: evaluation_bank
      locator: evals/eval-bank-v0.md:57
      role: source_query
    - type: EvidenceRef
      id: fixture_ev_f08_query_harvest
      source_type: document
      locator: /Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:23
      role: source_query_related_phrasing
    - type: EvidenceRef
      id: fixture_ev_f08_architecture_layers
      source_type: design_document
      locator: project-docs/ARCHITECTURE.md:73-98
      role: defines_L0_through_L4
    - type: EvidenceRef
      id: fixture_ev_f08_architecture_slice
      source_type: design_document
      locator: project-docs/ARCHITECTURE.md:395-422
      role: portfolio_vertical_slice_and_step_order
    - type: EvidenceRef
      id: fixture_ev_f08_project_brief
      source_type: project_brief
      locator: PROJECT-BRIEF.md:62-69
      role: historical_direction_names_four_layers
    - type: EvidenceRef
      id: fixture_ev_f08_context_language
      source_type: canonical_language
      locator: CONTEXT.md:51-63
      role: current_ContextBrief_MyAPI_MyMCP_terms

  commit_refs:
    - commit: 281c056
      role: introduced_portfolio_brief_and_agents_scaffold
    - commit: 79cfdf2
      role: captured_cost_aware_architecture_including_layers
    - commit: 3b510d9
      role: renamed_project_documents_to_project_docs_preserving_architecture
    - commit: f50d24e
      role: implemented_ContextBrief_code_contract_for_L2_shape

  code_refs:
    - type: CodeRef
      path: project-docs/ARCHITECTURE.md
      symbols: []
      lines: 73-98
      role: current_layer_definition
    - type: CodeRef
      path: context_refinery/context_packets.py
      symbols: [ContextBrief, from_packet, as_envelope, validate_envelope]
      lines: 131-219
      role: current_L2_brief_contract_substrate
    - type: CodeRef
      path: mcp/server.py
      symbols: [get_project_context, get_person_context]
      lines: 17-37
      role: current_L3_fixture_surface
    - type: CodeRef
      path: scripts/source_manifest.py
      symbols: [Source, build_manifest, build_corpus_manifest, classify_corpus_tier]
      lines: 21-250
      role: current_L0_source_inventory_substrate

  relations:
    - type: DecisionRelation
      relation: refined_by
      target_decision_id: null
      target_locator: IMPLEMENTATION-PLAN.md:9-57
      note: >-
        2026-08-10 Decision Graph plan reframes the internal knowledge unit as
        Decision while retaining ContextBrief as the answer envelope; no production
        Decision ID exists yet for that refinement.

  acceptance_receipt: null
  acceptance_gap: >-
    Layer architecture is evidenced by committed design docs and partial code
    substrates; no AcceptanceReceipt EvidenceRef for this Decision was found.

  decision_code_divergence:
    type: DecisionCodeDivergence
    state: open
    classification: partial_implementation
    expected: >-
      Live L0→L1→L2→L3 path produces budgeted ContextBriefs from corpus and graph,
      with Decision graph truth behind the envelope.
    observed: >-
      L0 inventory (source_manifest), L2 dataclass (ContextBrief), and L3 fixture
      MCP exist; unified L1 graph store, brief assembly pipeline, and Decision-backed
      retrieval do not. IMPLEMENTATION-PLAN.md now centers Decision Graph nodes M1–M8
      rather than the older L0–L4 phase language cited by golden briefs.
    observed_at:
      - scripts/source_manifest.py:135-250
      - context_refinery/context_packets.py:131-219
      - mcp/server.py:17-59
      - IMPLEMENTATION-PLAN.md:92-107

  provenance_gaps:
    - Exact session that first locked the L0–L4 diagram is not assigned a stable Evidence ID.
    - eval-bank gold still says layers live in IMPLEMENTATION-PLAN; current plan text is Decision Graph, while ARCHITECTURE.md retains the layer diagram.
```

Expected `DecisionAnswer`: state the bottom-up L0–L3 chain from
`project-docs/ARCHITECTURE.md`, point at current L0/L2/L3 code substrates, and
surface the partial-implementation divergence.

---

## F09 — Human acceptance owns GDDP graph truth

Source query: **“Who advances the GDDP node `prove-first-durable-handoff` — human acceptance only, or runtime?”**

Query origin:
`/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:9`.

```yaml
fixture:
  id: fixture_f09_human_acceptance_owns_gddp_graph_truth
  kind: expected_canonical_decision
  production_ingestion: false
  review_state: worker_first_pass

decision:
  type: Decision
  id: fixture_dec_gddp_human_acceptance_owns_graph_truth
  project: myapi-rebuild
  statement: >-
    Human review owns acceptance and any change to MyAPI GDDP graph truth;
    runtime/executors may perform allowed work modes but must not silently advance
    or rewrite node acceptance.
  rationale: >-
    Separating execution from acceptance keeps graph progression auditable and
    prevents agent runs from becoming self-authorizing truth updates — the same
    boundary the broader Decision architecture later names as AcceptanceReceipt.
  status: active
  decided_at: 2026-07-17
  time_precision: day

  evidence_refs:
    - type: EvidenceRef
      id: fixture_ev_f09_query
      source_type: document
      locator: /Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:9
      role: source_query
    - type: EvidenceRef
      id: fixture_ev_f09_node_constraint
      source_type: document
      locator: gddp/nodes/prove-first-durable-handoff.yaml:47-57
      role: supports_statement
    - type: EvidenceRef
      id: fixture_ev_f09_project_policy
      source_type: document
      locator: gddp/project.yaml:40-44
      role: execution_policy_requires_human_review_gate
    - type: EvidenceRef
      id: fixture_ev_f09_handoff
      source_type: handoff
      locator: .handoffs/029-gddp-first-durable-handoff-node.md:32-34
      role: resume_requires_human_review_before_downstream_work
    - type: EvidenceRef
      id: fixture_ev_f09_truth_hierarchy
      source_type: implementation_plan
      locator: IMPLEMENTATION-PLAN.md:63-70
      role: later_language_aligns_acceptance_with_truth_model

  commit_refs:
    - commit: f004101
      role: introduced_node_constraint_human_review_owns_acceptance
    - commit: 783c49b
      role: handoff_records_human_review_resume_gate
    - commit: 0b28418
      role: Decision_plan_restates_human_acceptance_boundary

  code_refs:
    - type: CodeRef
      path: gddp/nodes/prove-first-durable-handoff.yaml
      symbols: [constraints, allowed_execution_modes, acceptance_criteria]
      lines: 47-57
      role: current_acceptance_authority_constraint
    - type: CodeRef
      path: gddp/project.yaml
      symbols: [execution_policy]
      lines: 40-44
      role: current_project_execution_policy

  relations:
    - type: DecisionRelation
      relation: constrains
      target_decision_id: fixture_dec_gddp_first_durable_handoff_node
      note: Fixture-local link to F06.

  acceptance_receipt: null
  acceptance_gap: >-
    The decision asserts that AcceptanceReceipt-class authority is human-owned, but
    this fixture itself has no production AcceptanceReceipt EvidenceRef. That gap is
    intentional and material to the claim.

  decision_code_divergence:
    type: DecisionCodeDivergence
    state: open
    classification: target_not_yet_implemented
    expected: >-
      Runtime jobs produce evidence/artifacts; only human acceptance mutates graph
      truth and emits durable AcceptanceReceipt records for Decisions/nodes.
    observed: >-
      Constraints exist in YAML; no runtime acceptance-receipt pipeline or graph
      writeback guard implementation is present in this repository beyond the
      declared node/project policy.
    observed_at:
      - gddp/nodes/prove-first-durable-handoff.yaml:47-57
      - gddp/project.yaml:40-44

  provenance_gaps:
    - No runtime code path yet to verify non-writeback behavior end to end in MyAPI-rebuild.
    - Cross-repo gddp-runtime ownership details live outside this subject corpus.
```

Expected `DecisionAnswer`: answer **human acceptance only**, cite the node
constraint and project execution policy, and note missing runtime receipt
machinery as an open divergence.

---

## F10 — Durable handoff format vs MCP brief response shape

Source query: **“Who owns the durable handoff format vs the MCP brief response shape?”**

Query origin:
`/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:6`.

```yaml
fixture:
  id: fixture_f10_handoff_format_vs_contextbrief_shape
  kind: expected_canonical_decision
  production_ingestion: false
  review_state: worker_first_pass

decision:
  type: Decision
  id: fixture_dec_handoff_vs_contextbrief_ownership
  project: myapi-rebuild
  statement: >-
    Durable handoffs are the continuity/evidence unit (session-boxed event and
    decision records under .handoffs/ with a fixed agent-section template);
    ContextBrief is the budgeted MCP/query response shape (machine metadata +
    human markdown) owned by the MyAPI brief contract, not a second handoff format.
  rationale: >-
    Collapsing handoff authoring and brief response into one document type reintroduces
    dump-shaped retrieval. Keeping the formats separate lets handoffs remain durable
    evidence while ContextBriefs stay small, intent-routed answers.
  status: active
  decided_at: 2026-07-01
  time_precision: day

  evidence_refs:
    - type: EvidenceRef
      id: fixture_ev_f10_query
      source_type: document
      locator: /Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md:6
      role: source_query
    - type: EvidenceRef
      id: fixture_ev_f10_anchor
      source_type: design_document
      locator: project-docs/REBUILD-CONTEXT-ANCHOR.md:11-30
      role: separates_event_trace_handoff_vault_and_context_brief
    - type: EvidenceRef
      id: fixture_ev_f10_handoff_template
      source_type: handoff
      locator: .handoffs/000-template.md:1-28
      role: durable_handoff_format_contract
    - type: EvidenceRef
      id: fixture_ev_f10_packet_contract
      source_type: design_document
      locator: project-docs/context-packet-contract-2026-07-01.md:1-26
      role: defines_ContextBrief_output_shape
    - type: EvidenceRef
      id: fixture_ev_f10_architecture_brief
      source_type: design_document
      locator: project-docs/ARCHITECTURE.md:176-194
      role: ContextBrief_as_L2_output_contract
    - type: EvidenceRef
      id: fixture_ev_f10_language
      source_type: canonical_language
      locator: CONTEXT.md:51-54
      role: current_ContextBrief_definition

  commit_refs:
    - commit: 3cac9da
      role: introduced_handoff_template_and_checkpoint_policy
    - commit: 678b9b7
      role: normalized_handoffs_directory
    - commit: f50d24e
      role: introduced_ContextBrief_code_contract
    - commit: 0b28418
      role: restates_ContextBrief_as_answer_envelope_not_canonical_Decision

  code_refs:
    - type: CodeRef
      path: .handoffs/000-template.md
      symbols: []
      lines: 1-28
      role: current_durable_handoff_template
    - type: CodeRef
      path: context_refinery/context_packets.py
      symbols: [ContextBrief, from_packet, validate_envelope, as_envelope, render_brief_markdown]
      lines: 131-249
      role: current_brief_response_contract
    - type: CodeRef
      path: mcp/server.py
      symbols: [get_project_context, get_person_context, _context_envelope]
      lines: 17-59
      role: public_surface_returns_brief_envelope_not_raw_handoff

  relations:
    - type: DecisionRelation
      relation: refined_by
      target_decision_id: null
      target_locator: CONTEXT.md:22-54
      note: >-
        Decision becomes the canonical knowledge unit; ContextBrief remains the
        delivery envelope. Durable handoffs remain evidence sources.

  acceptance_receipt: null
  acceptance_gap: >-
    Format split is evidenced by committed template + ContextBrief contract +
    language docs; no AcceptanceReceipt EvidenceRef was found for this Decision.

  decision_code_divergence:
    type: DecisionCodeDivergence
    state: open
    classification: partial_implementation
    expected: >-
      MyMCP/MyAPI serve ContextBrief envelopes assembled from Decisions and durable
      handoff evidence without requiring agents to parse handoff templates as the
      answer format.
    observed: >-
      ContextBrief dataclasses and handoff template both exist; mcp/server.py still
      returns golden fixture markdown rather than ContextBrief.as_envelope() built
      from handoff-linked Decisions.
    observed_at:
      - context_refinery/context_packets.py:197-219
      - mcp/server.py:39-59
      - .handoffs/000-template.md:8-26

  provenance_gaps:
    - No single session Evidence ID pins the first explicit 'handoff format vs brief shape' ownership statement.
    - CONTEXT.md Decision language (2026-08-10) refines but does not replace the handoff/brief split.
```

Expected `DecisionAnswer`: answer that **handoffs own continuity format** and
**ContextBrief owns MCP response shape**, cite template + `ContextBrief` code,
and surface the partial wiring gap.

---

## Verification log (worker first pass)

Commands intended for re-check on Mac in this worktree:

```bash
# Run on Mac:
cd /Users/sab-mini/repos/MyAPI-rebuild
git rev-parse --verify f004101^{commit} d799360^{commit} 783c49b^{commit} f35059c^{commit} 11d50fc^{commit} f50d24e^{commit} 281c056^{commit} 79cfdf2^{commit} 3b510d9^{commit} 3cac9da^{commit} 678b9b7^{commit} 0b28418^{commit}
test -f evals/golden_briefs/get_project_context_myapi_rebuild.md
test -f evals/golden_briefs/get_person_context_sab.md
test -f evals/golden_briefs/get_project_context_pi_needle.md
test -f gddp/nodes/prove-first-durable-handoff.yaml
test -f gddp/project.yaml
test -f .handoffs/029-gddp-first-durable-handoff-node.md
test -f project-docs/ARCHITECTURE.md
test -f project-docs/REBUILD-CONTEXT-ANCHOR.md
test -f context_refinery/context_packets.py
test -f mcp/server.py
test -f scripts/source_manifest.py
test -f /Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md
python3 -c "import ast; from pathlib import Path; t=ast.parse(Path('mcp/server.py').read_text()); print([n.name for n in t.body if isinstance(n, ast.FunctionDef)])"
python3 -c "import ast; from pathlib import Path; t=ast.parse(Path('context_refinery/context_packets.py').read_text()); print([n.name for n in t.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))])"
```

Worker verification performed before commit: all listed commit objects resolve;
all listed repo paths exist; named Python symbols parse from live AST; QUERIES
and eval-bank line locators match live files; YAML fixture blocks above were
mechanically load-checked as multi-document YAML fragments.
