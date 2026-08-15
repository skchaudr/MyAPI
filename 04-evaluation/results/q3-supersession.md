# Fixed evaluation Q3 — Supersession

**Node:** `node-11-eval-supersession-relationship`  
**Execution attempt:** `job_20260815T0045189302c8fd4a6af3:attempt:0`  
**Base commit:** `c605d36e63172b70bb960a63107bab1cd1926f83`  
**Queried:** `2026-08-15T00:49:41.377959Z`  
**Result:** **CAPTURED — one predetermined read-only Khoj search response, recorded without retry.**

## Exact query

```text
Which decision replaced an earlier one?
```

## Run record

- Query file: `04-evaluation/queries/q3.txt`
- Query file written: `2026-08-15T00:48:42.982036Z` (before the request began at `2026-08-15T00:49:41.377959Z`)
- Run in VM shell: GCE instance `khoj-38-b`, project `khoj-r2`, zone `us-east1-b`
- Interface: `GET http://localhost:42110/api/search` with `n=5` and `t=all`
- Canonical request URL: `http://localhost:42110/api/search?q=Which+decision+replaced+an+earlier+one%3F&n=5&t=all`
- Authentication: `Authorization: Bearer <token>`; token read only inside the VM process from `/home/sab-mini/.khoj/gddp-part1.token`
- Identity precheck: HTTP `200`; `email: gddp-part1@local`
- Search response: HTTP `200`; `5` results; `17326` raw response bytes
- Query count: one search request; no retry
- Graph truth/runtime databases: unchanged; read-only HTTP endpoints only

## Raw answer (verbatim)

The following is the exact UTF-8 HTTP response body returned by Khoj:

~~~~json
[{"entry":"# D07 — Human is last provisional gate\n\n> Human last provisional gate\n\n## Decision\n\nEvaluator is second-to-last gate; human is last on provisional nodes. Reject returns the node to `ready` for retry.\n\n## Rationale\n\nDefines acceptance authority and retry semantics.\n\n## Record\n\n- **Project:** `GDDP`\n- **Status:** `accepted`\n- **Decided on:** `2026-08-08`\n- **Decided by:** Sab\n\n## Sources\n\n- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D07 | Y | Human last provisional gate\n- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: Evaluator is second-to-last gate; human is last on provisional nodes. Reject returns the node to `ready` for retry.\n- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Evaluator is second-to-last gate; human is last on provisional nodes. Reject returns the node to `ready` for retry.\n","score":0.1429734230041504,"cross-score":null,"additional":{"source":"computer","file":"D07.md","compiled":"# D07.md\n## D07 — Human is last provisional gate\n\n> Human last provisional gate\n\n## Decision\n\nEvaluator is second-to-last gate; human is last on provisional nodes. Reject returns the node to `ready` for retry.\n\n## Rationale\n\nDefines acceptance authority and retry semantics.\n\n## Record\n\n- **Project:** `GDDP`\n- **Status:** `accepted`\n- **Decided on:** `2026-08-08`\n- **Decided by:** Sab\n\n## Sources\n\n- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D07 | Y | Human last provisional gate\n- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: Evaluator is second-to-last gate; human is last on provisional nodes. Reject returns the node to `ready` for retry.\n- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Evaluator is second-to-last gate; human is last on provisional nodes. Reject returns the node to `ready` for retry.","heading":"# D07.md\n## D07 — Human is last provisional gate"},"corpus-id":"2d05ae83-d0a5-4d3f-93e1-ee05e9705791"},{"entry":"# D12 — Prefer flow-on-provisional unless strict canary\n\n> Prefer flow-on-provisional\n\n## Decision\n\nDefault preference is flow-on-provisional (momentum; review can lag execution). Strict canary (`frontier_auto_advance: false`) only when explicitly flipped.\n\n## Rationale\n\nChooses speed-with-review-lag over stop-the-line canary as the normal mode.\n\n## Record\n\n- **Project:** `GDDP`\n- **Status:** `accepted`\n- **Decided on:** `2026-08-08`\n- **Decided by:** Sab\n\n## Sources\n\n- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D12 | Y | Prefer flow-on-provisional\n- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: Default preference is flow-on-provisional (momentum; review can lag execution). Strict canary (`frontier_auto_advance: false`) only when explicitly flipped.\n- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Default preference is flow-on-provisional (momentum; review can lag execution). Strict canary (`frontier_auto_advance: false`) only when explicitly flipped.\n","score":0.15266274495942767,"cross-score":null,"additional":{"source":"computer","file":"D12.md","compiled":"# D12.md\n## D12 — Prefer flow-on-provisional unless strict canary\n\n> Prefer flow-on-provisional\n\n## Decision\n\nDefault preference is flow-on-provisional (momentum; review can lag execution). Strict canary (`frontier_auto_advance: false`) only when explicitly flipped.\n\n## Rationale\n\nChooses speed-with-review-lag over stop-the-line canary as the normal mode.\n\n## Record\n\n- **Project:** `GDDP`\n- **Status:** `accepted`\n- **Decided on:** `2026-08-08`\n- **Decided by:** Sab\n\n## Sources\n\n- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D12 | Y | Prefer flow-on-provisional\n- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: Default preference is flow-on-provisional (momentum; review can lag execution). Strict canary (`frontier_auto_advance: false`) only when explicitly flipped.\n- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Default preference is flow-on-provisional (momentum; review can lag execution). Strict canary (`frontier_auto_advance: false`) only when explicitly flipped.","heading":"# D12.md\n## D12 — Prefer flow-on-provisional unless strict canary"},"corpus-id":"5e926cb6-1fc6-43e5-99b2-ccf7ebb3a686"},{"entry":"---\nid: \"D16\"\nschema_version: \"1.0\"\nproject: \"MyAPI\"\ntitle: \"Decision scan order\"\nsummary: \"Scan last 2w then full history\"\nstatement: \"Scan session transcripts for decisions last-2-weeks first, then widen to full history.\"\nstatus: \"accepted\"\nrationale: \"Newest operator intent first; full archive is phase 2.\"\ndecided_on: \"2026-08-08\"\ndecided_by: \"Sab\"\ntags:\n  - \"ops\"\nsources:\n  -\n    kind: \"review_sheet\"\n    ref: \"project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md\"\n    note: \"inclusion and status authority. Quote: D16 | Y | Scan last 2w then full history\"\n  -\n    kind: \"memo\"\n    ref: \"project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md\"\n    note: \"repo-local decision wording. Quote: Scan session transcripts for decisions last-2-weeks first, then widen to full history.\"\n  -\n    kind: \"other\"\n    ref: \"/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md\"\n    note: \"byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Scan session transcripts for decisions last-2-weeks first, then widen to full history.\"\nevidence_paths:\n  - \"project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md\"\n  - \"project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md\"\nconfidence: \"high\"\nreview_mark: \"Y\"\n---\n\n# D16 — Decision scan order\n\n> Scan last 2w then full history\n\n## Decision\n\nScan session transcripts for decisions last-2-weeks first, then widen to full history.\n\n## Rationale\n\nNewest operator intent first; full archive is phase 2.\n\n## Record\n\n- **Project:** `MyAPI`\n- **Status:** `accepted`\n- **Decided on:** `2026-08-08`\n- **Decided by:** Sab\n\n## Sources\n\n- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D16 | Y | Scan last 2w then full history\n- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: Scan session transcripts for decisions last-2-weeks first, then widen to full history.\n- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Scan session transcripts for decisions last-2-weeks first, then widen to full history.\n","score":0.15426676545937112,"cross-score":null,"additional":{"source":"computer","file":"D16.md","compiled":"# D16.md\n\n- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D16 | Y | Scan last 2w then full history\n- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: Scan session transcripts for decisions last-2-weeks first, then widen to full history.\n- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Scan session transcripts for decisions last-2-weeks first, then widen to full history.","heading":"# D16.md\n"},"corpus-id":"816a69c0-391d-47af-802d-33c5a219e03d"},{"entry":"# D01 — GDDP role vs harness\n\n> GDDP constrains/verifies loop; not harness rebuild\n\n## Decision\n\nGDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop.\n\n## Rationale\n\nKeeps GDDP a control/evidence layer around replaceable executors (Pi, Jules, Claude, etc.).\n\n## Record\n\n- **Project:** `GDDP`\n- **Status:** `accepted`\n- **Decided on:** `2026-08-08`\n- **Decided by:** Sab\n\n## Sources\n\n- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D01 | Y | GDDP constrains/verifies loop; not harness rebuild\n- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: GDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop.\n- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: GDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop.\n","score":0.15487658977508545,"cross-score":null,"additional":{"source":"computer","file":"D01.md","compiled":"# D01.md\n## D01 — GDDP role vs harness\n\n> GDDP constrains/verifies loop; not harness rebuild\n\n## Decision\n\nGDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop.\n\n## Rationale\n\nKeeps GDDP a control/evidence layer around replaceable executors (Pi, Jules, Claude, etc.).\n\n## Record\n\n- **Project:** `GDDP`\n- **Status:** `accepted`\n- **Decided on:** `2026-08-08`\n- **Decided by:** Sab\n\n## Sources\n\n- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D01 | Y | GDDP constrains/verifies loop; not harness rebuild\n- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: GDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop.\n- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: GDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop.","heading":"# D01.md\n## D01 — GDDP role vs harness"},"corpus-id":"515620ef-61ea-4aaf-80d7-78c4bc667779"},{"entry":"---\nid: \"D08\"\nschema_version: \"1.0\"\nproject: \"GDDP\"\ntitle: \"Reject revokes dependent admission\"\nsummary: \"Reject revokes dependent admission\"\nstatement: \"Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.\"\nstatus: \"accepted\"\nrationale: \"Doctrine: rejection must not leave downstream work still admitted.\"\ndecided_on: \"2026-08-08\"\ndecided_by: \"Sab\"\nsources:\n  -\n    kind: \"review_sheet\"\n    ref: \"project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md\"\n    note: \"inclusion and status authority. Quote: D08 | Y | Reject revokes dependent admission\"\n  -\n    kind: \"memo\"\n    ref: \"project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md\"\n    note: \"repo-local decision wording. Quote: Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.\"\n  -\n    kind: \"other\"\n    ref: \"/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md\"\n    note: \"byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.\"\nevidence_paths:\n  - \"project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md\"\n  - \"project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md\"\nconfidence: \"high\"\nreview_mark: \"Y\"\n---\n\n# D08 — Reject revokes dependent admission\n\n> Reject revokes dependent admission\n\n## Decision\n\nRejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.\n\n## Rationale\n\nDoctrine: rejection must not leave downstream work still admitted.\n\n## Record\n\n- **Project:** `GDDP`\n- **Status:** `accepted`\n- **Decided on:** `2026-08-08`\n- **Decided by:** Sab\n\n## Sources\n\n- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D08 | Y | Reject revokes dependent admission\n- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.\n- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.\n","score":0.16033553121474053,"cross-score":null,"additional":{"source":"computer","file":"D08.md","compiled":"# D08.md\n---\nid: \"D08\"\nschema_version: \"1.0\"\nproject: \"GDDP\"\ntitle: \"Reject revokes dependent admission\"\nsummary: \"Reject revokes dependent admission\"\nstatement: \"Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.\"\nstatus: \"accepted\"\nrationale: \"Doctrine: rejection must not leave downstream work still admitted.\"\ndecided_on: \"2026-08-08\"\ndecided_by: \"Sab\"\nsources:\n  -\n    kind: \"review_sheet\"\n    ref: \"project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md\"\n    note: \"inclusion and status authority. Quote: D08 | Y | Reject revokes dependent admission\"\n  -\n    kind: \"memo\"\n    ref: \"project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md\"\n    note: \"repo-local decision wording. Quote: Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.\"\n  -\n    kind: \"other\"\n    ref: \"/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md\"\n    note: \"byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.\"\nevidence_paths:\n  - \"project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md\"\n  - \"project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md\"\nconfidence: \"high\"\nreview_mark: \"Y\"\n---\n\n# D08 — Reject revokes dependent admission\n\n> Reject revokes dependent admission\n\n## Decision\n\nRejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.\n\n## Rationale\n\nDoctrine: rejection must not leave downstream work still admitted.\n\n## Record\n\n- **Project:** `GDDP`\n- **Status:** `accepted`\n- **Decided on:** `2026-08-08`\n- **Decided by:** Sab\n\n## Sources\n\n- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D08 | Y | Reject revokes dependent admission\n- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.\n- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.","heading":"# D08.md\n"},"corpus-id":"465068ba-bf52-469c-94f6-665c622d3aac"}]
~~~~

## Retrieved evidence passages

### Result 1 — `D07.md`

- `score`: `0.1429734230041504`
- `cross-score`: `null`
- `corpus-id`: `2d05ae83-d0a5-4d3f-93e1-ee05e9705791`

Verbatim `entry`:

~~~~text
# D07 — Human is last provisional gate

> Human last provisional gate

## Decision

Evaluator is second-to-last gate; human is last on provisional nodes. Reject returns the node to `ready` for retry.

## Rationale

Defines acceptance authority and retry semantics.

## Record

- **Project:** `GDDP`
- **Status:** `accepted`
- **Decided on:** `2026-08-08`
- **Decided by:** Sab

## Sources

- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D07 | Y | Human last provisional gate
- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: Evaluator is second-to-last gate; human is last on provisional nodes. Reject returns the node to `ready` for retry.
- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Evaluator is second-to-last gate; human is last on provisional nodes. Reject returns the node to `ready` for retry.

~~~~

### Result 2 — `D12.md`

- `score`: `0.15266274495942767`
- `cross-score`: `null`
- `corpus-id`: `5e926cb6-1fc6-43e5-99b2-ccf7ebb3a686`

Verbatim `entry`:

~~~~text
# D12 — Prefer flow-on-provisional unless strict canary

> Prefer flow-on-provisional

## Decision

Default preference is flow-on-provisional (momentum; review can lag execution). Strict canary (`frontier_auto_advance: false`) only when explicitly flipped.

## Rationale

Chooses speed-with-review-lag over stop-the-line canary as the normal mode.

## Record

- **Project:** `GDDP`
- **Status:** `accepted`
- **Decided on:** `2026-08-08`
- **Decided by:** Sab

## Sources

- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D12 | Y | Prefer flow-on-provisional
- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: Default preference is flow-on-provisional (momentum; review can lag execution). Strict canary (`frontier_auto_advance: false`) only when explicitly flipped.
- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Default preference is flow-on-provisional (momentum; review can lag execution). Strict canary (`frontier_auto_advance: false`) only when explicitly flipped.

~~~~

### Result 3 — `D16.md`

- `score`: `0.15426676545937112`
- `cross-score`: `null`
- `corpus-id`: `816a69c0-391d-47af-802d-33c5a219e03d`

Verbatim `entry`:

~~~~text
---
id: "D16"
schema_version: "1.0"
project: "MyAPI"
title: "Decision scan order"
summary: "Scan last 2w then full history"
statement: "Scan session transcripts for decisions last-2-weeks first, then widen to full history."
status: "accepted"
rationale: "Newest operator intent first; full archive is phase 2."
decided_on: "2026-08-08"
decided_by: "Sab"
tags:
  - "ops"
sources:
  -
    kind: "review_sheet"
    ref: "project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md"
    note: "inclusion and status authority. Quote: D16 | Y | Scan last 2w then full history"
  -
    kind: "memo"
    ref: "project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md"
    note: "repo-local decision wording. Quote: Scan session transcripts for decisions last-2-weeks first, then widen to full history."
  -
    kind: "other"
    ref: "/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md"
    note: "byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Scan session transcripts for decisions last-2-weeks first, then widen to full history."
evidence_paths:
  - "project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md"
  - "project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md"
confidence: "high"
review_mark: "Y"
---

# D16 — Decision scan order

> Scan last 2w then full history

## Decision

Scan session transcripts for decisions last-2-weeks first, then widen to full history.

## Rationale

Newest operator intent first; full archive is phase 2.

## Record

- **Project:** `MyAPI`
- **Status:** `accepted`
- **Decided on:** `2026-08-08`
- **Decided by:** Sab

## Sources

- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D16 | Y | Scan last 2w then full history
- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: Scan session transcripts for decisions last-2-weeks first, then widen to full history.
- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Scan session transcripts for decisions last-2-weeks first, then widen to full history.

~~~~

### Result 4 — `D01.md`

- `score`: `0.15487658977508545`
- `cross-score`: `null`
- `corpus-id`: `515620ef-61ea-4aaf-80d7-78c4bc667779`

Verbatim `entry`:

~~~~text
# D01 — GDDP role vs harness

> GDDP constrains/verifies loop; not harness rebuild

## Decision

GDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop.

## Rationale

Keeps GDDP a control/evidence layer around replaceable executors (Pi, Jules, Claude, etc.).

## Record

- **Project:** `GDDP`
- **Status:** `accepted`
- **Decided on:** `2026-08-08`
- **Decided by:** Sab

## Sources

- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D01 | Y | GDDP constrains/verifies loop; not harness rebuild
- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: GDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop.
- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: GDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop.

~~~~

### Result 5 — `D08.md`

- `score`: `0.16033553121474053`
- `cross-score`: `null`
- `corpus-id`: `465068ba-bf52-469c-94f6-665c622d3aac`

Verbatim `entry`:

~~~~text
---
id: "D08"
schema_version: "1.0"
project: "GDDP"
title: "Reject revokes dependent admission"
summary: "Reject revokes dependent admission"
statement: "Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block."
status: "accepted"
rationale: "Doctrine: rejection must not leave downstream work still admitted."
decided_on: "2026-08-08"
decided_by: "Sab"
sources:
  -
    kind: "review_sheet"
    ref: "project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md"
    note: "inclusion and status authority. Quote: D08 | Y | Reject revokes dependent admission"
  -
    kind: "memo"
    ref: "project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md"
    note: "repo-local decision wording. Quote: Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block."
  -
    kind: "other"
    ref: "/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md"
    note: "byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block."
evidence_paths:
  - "project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md"
  - "project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md"
confidence: "high"
review_mark: "Y"
---

# D08 — Reject revokes dependent admission

> Reject revokes dependent admission

## Decision

Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.

## Rationale

Doctrine: rejection must not leave downstream work still admitted.

## Record

- **Project:** `GDDP`
- **Status:** `accepted`
- **Decided on:** `2026-08-08`
- **Decided by:** Sab

## Sources

- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D08 | Y | Reject revokes dependent admission
- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.
- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.

~~~~

## Acceptance status

- `answers-captured`: **MET** — exact query, complete raw response body, and every returned evidence passage are preserved above.
- `queries-predetermined`: **MET** — the query file timestamp precedes the recorded request start.
- Answer quality was recorded as returned and was not used as a retry gate.
