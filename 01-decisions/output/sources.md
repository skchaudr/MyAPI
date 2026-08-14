# Authoritative decision sources

Stage B source manifest for MyAPI Part 1. This is a closed, inspectable source set: extract the 2026-08-08 reviewed decision set from the decision-truth sources, use supporting sources only to clarify rationale or provenance, and do not promote material from the exclusions.

## Authority order

When sources disagree, apply this order:

1. Sab's review mark controls inclusion and status.
2. The normalized decision note supplies the canonical decision wording.
3. The schema controls object shape, required provenance, and relationships.
4. Anchors, plans, and handoffs may clarify rationale or evidence, but cannot create or reverse a decision.

The closed review contains D01–D18: D01–D10 and D12–D18 are the 17 accepted extraction candidates; D11 is explicitly dropped. Preserve D11 as rejection evidence, not as an accepted decision. The two copies of the normalized note have SHA-256 `4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558` and are byte-identical as inspected on 2026-08-14.

## Decision-truth sources

| Source | Authority rationale |
|---|---|
| `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` | Sab-closed review sheet; its Y/N marks are the final inclusion and status authority for D01–D18. |
| `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` | Repo-local canonical prose for the 17 accepted decisions, including rationale and the explicit D11 drop. |
| `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` | Prior normalized keeper named by the review sheet; it independently confirms the durable Corpus v1.0 decision artifact and currently matches the repo-local copy byte for byte. |

Treat the repo-local normalized note as the working copy. Treat the Corpus v1.0 copy as a parity witness, not as a second decision record; a future mismatch must stop extraction for reconciliation rather than silently picking one.

## Supporting authority and provenance

These sources may support fields on decisions already admitted by the review sheet. They do not expand the 17-decision extraction set.

| Source | Authority rationale |
|---|---|
| `/Users/sab-mini/repos/GDDP v MyAPI Part 1 - the first slice.md` | Governing operator memo; fixes Part 1 to canonical decisions → corpus → Khoj → evaluation and defines the stop boundary. |
| `01-decisions/CONTEXT.md` | Stage-room contract; limits this room to decision schema, extraction, normalization, and validation. |
| `01-decisions/output/decision-schema.md` | Accepted Stage A contract for object fields, provenance, status, supersession, and relationship invariants. |
| `project-docs/corpus-work-2026-08/CORPUS-TARGET-SHAPE.md` | Sab-dated corpus policy supporting D14–D16 rationale: query-grounded curation, decisions, and small evidence-linked git receipts. |
| `project-docs/REBUILD-CONTEXT-ANCHOR.md` | Cold-start narrative anchor; authoritative for rebuild vocabulary and the Graphify/Khoj and handoff-vault framing relevant to D14–D15. |
| `project-docs/ARCHITECTURE.md` | Canonical build-plan companion to the rebuild anchor; supports current layer boundaries where an accepted decision needs architectural context. |
| `.handoffs/030-corpus-vm-semantic-graphify.md` | Empirical provenance for the closed review artifact, its 17 accepted decisions, the corpus policy, and the move of later corpus work to the VM. |

## Deliberate exclusions

| Excluded source or class | Reason |
|---|---|
| D11 in `DECISIONS-REVIEW-SHEET.md` and both normalized decision-note copies | Sab marked it N; it is rejection evidence and must not enter the accepted decision set. |
| The MCP naming/supersession examples in `01-decisions/output/decision-schema.md` | They demonstrate schema behavior but are outside the closed D01–D18 review set, so examples cannot mint Stage B decisions. |
| `project-docs/corpus-work-2026-08/QUERIES-myapi.md` | Evaluation questions define desired answer coverage, not accepted decisions. |
| `project-docs/corpus-work-2026-08/QUERIES-gddp.md` | Evaluation questions define desired answer coverage, not accepted decisions. |
| `project-docs/corpus-work-2026-08/QUERIES-pi.md` | Evaluation questions define desired answer coverage, not accepted decisions. |
| `project-docs/corpus-work-2026-08/QUERY-GROUNDING-PASS1.md` | Derivative harvesting/grounding synthesis; useful for retrieval work but lacks Sab's per-decision review marks. |
| `project-docs/corpus-work-2026-08/WORK-MOVED-TO-VM.md` | Workplace pointer only; it contains no decision record or acceptance evidence. |
| Other files under `Corpus v1.0/` | Historical/cold substrate is outside this closed last-two-weeks decision slice unless a later reviewed manifest explicitly admits a path. |
| `project-docs/source-of-truth-anchors/*.md` | Older operational retrieval anchors are dated snapshots and were not reviewed as members of D01–D18; some also describe the superseded bulk-corpus state. |
| `.handoffs/*` other than `.handoffs/030-corpus-vm-semantic-graphify.md` | Handoffs are empirical leads, not blanket decision authority; no other handoff is admitted without an explicit review mark. |
| `PROJECT-BRIEF.md`, `README.md`, `IMPLEMENTATION-PLAN.md`, and general project docs | Project framing and implementation plans may contain proposals or stale state, but they are not the closed decision review or its normalized keeper. |
| Raw CLI sessions, chat exports, Obsidian bulk notes, and `scratch/corpus-hot/**` | Unreviewed evidence can suggest candidates but cannot enter this review-bounded extraction set. |
| `graphify-out/**` | Structural/generated analysis is evidence navigation, not semantic decision authority, and graph truth must remain untouched. |
| Git history beyond refs already cited by an admitted decision | Commits can prove enactment but do not by themselves establish Sab's decision wording or review status. |
| Runtime databases, Khoj indexes, GDDP job state, and VM corpus state | Mutable runtime state is outside this filesystem inventory and must never be read as or written into decision truth. |

## Stage B use rule

For each extracted object, cite the review sheet and the normalized repo-local note in `sources[]`; cite the Corpus v1.0 keeper as parity provenance. Add supporting sources only where they directly substantiate a field. If a candidate appears only in an excluded source, leave it out and route it through a future explicit Sab review instead of silently widening scope.
