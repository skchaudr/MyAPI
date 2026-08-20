# Part 2 evidence-contract rationale (non-normative)

Nodes 02–09 validate only against `part2/contract/evidence-contract.md`.  
`contract-rationale.md` must not be imported as PASS/FAIL law.

## Meta

| Key | Value |
|---|---|
| baseline_commit | `431b98a1953bd1a136a42ce8d270e1f0d96a40d3` |
| original_path | `part2/contract/evidence-contract.md` |
| original_sha256 | `eb9f225a45587a30861d4b79707d29776f456fdd6f41fec87b5ffd2d3c05034f` |
| original_line_count | 1179 |
| original_bytes | 76548 |
| original_schema | `part2-evidence-contract-1.0` / envelope `2.0-part2-prov` |
| revised_envelope | `2.0-part2-prov-min` |
| relationship | this file is explanatory; `evidence-contract.md` is the sole normative surface |
| worktree_head_at_01b | `431b98a1953bd1a136a42ce8d270e1f0d96a40d3` (original narrative HEAD `ffece0a9…` is the parent pin) |

**Citation convention.** `ORIG-§N` / `ORIG-§N.M` / `ORIG-SC-0k` / `ORIG-AO-0k` / `ORIG-IN-0k` / `ORIG-EX-*` / `ORIG-TC-nn` / `ORIG-P-*` / `ORIG-SU-01` / `ORIG-TM-01` / `ORIG-CENSUS-HANDOFF` / `ORIG-R#` resolve to the baseline blob above. `RAT-<slug>` anchors in this file hold moved bodies.

**Bins.** necessary-contract = downstream nodes need it to behave consistently (kept in revised contract). useful-explanation = interpret, not mandate. speculative-machinery = edge-case policy / future-proofing / abstractions no planned Part 2 treatment exercises — explicitly non-normative.

**Disposition markers.** KEEP / COMPRESS / SPLIT / MOVE / NON-NORM / RETIRE-AS-MANDATE / PIN-REFRESH.

### Baseline heading inventory (verbatim from `431b98a`)

Every original `##` / `###` heading is preserved here so none are silently deleted. Bodies live in the RAT-* sections below or remain compressed in the revised contract.

# Part 2 evidence contract
## 1. Research question
## 2. Experimental gate
## 3. Self-describing layout
## 4. Locked measured pins
## 5. Source classes
### SC-01 `anchor`
### SC-02 `decisions`
### SC-03 `handoffs`
### SC-04 `git`
### SC-05 `graphify`
### SC-06 `cli-derived`
## 6. Source authority
### AO-01 Conflict rule
### AO-02 Part 1 decision-internal order
### AO-03 Control payload vs normalized twin
## 7. Provenance fields
### 7.1 Required flat envelope (every item)
### 7.2 Nested origin / content / trace objects
### 7.3 Conditional extras by `source_class`
### 7.4 Provenance PASS/FAIL
## 8. occurred_at versus recorded_at
### 8.1 Temporal fields
### 8.2 Class mapping
### 8.3 Hard rules
## 9. Inclusion rules
### IN-01 Class membership
### IN-02 Provenance complete
### IN-03 Project-history relevance
### IN-04 Treatment eligibility declared
### IN-05 Handoff inclusion is manifest-explicit
### IN-06 Git inclusion is bounded
### IN-07 Graphify inclusion is snapshot-pinned
## 10. Exclusion rules
## 11. Treatment composition
### 11.1 `TreatmentManifest` fields
### 11.2 Layer item / manifest fields used at assembly
### 11.3 Ordering
### 11.4 Duplicate handling
### 11.5 `part1-control` isolation
### 11.6 No silent mutation / poor results stay
### 11.7 Treatment PASS/FAIL
## 12. Supersession rules
### 12.1 Fields
### 12.2 Invariants
## 13. Git / Graphify experimental exception
## 14. Corpus item format
## 15. Measured versus inferred
## 16. Continuation proposals
## 17. What later nodes must not do
## 18. Field index
## 19. Risks left for later nodes

---

## A. Why the original grew (coverage incentive narrative)

The 1179-line / 76.5 KB contract is a competent coverage product. Four analysis lanes, a sole integrator, and multiple reviewers are each incentivized to close an edge case. The lens question is not “is 1179 too long?” It is: what downstream decision becomes more correct because each major section exists, and can Nodes 02–09 consume it without becoming more complicated?

The executable idea is a page or two of fields, invariants, and treatment rules. The rest is explanation, runbook, or unused machinery (zero live decision-supersession edges; `cli-derived` is Node 17; AO-04 is answer policy; nested origin/span/encoding enums are not required to export a commit).

Cancelled node-06 commit `5d714e9` is a **consumability data point only**. Its tree equals `431b98a`. That is compatible with “fat contract + orchestration tax” and also compatible with harness abort. It is not proof the original reasoning is wrong.

---

## B. Executable core (operational idea)

1. Ask which sources improve grounded project-history answers.
2. Use six source classes with fixed authority on claim types.
3. Give every item identity, origin, content hash, two clocks, inclusion, and a supersession edge list.
4. Include/exclude with an explicit `EX-*` vocabulary; never silently drop known gaps.
5. Compose seven treatments from a frozen matrix without mutating sources; keep poor results.
6. Pin Part 1 bytes and the rebuild anchor; exception-allow git/graphify layers under `part2/` without rewriting product direction.
7. Label measured vs inferred; stop before Part 3 routing.

---

## C. Traceability matrix

| ORIG ID | Lines | Title | Lens bin | Disposition | Revised home | Rationale home | Downstream decision preserved |
|---|---:|---|---|---|---|---|---|
| ORIG-header | 1–11 | Node/schema identity | useful-explanation | COMPRESS | title + schema + rationale pointer | RAT-meta | which file is law |
| ORIG-§1 | 13–27 | Research question | necessary-contract | KEEP | §1 both strings | RAT-RQ | Node 18 framing; `rg -F` |
| ORIG-§2 | 29–41 | Experimental gate | necessary-contract | COMPRESS | §2 | RAT-gate | 09/11–17 keep poor treatments |
| ORIG-§3 | 43–81 | Self-describing layout | necessary-contract | COMPRESS | §3 | RAT-layout | 02–18 write only under `part2/` |
| ORIG-§4 | 83–134 | Locked measured pins | SPLIT | KEEP pin rule + critical hashes; MOVE census detail | §4 | RAT-pins | 04/11 continuity |
| ORIG-§5 | 136–159 | Source classes enum | necessary-contract | KEEP | §5 | RAT-sc-aliases | no 7th durable class |
| ORIG-SC-01 | 161–179 | anchor | necessary-contract | COMPRESS | §5 SC-01 | RAT-SC-01 | Node 03 bounds |
| ORIG-SC-02 | 181–198 | decisions | necessary-contract | COMPRESS | §5 SC-02 | RAT-SC-02 | Node 04/11 control |
| ORIG-SC-03 | 200–226 | handoffs | SPLIT | KEEP axes; MOVE census procedure | §5 CENSUS | RAT-CENSUS-HANDOFF | Node 05 vs memo 29 |
| ORIG-SC-04 | 228–273 | git | SPLIT | KEEP role + IN-06; MOVE repo menu | §5 IN-06 | RAT-SC-04 | Node 06 export |
| ORIG-SC-05 | 275–294 | graphify | SPLIT | KEEP pin + dual reps | §5 SC-05 | RAT-SC-05 | Node 07 dual surface |
| ORIG-SC-06 | 296–324 | cli-derived | necessary-contract | COMPRESS | §5 SC-06 | RAT-SC-06 | Node 17 boundary |
| ORIG-IN-01 | 318–324 | Class membership | necessary-contract | KEEP | §5 / §9 | — | reject v1 source_type |
| ORIG-§6 | 326–337 | Authority rank table | necessary-contract | KEEP | §6 | RAT-authority | conflict resolution |
| ORIG-AO-01 | 339–347 | Same-rank conflict | necessary-contract | COMPRESS | §6 | RAT-AO-01 | Node 09 conflict audit |
| ORIG-AO-02 | 349–360 | Decision-internal order | necessary-contract | COMPRESS | §6 | RAT-AO-02 | Node 04 status authority |
| ORIG-AO-03 | 362–372 | Control vs twin | necessary-contract | KEEP | §6 | RAT-AO-03 | Node 11 isolation |
| ORIG-AO-04 | 374–386 | Claim-type winner table | speculative-machinery (02–09) | MOVE / NON-NORM | — | RAT-AO-04 | Node 10/18 answer policy |
| ORIG-§7 | 388–394 | Provenance intro | useful-explanation | COMPRESS | §7 serialization | RAT-khoj-metadata | Node 02 observation ≠ drop |
| ORIG-§7.1 | 396–458 | Required flat envelope | SPLIT | COMPRESS to 12 | §7 table | RAT-envelope-full | 08–09 identity/provenance |
| ORIG-§7.2 | 460–509 | Nested objects | speculative-machinery | MOVE / RETIRE-AS-MANDATE | pointer | RAT-nested-objects | deep forensics optional |
| ORIG-§7.3 | 511–528 | Conditional extras | necessary-contract | COMPRESS | §7 class extras | RAT-class-extras | SC-specific inventory |
| ORIG-§7.4 | 530–549 | Provenance PASS/FAIL | SPLIT | KEEP core IDs | §12 checks | RAT-checks-prov | Node 09 green/red |
| ORIG-§8 | 551–558 | Two clocks | necessary-contract | KEEP | §8 | RAT-temporal-intro | dated vs inscription |
| ORIG-§8.1 | 560–576 | Temporal field enum set | speculative as all-required | MOVE most | three fields kept | RAT-temporal-fields | precision available |
| ORIG-§8.2 | 578–588 | Class mapping | necessary-contract | COMPRESS | §8 class map | RAT-temporal-class-map | consistent stamping |
| ORIG-§8.3 | 590–619 | Hard rules + P-T | SPLIT | KEEP core rules | §8 hard rules | RAT-temporal-hard | eval integrity |
| ORIG-§9 | 621–677 | Inclusion IN-01…07 | necessary-contract | COMPRESS | §9 | RAT-inclusion-tables | what may enter treatments |
| ORIG-§10 | 679–704 | Exclusion EX-* | SPLIT | KEEP codes; MOVE PASS columns | §9 | RAT-exclusion-detail | silent omission fails |
| ORIG-§11 | 706–734 | Treatment matrix | necessary-contract | KEEP | §10 | RAT-treatment-aliases | 12–17 composition |
| ORIG-§11.1 | 736–768 | TreatmentManifest | SPLIT | KEEP hash + disposition | §10 | RAT-TreatmentManifest | reproducible assembly |
| ORIG-§11.2 | 770–780 | LayerItem extras | speculative-as-mandate | MOVE | — | RAT-layer-manifest | assembly bookkeeping |
| ORIG-§11.3 | 782–796 | Ordering | COMPRESS | KEEP determinism | §10 | RAT-ordering | rebuild equality |
| ORIG-§11.4 | 798–810 | Duplicates | SPLIT | KEEP one-copy + STOP | §10 | RAT-duplicates | dedup without history loss |
| ORIG-§11.5 | 812–829 | part1-control isolation | necessary-contract | COMPRESS | §10 | RAT-part1-control | control validity |
| ORIG-§11.6 | 831–861 | No silent mutation | necessary-contract | COMPRESS | §10 | RAT-mutation-table | experimental gate |
| ORIG-§11.7 | 863–890 | TC-01…22 | SPLIT | KEEP load-bearing TCs | §12 | RAT-TC-register | Node 09 automation |
| ORIG-§12 | 892–901 | Alias mapping | COMPRESS | KEEP names | §11 | RAT-supersession-map | schema compatibility |
| ORIG-§12.1 | 903–921 | Supersession fields | SPLIT | KEEP `replaces` | §11 | RAT-supersession-fields | history questions |
| ORIG-§12.2 | 923–959 | Invariants + P-S | SPLIT | KEEP reciprocity/retain/0-edges | §11 | RAT-P-S-register | Node 09 + eval honesty |
| ORIG-§13 | 961–973 | Git/Graphify exception | necessary-contract | KEEP | §5 | RAT-R2 | unblocks 06/07 |
| ORIG-§14 | 975–990 | Corpus item format | COMPRESS | KEEP emission | §10 | RAT-item-format | Node 08 emit shape |
| ORIG-§15 | 992–1002 | Measured vs inferred | COMPRESS | KEEP label rule | §13 | RAT-measured | finding integrity |
| ORIG-§16 | 1004–1022 | Continuation proposals | useful-explanation | MOVE entire | pointer | RAT-continuations | next-node runbook |
| ORIG-§17 | 1024–1033 | Must not | necessary-contract | KEEP short | §13 | — | hard stop |
| ORIG-§18 | 1035–1167 | Field index | speculative-machinery | MOVE | — | RAT-field-index | author grep aid |
| ORIG-§19 | 1168–1179 | Risks R1–R8 | useful-explanation | MOVE | R1/R2 one-liners | RAT-risks | 05/06/07 awareness |

---

## D. Field-reduction map (ORIG-§7.1 36 required → 12)

Live §7.1 at baseline listed **38 field rows**: 36 required keys (34 `yes` + 2 `yes (key required)`), 1 conditional (`canonical_item_id`), 1 optional (`claim_type`). Packet “39 required flat fields” is not reproduced by that parse.

### D.1 Normative core (exactly 12)

| # | Revised field | Absorbs / replaces | Primary src |
|---:|---|---|---|
| 1 | `item_id` | `stable_key` (may equal) | ORIG-§7.1 |
| 2 | `source_class` | `layer_id` (same enum; store once) | ORIG-§5, ORIG-§7.1 |
| 3 | `source_id` | native identity | ORIG-§5, ORIG-§7.1 |
| 4 | `origin_path` | nested `origin.*` non-normative | ORIG-§7.1, ORIG-§7.2 |
| 5 | `origin_sha256` | — | ORIG-§7.1 |
| 6 | `content_sha256` | `layer_item_sha256` when hash_scope=item_bytes | ORIG-§7.1 |
| 7 | `occurred_at` | precision/basis/ambiguity → RAT-temporal | ORIG-§7.1, ORIG-§8 |
| 8 | `recorded_at` | same | ORIG-§7.1, ORIG-§8 |
| 9 | `temporal_confidence` | packs `occurred_at_ambiguity` for dated vs not | ORIG-§7.1, ORIG-§8.1 |
| 10 | `authority_rank` | pairs with source_class defaults | ORIG-§6, ORIG-§7.1 |
| 11 | `inclusion_status` | drives EX pairing | ORIG-§7.1, ORIG-§9–10 |
| 12 | `replaces` | supersession edge; Node 09 infers `replaced_by` | ORIG-§7.1, ORIG-§12 |

Counting choice (documented, not silent): `replaced_by` and `representation` are **not** universal required keys. `replaced_by` is inferred by Node 09 and must be reciprocal. `representation` is class-conditional (required for decisions/graphify/control; default `verbatim` elsewhere). `exclusion_reason` is required when not included, as a conditional non-envelope key, not a 13th envelope field. This keeps the header count at 12 without dropping history reciprocity.

### D.2 Fields moved (definitions retained; not universal mandates)

Reconcile: 36 original universal required keys − 12 retained in D.1 = **24 moved required keys** below. The two leftover §7.1 rows were never in the 36: `canonical_item_id` (conditional) and `claim_type` (optional).

| Field | Disposition | Why not universal mandate |
|---|---|---|
| `schema_version` | file-level header constant `2.0-part2-prov-min` | global pin beats per-row tax |
| `source_role` | derive from source_class | redundant with §5 table |
| `layer_id` | synonym of source_class | duplicate enum |
| `stable_key` | may equal item_id | overlap |
| `control_role` | conditional on decisions/parity | most items `none` |
| `project` | default `MyAPI`; validate under IN-03 | rare multi-home |
| `layer_item_sha256` | retire if content_sha256==item bytes | duplicate hash |
| `provenance_kind` | class extra / useful | overlaps source_class |
| `occurred_at_precision` | RAT-temporal | edge precision |
| `occurred_at_basis` | RAT-temporal | edge precision |
| `occurred_at_ambiguity` | RAT-temporal | edge precision |
| `recorded_at_precision` | RAT-temporal | same |
| `recorded_at_basis` | RAT-temporal | same |
| `recorded_at_ambiguity` | RAT-temporal | same |
| `timezone_basis` | RAT-temporal | edge TZ |
| `temporal_candidates` | NON-NORM as always-required | use when conflicting |
| `presence` | handoff census stubs | not all classes |
| `exclusion_reason` | required when not included | conditional non-envelope |
| `supersession_status` | infer from replaces / Part 1 status | pair with replaces |
| `replaced_by` | Node 09 inverse | keep reciprocity without a 13th key |
| `representation` | class-conditional | Graphify dual + control twin |
| `treatment_eligibility` | derive from matrix+class | computed |
| `origin_backing` | handoff/git conditional | not universal |
| `identity_axis` | handoff conditional | not universal |
| `canonical_item_id` | not in the 36 | already conditional |
| `claim_type` | not in the 36 | already optional |

---

## E. Check-ID disposition register

Every ID inventoried from baseline. KEEP = still a Node 09 (or named-node) hard fail via the revised check table or an equivalent named rule. RETIRE-AS-MANDATE = history retained; do not fail solely on the fine ID. NON-NORM = never was / no longer a FAIL surface.

### E.1 KEEP as normative (load-bearing)

`research-question` both strings · SC closed enum · SC-01…SC-06 compressed PASS · SC-06 gap boundary · P-C-1 / TC-11 / AO-03-P (Part 1 byte continuity) · TC-12 (five question pins) · TC-14 / TC-15 / TC-16 (matrix integrity; appear as TC-2/TC-3) · TC-17 / TC-20 / EX-score-tuning · IN-01…IN-07 compressed · EX-* code set · AO-01 / AO-02 / AO-03 · P-T-1, P-T-2, P-T-8, P-T-11, TM-01 · P-S-1, P-S-8, P-S-12, SU-01 · P-HASH-1, P-HASH-2 · P-ID-1, P-ID-2, P-ID-3, P-ID-5, P-ID-8 · §13 exception · TC-01, TC-10 · P-A-4 (hashes omit extracted_at/build_id).

Revised check IDs map: ID-1←P-ID-1; ID-2←P-ID-2; ID-3←P-ID-3; P-1←P-ID-5/IN-02; P-2←P-HASH-1; P-3←P-HASH-2; T-1←P-T-1; T-2←P-T-2; T-3←P-T-11; T-4←P-T-8; A-1←AO-01; A-2←AO-02; TC-1←TC-01; TC-2←TC-14/16; TC-3←TC-15; TC-4←TC-11; R-1←TC-09; R-2←TC-10; X-1←§2/TC-20.

### E.2 RETIRE-AS-MANDATE → advisory

P-ID-4 (project homes still validated under IN-03, not a 13th field) · P-ID-6 · P-ID-7 · P-HASH-3 · P-HASH-4 · P-HASH-8 as a universal “every secondary pin” (critical pins remain P-C-1) · P-T-3, P-T-4, P-T-5, P-T-6, P-T-7, P-T-9, P-T-10, P-T-12 · P-S-2…P-S-7, P-S-9…P-S-11 · TC-02…TC-08, TC-13, TC-18, TC-19, TC-21, TC-22 as separate IDs (principles folded) · P-C-6 (parity witness is a Node 04/09 special case) · P-A-4 remains KEEP as a hash-recipe note · AO-04-P · IN-04 as a stored `treatment_eligibility[]` field · IN-06-P wording kept via IN-06.

### E.3 NON-NORM

AO-04-P as Node 09 FAIL · LayerItem.inclusion / temporal_quality enums · supersession.kind/confidence/as_of · satellite last-30 repo menu · exact `change_evidence.max_bytes=65536` constant (bound+truncated remains KEEP) · §18 field index as schema · CENSUS-HANDOFF steps 2–4 as contract law (outcome KEEP).

Full baseline token list (116): `AO-01, AO-01-P, AO-02, AO-02-P, AO-03, AO-03-P, AO-04-P, CENSUS-HANDOFF, EX-bulk-chat, EX-bulk-cli, EX-bulk-vault, EX-d11-rejected, EX-duplicate, EX-eval-questions, EX-graph-truth-write, EX-missing, EX-part3-routing, EX-runtime, EX-schema-example, EX-score-tuning, EX-stale-operational-anchor, EX-template, EX-unreachable-vm, EX-unreviewed-decision, IN-01…IN-07, IN-06-P, P-A-4, P-C-1, P-C-6, P-HASH-1…4, P-HASH-8, P-ID-1…8, P-S-1…12, P-T-1…12, R1…R8, SC-01…06 (+-P), SU-01, TC-01…22, TM-01`.

---

## F. Moved section bodies (RAT-* anchors)

### RAT-meta — moved from ORIG-header [lines 1–11]
**Normative residue:** schema id + envelope + baseline pin.  
**Bin:** useful-explanation  
**Why moved:** writing-time HEAD `ffece0a9eeae1d61d1fef8e90595b9d8296d80bf` and “this file is the sole Node 01 artifact” are identity notes, not 02–09 checks.  
**Downstream decision preserved:** which file is law.

Original header also named **Node:** `node-01-evidence-contract`, **Artifact:** `part2/contract/evidence-contract.md`, **Envelope schema:** `2.0-part2-prov`. Revised envelope id is `2.0-part2-prov-min`; this file keeps `2.0-part2-prov` as the historical name.

### RAT-RQ — notes from ORIG-§1 [lines 13–27]
**Normative residue:** both strings in revised §1.  
**Bin:** necessary-contract (strings) + useful-explanation (surrounding prose).  
**Why moved:** dual `rg -F` theater around two phrasings is kept because memo + packet require both; extra “what happened / why / what exists now” sentence is explanation.  
**Downstream:** Node 18 contribution framing.

Original surrounding prose: “Part 2 measures which source classes and representations improve grounded answers about what happened, why it happened, and what exists now.”

### RAT-gate — moved table detail from ORIG-§2 [lines 29–41]
**Normative residue:** revised §2.  
**Bin:** necessary-contract  
**Why moved:** the three-row PASS/FAIL table is restated more tightly.  
**Downstream:** 09/11–17 may not drop poor treatments.

Original table:

| Field / object | Rule | Downstream PASS | Downstream FAIL |
|---|---|---|---|
| `result_disposition` | Must equal `preserve_even_if_regressed` on every `TreatmentManifest` | value present and exact | omitted, or rewritten to drop poor scores |
| treatment logs | A correctly executed, evidence-preserving treatment PASSES even if it scores poorly | Node 09/11–17 record scores + raw responses | discarded, rerun-to-improve, or corpus edited to raise a score |
| `exclusion_reason=EX-score-tuning` | Any add/drop done to raise judge scores | zero such rows after treatment start | post-start corpus mutation |

“Source pollution and regressions are findings. Valid poor and regressive treatment outcomes stay in `part2/treatments/`.”

### RAT-layout — FAIL examples from ORIG-§3 [lines 43–81]
**Normative residue:** revised §3 tree + writer bullets.  
**Bin:** necessary-contract  
**Why moved:** original writer-node PASS/FAIL table is verbose around the same tree.

Original writer table:

| Path | Writer node | PASS | FAIL |
|---|---|---|---|
| `part2/contract/evidence-contract.md` | 01 | file exists, markdown, non-empty | missing, or non-markdown sibling under `part2/` from this node |
| `part2/layers/{anchor,decisions,handoffs,git,graphify}/` | 03–08 | five durable layer dirs | mixing layers into one dump |
| `part2/layers/cli-derived/` | 17 | created only after failure classification | present in Node 09 six manifests |
| `part2/validation/treatment-manifests/` | 09 | one file per `treatment_id` in §11 except `cli-gap-fill` | sixth durable class invented; `cli-gap-fill` emitted as a Node 09 manifest |

“Node 01 creates this markdown file only. It does not create layer content.”

### RAT-pins — full ORIG-§4 tables [lines 83–134]
**Normative residue:** revised §4 critical pins + live census numbers.  
**Bin:** necessary-contract (pins) + useful-explanation (key dumps).  
**Why moved:** inventory measurements are not item schema.  
**Downstream:** 04/11 continuity; 05/07 start from measured facts.

These are measured facts originally recorded at HEAD `ffece0a9eeae1d61d1fef8e90595b9d8296d80bf`. File pins still match live `431b98a`. Later nodes re-hash; they do not “fix” a mismatch by picking another copy.

| `pin_name` | Path | SHA-256 | Role |
|---|---|---|---|
| `part1_canonical_jsonl` | `01-decisions/output/decisions-canonical.jsonl` | `09c15aebd3a424e7f09ce2c27985fa0cbc24a23d9c474182ea4c912b926750a8` | Primary Part 1 continuity payload (17 objects: `D01`–`D10`, `D12`–`D18`) |
| `part1_raw_jsonl` | `01-decisions/output/decisions-raw.jsonl` | `70c54903cf55855b3163b056254cc94583af616a03d20d394d6f673b29b35956` | Extraction-trace witness, not the eval payload |
| `part1_schema` | `01-decisions/output/decision-schema.md` | `41289d2b30b1069897db4d3a3f9d2d1431a1c55e15039b82c81b7199dd25f636` | Decision object shape |
| `part1_review_sheet` | `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` | `e0eddc85c0a24b1a5234f1822012027bcb103007241ddd432b57812694d114b5` | Inclusion/status authority for D01–D18 |
| `part1_wording_note` | `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` | `4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558` | Canonical wording; Corpus v1.0 keeper is the parity witness of the same hash |
| `part1_corpus_index` | `02-corpus/output/corpus/index.md` | `54499bb3532288d1532729861607e532d1210744f9513a08c2b855fe9c03d417` | Snapshot index |
| `part1_d18_md` | `02-corpus/output/corpus/D18.md` | `1f3f805a852a8437547ab603b82413cde6a42e8fcf197a75446ff657f595c574` | Snapshot/Khoj byte-identity exemplar |
| `part1_khoj_manifest` | `03-ingestion/output/khoj-corpus/` file→hash dict | `c1fa76ad157d197e28d16f8e9306680e3c870329808e9c1c115dc7587d2f1a3c` | 18-file Stage E manifest; equals Stage D |
| `anchor_rebuild` | `project-docs/REBUILD-CONTEXT-ANCHOR.md` | `92d212841321dffc9add20c01c9ecb3d832e9ce58fcecce6c652ecd61ea7df7a` | Sole primary anchor (8815 bytes) |
| `anchor_architecture` | `project-docs/ARCHITECTURE.md` | `d624c6686848eeb67747f44eda3a434eff78104a1009fb58e9578573505b9d1c` | Companion memo, not a second golden brief |

Part 1 question pins (also in revised §4):

| File | SHA-256 | Bytes |
|---|---|---:|
| `04-evaluation/queries/q1.txt` | `8a0d97d65c399e6c6811dd256594467829e2b7974da88ac5621b24480615b6b7` | 58 |
| `04-evaluation/queries/q2.txt` | `57cb1ddef8745873b6fd7e7f644d6f3b410bb70b16ffcafe9fb970cf31e2fb8e` | 80 |
| `04-evaluation/queries/q3.txt` | `eec2140fd57fded73bbe73918f6fe6393b89c16c6ac19c669aa59542c716de77` | 40 |
| `04-evaluation/queries/q4.txt` | `c61a6b42943ae1bac931fa33aee99b9ba150999951fb790984a21be57173c11d` | 29 |
| `04-evaluation/queries/q5.txt` | `57ca8fc42d1dc55cc51b3757331d462dea3dba413a1806cc70a58da105984c93` | 65 |

Live inventory facts (re-measure; do not invent):

| Fact | Measured value | Field later nodes stamp |
|---|---|---|
| Closed decision IDs | `D01`–`D10`, `D12`–`D18` (17). `D11` rejected and absent from the JSONL | `part1_id`, `status` |
| Closed-set supersession | 0 `replaces` / `replaced_by` links | `replaces=[]`, `replaced_by=null` |
| Sole represented relationship | D18 `companion` → D17 | `related_decisions` |
| This-tree handoff files | 26 markdown files under `.handoffs/` | `handoff_number`, `presence` |
| Present handoff numbers | `000`, `002`, `009`–`015`, `020`–`036` | `handoff_number` |
| Missing handoff numbers in `000`–`036` | `001`, `003`, `004`, `005`, `006`, `007`, `008`, `016`, `017`, `018`, `019` | `presence=missing` |
| Memo census claim | “29 known handoffs” in the Part 2 memo / Node 05 text | search target, not a recovered count |
| Graph snapshot | `graphify-out/graph.json` 67111631 bytes; `built_at_commit=d82a5eaefaa76ed8a9f815660052c8637a50e1b9`; 53573 nodes / 73117 links | `graph_sha256`, `built_at_commit` |
| Graph vs HEAD | snapshot commit `d82a5eae…`; original narrative worktree `ffece0a9…`; live 01b HEAD `431b98a…` | both recorded; no silent refresh |
| Node keys | `_origin, community, community_name, file_type, id, label, norm_label, source_file, source_location` | inventory only |
| Link keys | `_origin, confidence, confidence_score, relation, source, source_file, source_location, target, weight` | inventory only |
| File types | document 41068, code 12337, rationale 163, concept 5 | filter evidence for Node 07 |
| Allowed `project` homes | `MyAPI`, `GDDP`, `Pi`, `MyAPI/Khoj`, `MyAPI/Pi/GDDP` (verbatim; do not case-fold or reorder) | `project` |

Original pin checks: `P-C-1` live canonical hash equals pin; `P-C-6` parity witness still `4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558` or STOP; `P-HASH-8` every named pin in the full table still matches live bytes.

### RAT-sc-aliases — ORIG-§5 alias table [lines 136–159]
**Normative residue:** closed enum + illegal singulars in revised §5.  
**Bin:** necessary-contract  
Original alias table:

| Alias seen in advisory notes | Stored value | Rule |
|---|---|---|
| `decision` | `decisions` | singular is not a legal stored value |
| `handoff` | `handoffs` | singular is not a legal stored value |
| `cli_derived` | `cli-derived` | underscore form is not a legal stored value |

Do not reuse Part 1 `sources[].kind` (`memo` · `handoff` · `session` · `anchor` · `review_sheet` · `commit` · `other`) or v1 `source_type` (`daily_note`, `conversation`, `cli_session`, …) as `source_class`. Those may appear only inside `provenance_kind` or `extraction_trace.notes`.

---

## I. Class-specific runbooks (SC-01…SC-06 long form)

### RAT-SC-01 — moved from ORIG-SC-01 [lines 161–179]
**Normative residue:** no-rival + pin `92d21284…`.  
**Bin:** necessary-contract  
**Why moved:** per-field required-value table is a runbook.

| Field | Required value |
|---|---|
| `source_class` | `anchor` |
| `source_role` | `orientation` |
| `authority_rank` | `1` |
| `anchor_path` | `project-docs/REBUILD-CONTEXT-ANCHOR.md` |
| `representation` | `verbatim` for the pre-existing body |
| `extension` | `none`, or a quoted added span with its own `occurred_at` |

**Does:** interpret retrieved facts (identity, glossary, MCP names `get_project_context` / `get_person_context`, layer boundaries).  
**Does not:** mint decisions or replace Git/Graphify.

Architecture (`project-docs/ARCHITECTURE.md`) may be cited as `provenance_kind=memo` support. It is not a second golden brief. `project-docs/source-of-truth-anchors/*.md` are not the Part 2 primary (`EX-stale-operational-anchor`).

| Check | Node | PASS | FAIL |
|---|---|---|---|
| SC-01-P | 03 | `part2/layers/anchor/anchor-assessment.md` exists; `origin_sha256` of the pre-2026-08-16 body equals `92d212841321dffc9add20c01c9ecb3d832e9ce58fcecce6c652ecd61ea7df7a` unless the assessment quotes the exact appended bytes; no rival brief | new rival anchor; rewrite of the 2026-06-21 body; treating `project-docs/source-of-truth-anchors/*.md` as primary |

### RAT-SC-02 — moved from ORIG-SC-02 [lines 181–198]
**Normative residue:** closed set + payload pin + D11 out.

| Field | Required value |
|---|---|
| `source_class` | `decisions` |
| `source_role` | `canonical_choice` |
| `authority_rank` | `2` |
| `part1_id` | one of `D01`–`D10`, `D12`–`D18` |
| `part1_payload_sha256` | `09c15aebd3a424e7f09ce2c27985fa0cbc24a23d9c474182ea4c912b926750a8` |
| `status` | Part 1 enum: `accepted` · `provisional` · `superseded` · `rejected` · `deprecated` |

Reuse Part 1 object fields on the **normalized** twin: `id`, `status`, `statement`, `rationale`, `decided_on`, `replaces`, `replaced_by`, `related_decisions`, `sources[]`. Do not write those fields into the control JSONL. Live control set is all `accepted`. D11 is rejection evidence outside the canonical JSONL.

| Check | Node | PASS | FAIL |
|---|---|---|---|
| SC-02-P | 04 | `part2/layers/decisions/payload-sha256.txt` equals `09c15aebd3a424e7f09ce2c27985fa0cbc24a23d9c474182ea4c912b926750a8`; Part 1 files unmodified; inventory has one row per of the 17 objects covering statement, rationale, supersession, relations, evidence | regenerate or replace the Part 1 payload; add schema-example MCP decisions; promote D11 |

### RAT-CENSUS-HANDOFF — moved from ORIG-SC-03 [lines 200–226]
**Normative residue:** one census row per hit; templates excluded; do not redefine 29 as 26.  
**Bin:** necessary-contract (outcome) + useful-explanation (procedure).  
**Why moved:** multi-checkout/VM choreography is a runbook, not item schema.

| Field | Required value |
|---|---|
| `source_class` | `handoffs` |
| `source_role` | `why_evidence` |
| `authority_rank` | `3` |
| `origin_backing` | `git-backed` · `vm-only` |
| `identity_axis` | `unique` · `duplicate` · `moved` |
| `supersession_status` | `current` · `superseded` |
| `temporal_confidence` | `dated` · `temporally-ambiguous` |
| `presence` | `present` · `missing` |
| `handoff_number` | numeric stem as string, or `unnumbered` |

**Census method `CENSUS-HANDOFF` (replaces the bare number 29):**

1. Enumerate `.handoffs/*.md` in this worktree (measured: 26 files).
2. Enumerate `.handoffs/*.md` in `/Users/sab-mini/repos/MyAPI` if that tree is a distinct checkout.
3. Emit a stub row for each missing number in `000`–`036` that has no file (`001`, `003`–`008`, `016`–`019` in this tree).
4. Probe VM surfaces named in `AGENTS.md` (`sab-dev`, and any path recorded in `.handoffs/030`). Unreachable surfaces become rows with `presence=missing`, `origin_backing=vm-only`, and `exclusion_reason` containing the probe command plus an ISO-8601 probe timestamp.
5. Treat the memo phrase “29 known handoffs” as a **search target**. Node 05 must find, duplicate-match, or mark missing until every claimed identity has a row. Do not redefine 29 as 26.

Templates `000-template.md` and `009-legacy-handoff-template.md` enter the census and default to `inclusion_status=excluded`, `exclusion_reason=EX-template`.

| Check | Node | PASS | FAIL |
|---|---|---|---|
| SC-03-P | 05 | `part2/layers/handoffs/handoff-manifest.jsonl` has one row per census hit; every axis filled; included set rebuilds from the manifest; `occurred_at` and `recorded_at` keys exist; missing numbers are `presence=missing` rows | summarize away the listing; drop unreachable VM artifacts; treat templates as project history; silently change 29 into 26 |

### RAT-SC-04 — moved from ORIG-SC-04 [lines 228–273]
**Normative residue:** what-changed + IN-06 + stat required / diff bounded+truncated.  
**Bin:** necessary-contract (role) + speculative-machinery (optional last-30 satellite repos).  
**Why moved:** 7-repo survey is not the Git job.

Git is **what changed**. It is not a second decision authority. See ORIG-§13.

**Repositories the original contract named** (`repo` / `origin.repo`) — NON-NORM unless a decision cites them:

| `repo` | Checkout | Depth rule | Required? |
|---|---|---|---|
| `MyAPI` | this worktree / `skchaudr/MyAPI` (originally pinned at `ffece0a9…`) | IN-06 path/date/cite bounds | yes |
| `MyAPI` sibling | `/Users/sab-mini/repos/MyAPI` if distinct and reachable | same bounds; compare as witness | if reachable |
| cited decision repos | any repo named by an admitted decision `git_refs[]` | those refs only | yes, those refs |
| `gddp-runtime` | reachable clone named by `.handoffs/030` | last-30 inventory only | optional; mark unreachable rather than drop |
| `gddp-config` | same | last-30 inventory only | optional |
| `pi-agent` | same | last-30 inventory only | optional |
| `myapi-corpus` | sibling corpus worktree if present | only paths an admitted decision already cites | if cited |

Do not widen into full eternal history.

**Required export fields per commit item:**

| Field | Type | Rule |
|---|---|---|
| `commit_sha` | string | full 40-char SHA |
| `parent_shas` | string[] | full SHAs; `[]` for roots |
| `author_date` | string | absolute ISO-8601 |
| `committer_date` | string | absolute ISO-8601 |
| `subject` | string | commit subject |
| `affected_paths` | string[] | from name-status |
| `change_evidence` | object | see below |

`change_evidence` policy (named, not adjectival). The exact constant `65536` is a useful default, not a Node 09 schema field:

| Subfield | Required | Rule |
|---|---|---|
| `change_evidence.stat` | yes | `git log --name-status` plus numstat for that commit |
| `change_evidence.diff` | yes when IN-06 includes the commit | unified diff, path-bounded to IN-06 paths |
| `change_evidence.max_bytes` | advisory default | `65536` per commit |
| `change_evidence.truncated` | yes | `true` if diff exceeded max; stat still required |

Full-repo dumps, generated Graphify HTML, and `.pi-subagents/` session dumps are excluded. Temporal mapping: `occurred_at` = `author_date`; `recorded_at` = `committer_date`.

| Check | Node | PASS | FAIL |
|---|---|---|---|
| SC-04-P | 06 | export + `build_git_export.(py|sh)` under `part2/layers/git/`; rebuild SHA matches; every date is absolute ISO-8601; repo set and depth rule recorded | ingest raw `git log` as the only layer; relative dates; treat commit messages as Sab review marks; dump entire clone |

### RAT-SC-05 — moved from ORIG-SC-05 [lines 275–294]
**Normative residue:** pin live graph; keep both representations.

| Field | Required value |
|---|---|
| `source_class` | `graphify` |
| `source_role` | `what_exists_now` |
| `authority_rank` | `5` |
| `graph_sha256` | SHA-256 of the pinned `graphify-out/graph.json` bytes |
| `built_at_commit` | `d82a5eaefaa76ed8a9f815660052c8637a50e1b9` until a later node is authorized to pin a new snapshot |
| `representation` | `retrieval_text` **or** `deterministic_struct` (both must exist as items sharing `source_id`) |

Pin the live file. Do not refresh graph truth in this experiment unless a later node is explicitly authorized. Node 07 records both `built_at_commit` and worktree HEAD. Retrieval-text is a bounded projection (ids, labels, `source_file`, relations). It must not dump the 41068 document nodes. Node 07 states the filter it used (`file_type`, `source_file` prefix).

| Check | Node | PASS | FAIL |
|---|---|---|---|
| SC-05-P | 07 | inventory states live counts from actual `graph.json`; both representations preserved; questions split into retrieval-friendly vs deterministic lookup; both SHAs recorded | treat `GRAPH_REPORT.md` hubs as semantic truth; collapse Graphify into Khoj; mutate `graphify-out/` as graph truth; mix a mid-experiment `graphify update` without a new pin |

### RAT-SC-06 — moved from ORIG-SC-06 [lines 296–324]
**Normative residue:** gap_only; genuinely-absent only; not in 12–16.

| Field | Required value |
|---|---|
| `source_class` | `cli-derived` |
| `source_role` | `gap_fill` |
| `authority_rank` | `6` |
| `inclusion_status` | `gap_only` |
| `provenance_kind` | `session` |
| `session_ref` | native session id or path |
| `failure_class` | `genuinely-absent` |

`origin_path` must be the session file (`~/.codex/sessions/**`, `~/.claude/projects/**`, `~/.pi/agent/sessions/**` stored without `~` expansion, or a copied `part2/` extract that still cites that path). Allowed failure classes (Node 17): exactly one of `retrieval-missed` · `synthesis-failed` · `genuinely-absent`. Only the third earns extraction.

| Check | Node | PASS | FAIL |
|---|---|---|---|
| SC-06-P | 17 | every `cli-derived` item cites `session_ref` and a `genuinely-absent` question id; holdout run once; other failure classes never extract | bulk-ingest CLI/chat as a sixth durable layer; extract to raise scores; touch the holdout before the designated run |

---

## Authority runbooks

### RAT-authority — ORIG-§6 rank table [lines 326–337]
**Normative residue:** ranks 1–6 + home claim_type in revised §5/§6.

When two included items disagree, later nodes apply this order. Lower `authority_rank` wins on the class’s home `claim_type` and yields elsewhere.

| `authority_rank` | `source_class` | Wins on `claim_type` | Yields on |
|---|---|---|---|
| `1` | `anchor` | `identity_orientation` (identity, glossary, MCP names, do-not-re-litigate, layer boundaries) | specific dated facts, commit contents, graph edges |
| `2` | `decisions` | `what_was_decided` (status, rationale, supersession, relations inside the closed set) | expanding the set; current code shape if Git/Graphify contradict enactment |
| `3` | `handoffs` | `why_changed` (session chronology, empirical leads) | reversing a reviewed decision; creating new canonical decisions |
| `4` | `git` | `what_changed` (when, which files, parent lineage) | Sab’s wording or review mark |
| `5` | `graphify` | `what_exists_now` (structure in the pinned snapshot) | historical why; decisions not present as code/docs |
| `6` | `cli-derived` | a fact proven absent from ranks 1–5 | any durable-layer contradiction; holdout leakage |

### RAT-AO-01 — ORIG-AO-01 [lines 339–347]
Same-rank conflicts resolve by (1) `supersession_status=current` over `superseded`, then (2) later `occurred_at` if both are non-null and `temporal_confidence=dated`, else (3) set `temporal_confidence=temporally-ambiguous` and keep both items with distinct `item_id`s — do not silently pick. AO-01-P: no included pair with contradictory normative statements shares the same rank without a recorded resolver. FAIL: retrieval rank or embedding similarity used as authority.

### RAT-AO-02 — ORIG-AO-02 [lines 349–360]
Applies only inside `source_class=decisions`. Inherited from `01-decisions/output/sources.md`:

1. Sab review mark (`provenance_kind=review_sheet`) controls inclusion/status.
2. Normalized decision note supplies wording.
3. Schema controls shape.
4. Anchors / plans / handoffs may clarify, not create or reverse.

AO-02-P: every canonical decision still cites review sheet + repo-local note + Corpus v1.0 parity witness. FAIL: handoff or Graphify used to flip a `Y`/`N`.

### RAT-AO-03 — ORIG-AO-03 [lines 362–372]
Node 11 uses `control_role=part1_continuity_control` and the Part 1 bytes. Nodes 12/14/15/16 may use `representation=normalized` twins under `part2/` only. The twin must cite the control SHA and must not replace it. AO-03-P: `payload-sha256.txt` still matches live `01-decisions/output/decisions-canonical.jsonl`. FAIL: Node 11 ingests the normalized twin instead of the Part 1 snapshot.

### RAT-AO-04 — moved from ORIG-AO-04 [lines 374–386]
**Normative residue:** none for Nodes 02–09.  
**Bin:** speculative-machinery as a Node 09 FAIL; useful as Node 10/18 answer policy.  
**Why moved:** treatments measure contribution; they do not route.

Claim-type override table (when `claim_type` is set on a question or answer span):

| `claim_type` | Winner | Then | Then | Must not win |
|---|---|---|---|---|
| `identity_orientation` | `anchor` | `decisions` | `handoffs` | `cli-derived` |
| `what_was_decided` | `decisions` | `anchor` | `handoffs` | `git` / `graphify` as decision text |
| `why_changed` | `handoffs` | `decisions` | `git` | `graphify` |
| `what_changed` | `git` | `handoffs` | `decisions` | `anchor` recency |
| `what_exists_now` | `graphify` | `git` | `decisions` | `handoffs` as structure |

AO-04-P (advisory): each conflict with a non-null `claim_type` uses the winner order in this table, and the applied source order is recorded.

### RAT-khoj-metadata — ORIG-§7 intro [lines 388–394]
Serialization: YAML frontmatter on Markdown items **and** the same fields on JSON/JSONL records. Khoj may index these fields as metadata or only as document text (Node 02 records which). The fields must exist on the item even if Khoj ignores them as metadata. The Part 1 control payload must not grow these fields.

---

## Envelope archives

### RAT-envelope-full — moved from ORIG-§7.1 [lines 396–458]
**Normative residue:** the 12-field table.  
**Bin:** speculative-machinery as a universal 36-required set.  
**Why moved:** exported complexity; Node 05 cannot “stamp six fields and move on.”

Original required flat envelope (every item). Missing or illegal values failed Node 09:

| Field | Type / format | Nullability | Required | Mechanical rule |
|---|---|---|---|---|
| `schema_version` | string | non-null | yes | must equal `2.0-part2-prov` |
| `item_id` | string | non-null | yes | unique within layer; `^[A-Za-z0-9][A-Za-z0-9_.:/-]{2,127}$`; pattern `{source_class}:{stable-id}[:variant]`; preserve native ID case |
| `source_class` | enum | non-null | yes | `anchor` \| `decisions` \| `handoffs` \| `git` \| `graphify` \| `cli-derived` |
| `source_id` | string | non-null | yes | durable ID of the originating source; `{source_class}:{native-id}` |
| `source_role` | enum | non-null | yes | `orientation` \| `canonical_choice` \| `why_evidence` \| `what_changed` \| `what_exists_now` \| `gap_fill` |
| `layer_id` | enum | non-null | yes | same closed set as `source_class` |
| `stable_key` | string | non-null | yes | unique within the layer |
| `authority_rank` | int | non-null | yes | `1`–`6` matching §6 |
| `control_role` | enum | non-null | yes | `none` \| `part1_continuity_control` \| `parity_witness` |
| `project` | string | non-null | yes | verbatim home(s), slash-joined; ∈ {`MyAPI`, `GDDP`, `Pi`, `MyAPI/Khoj`, `MyAPI/Pi/GDDP`} |
| `origin_path` | string | non-null | yes | repo-relative POSIX path, or `vm:{host}:{abs-path}`, or `git:{repo}@{sha}`; no `~`; no backslashes |
| `origin_sha256` | 64-hex or sentinel | sentinel only if missing | yes | SHA-256 of source bytes, or `origin_unavailable` iff `presence=missing` |
| `layer_item_sha256` | 64 lowercase hex | non-null if `presence=present` | yes | SHA-256 of the normalized item bytes that will be indexed |
| `content_sha256` | 64 lowercase hex | null iff availability is missing, redacted, or unreadable | yes | same bytes Node 09 re-hashes |
| `provenance_kind` | enum | non-null | yes | `anchor` \| `memo` \| `review_sheet` \| `handoff` \| `commit` \| `graph` \| `session` \| `other` |
| `occurred_at` | ISO-8601 date/datetime or `null` | `null` allowed | yes (key required) | event/validity time; never a relative phrase |
| `occurred_at_precision` | enum | non-null | yes | `second` \| `minute` \| `day` \| `month` \| `year` \| `unknown`; `unknown` iff `occurred_at=null` |
| `occurred_at_basis` | enum | non-null | yes | a §8.1 occurred-basis value |
| `occurred_at_ambiguity` | enum | non-null | yes | `none` \| `approximate` \| `conflicting` \| `missing` |
| `recorded_at` | ISO-8601 date/datetime or `null` | `null` allowed when no evidenced inscription clock exists | yes (key required) | inscription/capture time |
| `recorded_at_precision` | enum | non-null | yes | same enum as `occurred_at_precision` |
| `recorded_at_basis` | enum | non-null | yes | a §8.1 recorded-basis value |
| `recorded_at_ambiguity` | enum | non-null | yes | `none` \| `approximate` \| `conflicting` \| `missing` |
| `timezone_basis` | enum | non-null | yes | `utc` \| `local_unknown` \| `source_offset` |
| `temporal_candidates` | object[] | non-null (may be `[]`) | yes | at least two candidates for a `conflicting` clock |
| `temporal_confidence` | enum | non-null | yes | `dated` \| `temporally-ambiguous` |
| `presence` | enum | non-null | yes | `present` \| `missing` |
| `inclusion_status` | enum | non-null | yes | `included` \| `excluded` \| `control_only` \| `gap_only` |
| `exclusion_reason` | enum or `null` | `null` iff `inclusion_status=included` | yes | a §10 `EX-*` code when not included |
| `supersession_status` | enum | non-null | yes | `current` \| `superseded` \| `rejected` \| `not_applicable` |
| `replaces` | string[] | non-null (may be `[]`) | yes | `item_id`s this item supersedes |
| `replaced_by` | string or `null` | `null` allowed | yes | single successor `item_id` |
| `representation` | enum | non-null | yes | `verbatim` \| `normalized` \| `retrieval_text` \| `deterministic_struct` \| `parity_witness` |
| `treatment_eligibility` | string[] | non-null (may be `[]`) | yes | subset of the §11 treatment ids |
| `origin_backing` | enum | non-null | yes | `git-backed` \| `vm-only` \| `derived` |
| `identity_axis` | enum | non-null | yes | `unique` \| `duplicate` \| `moved` |
| `canonical_item_id` | string or `null` | required if duplicate/moved | conditional | survivor `item_id` |
| `claim_type` | enum or `null` | `null` allowed | no | `identity_orientation` \| `what_was_decided` \| `why_changed` \| `what_changed` \| `what_exists_now` |

`inclusion_status` mapping used by Node 09 treatment assembly:

| `inclusion_status` | May enter a retrieval treatment? |
|---|---|
| `included` | yes, if `presence=present` and the treatment’s class set contains `source_class` |
| `control_only` | only `part1-control` |
| `gap_only` | only `cli-gap-fill` |
| `excluded` | no |

Original invariants:

- `presence=missing` ⇒ `inclusion_status=excluded` and `origin_sha256=origin_unavailable`.
- `supersession_status=superseded` ⇒ `replaced_by != null`.
- `identity_axis` ∈ {`duplicate`, `moved`} ⇒ `canonical_item_id != null`.
- `inclusion_status=included` ⇒ `exclusion_reason=null`.
- `inclusion_status≠included` ⇒ `exclusion_reason` is a §10 code.
- If `content_identity.hash_scope=item_bytes`, then `layer_item_sha256 == content_sha256 == content_identity.content_sha256`.
- On a derived present item, `origin_sha256 == content_identity.source_content_sha256`; on a non-derived origin item, `content_identity.source_content_sha256=null`.

### RAT-nested-objects — moved from ORIG-§7.2 [lines 460–509]
**Normative residue:** none as universal mandate; `extracted_at ≠ occurred_at` kept as a time rule.  
**Bin:** speculative-machinery  
**Why moved:** duplicates §7.1 (`origin_path` vs `origin.ref`). 06/08 do not need OriginSpan / newline / encoding enums to export a commit.

These were required on Node 08+ items in addition to the flat fields. Flat `origin_path` must equal `origin.ref` when `origin.scheme` is `repo_path` or `vm_path`.

#### `origin`

| Field | Type | Required | Allowed values |
|---|---|---|---|
| `origin.scheme` | enum | yes | `repo_path` · `abs_path` · `git_object` · `session_id` · `vm_path` · `url` · `graphify_node` |
| `origin.ref` | string | yes | Exact locator. POSIX `/`. Full SHAs. No `~`. |
| `origin.repo` | string or `null` | yes | `MyAPI` · `MyAPI-rebuild` · `gddp-runtime` · `gddp-config` · `pi-agent` · `myapi-corpus` · `none` |
| `origin.git_rev` | string or `null` | yes | Full commit SHA that contains `ref` when `scheme=repo_path` and the file is git-backed; else `null` |
| `origin.host` | enum | yes | `mac` · `vm` · `external` · `unknown` |
| `origin.span` | object or `null` | yes | `OriginSpan` when the item is not the whole file |
| `origin.exists_at_record` | enum | yes | `present` · `missing` · `unverified` |

`OriginSpan`: `kind` ∈ {`lines`, `bytes`, `json_pointer`, `commit_path`, `symbol`, `heading`}; `start` required; `end` optional. Do not store file mtimes in `origin`.

#### `content_identity`

| Field | Type | Required | Allowed values |
|---|---|---|---|
| `content_identity.alg` | enum | yes | `sha256` only |
| `content_identity.content_sha256` | string | unless missing/redacted/unreadable | `^[0-9a-f]{64}$` |
| `content_identity.hash_scope` | enum | yes | `source_bytes` · `item_bytes` · `payload_bytes` · `git_object` |
| `content_identity.byte_length` | int or `null` | yes | `null` only when missing/redacted |
| `content_identity.encoding` | enum | yes | `utf-8` · `binary` · `unknown` |
| `content_identity.availability` | enum | yes | `present` · `missing` · `redacted` · `unreadable` |
| `content_identity.source_content_sha256` | string or `null` | yes | origin bytes when derived |
| `content_identity.newline` | enum or `null` | if utf-8 present | `lf` · `crlf` · `mixed` · `none` |
| `content_identity.pin_name` | string or `null` | if `control_role≠none` | a §4 pin name |

Hashed `item_bytes` omit `extracted_at` and `build_id` (`P-A-4`). Those clocks live on the layer-manifest row.

#### `extraction_trace`

| Field | Type | Required | Allowed values |
|---|---|---|---|
| `extraction_trace.extracted_at` | datetime | yes | UTC ISO-8601 with `Z` |
| `extraction_trace.extractor_id` | string | yes | node or script id |
| `extraction_trace.extractor_version` | string | yes | git SHA or dated version string |
| `extraction_trace.method` | enum | yes | `copy_bytes` · `structured_extract` · `normalize` · `inventory_stub` · `cli_gap_fill` |
| `extraction_trace.inputs` | object[] | yes | each `{ref, sha256, role}`; `role` ∈ {`wording`, `inclusion_authority`, `parity_witness`, `rationale_support`, `extraction_contract`, `payload`, `span_source`} |
| `extraction_trace.build_id` | string or `null` | no | GDDP job/attempt id; never written into graph truth |
| `extraction_trace.source_manifest_sha256` | string or `null` | Node 08+ | hash of the layer manifest |
| `extraction_trace.notes` | string or `null` | no | non-normative; cannot carry a date absent from the flat temporal fields or `temporal_candidates` |

`extracted_at` must not be copied into `occurred_at` or `recorded_at`.

### RAT-class-extras — ORIG-§7.3 [lines 511–528]
**Normative residue:** compressed class-extra list in revised §7.

| `source_class` | Extra required fields |
|---|---|
| `anchor` | `anchor_path` = `project-docs/REBUILD-CONTEXT-ANCHOR.md`; `extension` = `none` or quoted added span |
| `decisions` | all Part 1 object fields: `id`, `schema_version`, `project`, `title`, `summary`, `statement`, `rationale`, `status`, `decided_on`, `decided_by`, `review_mark`, `confidence`, `sources`, `evidence_paths`, `git_refs`, `replaces`, `replaced_by`, `related_decisions`, `tags`, `notes`; plus `part1_id`, `part1_payload_sha256` |
| `handoffs` | `handoff_number`; `origin_backing`; `identity_axis`; `presence`; `temporal_confidence` |
| `git` | `commit_sha`, `parent_shas[]`, `affected_paths[]`, `subject`, `change_evidence` |
| `graphify` | `graph_sha256`, `built_at_commit`, `representation` ∈ {`retrieval_text`, `deterministic_struct`} |
| `cli-derived` | `session_ref`; `failure_class=genuinely-absent` |

`source_family` was required when: handoffs `repo_handoff` \| `vm_handoff`; git `git_commit` \| `git_diff`; graphify `graphify_snapshot` \| `graphify_node`. RETIRE-AS-MANDATE as a universal extra.

### RAT-checks-prov — ORIG-§7.4 [lines 530–549]
**Normative residue:** ID-1/2/3, P-1/2/3 in revised §12.

| ID | Fields | PASS | FAIL |
|---|---|---|---|
| `P-ID-1` | `item_id` | 0 collisions inside a layer | any duplicate `item_id` |
| `P-ID-2` | `source_class` | all values in the closed enum | unknown class |
| `P-ID-3` | `source_id` | matches class pattern | malformed or prefix mismatch |
| `P-ID-4` | `project` | verbatim homes, no empty segment | spaced aliases, case-fold |
| `P-ID-5` | `origin_path` / `origin.ref` | POSIX, non-empty | `~`, backslashes, blank |
| `P-ID-6` | `origin.git_rev` | set on git-backed `repo_path` | `null` on a tracked file claimed git-backed |
| `P-ID-7` | `origin.scheme`, `origin.host` | `vm_path` + `vm` for `source_family=vm_handoff` | invented Mac path for a VM-only file |
| `P-ID-8` | `presence`, `inclusion_status` | missing items are stubs only | missing origin included as present |
| `P-HASH-1` | `origin_sha256`, `content_sha256` | `^[0-9a-f]{64}$` or legal sentinel | uppercase, SHA-1 length |
| `P-HASH-2` | `content_sha256` | recomputed bytes equal stored hash | any mismatch |
| `P-HASH-3` | `layer_item_sha256`, `content_sha256`, `content_identity.content_sha256` | all three equal when `content_identity.hash_scope=item_bytes` | any divergence |
| `P-HASH-4` | `origin_sha256`, `content_identity.source_content_sha256` | equal on every derived present item | null or mismatch on a derived present item |
| `P-A-4` | `content_identity.hash_scope`, `extraction_trace.extracted_at`, `extraction_trace.build_id` | hashed canonical `item_bytes` omit both volatile trace fields | either volatile field changes an item hash |
| `IN-02` | `origin_path`, `origin_sha256`, `provenance_kind`, `recorded_at` | Node 09 provenance-integrity green per layer | “from memory”; Khoj-index-only with no filesystem/git origin |

---

## K. Temporal edge-case handbook

### RAT-temporal-intro — ORIG-§8 [lines 551–558]
These two fields are the entire temporal contract. Other clocks (`created_at`, `updated_at`, `ingested_at`, `decided_on`, `extracted_at`, filesystem mtime) are inputs to basis, not substitutes.

| Field | Meaning | Answers |
|---|---|---|
| `occurred_at` | Event / validity time. When the decision was made, the commit was authored, the handoff episode happened, or the named change happened. | “What happened on 2026-08-14?” |
| `recorded_at` | Inscription / observation time. When this fact was written down, committed by the committer, handoff-dated, review-marked, or structurally observed. | “When was this written or captured?” |

### RAT-temporal-fields — ORIG-§8.1 [lines 560–576]
**Normative residue:** `occurred_at`, `recorded_at`, `temporal_confidence`.  
**Bin:** speculative as all-required micro-enums.

| Field | Type | Required | Allowed values |
|---|---|---|---|
| `occurred_at` | string or `null` | yes | `YYYY-MM-DD` or `YYYY-MM-DDTHH:MM:SSZ` or offset datetime; `null` if unknown |
| `occurred_at_precision` | enum | yes | `second` · `minute` · `day` · `month` · `year` · `unknown` |
| `occurred_at_basis` | enum | yes | `author_date` · `committer_date` · `decided_on` · `handoff_date` · `frontmatter_date` · `session_first_event` · `explicit_in_text` · `review_mark_date` · `unknown` |
| `occurred_at_ambiguity` | enum | yes | `none` · `approximate` · `conflicting` · `missing` |
| `recorded_at` | string or `null` | yes | same type rules as `occurred_at` |
| `recorded_at_precision` | enum | yes | same as occurred |
| `recorded_at_basis` | enum | yes | `committer_date` · `handoff_date` · `frontmatter_date` · `review_mark_date` · `ingest_time` · `snapshot_time` · `file_write` · `explicit_in_text` · `unknown` |
| `recorded_at_ambiguity` | enum | yes | `none` · `approximate` · `conflicting` · `missing` |
| `timezone_basis` | enum | yes | `utc` · `local_unknown` · `source_offset` |
| `temporal_candidates` | object[] | yes | each entry is `{role, value, basis, source_ref}` |
| `temporal_confidence` | enum | yes | `dated` iff `occurred_at` is a calendar date taken from the source and `occurred_at_ambiguity` ∈ {`none`, `approximate`}; else `temporally-ambiguous` |

### RAT-temporal-class-map — ORIG-§8.2 [lines 578–588]
**Normative residue:** compressed class map in revised §8.

| `source_class` | `occurred_at` | `recorded_at` |
|---|---|---|
| `anchor` | dated current-direction stamp if present; else `2026-06-21` (status line) with `occurred_at_basis=explicit_in_text` | document dated header if distinct; else `null` + `recorded_at_ambiguity=missing`. File mtime must not replace the document date. |
| `decisions` | `decided_on` as day-precision (`occurred_at_basis=decided_on`) | independently evidenced write/review/commit date of the JSONL or review sheet. Do not clone `decided_on` into `recorded_at`. |
| `handoffs` | explicit episode date in the body; else `null` + `temporally-ambiguous` | `Date:` in Agent Section if `YYYY-MM-DD` (`recorded_at_basis=handoff_date`); else git author date if `git-backed`, else copy timestamp with `recorded_at_ambiguity` ≠ `none` if that clock is mtime |
| `git` | `author_date` | `committer_date` |
| `graphify` snapshot | author date of `built_at_commit` (absolute, from git) | graph file commit/export time |
| `graphify` node | `null` unless the node encodes an event | snapshot / extract time |
| `cli-derived` | session event time (`session_first_event`) | extract time is **not** either field; it is `extracted_at` only |

### RAT-temporal-hard — ORIG-§8.3 [lines 590–619]
**Normative residue:** keys exist; no relative dates; no invent occurred_at; git author/committer; null is first-class.

Original hard rules 1–10 (kept in compressed form; full text retained here):

1. Timestamp keys always exist. Forbidden date values: `""`, `"null"`, `"N/A"`, `"unknown"`, `"TBD"`, `0`, epoch-zero. Unknown event time uses YAML/JSON `null`, not the string `unknown`.
2. If the date’s role is unclear, leave `occurred_at=null` with `occurred_at_ambiguity=missing` and `temporal_confidence=temporally-ambiguous`. Do not guess that a write date is an event date. Do not copy `recorded_at` into `occurred_at`.
3. If two evidenced dates disagree, do not pick a winner. Set the matching `*_ambiguity=conflicting`, keep the primary field `null`, and list every candidate.
4. Coarse dates (“August 2026”) store `YYYY-MM-01` or `YYYY-01-01` only with `precision=month|year` and `ambiguity=approximate`, and keep the original token in `temporal_candidates[].value`.
5. `precision=unknown` is allowed only when the timestamp is `null`.
6. `extracted_at`, Khoj ingest time, and mtime are not `occurred_at`. Mtime may appear as a `temporal_candidates` row with `basis=file_write` only when no better recorded clock exists, and then `recorded_at_ambiguity` cannot be `none`.
7. Evaluation questions use absolute dates. Items that can answer “What changed on 2026-08-14?” must have `occurred_at` at day precision or finer, `ambiguity` ∈ {`none`, `approximate`}, and `occurred_at_basis` ∈ {`author_date`, `explicit_in_text`, `decided_on`, `session_first_event`}.
8. A null `occurred_at` is a first-class answer. Retrieval may still use the item for `what_exists_now` / rationale questions. It is a FAIL to backfill it to make a temporal question look answered.
9. `timezone_basis=local_unknown` is required when the source date has no offset (Part 1 `decided_on`, most handoff `Date:` headers). Store the calendar date as `YYYY-MM-DD` without inventing `T00:00:00Z`.
10. Relative date words are forbidden in items **and** in this contract’s normative examples.

| ID | Fields | PASS | FAIL |
|---|---|---|---|
| `P-T-1` | `occurred_at`, `recorded_at` | keys exist as value or `null` | omitted fields |
| `P-T-2` | both timestamps | only ISO date/datetime or `null` | forbidden sentinels |
| `P-T-3` | null timestamp | matching `ambiguity` ∈ {`missing`, `conflicting`} and `precision=unknown` | null with `ambiguity` ∈ {`none`, `approximate`} |
| `P-T-4` | non-null timestamp | parses and matches `precision` | `2026-08-08T00:00:00Z` minted from a date-only source |
| `P-T-5` | `occurred_at_basis` | legal for class | mtime / ingest / `extracted_at` as occurred |
| `P-T-6` | `extracted_at` | ≠ `occurred_at` and ≠ `recorded_at` unless the item is the extraction event | cloned clocks |
| `P-T-7` | `temporal_candidates` | listed when `conflicting`; primary fields null | winner picked without evidence |
| `P-T-8` | git items | occurred=author, recorded=committer | swapped or mtime used |
| `P-T-9` | graphify node items | occurred null unless node-encoded event | snapshot time stored as occurred on a node |
| `P-T-10` | Part 1 `decided_on` | maps to occurred day; recorded not cloned | `recorded_at=decided_on` with no second clock |
| `P-T-11` | dated questions | require occurred day+ and ambiguity in {`none`,`approximate`} | answering a dated question from recorded/mtime only |
| `P-T-12` | date-only sources | `timezone_basis=local_unknown` | silent UTC conversion |
| TM-01 | all classes | no relative dates; `unknown` string not used as a timestamp | recency decay used to override `decisions` / `anchor` authority |

---

## Inclusion / exclusion archives

### RAT-inclusion-tables — ORIG-§9 [lines 621–677]
**Normative residue:** compressed IN-01…IN-07 in revised §9.

An item is `inclusion_status=included` only if all of IN-01–IN-07 hold.

**IN-01 Class membership.** `source_class` ∈ §5 closed set. PASS: unknown class count = 0. FAIL: v1 `source_type` used as `source_class`.

**IN-02 Provenance complete.** `origin_path`, `origin_sha256`, `provenance_kind`, `recorded_at` all present and legal. PASS: Node 09 provenance-integrity green. FAIL: memory-only or index-only items. (`provenance_kind` is no longer envelope-required; the 12-field set replaces this predicate.)

**IN-03 Project-history relevance.** `project` ∈ {`MyAPI`, `GDDP`, `Pi`, `MyAPI/Khoj`, `MyAPI/Pi/GDDP`}. FAIL: friend-refinery dumps, personal-life notes, or Corpus v1.0 bulk as default members.

**IN-04 Treatment eligibility declared.** `treatment_eligibility[]` equals the §11 matrix. FAIL: CLI in any 12–16 treatment; decisions leaking into `no-decisions`; handoffs leaking into `code-reality`. RETIRE-AS-MANDATE as a stored field; TC-2/TC-3 still fail those leaks.

**IN-05 Handoff inclusion is manifest-explicit.** Included only if `presence=present` and backing is `git-backed` or a copied VM artifact with recorded origin. Templates default to `excluded`. `control_only` is forbidden for templates.

**IN-06 Git inclusion is bounded.** Include a commit iff it touches `.handoffs/`, `project-docs/`, `01-decisions/`, `02-corpus/`, `03-ingestion/`, `04-evaluation/`, `AGENTS.md`, `PROJECT-BRIEF.md`, `gddp/`, `graphify-out/GRAPH_REPORT.md`, or is cited in an admitted decision `git_refs[]`, or falls inside a dated eval window once Node 10 freezes absolute dates. Always emit `change_evidence.stat`. Emit `change_evidence.diff` only for those commits. IN-06-P FAIL: full clone dump; generated HTML from Graphify; `.pi-subagents/` session dumps.

**IN-07 Graphify inclusion is snapshot-pinned.** One pinned snapshot; retrieval text derived from that snapshot only. FAIL: mixing live `graphify update` output mid-experiment without a new pin + hash.

### RAT-exclusion-detail — ORIG-§10 [lines 679–704]
**Normative residue:** the 16 `EX-*` codes. Long PASS columns live here.

`exclusion_reason` is required whenever `inclusion_status≠included`.

| Code | Exclude | Why | PASS check |
|---|---|---|---|
| `EX-bulk-vault` | Full `Corpus v1.0/` except the decision-note parity witness and items an admitted decision already cites | v0 gravity well; Part 1 `sources.md` already excludes it | Node 08 file set contains 0 extra vault notes |
| `EX-bulk-chat` | ChatGPT/Claude-web exports, `_chats/`, conversational dumps | Volume drowned v0; not a Part 2 class | no `source_class` minted from those paths |
| `EX-bulk-cli` | Raw CLI session archives as durable layers | Node 17 only, and only `genuinely-absent` | Nodes 12–16 manifests have zero `cli-derived` |
| `EX-unreviewed-decision` | Any new decision not in D01–D10, D12–D18 / not Y-marked | Closed review is the control | inventory count == 17 accepted |
| `EX-d11-rejected` | D11 as an accepted object | Sab marked N; keep as rejection evidence only | D11 absent from canonical JSONL and from `decisions-only` hashes |
| `EX-schema-example` | MCP naming examples inside `decision-schema.md` | Demonstrate shape; outside closed review | those ids never appear as layer items |
| `EX-eval-questions` | `QUERIES-*.md`, `04-evaluation/queries/*` as corpus | Questions are the ruler, not evidence | Node 10 may freeze them; Node 08 must not ingest them |
| `EX-runtime` | Khoj indexes, GDDP runtime DBs, job receipts, VM live notes except copied-and-hashed artifacts | Mutable; not reconstructible | no runtime path in `origin_path` unless copied under `part2/` with hash |
| `EX-graph-truth-write` | Edits to `graphify-out/graph.json` / GDDP graph import as a side effect of this experiment | Graph truth stays untouched | `git status` on those paths remains clean for this node |
| `EX-template` | `.handoffs/000-template.md`, `.handoffs/009-legacy-handoff-template.md`, empty SAB-only tails as knowledge | Form, not history | template `inclusion_status=excluded` |
| `EX-duplicate` | Byte-identical second copy (e.g. Corpus v1.0 keeper vs repo-local note) | Parity witness, not a second record | duplicate has `identity_axis=duplicate` and is not double-ingested |
| `EX-missing` | Numbered handoff slots with no file (`001`, `003`–`008`, `016`–`019` in this tree) | Must be logged, not invented | manifest rows exist; `presence=missing`; `origin_sha256=origin_unavailable` |
| `EX-stale-operational-anchor` | `project-docs/source-of-truth-anchors/*.md` as primary | Dated operational snapshots; not the rebuild candidate | not in `anchor/` layer unless Node 03 explicitly cites one as evidence; `authority_rank` still 1 only for `REBUILD-CONTEXT-ANCHOR.md` |
| `EX-score-tuning` | Any add/drop done to improve judge scores | Violates experimental gate | treatment logs show no post-start corpus edits |
| `EX-part3-routing` | Classifier/router logic, extra MCP tools | Stop boundary | no routing code or corpus built “for the router” |
| `EX-unreachable-vm` | VM-only path that did not answer a probe | Must be a row, not a silent drop | `presence=missing` + probe command + ISO-8601 probe time in `exclusion_reason` note / `extraction_trace.notes` |

**Downstream PASS/FAIL (Node 09):** every excluded candidate that was *considered* has a manifest row + `exclusion_reason`. Silent omission of a known class (especially the missing handoff numbers, D11, or VM-only paths) is FAIL.

---

## J. Treatment assembly appendix

### RAT-treatment-aliases — ORIG-§11 [lines 706–734]
**Normative residue:** frozen 7-id matrix.

Aliases (advisory notes only; do not store):

| Stored `treatment_id` | Alias |
|---|---|
| `part1-control` | `t11_part1_control` |
| `decisions-only` | `t12_normalized_decisions`, “Normalized decisions” |
| `no-decisions` | `t13_no_decisions` |
| `handoff-enriched` | `t14_handoff_enriched` |
| `code-reality` | `t15_code_reality` |
| `full-durable` | `t16_full_durable` |
| `cli-gap-fill` | `t17_cli_gapfill` |

Node 09 emits exactly the six manifests `part1-control`, `decisions-only`, `no-decisions`, `handoff-enriched`, `code-reality`, `full-durable`. Absence of `cli-gap-fill` from that directory is intentional.

### RAT-TreatmentManifest — ORIG-§11.1 [lines 736–768]
**Normative residue:** hash recipe + `result_disposition` + id/layers/item_ids.

Full original 14-field schema (policy enums RETIRE-AS-MANDATE until a Node 09 check needs them):

| Field | Type | Required | Rule |
|---|---|---|---|
| `schema_version` | string | yes | `part2-treatment-1.0` |
| `treatment_id` | enum | yes | one of the seven ids |
| `node_id` | string | yes | `11`…`17` |
| `layers_included` | `source_class`[] | yes | exact set from the matrix; order frozen |
| `layers_excluded` | `source_class`[] | yes | complement |
| `item_ids` | string[] | yes | concatenation of each included layer’s indexed `item_id`s in layer order, then item order |
| `layer_manifest_sha256` | object | yes | `{layer_id: sha256}` |
| `treatment_manifest_sha256` | string | yes | SHA-256 of canonical JSON of `{treatment_id, layers_included, item_ids, layer_manifest_sha256}` |
| `isolation_scope` | object | yes | `{khoj_user, experiment_name, payload_root}` |
| `part1_control` | bool | yes | `true` only for `part1-control` |
| `query_set` | object | yes | `{part1_five: "frozen", part2_suite: "node10_or_appropriate_subset"}` |
| `supersession_policy` | enum | yes | `retain_and_stamp` |
| `duplicate_policy` | enum | yes | `one_indexed_copy_plus_witness` |
| `mutation_policy` | enum | yes | `compose_by_reference` |
| `result_disposition` | enum | yes | `preserve_even_if_regressed` |

Canonical JSON for all hashes: UTF-8, `json.dumps(..., sort_keys=True, separators=(",", ":"))`, then SHA-256. This is the live Part 1 convention in `03-ingestion/transform_for_khoj.py`.

### RAT-layer-manifest — ORIG-§11.2 [lines 770–780]
**Normative residue:** none. Dual inclusion vocabulary retired as mandate.

| Field | Type | Required | Rule |
|---|---|---|---|
| `LayerItem.inclusion` | enum | yes | `index` · `witness_not_indexed` · `inventory_only` · `excluded` |
| `LayerItem.temporal_quality` | enum | yes | `dated` · `derived` · `ambiguous` (maps to `temporal_confidence`) |
| `LayerManifest.schema_version` | string | yes | `part2-layer-1.0` |
| `LayerManifest.mutation_policy` | string | yes | `write_once_after_node_08` |
| `LayerManifest.file_manifest` | object | yes | `{relative_path: sha256}` |
| `LayerManifest.item_count` | int | yes | rows with `inclusion` ∈ {`index`, `witness_not_indexed`, `inventory_only`} |
| `LayerManifest.indexed_count` | int | yes | rows with `inclusion=index` |

Do not fail Node 09 solely because an item lacks `LayerItem.inclusion`. Use `inclusion_status`.

### RAT-ordering — ORIG-§11.3 [lines 782–796]
**Normative residue:** two assemblies → identical `item_ids` / hash; no mtime/readdir.

1. Layer order inside a treatment is the frozen `layers_included` array. Do not sort layers alphabetically at assembly time.
2. Item order inside a layer:
   - `anchor`: single item; dated addenda sort by `occurred_at`, then `stable_key`.
   - `decisions` / `part1-control`: `stable_key` / filename ascending (matches `02-corpus/build_corpus.py`).
   - `handoffs`: integer prefix ascending, then remaining stem (`002` before `009` before `030`).
   - `git`: `occurred_at` ascending, then full SHA.
   - `graphify`: `stable_key` lexicographic.
   - `cli-derived`: `occurred_at` ascending, then `stable_key`.
3. File manifests: keys sorted.
4. Treatment `item_ids`: walk `layers_included`; append that layer’s indexed items. No interleaving.

### RAT-duplicates — ORIG-§11.4 [lines 798–810]
**Normative residue:** one indexed copy + witness; no silent merge; parity STOP on mismatch.

| Case | Detection fields | Required action |
|---|---|---|
| Same `item_id`, same `content_sha256` | identity collision with identical bytes | FAIL the layer build |
| Same `item_id`, different `content_sha256` | identity collision or unrecorded supersession | STOP. Do not pick a winner. Route to inventory node 04/05/06/07 |
| Different `item_id`, same `content_sha256`, same layer | byte-identical copies | Keep one indexed. Others set `identity_axis=duplicate` and `canonical_item_id`. Original also set `supersession.kind=canonicalizes_duplicate` and `inclusion=witness_not_indexed` — those two are NON-NORM as mandated fields |
| Different layer, same or similar prose | expected cross-source overlap | Keep both. Different `layer_id` means different source class |
| Repo-local vs Corpus v1.0 parity pair | SHA-256 `4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558` | One indexed record; Corpus v1.0 row sets `control_role=parity_witness`, `identity_axis=duplicate`, and `canonical_item_id` to the indexed record. Future hash mismatch is a STOP |

`scripts/source_manifest.py` must not be used as a deduper.

### RAT-part1-control — ORIG-§11.5 [lines 812–829]
**Normative residue:** byte pins, five q hashes, no other layers, sidecar only.

`part1-control` is not “decisions-only with extra files removed.” It is the historical control.

| Rule | Mechanical check |
|---|---|
| Payload is the 18-file set | filenames exact; no extras |
| Bytes equal Stage D and Stage E | `diff -qr 02-corpus/output/corpus 03-ingestion/output/khoj-corpus` exits 0; manifest `c1fa76ad157d197e28d16f8e9306680e3c870329808e9c1c115dc7587d2f1a3c` |
| JSONL input remains `09c15aebd3a424e7f09ce2c27985fa0cbc24a23d9c474182ea4c912b926750a8` | hash gate before any replay |
| First query set is the exact five Part 1 files | each `qN.txt` hash in §4 |
| Isolated Khoj identity | dedicated user, not a mixed write into the preserved Part 1 archive user |
| No composable layers | `layers_included` contains none of `anchor` / `handoffs` / `git` / `graphify` / `cli-derived` |
| Normalized `decisions/` is a different treatment | `decisions-only` may use it; `part1-control` may not |
| Provenance sidecar only | envelope fields live in `part2/layers/decisions/` sidecar / normalized tree, never inside `decisions-canonical.jsonl` |

Question this control answers: **Did behavior change before the corpus changed?**

Part 1 already preserved poor results (chat HTTP 500; Q3 has no represented supersession; Q4 missed D18/D17). Isolation includes preserving those result files under `04-evaluation/results/`. They are the baseline, not defects to erase. “Technically appropriate Part 2 questions” is a Node 10/11 selection by `question_class`, not a Node 01 rule.

### RAT-mutation-table — ORIG-§11.6 [lines 831–861]
**Normative residue:** compose-by-reference; preserve scores+raw; failure classes for N17.

| Action | Allowed? |
|---|---|
| Copy or mount layer files into a treatment staging dir after hash check | yes |
| Add a treatment-level manifest beside the copy | yes |
| Rewrite frontmatter, bodies, filenames, or links inside a source layer | no |
| Normalize in place over `01-decisions/output/decisions-canonical.jsonl` or `02-corpus/output/corpus/` | no |
| Drop superseded / duplicate / inconvenient items to improve a score | no |
| Change Khoj user contents from a previous treatment without a clean-target precheck | no |
| Use Node 17 CLI extracts to backfill treatments 12–16 after the fact | no |
| Derive a retrieval-friendly Graphify text view with `derived_from` + both hashes | yes |

Materializer rule: **compose by reference**. Clean-target rule: before any treatment ingest, authenticated file list must be empty (or a verified hash-identical restore of that treatment only).

Required preservation per treatment, even when worse than `part1-control` or `decisions-only`: retrieval evidence; generated answer or explicit generation failure; grounding / provenance citations; abstention / negative-control behavior.

| Observation | Disposition |
|---|---|
| Treatment executed correctly and scored worse | PASS the node; record a regression finding |
| Source pollution (handoffs or Git drowning decisions) | Part 2 finding; keep `full-durable` intact |
| Knowledge present but retrieval missed it | Node 17 class `retrieval-missed`; no CLI layer |
| Retrieved but synthesis failed | Node 17 class `synthesis-failed`; no CLI layer |
| Knowledge genuinely absent from durable layers | only this class earns `cli-derived` |
| Chat/search infrastructure failure (as in Part 1 HTTP 500) | preserve raw status codes; do not retry-away the evidence |
| Operator edits the corpus mid-matrix | FAIL the experiment |

### RAT-TC-register — ORIG-§11.7 [lines 863–890]
**Normative residue:** TC-01, TC-11–17, TC-20 as revised TC-1…TC-4 / R-1 / R-2 / X-1.

| ID | Check | PASS | FAIL |
|---|---|---|---|
| TC-01 | Layer directories exist as independent trees | `anchor/` `decisions/` `handoffs/` `git/` `graphify/` present and separately hashable | mixed dump or in-place overwrite of Part 1 snapshot |
| TC-02 | Every indexed item has `item_id`, `content_sha256`, provenance fields, `occurred_at`/`recorded_at`/`temporal_confidence` | required fields present | missing identity or provenance |
| TC-03 | `item_id` unique per layer | 0 collisions | any duplicate `item_id` |
| TC-04 | Item order matches §11.3 | rebuild emits identical `item_ids` | mtime or readdir order |
| TC-05 | Byte-identical same-layer copies | one indexed + witness rows | two indexed copies or silent drop |
| TC-06 | Identity collision with different hash | build stopped | winner picked |
| TC-07 | Supersession reciprocity | A.`replaces` contains B ⇒ B.`replaced_by`=A and B.`supersession_status=superseded` | dangling or one-sided links |
| TC-08 | Superseded retained | superseded rows still in treatment manifest | dropped to improve retrieval |
| TC-09 | Hashes use Part 1 canonical JSON | digest algorithm matches `transform_for_khoj.py` | ad-hoc hashing |
| TC-10 | Layer rebuild byte-identical | `diff -qr` 0 and manifest dicts equal | nondeterministic render |
| TC-11 | `part1-control` payload hash | JSONL `09c15ae…` and corpus manifest `c1fa76ad…` | any byte change |
| TC-12 | `part1-control` questions | five `qN.txt` hashes match §4 | reworded or replaced prompts |
| TC-13 | `part1-control` isolation | dedicated/clean user; no other layers | shared index with 12–16 or extra files |
| TC-14 | Treatment inclusion set | `layers_included` exact match to this section | extra or missing layer |
| TC-15 | `no-decisions` omits decisions | 0 `decisions:*` and 0 Part 1 decision files | decisions leaked |
| TC-16 | `cli-derived` absent before Node 17 | treatments `part1-control`…`full-durable` have 0 `cli-derived:*` | premature gap-fill |
| TC-17 | No silent mutation | source layer hashes unchanged after assembly | rewritten bodies/frontmatter |
| TC-18 | Clean-target ingest | pre-write file list empty or hash-identical restore | mixed treatment residue |
| TC-19 | Graph/runtime isolation | no graph-truth or job-state reads/writes | composition touched runtime truth |
| TC-20 | Poor results preserved | scores and raw responses stored for every treatment | discarded or rerun-to-improve without new `treatment_id` |
| TC-21 | D11 stays out | rejected candidate not indexed | D11 minted into a layer |
| TC-22 | Schema examples stay out of control | MCP supersession pair not in `part1-control` | example objects mixed into Part 1 payload |

---

## L. Supersession edge-case handbook

### RAT-supersession-map — ORIG-§12 [lines 892–901]
Part 2 item envelope stores `replaces` / `replaced_by` (Part 1 names; Node 04 looks these up). Mapping to the provenance-temporal aliases is mechanical:

```
item.replaces      ≡  item.supersedes      ≡  decision.replaces
item.replaced_by   ≡  item.superseded_by   ≡  decision.replaced_by
```

Do not encode replacement as `related_decisions[].rel = supersedes`.

### RAT-supersession-fields — ORIG-§12.1 [lines 903–921]
**Normative residue:** `replaces` required; reciprocity via Node 09 inverse.

| Field | Type | Required | Allowed values |
|---|---|---|---|
| `supersession_status` | enum | yes (original) / derived (revised) | `current` · `superseded` · `rejected` · `not_applicable` |
| `replaces` | string[] | yes | `item_id`s this item replaces. Empty array = replaces nothing. |
| `replaced_by` | string or `null` | yes (original) / inferred (revised) | Single successor `item_id`, or `null`. |
| `supersession.kind` | enum | NON-NORM | `none` · `replaces_decision` · `moves_artifact` · `canonicalizes_duplicate` · `updates_anchor` · `rewrites_policy` |
| `supersession.confidence` | enum | NON-NORM | `asserted` · `inferred` |
| `supersession.as_of` | string or `null` | no | `occurred_at` of the successor when known |
| `supersession.note` | string or `null` | no | One-line human rationale. Not a date field. |

Status mapping from Part 1 `status`:

- Decision `status=superseded` ⇒ `supersession_status=superseded`.
- Decision `status=rejected` (D11-class) ⇒ `supersession_status=rejected`; not a replacement.
- Decision `status=accepted|provisional` with empty `replaces` ⇒ `supersession_status=current` and `supersession.kind=none`.
- Graphify structural snapshots default to `not_applicable` unless one snapshot is declared to replace another.
- Recency, higher retrieval score, or later `recorded_at` never implies `superseded`.

### RAT-P-S-register — ORIG-§12.2 [lines 923–959]
**Normative residue:** reciprocity, retain superseded bytes, no recency-as-supersession, no minting for Q3, 0 edges is evidence.

Original invariants 1–13:

1. If A.`replaces` contains B, then B.`replaced_by` == A.`item_id` and B.`supersession_status` == `superseded`.
2. If B.`replaced_by` == A.`item_id`, then A.`replaces` contains B.
3. `replaced_by` is singular. Two claimed successors is a FAIL (`supersession_fork`). Record both IDs in a validation error; do not last-writer-wins.
4. One successor may supersede many predecessors.
5. Cycles are a FAIL.
6. Dangling IDs (target not in the same layer manifest, and not a known external `item_id` listed as `missing`) are a FAIL.
7. `supersession_status=superseded` with `replaced_by=null` is a FAIL.
8. `supersession_status=current` with `replaced_by!=null` is a FAIL.
9. `supersession.confidence=inferred` is allowed on inventory (Node 05 moved/duplicate handoffs) but Node 09 must surface inferred edges separately from asserted decision replacements. Inferred edges cannot be the sole support for a scored supersession answer.
10. Byte-identical copies set `identity_axis=duplicate` and `canonical_item_id`. Ordinary copies also use `supersession.kind=canonicalizes_duplicate`; parity witnesses instead set `control_role=parity_witness`. Neither is a temporal successor.
11. A moved handoff uses `supersession.kind=moves_artifact`. The kept locator is `current`; the old locator is `superseded`. Content may be identical.
12. Superseded items **remain in the layer**. Treatments may include them. Deletion is not supersession. Treatments that ask “current” filter `supersession_status=current`.
13. `not_applicable` forbids non-empty `replaces` and non-null `replaced_by`.

**Live measured fact:** the closed 17 have **zero** `replaces`/`replaced_by`. Q3 has no represented replacement. That absence is evidence, not a contract defect. Do not mint supersession to make Q3 look answerable. If Node 04’s semantic inventory records supersession that the byte-identical payload does not, that knowledge lives only in the normalized `decisions/` layer.

Handoff `supersession_status=superseded` when a later handoff explicitly resumes/replaces it, or when `identity_axis=moved` and a successor path is recorded. Composition consumes that stamp; it does not infer it from filenames.

| ID | Fields | PASS | FAIL |
|---|---|---|---|
| `P-S-1` | `replaces`, `replaced_by` | every edge has reverse | one-sided edge |
| `P-S-2` | `supersession_status`, `replaced_by` | superseded ⇒ successor set | dangling superseded |
| `P-S-3` | `supersession_status`, `replaced_by` | current ⇒ successor null | current+successor |
| `P-S-4` | `replaced_by` / `replaces` | targets exist or listed missing | dangling ID |
| `P-S-5` | edge graph | acyclic | cycle |
| `P-S-6` | `replaced_by` | singular | fork / array smuggled as string |
| `P-S-7` | decision mapping | envelope fields == Part 1 `replaces`/`replaced_by` | renamed or dropped edges |
| `P-S-8` | control payload | still zero supersession edges | invented replacements inside the control |
| `P-S-9` | `not_applicable` | empty edges | Graphify snapshot with casual replaces |
| `P-S-10` | `supersession.confidence` | inferred-only cannot support a scored supersession answer | inferred-only “A replaced B” |
| `P-S-11` | `identity_axis`, `supersession.kind` | moved/duplicate use `moves_artifact` or `canonicalizes_duplicate` | treated as `replaces_decision` |
| `P-S-12` | layer membership | superseded bytes retained | deleted “because old” |
| SU-01 | `supersession_status`, `replaces`, `replaced_by` | reciprocal links; current-filter possible | dropping superseded items so history questions become unanswerable |

### RAT-R2 — ORIG-§13 [lines 961–973]
Dated 2026-08-16. Resolves the living-anchor conflict.

`project-docs/REBUILD-CONTEXT-ANCHOR.md` (2026-06-21 body) says agents use git tools directly and must not ingest commit history into the corpus engine, and that Graphify is a current code-structure map, not git history as a graph.

Part 2 Node 06 / Node 07 require a Git layer and a Graphify layer under `part2/layers/`.

**Contract stance:** those layers are a **dated experimental exception** for Part 2 treatments only. They live under `part2/layers/git/` and `part2/layers/graphify/`. They are not a rebuild of the MyAPI corpus engine and they do not amend the living anchor’s product direction. `authority_rank=1` `anchor` still wins on `identity_orientation`. `git` wins on `what_changed`. `graphify` wins on `what_exists_now` inside the pinned snapshot.

Node 03 must not rewrite the 2026-06-21 body to hide this tension. If Node 03 adds dated current-direction context, it is additive and separately hashed.

### RAT-item-format — ORIG-§14 [lines 975–990]
Node 08 emits items. Node 01 only defines them.

| Surface | Rule |
|---|---|
| File type | Markdown with YAML frontmatter of the envelope; body = retrieval text |
| File stem | sanitized `item_id` (replace `/` with `__` if needed); record `derived_path` if renamed |
| Hashes | SHA-256 of the emitted file bytes (`hash_scope=item_bytes`), excluding `extracted_at` / `build_id` from the hashed canonical form |
| Per-layer `manifest.json` | `{schema_version, layer_id, item_count, indexed_count, items:[{item_id, sha256, source_class, inclusion_status, origin_path}], file_manifest, layer_manifest_sha256}` |
| Build script | each layer has its own script under that layer directory; a script must not read another layer’s output |
| Dual Graphify files | `deterministic_struct` keeps `graph.json` (copy or pin + `graph_sha256`); `retrieval_text` is a separate item sharing `source_id` |

Node 01 must not emit `manifest.json` or any non-markdown file.

### RAT-measured — ORIG-§15 [lines 992–1002]

| Class | How later nodes must label it |
|---|---|
| Measured | live hash, live file count, live graph parse, git show dates, review-sheet `Y`/`N` |
| Inferred | `supersession.confidence=inferred`; any `occurred_at` reconstructed from a non-event clock; “29 known” until Node 05 resolves a row |
| Forbidden as measurement | embedding similarity as authority; score improvement as inclusion; recency as supersession |

Node 18 maps question class → per-source contribution and must tag each cell `measured` or `inferred`. This contract does not execute that map. Claims that “the 1179-line contract caused Node 06 to emit an empty tree” are **inferred**. Measured: `5d714e9` tree equals `431b98a`.

---

## M. Continuation proposals & “must not” list

### RAT-continuations — moved from ORIG-§16 [lines 1004–1022]
**Normative residue:** none.  
**Bin:** useful-explanation  
These are not this node’s work. Do not execute them from Node 01 / 01b.

1. **Node 02** — prove one-shot chat + scorer; record whether Khoj consumes `occurred_at` / `recorded_at` / provenance fields as metadata or as document text. Do not redesign the corpus around that observation.
2. **Node 03** — assess `project-docs/REBUILD-CONTEXT-ANCHOR.md` against this contract; no rival brief; additive dated current-direction only if Part 2 questions require it; record the Git-ingest tension rather than rewriting the 2026-06-21 body.
3. **Node 04** — write `payload-sha256.txt` for pin `part1_canonical_jsonl`; inventory all 17 IDs plus D11 rejection evidence under `part2/` only; map `decided_on` → `occurred_at`; leave control `replaces`/`replaced_by` empty.
4. **Node 05** — execute `CENSUS-HANDOFF`; resolve the memo’s 29 against the live 26 + missing numbers + VM/rebuild copies; classify every row on the five axes; never silently drop.
5. **Node 06** — emit the named repos, IN-06 depth, `change_evidence` columns, and `build_git_export.(py|sh)` under `part2/layers/git/`. Replay against the revised ≤300-line contract. Preserve empty `5d714e9` as a poor/incomplete result; do not rewrite it.
6. **Node 07** — pin live `graph.json`; record `d82a5eae…` vs live HEAD; keep `retrieval_text` and `deterministic_struct`; state the filter; do not rebuild graph truth. Sibling empty result `96726e1` is the same data point as `5d714e9`.
7. **Node 08** — materialize five durable directories using the 12-field envelope; write layer manifests first; no `cli-derived`.
8. **Node 09** — run the revised mechanical checks; emit the six treatment manifests; do not emit `cli-gap-fill`.
9. **Node 10** — freeze the 15–25 question suite, holdout, judge, rubric, and absolute dates. Until then only the five Part 1 questions are frozen. AO-04 may be consulted here as answer policy, not as a Node 09 FAIL.
10. **Node 11** — replay control against the isolated payload; compare to `04-evaluation/results/*` without altering them. Quality is not a gate. Part 1 chat HTTP 500 is preserved evidence.
11. **Nodes 12–16** — assemble from the matrix only; share the Node 10 ruler; preserve regressions.
12. **Node 17** — admit `cli-derived` only for `genuinely-absent`; rerun targeted questions plus untouched holdout once.
13. **Node 18** — map question class → per-source contribution; distinguish measured vs inferred; no Part 3 router.

Beyond-scope discoveries (not executed here):

14. **Harness / receipt bug (GDDP runtime).** A zero-diff result commit with `exit.cancelled=false` / rc 0 is a false complete. Investigate why node-06 and node-07 were receipted that way while 02–05 were not.
15. **Do not recover the deleted node-06 worktree** `/var/folders/5p/ll5gds4n5k3_x7kbrfp25pkw0000gn/T/gddp-agent-wt-lw1i1u8h` as evidence. Path is gone.
16. **Node spawn ENOENT** (`/opt/homebrew/Cellar/node/26.4.0/bin/node`) is a machine/runtime defect observed during node-06. Not a contract-content finding.

Original ORIG-§17 list (compressed into revised §13): invent `occurred_at`; drop fields because Khoj ignores metadata; mutate graph truth / runtime DBs / job state; widen `source_class` beyond six values; construct corpus content in this node; build Part 3 routing intelligence.

---

## N. Risks carried forward

### RAT-risks — moved from ORIG-§19 [lines 1168–1179]

| ID | Severity | Finding | Contract stance |
|---|---|---|---|
| R1 | high | Memo says 29 known handoffs; this tree has 26 files and missing numbers in `000`–`036` | Do not redefine 29 as 26. Node 05 executes `CENSUS-HANDOFF`. |
| R2 | high | Rebuild anchor says do not ingest commit history; Part 2 requires a Git layer | §13 dated experimental exception. Anchor still wins on product direction. |
| R3 | medium | Graphify snapshot is stale vs HEAD and vault-heavy | Pin and measure pollution; do not silently rebuild. |
| R4 | medium | Closed decision set has no supersession links; Part 1 Q3 is structurally unanswerable from decisions | Do not invent replacements. |
| R5 | medium | Part 1 chat path returned HTTP 500; search worked | Preserve; fixing chat is Node 02, not a reason to alter sources. |
| R6 | low | v1 `source_type` overlaps names | Keep Part 2 `source_class` distinct. |
| R7 | low | Corpus v1.0 keeper is a byte-identical parity witness | Cite, do not double-ingest. |
| R8 | low | `cli-derived` can pollute `full-durable` if mixed early | Hard-exclude from treatments 12–16. |

01b-added risks (not original §19): R-empty-receipt (runtime may accept another empty tree); R-inference (do not claim 1179 lines caused Node 06 to fail); R-field-count (packet said 39; live §7.1 is 36 required / 38 rows); R-replaced_by-inference (Node 09 must still fail one-sided `replaces`); R-project-default (`MyAPI` default can hide a GDDP/Pi item unless 05/06 stamp a non-default).

---

## O. Full original field index (ORIG-§18)

Alphabetical backtick list of every metadata field the original contract named. Downstream authors may grep this section. It is **not** a required-per-item envelope.

`anchor_path`  
`affected_paths`  
`author_date`  
`authority_rank`  
`built_at_commit`  
`canonical_item_id`  
`change_evidence`  
`change_evidence.diff`  
`change_evidence.max_bytes`  
`change_evidence.stat`  
`change_evidence.truncated`  
`claim_type`  
`commit_sha`  
`committer_date`  
`content_identity.alg`  
`content_identity.availability`  
`content_identity.byte_length`  
`content_identity.content_sha256`  
`content_identity.encoding`  
`content_identity.hash_scope`  
`content_identity.newline`  
`content_identity.pin_name`  
`content_identity.source_content_sha256`  
`confidence`  
`content_sha256`  
`control_role`  
`decided_by`  
`decided_on`  
`derived_path`  
`duplicate_policy`  
`evidence_paths`  
`exclusion_reason`  
`extension`  
`extraction_trace.build_id`  
`extraction_trace.extracted_at`  
`extraction_trace.extractor_id`  
`extraction_trace.extractor_version`  
`extraction_trace.inputs`  
`extraction_trace.method`  
`extraction_trace.notes`  
`extraction_trace.source_manifest_sha256`  
`failure_class`  
`file_manifest`  
`git_refs`  
`graph_sha256`  
`handoff_number`  
`id`  
`identity_axis`  
`inclusion`  
`inclusion_status`  
`indexed_count`  
`isolation_scope`  
`item_count`  
`item_id`  
`item_ids`  
`layer_id`  
`layer_item_sha256`  
`layer_manifest_sha256`  
`layers_excluded`  
`layers_included`  
`mutation_policy`  
`node_id`  
`notes`  
`occurred_at`  
`occurred_at_ambiguity`  
`occurred_at_basis`  
`occurred_at_precision`  
`origin.exists_at_record`  
`origin.git_rev`  
`origin.host`  
`origin.ref`  
`origin.repo`  
`origin.scheme`  
`origin.span`  
`origin_backing`  
`origin_path`  
`origin_sha256`  
`parent_shas`  
`part1_control`  
`part1_id`  
`part1_payload_sha256`  
`pin_name`  
`presence`  
`project`  
`provenance_kind`  
`query_set`  
`rationale`  
`recorded_at`  
`recorded_at_ambiguity`  
`recorded_at_basis`  
`recorded_at_precision`  
`related_decisions`  
`replaced_by`  
`replaces`  
`representation`  
`result_disposition`  
`review_mark`  
`schema_version`  
`session_ref`  
`source_class`  
`source_family`  
`source_id`  
`source_role`  
`sources`  
`stable_key`  
`statement`  
`status`  
`subject`  
`summary`  
`superseded_by`  
`supersedes`  
`supersession.as_of`  
`supersession.confidence`  
`supersession.kind`  
`supersession.note`  
`supersession_policy`  
`supersession_status`  
`tags`  
`temporal_candidates`  
`temporal_confidence`  
`temporal_quality`  
`timezone_basis`  
`title`  
`treatment_eligibility`  
`treatment_id`  
`treatment_manifest_sha256`

Required / optional / retired overlay: the 12 revised required fields stay required. Conditional extras in revised §7 stay class-conditional. Everything else in this index is optional or retired-as-mandate.

---

## G. Explicitly non-normative catalog

Do not fail Node 09 solely on these:

1. Universal nested provenance objects (ORIG-§7.2).
2. Full temporal micro-enums always required (ORIG-§8.1).
3. CENSUS-HANDOFF multi-checkout/VM probe choreography as contract law (steps 2–4). Outcome (every claimed identity has a row) remains normative.
4. Optional satellite repo menu (`gddp-runtime`, `gddp-config`, `pi-agent` last-30).
5. Exact `change_evidence.max_bytes=65536` constant. Contract needs stat required; diff bounded+truncation flagged.
6. Graphify live file_type histograms / node-key inventories.
7. TreatmentManifest full 14-field schema + separator dogma beyond id/layers/item_ids/hashes/result_disposition.
8. `LayerItem.inclusion` / `temporal_quality` parallel enums.
9. Per-class sort algorithms beyond “deterministic, documented, rebuild-identical.”
10. `supersession.kind` / `confidence` / `as_of` / `note`.
11. Inferred-supersession scoring ban detail (P-S-10) as a separate ID.
12. Alias tables for treatments and source_class singular forms (stored values still normative).
13. Continuation proposals ORIG-§16.
14. Alphabetical field index ORIG-§18.
15. Claim-type override extended examples / AO-04 as Node 09 FAIL.
16. Exact PASS/FAIL prose for every EX row (codes+why remain normative).
17. Forbidding specific string sentinels list as its own schema (compressed to “null not sentinel strings”).
18. Khoj user isolation operational runbook details inside TC-13/18.
19. Pin table rows for secondary witnesses until the node that consumes them.
20. Any future-proofing for Part 3 routing (EX-part3-routing remains an exclusion, not positive machinery).

---

## P. Open questions (not decided here)

1. AO-04: needed for Node 09 conflict validation, or only for Node 10/18 answer scoring? This revision cut it from 02–09 normative on the “treatments measure contribution, they do not route” reading.
2. How much envelope Node 08 must stamp for Git/Graphify items: the 12-field core plus class extras in revised §7. Not the 36-field set.
3. Stale original HEAD pin `ffece0a9` vs live `431b98a`: file pins match; narrative HEAD restamped.
4. Empty node-06 tree cause is unknown. Task forbids treating it as anything but consumability evidence.
5. “29 known handoffs” remains a Node 05 search target (R1). Not a contract defect.

---

## Self-describing paths for the next node

```
part2/
├── contract/
│   ├── evidence-contract.md       # NORMATIVE, ≤300 lines, 12 envelope fields
│   ├── contract-review.md         # classification of 431b98a
│   └── contract-rationale.md      # this file; non-normative
└── layers/                        # do not create content in 01b
```

| Convention | Value |
|---|---|
| Normative file | `part2/contract/evidence-contract.md` only |
| Non-normative | `part2/contract/contract-rationale.md` |
| Review evidence | `part2/contract/contract-review.md` |
| Baseline pin | commit `431b98a`; file hash `eb9f225a45587a30861d4b79707d29776f456fdd6f41fec87b5ffd2d3c05034f` |
| Next writer | Node 02 writes only under `part2/probe/` |
| Git layer, when 01b passes | `part2/layers/git/` + `build_git_export.(py\|sh)` |
| Do not treat as success | a result commit whose tree equals `431b98a` |
