# Canonical decision-set validation report

**Node:** `node-05-validate-decision-set`  
**Execution attempt:** `job_20260814T214732845a5af48c5dcf:attempt:0`  
**Validated:** 2026-08-14  
**Base commit:** `bdf55a6bed363579a84aeb60ea7e403a19b0ce47`  
**Overall result:** **PASS — the 17-object canonical set is structurally valid, complete against the closed review, and ready for the Stage C gate.**

## Inputs fixed for this validation

| Input | SHA-256 |
|---|---|
| `01-decisions/output/decision-schema.md` | `41289d2b30b1069897db4d3a3f9d2d1431a1c55e15039b82c81b7199dd25f636` |
| `01-decisions/output/sources.md` | `59ea400b5b682337ebcc51e8d587d600a3412690513bcd67433e79a31d56587e` |
| `01-decisions/output/decisions-raw.jsonl` | `70c54903cf55855b3163b056254cc94583af616a03d20d394d6f673b29b35956` |
| `01-decisions/output/decisions-canonical.jsonl` | `09c15aebd3a424e7f09ce2c27985fa0cbc24a23d9c474182ea4c912b926750a8` |
| `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` | `e0eddc85c0a24b1a5234f1822012027bcb103007241ddd432b57812694d114b5` |
| `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` | `4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558` |

The external Corpus v1.0 keeper has the same `4124f8…5558` hash as the repo-local normalized note.

## Structural checks

A `jq 1.7.1` validator loaded all JSONL records and evaluated the schema's required fields, declared types, enums, date format, nested source/relation shapes, ID rules, and cross-record links. The final validator invocation exited `0`.

| Check | Result | Evidence |
|---|---|---|
| JSONL parsing and object count | **PASS** | 17 lines parsed as 17 objects. |
| Schema conformance | **PASS** | All 17 carry the required `id`, `schema_version`, `project`, `title`, `summary`, `statement`, `status`, `rationale`, `decided_on`, and non-empty `sources[]`; all checked optional fields and nested objects match their declared types/enums. |
| Unique IDs | **PASS** | 17 IDs, 17 unique, 0 duplicates: D01–D10 and D12–D18. |
| Dangling supersession links | **PASS** | 0 `replaces`/`replaced_by` references, 0 dangling references, 0 reciprocal failures. The closed set contains no supersession claim; the schema's MCP supersession pair is an excluded example, not Stage B data. |
| Relationship targets | **PASS** | One relationship, D18 `companion` → D17; target exists. 0 dangling relationship targets. |
| Canonical status | **PASS** | All 17 objects are `status: accepted` with `review_mark: Y`, matching the closed review sheet. D13's clarified-then-Y disposition is retained in `notes`. |
| Rejected candidate disposition | **PASS** | D11 is absent from the canonical set because Sab marked it **N**. Its rejection remains in the review sheet and normalized note. |
| Required provenance | **PASS** | Every canonical object cites all three decision-truth sources: closed review sheet, repo-local normalized note, and Corpus v1.0 parity witness. |

**Structural failures requiring disposition: none.**

## Completeness and source coverage

The closed review contains 18 candidates: 17 accepted and one rejected. Canonical IDs exactly equal the accepted set:

`D01 D02 D03 D04 D05 D06 D07 D08 D09 D10 D12 D13 D14 D15 D16 D17 D18`

D11 is the sole non-canonical candidate and is explicitly dispositioned as rejected. No accepted ID is missing and no unreviewed ID was added.

### Decision count per admitted source

Here, **count** means canonical objects whose `sources[].ref` cites the source. Process-only sources can therefore have zero canonical decisions while still appearing in every raw object's `extraction_context`.

| Source | Count | Canonical IDs / explanation |
|---|---:|---|
| `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` | 17 | All accepted IDs; also supplies D11 rejection evidence. |
| `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` | 17 | All accepted IDs; canonical wording. |
| `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` | 17 | All accepted IDs; byte-identical parity witness. |
| `project-docs/corpus-work-2026-08/CORPUS-TARGET-SHAPE.md` | 1 | D14. |
| `project-docs/REBUILD-CONTEXT-ANCHOR.md` | 2 | D14, D15. |
| `project-docs/ARCHITECTURE.md` | 2 | D14, D15. |
| `.handoffs/030-corpus-vm-semantic-graphify.md` | 1 | D14. |
| `/Users/sab-mini/repos/GDDP v MyAPI Part 1 - the first slice.md` | 0 | Governing boundary, not decision-content authority; recorded on all 17 raw objects as extraction context. |
| `01-decisions/CONTEXT.md` | 0 | Stage-room contract, not decision-content authority; recorded on all 17 raw objects as extraction context. |
| `01-decisions/output/decision-schema.md` | 0 | Shape contract, not decision-content authority; recorded on all 17 raw objects as extraction context. |
| `01-decisions/output/sources.md` | 0 | Source-selection contract, not decision-content authority; recorded on all 17 raw objects as extraction context. |

Supporting citations are deliberately sparse: they clarify fields on already-admitted decisions and do not expand the 17-decision set.

### Zero-yield excluded sources

| Excluded source or class | Canonical count | Explicit disposition |
|---|---:|---|
| D11 in the review sheet and normalized note | 0 | Sab marked N; preserve only as rejection evidence. |
| MCP naming/supersession examples in `decision-schema.md` | 0 | Schema examples lie outside the closed D01–D18 review. |
| `QUERIES-myapi.md`, `QUERIES-gddp.md`, `QUERIES-pi.md` | 0 each | Evaluation questions are not decisions. |
| `QUERY-GROUNDING-PASS1.md` | 0 | Derivative synthesis lacks per-decision review marks. |
| `WORK-MOVED-TO-VM.md` | 0 | Workplace pointer contains no decision record. |
| Other `Corpus v1.0/` files | 0 | Outside this closed last-two-weeks slice. |
| `project-docs/source-of-truth-anchors/*.md` | 0 | Older snapshots were not reviewed into D01–D18. |
| `.handoffs/*` other than handoff 030 | 0 | Empirical leads are not blanket decision authority. |
| `PROJECT-BRIEF.md`, `README.md`, `IMPLEMENTATION-PLAN.md`, general project docs | 0 | Framing/plans are outside the closed review. |
| Raw CLI/chat/Obsidian sources and `scratch/corpus-hot/**` | 0 | Unreviewed evidence cannot enter this set. |
| `graphify-out/**` | 0 | Generated structural navigation is not semantic decision authority. |
| Git history beyond cited refs | 0 | Enactment evidence alone does not establish a reviewed decision. |
| Runtime databases, Khoj indexes, GDDP job state, VM corpus state | 0 | Mutable runtime state is outside the inventory and was not read or modified. |

**Coverage result:** **PASS.** Every admitted decision-truth source yielded 17 canonical decisions; every supporting source has its exact citation count; every zero-count source/class has an explicit authority or exclusion explanation. **No source yielded zero without explanation.**

## Independent review evidence

Three read-only reviewer passes on `xai/grok-4.6` independently checked (1) schema/type conformance, (2) source coverage and closed-set completeness, and (3) IDs, links, and canonical status. All three reported no blocker or structural failure. One reviewer noted that the schema examples are correctly absent; another confirmed D18 → D17 is the only relationship and that supersession reciprocity passes vacuously.

## Stage C disposition

**Gate recommendation: PASS.** Use `01-decisions/output/decisions-canonical.jsonl` as the validated Stage D input. This validation wrote no graph truth and read or wrote no runtime database.
