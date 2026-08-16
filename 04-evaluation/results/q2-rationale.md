# Khoj evaluation result — Rationale

**Node:** `node-10-eval-factual-rationale`  
**Execution attempt:** `job_20260815T0045189219fa28cd0235:attempt:0`  
**Target:** `gddp-part1@local` on `khoj-38-b`  
**Result:** **Captured — chat returned HTTP 500; the read-only search endpoint returned 5 evidence passages.**

## Exact predetermined query

```text
Why was the import tool chosen as the only path for nodes to enter GDDP graphs?
```

- Query file: `04-evaluation/queries/q2.txt`
- Query file SHA-256: `57cb1ddef8745873b6fd7e7f644d6f3b410bb70b16ffcafe9fb970cf31e2fb8e`
- Query file modification time: `2026-08-15T00:46:01.954934+00:00`
- Chat request sent: `2026-08-15T00:48:03.203924+00:00`
- Evidence request sent: `2026-08-15T00:48:56.090603+00:00`
- Ordering check: **PASS** — the query file timestamp precedes both live requests.

## Khoj raw answer (verbatim)

Khoj `POST /api/chat?client=api` returned HTTP `500` with this complete response body:

```json
{"detail":"Set your OpenAI API key or enable Local LLM via Khoj settings."}
```

This is the raw result for the predetermined query. It was not retried. Khoj produced no natural-language answer because the isolated user had no chat model configured.

## Retrieved evidence passages

Because chat stopped before document search, each passage below was captured once through the authenticated, read-only `GET /api/search` interface using the exact same predetermined query (`n=5`, `t=all`). Passage text is reproduced verbatim from each response `entry`.

### Passage 1

- File: `D09.md`
- Score: `0.0753333568572998`
- Corpus ID: `6048f5f1-a203-46c1-9f0e-629a7929da82`

````text
# D09 — Nodes enter graphs only via import tool

> Nodes only via import tool

## Decision

Nodes enter graphs only through the import tool. No hand-authored graph mutation shortcuts.

## Rationale

One write path; prevents silent graph drift and review bypass.

## Record

- **Project:** `GDDP`
- **Status:** `accepted`
- **Decided on:** `2026-08-08`
- **Decided by:** Sab

## Sources

- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md` — inclusion and status authority. Quote: D09 | Y | Nodes only via import tool
- `memo` `project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md` — repo-local decision wording. Quote: Nodes enter graphs only through the import tool. No hand-authored graph mutation shortcuts.
- `other` `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md` — byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Nodes enter graphs only through the import tool. No hand-authored graph mutation shortcuts.
````

### Passage 2

- File: `D09.md`
- Score: `0.09891884929425265`
- Corpus ID: `0c91bccc-0b20-48e2-b170-9e4dba1fa13a`

````text
---
id: "D09"
schema_version: "1.0"
project: "GDDP"
title: "Nodes enter graphs only via import tool"
summary: "Nodes only via import tool"
statement: "Nodes enter graphs only through the import tool. No hand-authored graph mutation shortcuts."
status: "accepted"
rationale: "One write path; prevents silent graph drift and review bypass."
decided_on: "2026-08-08"
decided_by: "Sab"
sources:
  -
    kind: "review_sheet"
    ref: "project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md"
    note: "inclusion and status authority. Quote: D09 | Y | Nodes only via import tool"
  -
    kind: "memo"
    ref: "project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md"
    note: "repo-local decision wording. Quote: Nodes enter graphs only through the import tool. No hand-authored graph mutation shortcuts."
  -
    kind: "other"
    ref: "/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md"
    note: "byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: Nodes enter graphs only through the import tool. No hand-authored graph mutation shortcuts."
evidence_paths:
  - "project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md"
  - "project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md"
confidence: "high"
review_mark: "Y"
---
````

### Passage 3

- File: `index.md`
- Score: `0.14921659231185913`
- Corpus ID: `515f2c97-b249-453c-b89a-86eeca56e2cb`

````text
# Canonical decision corpus
## Project homes

### GDDP

- [D01 — GDDP role vs harness](D01.md) — `GDDP`
- [D02 — Job disposal path](D02.md) — `GDDP`
- [D03 — No silent system-python eval fallback](D03.md) — `GDDP`
- [D04 — `agent` is literal, not wildcard](D04.md) — `GDDP`
- [D05 — Empty allow-list → operator / default executor](D05.md) — `GDDP`
- [D06 — Bookkeeping mismatch is evidence, not a hard block](D06.md) — `GDDP`
- [D07 — Human is last provisional gate](D07.md) — `GDDP`
- [D08 — Reject revokes dependent admission](D08.md) — `GDDP`
- [D09 — Nodes enter graphs only via import tool](D09.md) — `GDDP`
- [D10 — No merge-to-main by default on acceptance](D10.md) — `GDDP`
- [D12 — Prefer flow-on-provisional unless strict canary](D12.md) — `GDDP`
- [D13 — Prove pass-write and reject-revoke before mission scale](D13.md) — `GDDP`
- [D15 — Graphify structural, Khoj semantic](D15.md) — `MyAPI/Pi/GDDP`

### Khoj

- [D14 — Khoj corpus composition](D14.md) — `MyAPI/Khoj`

### MyAPI

- [D14 — Khoj corpus composition](D14.md) — `MyAPI/Khoj`
- [D15 — Graphify structural, Khoj semantic](D15.md) — `MyAPI/Pi/GDDP`
- [D16 — Decision scan order](D16.md) — `MyAPI`

### Pi

- [D15 — Graphify structural, Khoj semantic](D15.md) — `MyAPI/Pi/GDDP`
- [D17 — Read code before new machinery](D17.md) — `Pi`
- [D18 — No load-bearing unverified assumptions](D18.md) — `Pi`
````

### Passage 4

- File: `D01.md`
- Score: `0.15300226211547852`
- Corpus ID: `515620ef-61ea-4aaf-80d7-78c4bc667779`

````text
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
````

### Passage 5

- File: `D01.md`
- Score: `0.15568077564239502`
- Corpus ID: `0b8f60c0-7d3d-49d8-871a-aeb406ff5802`

````text
---
id: "D01"
schema_version: "1.0"
project: "GDDP"
title: "GDDP role vs harness"
summary: "GDDP constrains/verifies loop; not harness rebuild"
statement: "GDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop."
status: "accepted"
rationale: "Keeps GDDP a control/evidence layer around replaceable executors (Pi, Jules, Claude, etc.)."
decided_on: "2026-08-08"
decided_by: "Sab"
sources:
  -
    kind: "review_sheet"
    ref: "project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md"
    note: "inclusion and status authority. Quote: D01 | Y | GDDP constrains/verifies loop; not harness rebuild"
  -
    kind: "memo"
    ref: "project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md"
    note: "repo-local decision wording. Quote: GDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop."
  -
    kind: "other"
    ref: "/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md"
    note: "byte-identical parity witness for the decision wording. SHA-256 4124f8001b656d913e0ac7f4ba0c3737ba7199af94d94e462c481e20e41a5558. Quote: GDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop."
evidence_paths:
  - "project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md"
  - "project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md"
confidence: "high"
review_mark: "Y"
---
````

## Run method and boundary

- Auth used `Authorization: Bearer <token>`; the token was read only inside the VM process from `/home/sab-mini/.khoj/gddp-part1.token` and is absent from this artifact.
- An authenticated `GET /api/health` returned HTTP `200` and `email: gddp-part1@local` before the chat requests.
- The evidence API returned HTTP `200` for this query.
- No graph truth or runtime database was directly accessed or modified.
