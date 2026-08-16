# Part 2 evidence contract

**Schema id:** `part2-evidence-contract-1.0`  
**Envelope schema:** `2.0-part2-prov-min`  
**Baseline:** commit `431b98a1953bd1a136a42ce8d270e1f0d96a40d3` blob `eb9f225a45587a30861d4b79707d29776f456fdd6f41fec87b5ffd2d3c05034f`  
**Worktree HEAD:** `431b98a1953bd1a136a42ce8d270e1f0d96a40d3`  
**Non-normative:** `part2/contract/contract-rationale.md` · review: `part2/contract/contract-review.md`

Nodes 02–09 validate only against this file. `contract-rationale.md` is not PASS/FAIL law. Citations `[src: ORIG-…]` resolve to the baseline file above. Node 01 writes markdown under `part2/contract/` only. [src: ORIG-header; ORIG-§3]

## 1. Research question

Memo form: **Which sources materially improve grounded project-history answers?**  
Packet form (contiguous lowercase): which sources materially improve grounded project-history answers

Both strings are normative. Downstream `rg -F` must hit both. Do not paraphrase. Contribution is a Node 18 measured result, not a Node 01 inclusion predicate. [src: ORIG-§1]

## 2. Experimental gate

GDDP gates execution correctness, never whether a treatment won. `result_disposition` on every treatment manifest = `preserve_even_if_regressed`. A correctly executed poor/regressive treatment PASSES. Source pollution is a finding. FAIL: discarded scores, rerun-to-improve, or post-start corpus mutation (`EX-score-tuning`). [src: ORIG-§2; ORIG-TC-20]

## 3. Layout writers

Later nodes write only under `part2/`. Do not invent a parallel tree. [src: ORIG-§3]

```
part2/contract/                         # 01
part2/probe/                            # 02
part2/layers/{anchor,decisions,handoffs,git,graphify}/   # 03–08
part2/layers/cli-derived/               # 17 only
part2/validation/treatment-manifests/   # 09: six manifests, no cli-gap-fill
part2/ruler/                            # 10
part2/treatments/{part1-control,decisions-only,no-decisions,handoff-enriched,code-reality,full-durable,cli-gap-fill}/
part2/analysis/                         # 17–18
```

**02** writes `part2/probe/` only. **03–07** write under their layer dirs. **08** materializes five durable dirs. **09** emits six manifests under `part2/validation/treatment-manifests/` and must not emit `cli-gap-fill`. [src: ORIG-§3]

## 4. Locked measured pins

Re-hash; do not fix a mismatch by picking another copy. `P-C-1` / `P-HASH-8`: live bytes equal the pin or STOP. [src: ORIG-§4]

| pin | path | sha256 |
|---|---|---|
| part1_canonical_jsonl | `01-decisions/output/decisions-canonical.jsonl` | `09c15aebd3a424e7f09ce2c27985fa0cbc24a23d9c474182ea4c912b926750a8` |
| part1_khoj_manifest | `03-ingestion/output/khoj-corpus/` name→hash digest | `c1fa76ad157d197e28d16f8e9306680e3c870329808e9c1c115dc7587d2f1a3c` |
| anchor_rebuild | `project-docs/REBUILD-CONTEXT-ANCHOR.md` | `92d212841321dffc9add20c01c9ecb3d832e9ce58fcecce6c652ecd61ea7df7a` |
| q1 | `04-evaluation/queries/q1.txt` | `8a0d97d65c399e6c6811dd256594467829e2b7974da88ac5621b24480615b6b7` |
| q2 | `04-evaluation/queries/q2.txt` | `57cb1ddef8745873b6fd7e7f644d6f3b410bb70b16ffcafe9fb970cf31e2fb8e` |
| q3 | `04-evaluation/queries/q3.txt` | `eec2140fd57fded73bbe73918f6fe6393b89c16c6ac19c669aa59542c716de77` |
| q4 | `04-evaluation/queries/q4.txt` | `c61a6b42943ae1bac931fa33aee99b9ba150999951fb790984a21be57173c11d` |
| q5 | `04-evaluation/queries/q5.txt` | `57ca8fc42d1dc55cc51b3757331d462dea3dba413a1806cc70a58da105984c93` |

Live facts (re-measure; do not invent): 17 closed IDs `D01`–`D10`,`D12`–`D18`; 0 `replaces`/`replaced_by`; 26 `.handoffs/*.md`; missing numbers `001`,`003`–`008`,`016`–`019`; memo “29 known handoffs” is a search target, not a recovered count; `graphify-out/graph.json` 67111631 bytes, `built_at_commit=d82a5eaefaa76ed8a9f815660052c8637a50e1b9`. Remaining orig-§4 pins live in rationale. [src: ORIG-§4; ORIG-R1; ORIG-R3]

## 5. Source classes

Closed `source_class` / `layer_id` enum (no seventh durable class): `anchor` · `decisions` · `handoffs` · `git` · `graphify` · `cli-derived`. Singular aliases (`decision`,`handoff`,`cli_derived`) are illegal stored values. Do not reuse Part 1 `sources[].kind` or v1 `source_type` as `source_class`. `cli-derived` is Node 17 only, and only for failure class `genuinely-absent`. [src: ORIG-§5; ORIG-IN-01; ORIG-SC-06]

| class | role | rank | wins on | native `source_id` |
|---|---|---:|---|---|
| `anchor` | orientation | 1 | identity_orientation | `anchor:project-docs/REBUILD-CONTEXT-ANCHOR.md` |
| `decisions` | canonical_choice | 2 | what_was_decided | `decisions:D14` |
| `handoffs` | why_evidence | 3 | why_changed | `handoffs:.handoffs/030-….md` |
| `git` | what_changed | 4 | what_changed | `git:{40-char-sha}` |
| `graphify` | what_exists_now | 5 | what_exists_now | `graphify:snapshot:{sha256}` or `graphify:node:{id}` |
| `cli-derived` | gap_fill | 6 | gap after ranks 1–5 | `cli-derived:session:{id}:{slug}` |

Class PASS: SC-01 no rival anchor, pin `92d21284…`; SC-02 Part 1 JSONL unmodified and pin-matched, D11 out; SC-03 one census row per hit, templates excluded; SC-04 reproducible git export, absolute ISO-8601; SC-05 pin live graph, keep `retrieval_text` ≠ `deterministic_struct`; SC-06 no CLI in treatments 12–16. [src: ORIG-SC-01; ORIG-SC-02; ORIG-SC-03; ORIG-SC-04; ORIG-SC-05; ORIG-SC-06]

**CENSUS-HANDOFF (05):** enumerate this-tree `.handoffs/*.md` (26); stub missing `000`–`036`; probe VM paths named in `AGENTS.md` / `.handoffs/030` and keep unreachable as `inclusion_status=excluded` + `EX-unreachable-vm`; do not redefine 29 as 26. [src: ORIG-CENSUS-HANDOFF; ORIG-SC-03; ORIG-R1]

**IN-06 Git bound (06):** include a commit iff it touches `.handoffs/`,`project-docs/`,`01-decisions/`,`02-corpus/`,`03-ingestion/`,`04-evaluation/`,`AGENTS.md`,`PROJECT-BRIEF.md`,`gddp/`,`graphify-out/GRAPH_REPORT.md`, or is cited in an admitted decision `git_refs[]`, or falls in a Node-10 dated window. Always emit `change_evidence.stat`. Emit `change_evidence.diff` only for those commits, bounded and `truncated` if clipped. No full-clone dump. [src: ORIG-IN-06; ORIG-SC-04]

**§13 exception:** `part2/layers/git/` and `part2/layers/graphify/` are a dated 2026-08-16 experimental exception. They do not amend the living anchor. Anchor still wins `identity_orientation`. [src: ORIG-§13; ORIG-R2]

## 6. Authority

`authority_rank` is stamped and must match §5. Lower rank wins on its home `claim_type` and yields elsewhere. Same-rank: `replaces` current over replaced; else later non-null `occurred_at` if both `dated`; else keep both `item_id`s. Never use retrieval rank, recency, or embedding similarity as authority. [src: ORIG-§6; ORIG-AO-01]

AO-02 (decisions only): review sheet controls inclusion/status; wording note supplies text; schema supplies shape; handoffs/git/graphify may not flip a `Y`/`N`. [src: ORIG-AO-02]  
AO-03: Node 11 uses byte-identical Part 1 payload; normalized twins cite the control SHA and never replace it. [src: ORIG-AO-03]

## 7. Required provenance envelope

Every corpus item, layer-manifest row, and treatment-membership row carries **exactly these 12 universally required envelope keys**. Missing key = Node 09 FAIL. The envelope has no 13th required key. Conditional extras (including `exclusion_reason`) are not envelope-required. Serialization: YAML frontmatter on Markdown **and** the same 12 keys on JSON/JSONL. Node 02 records whether Khoj sees them as metadata or text; fields stay even if Khoj ignores them. [src: ORIG-§7; ORIG-§7.1]

### Required provenance envelope

| # | field | type | rule |
|---:|---|---|---|
| 1 | `item_id` | string | unique in layer; `^[A-Za-z0-9][A-Za-z0-9_.:/-]{2,127}$`; `{source_class}:{native-id}[:variant]` [src: ORIG-§7.1#item_id; absorbs ORIG-§7.1#stable_key] |
| 2 | `source_class` | enum | one of the six values in §5 [src: ORIG-§5; ORIG-§7.1#source_class] |
| 3 | `source_id` | string | durable origin `{source_class}:{native-id}`; shared by Graphify dual reps [src: ORIG-§5; ORIG-§7.1#source_id] |
| 4 | `origin_path` | string | repo-relative POSIX, or `vm:{host}:{abs-path}`, or `git:{repo}@{sha}`; no `~`; no `\` [src: ORIG-§7.1#origin_path; ORIG-P-ID-5] |
| 5 | `origin_sha256` | 64-hex or sentinel | SHA-256 of source bytes, or `origin_unavailable` iff the item is a missing stub [src: ORIG-§7.1#origin_sha256; ORIG-P-HASH-1] |
| 6 | `content_sha256` | 64-hex or null | SHA-256 of indexed item bytes; null only if missing/unreadable; Node 09 rehashes [src: ORIG-§7.1#content_sha256; absorbs ORIG-§7.1#layer_item_sha256] |
| 7 | `occurred_at` | ISO date/datetime or null | event/validity time; key required; never a relative phrase [src: ORIG-§7.1#occurred_at; ORIG-§8] |
| 8 | `recorded_at` | ISO date/datetime or null | inscription/capture time; key required; do not clone `occurred_at` [src: ORIG-§7.1#recorded_at; ORIG-§8] |
| 9 | `temporal_confidence` | enum | `dated` iff `occurred_at` is a source calendar date; else `temporally-ambiguous` [src: ORIG-§7.1#temporal_confidence; ORIG-§8.1] |
| 10 | `authority_rank` | int | `1`–`6` matching §5; Node 09 rejects drift from `source_class` [src: ORIG-§6; ORIG-§7.1#authority_rank] |
| 11 | `inclusion_status` | enum | `included` \| `excluded` \| `control_only` \| `gap_only` [src: ORIG-§7.1#inclusion_status; ORIG-§9] |
| 12 | `replaces` | string[] | `item_id`s this item supersedes; `[]` if none [src: ORIG-§7.1#replaces; ORIG-§12] |

Derived / conditional (not envelope-required): `layer_id=source_class`; `source_role` from §5; `presence=present` unless `origin_sha256=origin_unavailable`; `replaced_by` inferred by Node 09 from inverse `replaces` and must be reciprocal; `provenance_kind` may be recorded as a class extra, never as a 13th required key. Nested `origin` / `content_identity` / `extraction_trace` are non-normative. [src: ORIG-§7.1 invariants; ORIG-§7.2; ORIG-§7.3]

`exclusion_reason` is a **conditional non-envelope key**: required on excluded / `control_only` / `gap_only` rows (`inclusion_status≠included`); omitted from the 12-key envelope and not counted as a 13th universal field. [src: ORIG-§7.1#exclusion_reason; ORIG-§10]

Class extras (checked by class nodes): not-included → `exclusion_reason` ∈ the §9 `EX-*` set (still not an envelope key); `anchor` → `anchor_path=project-docs/REBUILD-CONTEXT-ANCHOR.md`; `decisions` → Part 1 object fields + `part1_payload_sha256` on the **normalized** twin only; `handoffs` → `handoff_number`, `origin_backing`, `identity_axis`; `git` → `commit_sha`,`parent_shas[]`,`affected_paths[]`,`subject`,`change_evidence.{stat,diff,truncated}`; `graphify` → `graph_sha256`,`built_at_commit`,`representation` ∈ {`retrieval_text`,`deterministic_struct`}; `cli-derived` → `session_ref`, `failure_class=genuinely-absent`. Hashed item bytes omit `extracted_at` / `build_id` (`P-A-4`). [src: ORIG-§7.3; ORIG-§10; ORIG-P-A-4]

## 8. Time

`occurred_at` = when it happened. `recorded_at` = when it was written down. Other clocks (`extracted_at`, mtime, ingest, `provenance_kind` timestamps) are not substitutes. [src: ORIG-§8]

Class map: decisions `occurred_at=decided_on` (do not clone into `recorded_at`); git `occurred_at=author_date`, `recorded_at=committer_date`; handoff episode date vs `Date:` header; graphify node `occurred_at=null` unless the node encodes an event; cli extract time is never either field. [src: ORIG-§8.2; ORIG-P-T-8; ORIG-P-T-10]

Hard rules: keys always exist; forbidden values `""`,`null`-string,`N/A`,`unknown`,`TBD`, epoch-zero; unknown uses JSON/YAML `null`; do not guess write-date = event-date; dated eval answers require `temporal_confidence=dated` and day-or-finer `occurred_at`; date-only sources stay `YYYY-MM-DD` (no minted `T00:00:00Z`); relative date words forbidden in items. [src: ORIG-§8.3; ORIG-P-T-1; ORIG-P-T-2; ORIG-P-T-11; ORIG-TM-01]

## 9. Inclusion and exclusion

`included` only if: class ∈ §5; 12 envelope fields legal; project home is MyAPI-family (default `MyAPI` if omitted; allowed `MyAPI`,`GDDP`,`Pi`,`MyAPI/Khoj`,`MyAPI/Pi/GDDP`); handoffs are manifest-explicit (`present` + git-backed or copied VM origin); git obeys IN-06; graphify is the pinned snapshot. Templates default `excluded`/`EX-template`. D11 never enters canonical JSONL or `decisions-only`. Silent omission of a known candidate (missing handoff numbers, D11, VM paths) is FAIL. [src: ORIG-§9; ORIG-IN-01; ORIG-IN-02; ORIG-IN-03; ORIG-IN-05; ORIG-IN-06; ORIG-IN-07]

`exclusion_reason` is required whenever `inclusion_status≠included`, as a row-level non-envelope key (not a 13th envelope field). Closed `EX-*` codes: `EX-bulk-vault`,`EX-bulk-chat`,`EX-bulk-cli`,`EX-unreviewed-decision`,`EX-d11-rejected`,`EX-schema-example`,`EX-eval-questions`,`EX-runtime`,`EX-graph-truth-write`,`EX-template`,`EX-duplicate`,`EX-missing`,`EX-stale-operational-anchor`,`EX-score-tuning`,`EX-part3-routing`,`EX-unreachable-vm`. [src: ORIG-§7.1#exclusion_reason; ORIG-§10]

## 10. Treatment composition

| treatment_id | node | classes |
|---|---|---|
| part1-control | 11 | none of the Part 2 layers; byte-identical JSONL + 18-file snapshot |
| decisions-only | 12 | `anchor` + `decisions` (normalized) |
| no-decisions | 13 | `anchor` + `handoffs` + `git` + `graphify` |
| handoff-enriched | 14 | `anchor` + `decisions` + `handoffs` |
| code-reality | 15 | `anchor` + `decisions` + `git` + `graphify` |
| full-durable | 16 | `anchor` + `decisions` + `handoffs` + `git` + `graphify` |
| cli-gap-fill | 17 | full-durable ∪ {`cli-derived`}; **not** a Node 09 manifest |

[src: ORIG-§11]

Compose by reference. No in-place rewrite of Part 1 bytes or layer bodies. Order: walk `layers_included` as written, then stable item order (decisions by id; handoffs by numeric stem; git by `occurred_at` then SHA). Two independent assemblies must emit identical `item_ids` / `treatment_manifest_sha256`. One indexed copy of byte-identical same-layer bytes; cross-layer overlap kept; identity collision with different hash is STOP. `part1-control` lists none of the Part 2 layers and must not write envelope fields into `decisions-canonical.jsonl`. [src: ORIG-§11.3; ORIG-§11.4; ORIG-§11.5; ORIG-§11.6; ORIG-TC-01; ORIG-TC-17]

Hash algorithm (live Part 1, `03-ingestion/transform_for_khoj.py`):

```
file_sha256(path) = SHA-256(bytes)
file_manifest = {relative_path: file_sha256}   # sort_keys
layer_digest(layer_id) = SHA-256(json.dumps(file_manifest, sort_keys=True, separators=(",", ":")))
layer_manifest_sha256 = {layer_id: layer_digest(layer_id) for layer_id in layers_included}  # deterministic mapping
treatment_manifest_sha256 = SHA-256(canonical_json({treatment_id, layers_included, item_ids, layer_manifest_sha256}))
```

`layer_manifest_sha256` is the deterministic object `{layer_id: sha256}` covering every id in `layers_included`, not a single scalar digest of one layer. [src: ORIG-§11.1#layer_manifest_sha256; ORIG-TC-09]

Required per treatment even if worse than control: retrieval evidence, generated answer or explicit failure, grounding citations, abstention. Node 17 classes: `retrieval-missed` / `synthesis-failed` / `genuinely-absent` — only the third extracts CLI. Node 08 emits Markdown+YAML items, per-layer `manifest.json`, one script per layer; dual Graphify files share `source_id`. [src: ORIG-§11.6; ORIG-§14; ORIG-TC-20]

## 11. Supersession

`replaces` is the required edge list. Node 09 builds inverse `replaced_by` and FAILs on one-sided edges, cycles, forks, or dropped superseded bytes. Recency is not supersession. Closed set currently has **zero** edges; do not mint any to make Q3 look answered. Duplicates use `EX-duplicate` + one indexed copy, not a temporal successor. Semantic-only supersession lives only on the normalized twin. [src: ORIG-§12; ORIG-P-S-1; ORIG-P-S-8; ORIG-P-S-12; ORIG-SU-01; ORIG-R4]

## 12. Mechanical checks for nodes 02–09

This table is the Node 02–09 executable check surface. Later consumers (`10`/`11`–`17`) appear only where a 02–09 check already names them; they do not widen the table into a Node 10–18 contract. [src: ORIG-§7.4; ORIG-§11.7]

| ID | axis | node | PASS | FAIL | src |
|---|---|---|---|---|---|
| ID-1 | identity | 08/09 | 0 `item_id` collisions in a layer | duplicate `item_id` | [src: ORIG-P-ID-1] |
| ID-2 | identity | 03–09 | every `source_class` ∈ §5 | v1 `source_type` used as class | [src: ORIG-P-ID-2] |
| ID-3 | identity | 08/09 | `source_id` prefix equals `source_class` | malformed / prefix mismatch | [src: ORIG-P-ID-3] |
| P-1 | provenance | 08/09 | `origin_path` POSIX, non-empty, no `~` | blank, `~`, backslash | [src: ORIG-P-ID-5; ORIG-IN-02] |
| P-2 | provenance | 08/09 | `origin_sha256` 64-hex or legal sentinel | uppercase, SHA-1 length, sentinel on present item | [src: ORIG-P-HASH-1] |
| P-3 | provenance | 09 | recomputed `content_sha256` matches | any mismatch | [src: ORIG-P-HASH-2] |
| T-1 | time | 08/09 | `occurred_at` and `recorded_at` keys exist | omitted keys | [src: ORIG-P-T-1] |
| T-2 | time | 08/09 | ISO or null only | relative words / forbidden sentinels | [src: ORIG-P-T-2] |
| T-3 | time | 09/10 | `dated` ⇒ non-null day-or-finer `occurred_at` | dated answer from `recorded_at`/mtime | [src: ORIG-P-T-11] |
| T-4 | time | 06/09 | git occurred=author, recorded=committer | swapped or mtime | [src: ORIG-P-T-8] |
| A-1 | authority | 09 | `authority_rank` matches §5 | stamped rank drifts from class | [src: ORIG-AO-01] |
| A-2 | authority | 04/09 | review sheet still controls decision Y/N | handoff/graphify flips a decision | [src: ORIG-AO-02] |
| TC-1 | treatment | 08/09 | five durable dirs independently hashable | mixed dump / in-place Part 1 overwrite | [src: ORIG-TC-01] |
| TC-2 | treatment | 09 | six manifests; sets exact to §10 | extra/missing layer; `cli-gap-fill` emitted | [src: ORIG-TC-14] |
| TC-3 | treatment | 09 | `no-decisions` has 0 `decisions:*` | decisions leaked | [src: ORIG-TC-15] |
| TC-4 | treatment | 09/11 | control JSONL + khoj manifest pins match | any byte change | [src: ORIG-TC-11] |
| R-1 | repro | 08/09 | hashes use Part 1 canonical JSON | ad-hoc hashing | [src: ORIG-TC-09] |
| R-2 | repro | 08/09 | rebuild `diff -qr` 0 and manifests equal | nondeterministic render | [src: ORIG-TC-10] |
| X-1 | gate | 09/11–17 | poor results stored | discarded / rerun-to-improve | [src: ORIG-§2; ORIG-TC-20] |

Node 02 additionally records Khoj metadata-vs-text behavior for the 12 fields; it does not drop fields. [src: ORIG-§7; ORIG-§17]

## 13. Prohibitions

Do not invent `occurred_at`. Do not drop envelope fields because Khoj ignores metadata. Do not mutate graph truth, runtime DBs, or job state. Do not widen `source_class` beyond the six values. Do not build Part 3 routing. Label hash/count/parse as measured; “29 known” and inferred supersession stay inferred; embedding similarity is not authority. [src: ORIG-§15; ORIG-§17; ORIG-R1]
