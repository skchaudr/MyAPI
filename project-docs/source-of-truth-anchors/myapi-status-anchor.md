---
title: MyAPI Status Anchor
aliases:
  - MyAPI status
  - MyAPI broken
  - MyAPI blocked
  - MyAPI known issues
  - MyAPI open issues
  - MyAPI refinement queue
  - what's broken in MyAPI
  - what's blocked in MyAPI
source: obsidian
document_kind: synthesized_note
type: anchor
status: active
projects:
  - myapi
  - context-refinery
tags:
  - myapi
  - status
  - known-issues
  - retrieval-anchor
  - operational
benchmark_targets:
  - retrieval-benchmark-v0/A7
related:
  - my-devinfra-system-anchor
  - khoj-deployment-indexing-anchor
  - vm-tailscale-ssh-access-anchor
---

# MyAPI Status Anchor

## What This Is

This note is the canonical answer to **"what's broken or blocked in MyAPI right now?"**. It targets A7 in the trust-categorized query bank. An agent on cold-start asking what to avoid stepping on should land here, not on raw eval notes.

Last updated: 2026-05-03. Issues are listed in severity order. For deeper detail on any item, follow the source-evidence links at the bottom — this anchor states the issues and the diagnosis; the eval notes hold the long-form forensics.

## Open Issues — Blocking

These gate trust or block ongoing work. Fix or work around before relying on adjacent functionality.

- **A1 anchor candidate-set gap (discovered 2026-05-03)** — `my-devinfra-system-anchor.md` no longer appears in the candidate set for the project-overview query "What is MyAPI and what is its current goal?". `obsidian-myapi-anchor.md` wins #1, but the devinfra anchor is absent from `total_after_filter: 4`. Not a ranking regression — the anchor is not reaching the pipeline. Likely indexing-side (file missing from `~/khoj-data/notes/` on VM, or stale Khoj index). Diagnosis owed.
- **A7 itself (until this anchor is indexed)** — the query "What's broken or blocked in MyAPI?" returns MyAPI subject-scoped anchors but misses the eval notes that actually carry the answer. Building this anchor is the fix, but it must be pushed into the Khoj corpus and reindexed before it surfaces.

## Open Issues — Annoying

Ship-blockers for polish, not for trust. Schedule when the leverage is right.

- **27 obsidian files missing from index** — known carry-over from 2026-04-25. Delta-patch reindex script identified them but they have not been re-pushed.
- **`source: "unknown"` on anchor docs** — anchor filenames in `project-docs/source-of-truth-anchors/` lack the `obsidian-` prefix that `MetadataParser._infer_source_from_filename` keys on. Anchors win without source/title boosts; fixing the prefix or the parser would widen margins.
- **A4 — `CLAUDE.md` is a corpus gap** — confirmed 2026-04-26. Repo-internal CLAUDE.md (Python conventions, shell rules) is not in any indexed batch. Agents can read it directly, but corpus should know about it. Fix is a "conventions corpus batch" decision, not yet made.
- **H1 intent re-routing** — bank says human-find-thread queries should route to `lookup`, not `operational`. Currently OPERATIONAL fires first and grabs queries like "find the thread where I set up the Khoj VM migration." Small classifier tweak.
- **Q18 dedicated end-to-end anchor missing** — A2 wins now via the my-devinfra anchor, but a dedicated `current-system-end-to-end-anchor.md` is the cleaner answer.

## Open Issues — Acceptable / Mapped

Known weak classes. Failures here are expected and shape the v1 → v2 roadmap, not the trust judgment.

- **F1 — time-scoped queries** — temporal filtering not deeply implemented. Probe maps the gap.
- **F2 — negation queries** — classifier doesn't recognize "X but not Y." Probe maps the boundary.
- **F3 — cross-entity queries** — hybrid keyword+vector should handle but untested.
- **F4 — decision-recovery / paths-not-taken** — likely corpus gap (decisions live in conversation, not notes).
- **H2 — design-note recall** — does a `source-aware-priors` design note exist? Untested. Diagnoses corpus vs retrieval gap.
- **H3 — temporal precision** — paired with F1; expected weak.

## Recently Closed

Fixes that landed; sentinels watching for regressions.

- **2026-05-03 — F5 phrase-lane fix.** `KeywordSearcher` was requiring every bare term in a query to appear in the document body, even when a quoted phrase was present. Long-sentence phrase queries (e.g. F5: `Find the note where I used the term "gold mine"`) silently dropped the answer document from the candidate set. One-line fix at `context_refinery/retrieval.py:269` (`not phrases and terms and ...`). F5 now returns the Trust-Threshold plan at #3, fs=0.838. Acceptance set: 4/5 → 5/5 mechanical. Commit `28a22b0`.
- **2026-04-25 — exact-phrase boost + classifier patches** (commit `5d713ab`). Hyphen/space/no-space normalization for exact phrases; MyAPI as first-class project name in classifier; OPERATIONAL fires before PROJECT; chat-dump synthesized_note guard. Closed the F5/H4 sentinel pair (until F5 regressed and was re-fixed 2026-05-03).
- **2026-05-02 — A7 vocab bridge** (deployed but no-op on target). Operational+problem-verb queries now append "known issues / fragile / thin / gap / weak / queue" to the Khoj query. Patch is live and harmless; the real A7 fix turned out to be subject-scope (this anchor), not terminology.

## Failure Modes / Gotchas

- **Subject-scope dominates the candidate set for operational queries.** The 2026-05-02 diagnosis is the load-bearing lesson: when an operational query mentions MyAPI, MyAPI subject-scoped docs dominate the candidates, and no amount of vocab expansion pulls in eval-of-retrieval-benchmark notes. The lesson generalizes — subject-scope your anchor frontmatter (`projects`, `tags`, `aliases`) to whatever the agent is asking about, not whatever the *document is about*.
- **Reranker can only re-rank what Khoj returns.** Boosts and priors are useless if the answer doc is absent from the candidate set. F5 was a candidate-set bug, not a ranking bug. Same shape as the A1 anchor gap above. When a query fails, check `total_after_filter` first — if it's small (≤5), the bug is upstream of the reranker.
- **VM auto-shutdown is 3 hours.** Acceptance and benchmark scripts will fail with a clean "VM unreachable" error if the VM is asleep. Start the VM (`gcloud compute instances start`) before running.

## Source Evidence

- `project-docs/STATUS_AND_NEXT_STEPS.md` — strategic frame and pending queue
- `project-docs/My-API-Trust-Threshold-Plan.md` — agent-cold-start product framing
- `project-docs/retrieval-benchmark-v0/Query/query-bank-trust-categorized-v1.md` — 17-query bank with class taxonomy and acceptance set
- `project-docs/retrieval-benchmark-v0/Harness evaluation/run-2026-05-02-tighten-pass.md` — A7 subject-scope re-diagnosis; F5 regression diagnosis
- `project-docs/retrieval-benchmark-v0/Harness evaluation/run-2026-04-25-blocker-pass.md` — 04-25 classifier and phrase-boost patches
- `project-docs/retrieval-benchmark-v0/refinement-queue-2026-04-20.md` — older refinement queue
- `scripts/acceptance.py` — six-query mechanical acceptance harness
- `handoffs/000-cleared-context-bare-retrieval.md` — 2026-05-03 session handoff (F5 fix)
