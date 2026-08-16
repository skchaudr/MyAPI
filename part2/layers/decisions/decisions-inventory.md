# Canonical decisions inventory

This file inventories the semantic knowledge represented by the
Part 1 historical-control payload. It does not replace that payload.
A normalized Part 2 representation, if produced later, must live
under `part2/` and cite this SHA-256; it cannot replace the control.

- control_path: `01-decisions/output/decisions-canonical.jsonl`
- part1_payload_sha256: `09c15aebd3a424e7f09ce2c27985fa0cbc24a23d9c474182ea4c912b926750a8`
- pin_id: `part1_canonical_jsonl`
- bytes: 26917
- lines: 17
- objects: 17
- ids: `D01 D02 D03 D04 D05 D06 D07 D08 D09 D10 D12 D13 D14 D15 D16 D17 D18`
- source_class: `decisions`
- authority_rank: `2`
- native_source_id_form: `decisions:D14`
- replaces_edges: `0` (key omitted on all 17 objects; not an empty list)
- replaced_by_edges: `0` (key omitted on all 17 objects; not JSON null)
- related_edges: `1` (`D18` `companion` `D17`; inverse `D17`→`D18` omitted)
- git_refs_edges: `0` (key omitted on all 17 objects)
- measured: live SHA-256, JSON parse, object/id counts, key presence
- labeled_absence: Q3 is structurally unanswerable from this payload
- D11: not a canonical object; rejection evidence only (`EX-d11-rejected`)
- schema-example MCP pair: not inventory members (`EX-schema-example`)

Canonical headings below are exactly the JSONL `id` values in file
order. Each object has the same six subsections. Omitted payload
keys are written as the token `None`, not skipped and not coerced
to `[]` / `null` inside the control file.

# Rejection evidence

## D11 (rejected)

- exclusion_reason: `EX-d11-rejected`
- inclusion_status: excluded from the closed canonical set
- review_mark: `N`
- review_sheet: `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- review_sheet_row: `D11 | N | Local Pi GDDP lane as fleet foundation — dropped`
- wording_note: `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
- wording_note_record: `Dropped: **D11**`
- control_payload: absent from `01-decisions/output/decisions-canonical.jsonl`
- this heading is not `## D11` and is not a canonical inventory entry

# Canonical objects

## D01

### Decision
- id: `D01`
- item_id: `decisions:D01`
- source_class: `decisions`
- schema_version: `1.0`
- project: `GDDP`
- title: GDDP role vs harness
- summary: GDDP constrains/verifies loop; not harness rebuild
- statement: GDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: None
- notes: None

### Rationale
- rationale: Keeps GDDP a control/evidence layer around replaceable executors (Pi, Jules, Claude, etc.).
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (3):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D01 | Y | GDDP constrains/verifies loop; not harness rebuild
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: GDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: GDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop.
- evidence_paths (2):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- git_refs
  None

## D02

### Decision
- id: `D02`
- item_id: `decisions:D02`
- source_class: `decisions`
- schema_version: `1.0`
- project: `GDDP`
- title: Job disposal path
- summary: Dedicated job disposal; no node_status/graph mutate
- statement: Job failure uses a dedicated disposal path (`mark_job_failed` + durable reason/receipt). Do not use `node_status` and do not mutate graph truth for disposal.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: None
- notes: None

### Rationale
- rationale: Separates runtime job bookkeeping from graph/node truth.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (3):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D02 | Y | Dedicated job disposal; no node_status/graph mutate
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: Job failure uses a dedicated disposal path (`mark_job_failed` + durable reason/receipt). Do not use `node_status` and do not mutate graph truth for disposal.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Job failure uses a dedicated disposal path (`mark_job_failed` + durable reason/receipt). Do not use `node_status` and do not mutate graph truth for disposal.
- evidence_paths (2):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- git_refs
  None

## D03

### Decision
- id: `D03`
- item_id: `decisions:D03`
- source_class: `decisions`
- schema_version: `1.0`
- project: `GDDP`
- title: No silent system-python eval fallback
- summary: No system-python eval fallback
- statement: If project `.venv` is missing, do not fall back to system Python. Report `probe_unavailable` unless the project declares an alternate evaluation environment.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: None
- notes: None

### Rationale
- rationale: Prevents false-green evidence from wrong dependencies.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (3):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D03 | Y | No system-python eval fallback
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: If project `.venv` is missing, do not fall back to system Python. Report `probe_unavailable` unless the project declares an alternate evaluation environment.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: If project `.venv` is missing, do not fall back to system Python. Report `probe_unavailable` unless the project declares an alternate evaluation environment.
- evidence_paths (2):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- git_refs
  None

## D04

### Decision
- id: `D04`
- item_id: `decisions:D04`
- source_class: `decisions`
- schema_version: `1.0`
- project: `GDDP`
- title: `agent` is literal, not wildcard
- summary: `agent` literal, not wildcard
- statement: Allowed mode `agent` is compared literally. It is not a wildcard. No executor-inheritance or wildcard-permission machinery.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: None
- notes: None

### Rationale
- rationale: Stops “clever” permission expansion; node allow-lists mean exactly what they say.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (3):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D04 | Y | `agent` literal, not wildcard
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: Allowed mode `agent` is compared literally. It is not a wildcard. No executor-inheritance or wildcard-permission machinery.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Allowed mode `agent` is compared literally. It is not a wildcard. No executor-inheritance or wildcard-permission machinery.
- evidence_paths (2):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- git_refs
  None

## D05

### Decision
- id: `D05`
- item_id: `decisions:D05`
- source_class: `decisions`
- schema_version: `1.0`
- project: `GDDP`
- title: Empty allow-list → operator / default executor
- summary: Empty allow-list → operator/default executor
- statement: When a node has not constrained executors, the operator’s explicit pick wins. `auto` resolves to configured `default_executor`.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: None
- notes: None

### Rationale
- rationale: Operator authority is the point of the allow-list; empty list must not strand dispatch.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (3):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D05 | Y | Empty allow-list → operator/default executor
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: When a node has not constrained executors, the operator’s explicit pick wins. `auto` resolves to configured `default_executor`.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: When a node has not constrained executors, the operator’s explicit pick wins. `auto` resolves to configured `default_executor`.
- evidence_paths (2):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- git_refs
  None

## D06

### Decision
- id: `D06`
- item_id: `decisions:D06`
- source_class: `decisions`
- schema_version: `1.0`
- project: `GDDP`
- title: Bookkeeping mismatch is evidence, not a hard block
- summary: Bookkeeping mismatch → evidence not hard block
- statement: Safeguards that only catch runtime bookkeeping mismatch (not genuinely unsafe action) should surface as evaluation evidence, not hard-reject usable work.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: None
- notes: None

### Rationale
- rationale: Protects momentum; commit/HEAD bookkeeping churn must not force full node reruns by default.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (3):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D06 | Y | Bookkeeping mismatch → evidence not hard block
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: Safeguards that only catch runtime bookkeeping mismatch (not genuinely unsafe action) should surface as evaluation evidence, not hard-reject usable work.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Safeguards that only catch runtime bookkeeping mismatch (not genuinely unsafe action) should surface as evaluation evidence, not hard-reject usable work.
- evidence_paths (2):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- git_refs
  None

## D07

### Decision
- id: `D07`
- item_id: `decisions:D07`
- source_class: `decisions`
- schema_version: `1.0`
- project: `GDDP`
- title: Human is last provisional gate
- summary: Human last provisional gate
- statement: Evaluator is second-to-last gate; human is last on provisional nodes. Reject returns the node to `ready` for retry.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: None
- notes: None

### Rationale
- rationale: Defines acceptance authority and retry semantics.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (3):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D07 | Y | Human last provisional gate
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: Evaluator is second-to-last gate; human is last on provisional nodes. Reject returns the node to `ready` for retry.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Evaluator is second-to-last gate; human is last on provisional nodes. Reject returns the node to `ready` for retry.
- evidence_paths (2):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- git_refs
  None

## D08

### Decision
- id: `D08`
- item_id: `decisions:D08`
- source_class: `decisions`
- schema_version: `1.0`
- project: `GDDP`
- title: Reject revokes dependent admission
- summary: Reject revokes dependent admission
- statement: Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: None
- notes: None

### Rationale
- rationale: Doctrine: rejection must not leave downstream work still admitted.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (3):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D08 | Y | Reject revokes dependent admission
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.
- evidence_paths (2):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- git_refs
  None

## D09

### Decision
- id: `D09`
- item_id: `decisions:D09`
- source_class: `decisions`
- schema_version: `1.0`
- project: `GDDP`
- title: Nodes enter graphs only via import tool
- summary: Nodes only via import tool
- statement: Nodes enter graphs only through the import tool. No hand-authored graph mutation shortcuts.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: None
- notes: None

### Rationale
- rationale: One write path; prevents silent graph drift and review bypass.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (3):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D09 | Y | Nodes only via import tool
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: Nodes enter graphs only through the import tool. No hand-authored graph mutation shortcuts.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Nodes enter graphs only through the import tool. No hand-authored graph mutation shortcuts.
- evidence_paths (2):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- git_refs
  None

## D10

### Decision
- id: `D10`
- item_id: `decisions:D10`
- source_class: `decisions`
- schema_version: `1.0`
- project: `GDDP`
- title: No merge-to-main by default on acceptance
- summary: No merge-to-main by default
- statement: Executor results live on worktree/result-branch. Acceptance does not merge to `main` by default.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: None
- notes: None

### Rationale
- rationale: Keeps main clean; acceptance ≠ land.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (3):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D10 | Y | No merge-to-main by default
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: Executor results live on worktree/result-branch. Acceptance does not merge to `main` by default.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Executor results live on worktree/result-branch. Acceptance does not merge to `main` by default.
- evidence_paths (2):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- git_refs
  None

## D12

### Decision
- id: `D12`
- item_id: `decisions:D12`
- source_class: `decisions`
- schema_version: `1.0`
- project: `GDDP`
- title: Prefer flow-on-provisional unless strict canary
- summary: Prefer flow-on-provisional
- statement: Default preference is flow-on-provisional (momentum; review can lag execution). Strict canary (`frontier_auto_advance: false`) only when explicitly flipped.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: None
- notes: None

### Rationale
- rationale: Chooses speed-with-review-lag over stop-the-line canary as the normal mode.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (3):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D12 | Y | Prefer flow-on-provisional
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: Default preference is flow-on-provisional (momentum; review can lag execution). Strict canary (`frontier_auto_advance: false`) only when explicitly flipped.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Default preference is flow-on-provisional (momentum; review can lag execution). Strict canary (`frontier_auto_advance: false`) only when explicitly flipped.
- evidence_paths (2):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- git_refs
  None

## D13

### Decision
- id: `D13`
- item_id: `decisions:D13`
- source_class: `decisions`
- schema_version: `1.0`
- project: `GDDP`
- title: Prove pass-write and reject-revoke before mission scale
- summary: Prove pass-write + reject-revoke before mission
- statement: Before mission-scale work depends on the gate system, run one tiny live heartbeat node and prove both: pass → admission token written; reject → token revoked and dependents blocked again.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: None
- notes: The closed review sheet records D13 as clarified, then accepted (Y).

### Rationale
- rationale: Cheap dress rehearsal so the first real proof is not a full mission.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (3):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D13 | Y | Prove pass-write + reject-revoke before mission
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: Before mission-scale work depends on the gate system, run one tiny live heartbeat node and prove both: pass → admission token written; reject → token revoked and dependents blocked again.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Before mission-scale work depends on the gate system, run one tiny live heartbeat node and prove both: pass → admission token written; reject → token revoked and dependents blocked again.
- evidence_paths (2):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- git_refs
  None

## D14

### Decision
- id: `D14`
- item_id: `decisions:D14`
- source_class: `decisions`
- schema_version: `1.0`
- project: `MyAPI/Khoj`
- title: Khoj corpus composition
- summary: Khoj = ~687 docs + hand-picked digests
- statement: Curated Khoj corpus = existing project docs/notes (~687) + hand-picked session digests. Not bulk dump of ~4k raw transcripts.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: None
- notes: None

### Rationale
- rationale: Signal over volume for semantic retrieval.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (7):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D14 | Y | Khoj = ~687 docs + hand-picked digests
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: Curated Khoj corpus = existing project docs/notes (~687) + hand-picked session digests. Not bulk dump of ~4k raw transcripts.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Curated Khoj corpus = existing project docs/notes (~687) + hand-picked session digests. Not bulk dump of ~4k raw transcripts.
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/CORPUS-TARGET-SHAPE.md` note=supports corpus-selection rationale. Quote: Full Obsidian vault dumps
  - kind=`anchor` ref=`project-docs/REBUILD-CONTEXT-ANCHOR.md` note=supports handoff-shaped corpus rationale. Quote: The fix is shape, not more data: sanitize → normalize → presentable narrative with evidence pointers (event traces), then briefs/MCP — not bigger dumps.
  - kind=`memo` ref=`project-docs/ARCHITECTURE.md` note=supports fresh, lean corpus rationale. Quote: MyAPI v0 proved that a large cold corpus can drown the active truth. The rebuild uses a fresh active window by default
  - kind=`handoff` ref=`.handoffs/030-corpus-vm-semantic-graphify.md` note=empirical provenance for corpus policy and the closed set. Quote: Full Obsidian vault dump to Khoj was wrong; stripped on VM.
- evidence_paths (3):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
  - `project-docs/corpus-work-2026-08/CORPUS-TARGET-SHAPE.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
  - `project-docs/REBUILD-CONTEXT-ANCHOR.md`
  - `project-docs/ARCHITECTURE.md`
  - `.handoffs/030-corpus-vm-semantic-graphify.md`
- git_refs
  None

## D15

### Decision
- id: `D15`
- item_id: `decisions:D15`
- source_class: `decisions`
- schema_version: `1.0`
- project: `MyAPI/Pi/GDDP`
- title: Graphify structural, Khoj semantic
- summary: Graphify structural; Khoj semantic
- statement: Graphify (`graph.json`, reports, `graphify query` paths) stays the structural layer. Khoj is the semantic answer layer over normalized notes, including these decision notes.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: None
- notes: None

### Rationale
- rationale: Agents need path structure *and* answered meaning; neither replaces the other alone.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (5):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D15 | Y | Graphify structural; Khoj semantic
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: Graphify (`graph.json`, reports, `graphify query` paths) stays the structural layer. Khoj is the semantic answer layer over normalized notes, including these decision notes.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Graphify (`graph.json`, reports, `graphify query` paths) stays the structural layer. Khoj is the semantic answer layer over normalized notes, including these decision notes.
  - kind=`anchor` ref=`project-docs/REBUILD-CONTEXT-ANCHOR.md` note=supports Graphify's structural role. Quote: Graphify: current code structure map only — not git history as a graph.
  - kind=`memo` ref=`project-docs/ARCHITECTURE.md` note=supports the separate Graphify and Khoj layers. Quote: MyAPI can keep using the existing Khoj RAG engine on the Google Cloud VM as a retrieval backend while the rebuild experiments with a radically fresher corpus.
- evidence_paths (3):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
  - `project-docs/REBUILD-CONTEXT-ANCHOR.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
  - `project-docs/ARCHITECTURE.md`
- git_refs
  None

## D16

### Decision
- id: `D16`
- item_id: `decisions:D16`
- source_class: `decisions`
- schema_version: `1.0`
- project: `MyAPI`
- title: Decision scan order
- summary: Scan last 2w then full history
- statement: Scan session transcripts for decisions last-2-weeks first, then widen to full history.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: `ops`
- notes: None

### Rationale
- rationale: Newest operator intent first; full archive is phase 2.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (3):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D16 | Y | Scan last 2w then full history
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: Scan session transcripts for decisions last-2-weeks first, then widen to full history.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Scan session transcripts for decisions last-2-weeks first, then widen to full history.
- evidence_paths (2):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- git_refs
  None

## D17

### Decision
- id: `D17`
- item_id: `decisions:D17`
- source_class: `decisions`
- schema_version: `1.0`
- project: `Pi`
- title: Read code before new machinery
- summary: Read code; reject needless machinery
- statement: Verify each claim against live code before designing workarounds. Reject new machinery when correcting a config word fixes the problem.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: `agent-ops`
- notes: None

### Rationale
- rationale: Stops assumption→workaround→load-bearing architecture loops.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
None

### Evidence references
- sources (3):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D17 | Y | Read code; reject needless machinery
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: Verify each claim against live code before designing workarounds. Reject new machinery when correcting a config word fixes the problem.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Verify each claim against live code before designing workarounds. Reject new machinery when correcting a config word fixes the problem.
- evidence_paths (2):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- git_refs
  None

## D18

### Decision
- id: `D18`
- item_id: `decisions:D18`
- source_class: `decisions`
- schema_version: `1.0`
- project: `Pi`
- title: No load-bearing unverified assumptions
- summary: No load-bearing unverified assumptions
- statement: Unverified assumptions must not become load-bearing architecture.
- status: `accepted`
- decided_on: `2026-08-08`
- decided_by: `Sab`
- review_mark: `Y`
- confidence: `high`
- tags: `agent-ops`
- notes: None

### Rationale
- rationale: Companion rule to D17; compounds with multi-agent proposal chains.
- alternatives_considered: None
- consequences: None

### Replaces
None

### Replaced-by
None

### Relationships
- related_decisions[0].target_id: `D17`
- related_decisions[0].rel: `companion`
- related_decisions[0].note: The accepted rationale explicitly identifies D18 as a companion rule to D17.

### Evidence references
- sources (3):
  - kind=`review_sheet` ref=`project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` note=inclusion and status authority. Quote: D18 | Y | No load-bearing unverified assumptions
  - kind=`memo` ref=`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` note=repo-local decision wording. Quote: Unverified assumptions must not become load-bearing architecture.
  - kind=`other` ref=`/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` note=byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Unverified assumptions must not become load-bearing architecture.
- evidence_paths (2):
  - `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
  - `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
- sources_not_in_evidence_paths:
  - `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- git_refs
  None
