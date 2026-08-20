# Part 2 contract review (node-01b)

**Baseline classified:** `431b98a:part2/contract/evidence-contract.md` (1179 lines / 76548 bytes / SHA-256 `eb9f225a45587a30861d4b79707d29776f456fdd6f41fec87b5ffd2d3c05034f`).  
**Revised normative file:** `part2/contract/evidence-contract.md` (schema `part2-evidence-contract-1.0`, envelope `2.0-part2-prov-min`).  
**Moved non-normative home:** `part2/contract/contract-rationale.md`.  
**Lens:** necessary-contract | useful-explanation | speculative-machinery.  
**Rule:** GDDP checks execution correctness, never whether a treatment won. Poor/regressive treatments that were executed correctly remain findings.

Nodes 02–09 validate only against the revised contract. This review is classification evidence, not a second schema.

## Consumability data point (not proof)

Commit `5d714e97371224e9d25d48ae28c02c2fa34c4655` (node-06 result) has an identical tree to `431b98a` (`git diff 431b98a 5d714e9` empty; both trees `17e7ae16…`). No `part2/layers/git/`, no `build_git_export.(py|sh)`. Job receipt records `expected_base_commit_sha=431b98a…`, `result_commit_sha=5d714e9…`, `returncode=0`, `cancelled=false`.

This is evidence that a downstream 02–09 consumer can finish “successfully” without emitting the artifacts the 1179-line contract names. It is **not** proof that Git is a bad source, that the original reasoning was wrong, or that workers bounced off the 36-field envelope. Process evidence also shows incomplete workers and a later graph amendment. Characterize `5d714e9` only as a consumability data point.

## Classification table

Every baseline `##` / `###` heading is classified. `Class` is exactly one of `necessary-contract` | `useful-explanation` | `speculative-machinery`. Mixed keep/move nuance lives in Rec, not in Class. “Kept” means the executable residue remains in the revised contract. Detail lives in `contract-rationale.md` under the named `RAT-*` anchor.

| Sec | Heading / range | Class | Rec | Downstream 02–09 decision made more correct (kept only) |
|---|---|---|---|---|
| 0 | `# Part 2 evidence contract` L1–11 | useful-explanation | **compress** header identity (`schema id`, envelope) into a pin block; restamp worktree HEAD to live `431b98a` | **02–09:** which file is law (`evidence-contract.md` only). |
| 1 | `## 1. Research question` L13–28 | necessary-contract | **keep** both memo and packet strings | **10/18:** score the right question. **02–09:** contribution is a later measured result, not an inclusion predicate. Nodes do not drop a source because they expect it to lose. |
| 2 | `## 2. Experimental gate` L29–42 | necessary-contract | **keep** | **08/09:** `result_disposition=preserve_even_if_regressed`; do not add/drop items to raise scores (`EX-score-tuning`). **02:** a broken chat path is preserved evidence, not a reason to reshape sources. |
| 3 | `## 3. Self-describing layout` L43–82 | necessary-contract | **keep** the `part2/` tree + writer-node table | **02** writes `part2/probe/` only. **03–07** write under their layer dirs, not a mixed dump. **08** materializes five durable dirs. **09** emits six manifests under `part2/validation/treatment-manifests/` and must not emit `cli-gap-fill`. |
| 4 | `## 4. Locked measured pins` L83–135 | necessary-contract | **keep** file/question pins, closed-set, handoff census, graph snapshot size; **move** node/link/file-type key dumps (useful-explanation) to rationale | **04/08/09:** fail if `decisions-canonical.jsonl` ≠ `09c15ae…`; do not replace the Part 1 payload. **03:** sole primary anchor hash `92d21284…`. **05:** 26 present files + missing numbers `001,003–008,016–019`; do not redefine 29 as 26. **07:** pin live `graph.json` (67111631 B). **02/11:** five `qN.txt` hashes stay frozen. |
| 5 | `## 5. Source classes` L136–160 | necessary-contract | **keep** closed enum + alias reject | **08:** no seventh durable class. **09:** unknown `source_class` count = 0. |
| 5.1 | `### SC-01 anchor` L161–179 | necessary-contract | **keep** no-rival + pin | **03:** one anchor, no rival brief; Architecture is memo support. |
| 5.2 | `### SC-02 decisions` L181–198 | necessary-contract | **keep** closed set + payload pin | **04:** 17 objects, D11 out, payload SHA pinned. |
| 5.3 | `### SC-03 handoffs` L200–226 | necessary-contract | **keep** five axes + manifest-one-row; **move** `CENSUS-HANDOFF` multi-checkout/VM choreography (useful-explanation) | **05:** `CENSUS-HANDOFF` five axes; templates excluded; missing slots are rows. |
| 5.4 | `### SC-04 git` L228–273 | necessary-contract | **keep** role + IN-06 + stat/diff bound; **cut-from-normative** optional last-30 satellite repos (speculative-machinery) | **06:** Git = what-changed; absolute ISO dates; bounded `change_evidence`. |
| 5.5 | `### SC-05 graphify` L275–294 | necessary-contract | **keep** pin + dual representation | **07:** keep `retrieval_text` ≠ `deterministic_struct`; do not refresh graph truth. |
| 5.6 | `### SC-06 cli-derived` L296–325 | necessary-contract | **keep** gap_only / genuinely-absent / not in 12–16 | **08:** no seventh durable class; no `cli-derived`. **09:** unknown class count = 0; no CLI in 12–16. |
| 6 | `## 6. Source authority` L326–337 | necessary-contract | **keep** rank table + home claim_type | **08:** stamp `authority_rank` 1–6 only. **09:** same-rank conflicts keep both or record a resolver. |
| 6.1 | `### AO-01 Conflict rule` L339–347 | necessary-contract | **keep** | **09:** do not use embedding similarity as authority. |
| 6.2 | `### AO-02 Part 1 decision-internal order` L349–360 | necessary-contract | **keep** | **04/09:** review sheet `Y`/`N` cannot be flipped by a handoff or Graphify. |
| 6.3 | `### AO-03 Control payload vs normalized twin` L362–372 | necessary-contract | **keep** | **04/11:** Node 11 uses byte-identical Part 1 payload; twins cite the control SHA. |
| 6.4 | AO-04 claim-type winner table L374–386 (unheaded) | speculative-machinery | **cut-from-normative**; winner table lives in rationale as Node 10/18 answer policy | — (treatments measure contribution; they do not route) |
| 7 | `## 7. Provenance fields` L388–394 | useful-explanation | **compress** serialization + Khoj-may-ignore note | **02:** record metadata-vs-text; do not drop fields. |
| 7.1 | `### 7.1 Required flat envelope` L396–459 | speculative-machinery | **cut-from-normative** as a universal 36-required / 38-row set; **keep** the 12-field identity + two clocks + inclusion + hashes core | **08/09** validate a small core, not fail a git item for missing `identity_axis` / `canonical_item_id` / `treatment_eligibility`. Empty node-06 tree is the consumability exhibit, not proof. |
| 7.2 | `### 7.2 Nested origin / content / trace` L460–509 | speculative-machinery | **cut-from-normative** as required; **move** useful bits (`origin.repo`, `hash_scope`, `extracted_at ≠ occurred_at`) | **06/08** do not need `OriginSpan` / newline / encoding enums to export a commit. |
| 7.3 | `### 7.3 Conditional extras by source_class` L511–528 | necessary-contract | **keep** as class extras, not envelope-required | **03–07** know which extra fields their class must stamp. **08** copies Part 1 decision fields onto the normalized twin only. |
| 7.4 | `### 7.4 Provenance PASS/FAIL` L530–549 | necessary-contract | **keep** P-ID-1/2/3/5/8, P-HASH-1/2, IN-02; **cut** checks that only police the nested duplicate schema | **09:** collision, class enum, POSIX origin, missing≠present, hash recompute. |
| 8 | `## 8. occurred_at versus recorded_at` L551–558 | necessary-contract | **keep** two-clock definitions | **02/10:** dated questions vs inscription. |
| 8.1 | `### 8.1 Temporal fields` L560–576 | useful-explanation | **keep** `occurred_at` / `recorded_at` / `temporal_confidence`; **move** precision/basis/ambiguity/candidates (speculative-machinery as all-required micro-enums) | **08/09:** keys always present; no relative dates. |
| 8.2 | `### 8.2 Class mapping` L578–588 | necessary-contract | **keep** | **04:** `decided_on` → `occurred_at`; do not clone into `recorded_at`. **06:** author=`occurred_at`, committer=`recorded_at`. **07:** node `occurred_at` null unless the node encodes an event. |
| 8.3 | `### 8.3 Hard rules` L590–619 | necessary-contract | **keep** keys-exist / no-guess / no-relative / git author-committer / null first-class; **move** full P-T-1…12 register (useful-explanation) | **08/09:** no backfill to make “What changed on 2026-08-14?” look answered. |
| 9 | `## 9. Inclusion rules` L621–623 | necessary-contract | **keep** | **08/09:** `inclusion_status` must match the matrix. |
| 9.1 | `### IN-01 Class membership` L625–629 | necessary-contract | **keep** | **09:** unknown `source_class` count = 0. |
| 9.2 | `### IN-02 Provenance complete` L631–635 | necessary-contract | **keep** as 12-field completeness (not the 36-field set) | **09:** no memory-only / index-only items. |
| 9.3 | `### IN-03 Project-history relevance` L637–641 | necessary-contract | **keep** allowed homes; default `MyAPI` | **05/06:** stamp a non-default when the source names another allowed home. |
| 9.4 | `### IN-04 Treatment eligibility declared` L643–647 | useful-explanation | **move**; eligibility is derived from the §10 matrix + class | **09:** still fails CLI in 12–16 / decisions in `no-decisions` via TC-2/TC-3. |
| 9.5 | `### IN-05 Handoff inclusion is manifest-explicit` L649–655 | necessary-contract | **keep** | **05:** include only present git-backed or copied-and-hashed VM artifacts; templates default excluded. |
| 9.6 | `### IN-06 Git inclusion is bounded` L657–669 | necessary-contract | **keep** | **06:** this is the actual Git job, not a 7-repo survey. |
| 9.7 | `### IN-07 Graphify inclusion is snapshot-pinned` L671–677 | necessary-contract | **keep** | **07:** one pinned snapshot. |
| 10 | `## 10. Exclusion rules` L679–705 | necessary-contract | **keep** the 16 `EX-*` codes | **03:** `EX-stale-operational-anchor`. **04:** `EX-unreviewed-decision`, `EX-d11-rejected`, `EX-schema-example`. **05:** `EX-template`, `EX-missing`, `EX-unreachable-vm`. **06/07/08:** `EX-bulk-vault/chat/cli`, `EX-runtime`, `EX-graph-truth-write`. **09:** every considered-and-excluded candidate has a row. |
| 11 | `## 11. Treatment composition` L706–735 | necessary-contract | **keep** the frozen 7-id matrix and “Node 09 emits exactly six” | **08:** five durable layers, independently hashable. **09:** assemble exactly those class sets; `cli-gap-fill` is not a Node 09 manifest. |
| 11.1 | `### 11.1 TreatmentManifest fields` L736–768 | necessary-contract | **keep** id, layers, item_ids, hash recipe, `result_disposition`; **cut-from-normative** extra policy enums / `query_set` / `isolation_scope` (speculative-machinery) | **09:** canonical JSON hash matches Part 1 `transform_for_khoj.py`; poor treatments still get a manifest. |
| 11.2 | `### 11.2 Layer item / manifest fields` L770–780 | speculative-machinery | **cut-from-normative** second inclusion vocabulary | Dual taxonomies would make **08/09** interpret twelve states. |
| 11.3 | `### 11.3 Ordering` L782–796 | necessary-contract | **keep** determinism rule; per-class sort tables in rationale | **08/09:** two independent assemblies emit identical `item_ids` / `treatment_manifest_sha256`. No mtime/readdir order. |
| 11.4 | `### 11.4 Duplicate handling` L798–810 | necessary-contract | **keep** | **04:** wording-note vs Corpus v1.0 keeper is one indexed record + parity witness (`4124f800…`). **05/08:** byte-identical copies → one index + witness. **09:** identity collision with different hash is STOP. |
| 11.5 | `### 11.5 part1-control isolation` L812–829 | necessary-contract | **keep** | **04/08:** do not write envelope fields into `decisions-canonical.jsonl`. **09:** `part1-control` lists none of the Part 2 layers. |
| 11.6 | `### 11.6 No silent mutation / poor results stay` L831–861 | necessary-contract | **keep** | **08:** compose by reference. **09:** source-layer hashes unchanged after assembly; regressions stored. Operationalizes §2 for 02–09. |
| 11.7 | `### 11.7 Treatment PASS/FAIL` L863–891 | useful-explanation | **keep** TC-01, TC-11–17, TC-20 as the executable set; **move** the rest | **09:** one place to run integrity checks without gating on treatment scores. |
| 12 | `## 12. Supersession rules` L892–901 | necessary-contract | **keep** Part 1 field names + mapping | **04/09:** look up `replaces` / `replaced_by`; do not smuggle via `related_decisions`. |
| 12.1 | `### 12.1 Fields` L903–921 | necessary-contract | **keep** `replaces`; **cut-from-normative** `supersession.kind` / confidence / as_of (speculative-machinery) | **04:** leave control `replaces`/`replaced_by` empty. **08/09:** superseded rows stay in the layer. |
| 12.2 | `### 12.2 Invariants` L923–959 | necessary-contract | **keep** reciprocity + retain + no minting + “0 edges is evidence”; **cut** unused kind-machine / 12 P-S checks on a zero-edge set (speculative-machinery) | **05:** moved handoff = locator successor, not a new decision. **09:** deletion ≠ supersession. |
| 13 | `## 13. Git / Graphify experimental exception` L961–974 | necessary-contract | **keep** | **03:** do not rewrite the 2026-06-21 body to hide the tension. **06/07:** layers under `part2/layers/{git,graphify}/` are a dated exception, not a product-direction change. |
| 14 | `## 14. Corpus item format` L975–991 | necessary-contract | **keep** emission rules for Node 08; Node-01-only last sentence is useful-explanation (folded, not a second mandate) | **08:** MD+YAML items, per-layer `manifest.json`, one script per layer, dual Graphify files sharing `source_id`. **07/08:** do not dump 41068 document nodes into retrieval text. |
| 15 | `## 15. Measured versus inferred` L992–1003 | necessary-contract | **keep** compressed label rule | **04–07:** hash/count/parse = measured; “29 known” and inferred supersession stay labeled inferred. **09:** embedding similarity is not a measurement of authority. |
| 16 | `## 16. Continuation proposals` L1004–1023 | useful-explanation | **move** entire (restates the Part 2 memo) | — |
| 17 | `## 17. What later nodes must not do` L1024–1034 | necessary-contract | **keep** short list (folded into revised §13) | **02–09:** hard stop boundary. |
| 18 | `## 18. Field index` L1035–1167 | speculative-machinery | **cut-from-normative** (133-line grep surface, L1035–1167 exclusive of §19; 11% of the file) | — |
| 19 | `## 19. Risks left for later nodes` L1168–1179 | useful-explanation | **move**; keep R1/R2 one-liners in contract | **05:** R1 29≠26 is a census job, not a redefinition. **03/06:** R2 is why §13 exists. **07:** R3 pin the stale graph. **04:** R4 do not invent replacements. **02:** R5 preserve HTTP 500 evidence. |

## Envelope count (measured, not the packet’s “39”)

Live §7.1 at `431b98a` has **38 named field rows**: 34 `yes` + 2 `yes (key required)` = **36 required keys**, plus 1 conditional (`canonical_item_id`) and 1 optional (`claim_type`). Nested §7.2 objects (`origin`, `content_identity`, `extraction_trace`) were additionally mandatory on Node 08+ items. The packet phrase “39 required flat fields” is not reproduced by a live parse. The revised contract publishes a counted 12-field table so later nodes stop inheriting that 39.

## What was kept as the operational core

1. Research question + experimental gate (orig §1–§2).
2. `part2/` layout (orig §3).
3. File/question pins + closed decision set + handoff census numbers + graph snapshot pin (orig §4, minus key dumps).
4. Six `source_class` values and the six SC-0n PASS checks (orig §5).
5. Authority ranks / home claim types / control-vs-twin (orig §6 without AO-04).
6. Twelve-field required envelope + class extras (reduced orig §7.1 + orig §7.3).
7. `occurred_at` vs `recorded_at` mapping and no-guess rules (orig §8.2 + hard rules).
8. IN-01–IN-07 residue and the 16 `EX-*` codes (orig §9–10).
9. Treatment matrix, ordering, duplicate rule, compose-by-reference, six manifests (orig §11 minus dual inclusion vocab and extra policy enums).
10. Supersession field names + retain + do-not-mint (orig §12 core).
11. Dated Git/Graphify exception (orig §13).
12. Node 08 item/manifest emission (orig §14).
13. Measured-vs-inferred label + prohibitions (orig §15, §17).

That is the “page or two of fields, invariants, and treatment rules” the overengineering memo asked for.

## Findings

| Sev | Finding |
|---|---|
| high | Orig §7.1 made ~36 flat fields required on every corpus item, then §7.2 duplicated them as nested objects. This is the exported-complexity failure the lens warned about. Revised contract collapses to 12 required fields. |
| high | Node 06 result `5d714e9` is an empty identical tree. Consumability data point only — not proof the original reasoning is wrong, and not a quality gate on Git. |
| medium | Orig §12 specified a supersession-kind machine for a closed set the contract itself measures as **0** edges. Unexercised machinery moved to rationale. |
| medium | Orig §18 (133 lines, L1035–1167 exclusive of §19) was a normative grep index. Downstream agents should not need 76 KB in context to do corpus work. |
| medium | Dual inclusion languages (`inclusion_status` vs `LayerItem.inclusion` vs `treatment_eligibility[]`) would have made 08/09 interpret twelve states. Second vocabulary retired as mandate. |
| medium | Original declared measured facts “at HEAD `ffece0a9…`” while this tree is `431b98a…`. File pins still match; only the narrative HEAD was stale. Revised contract restamps HEAD. |
| low | Orig §1 made two phrasings independently normative for `rg -F`. Both kept because memo + packet require them. |
| low | Orig §16–17 restated the Part 2 memo. §16 moved; §17 compressed into revised §13. |
| low | SC-04 named optional last-30 inventories of `gddp-runtime` / `gddp-config` / `pi-agent`, widening past IN-06. Optional menu is non-normative. |

## Continuation proposals (beyond this node — do not execute)

1. **Harness / receipt bug (GDDP runtime, not MyAPI Part 2).** A zero-diff result commit with `exit.cancelled=false` / rc 0 is a false complete. Investigate why node-06 and node-07 (`96726e1`, same empty tree) were receipted that way while 02–05 were not. Out of `part2/` write scope.
2. **Re-dispatch Node 06 only after 01b lands.** Replay against this ≤300-line contract. The empty `5d714e9` stays as a preserved poor/incomplete result; do not rewrite it.
3. **Same for Node 07** and Nodes 02–05 (no result commit, exit 143).
4. **Do not recover the deleted node-06 worktree as evidence.** Path is gone.
5. **Node spawn ENOENT** (`/opt/homebrew/Cellar/node/26.4.0/bin/node`) is a machine/runtime defect observed during node-06. Not a contract-content finding.
6. **AO-04 winner table** remains available in rationale if Node 10/18 later needs scored-synthesis routing. Do not re-import it as a Node 09 FAIL without a contract revision.

Next writer: Node 02 writes only under `part2/probe/`. Do not mint `part2/layers/**` from this node. Do not treat a result commit whose tree equals `431b98a` as success.
