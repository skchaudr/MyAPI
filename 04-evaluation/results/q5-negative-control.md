# Query 5 — negative control

**Node:** `node-12-eval-negative-control`  
**Execution attempt:** `job_20260815T00451894af7b62cd267e:attempt:0`  
**Run:** 2026-08-15T00:47:45Z on `khoj-38-b`  
**Authenticated user:** `gddp-part1@local`

## Exact query

```text
What was the exact color of Sab's front door on January 1, 2010?
```

This exact text was written to `04-evaluation/queries/q5.txt` at 2026-08-15T00:46:58Z, before Khoj was asked.

## Raw answer

Khoj returned HTTP `500` to the single `POST http://localhost:42110/api/chat?client=api` request and returned no answer. The client surfaced the following verbatim outcome:

```text
urllib.error.HTTPError: HTTP Error 500: Internal Server Error
```

The request body was `{"q": <exact query above>, "n": 5, "stream": false, "create_new": true}`. Immediately before the request, authenticated `GET /api/health` returned HTTP `200` with `email: gddp-part1@local`. The answer request was not retried.

## Retrieved evidence

A single Bearer-authenticated `GET http://localhost:42110/api/search` used the same exact query with `n=5&t=all`; it returned HTTP `200` and five unrelated corpus chunks:

1. `D16.md`, score `0.22638541460037231`

   > Scan session transcripts for decisions last-2-weeks first, then widen to full history.
   >
   > Newest operator intent first; full archive is phase 2.

2. `D07.md`, score `0.22705841064453125`

   > Evaluator is second-to-last gate; human is last on provisional nodes. Reject returns the node to `ready` for retry.
   >
   > Defines acceptance authority and retry semantics.

3. `D07.md`, score `0.23198473453521729`

   > statement: "Evaluator is second-to-last gate; human is last on provisional nodes. Reject returns the node to `ready` for retry."
   >
   > rationale: "Defines acceptance authority and retry semantics."

4. `D09.md`, score `0.23261271520777116`

   > statement: "Nodes enter graphs only through the import tool. No hand-authored graph mutation shortcuts."
   >
   > rationale: "One write path; prevents silent graph drift and review bypass."

5. `D06.md`, score `0.2346498966217041`

   > statement: "Safeguards that only catch runtime bookkeeping mismatch (not genuinely unsafe action) should surface as evaluation evidence, not hard-reject usable work."
   >
   > rationale: "Protects momentum; commit/HEAD bookkeeping churn must not force full node reruns by default."

None of the five retrieved passages contains a front-door color or a fact about January 1, 2010.

## Verdict

Khoj neither correctly declined/hedged nor confabulated because it returned HTTP `500` without an answer.
