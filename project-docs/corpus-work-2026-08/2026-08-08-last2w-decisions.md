# Durable decisions — last 2 weeks scan (accepted 2026-08-08)

Source: session transcript scan (2026-07-25 → 2026-08-08) → review sheet  
Accepted: D01–D10, D12–D18 (**17**). Dropped: **D11**.  
Status: Sab-reviewed. Ready for Khoj normalize/ingest.

---

## D01 — GDDP role vs harness
**Project:** GDDP  
**Decision:** GDDP constrains, interprets, and verifies the executor loop. It does not rebuild the agent harness loop.  
**Why it matters:** Keeps GDDP a control/evidence layer around replaceable executors (Pi, Jules, Claude, etc.).

## D02 — Job disposal path
**Project:** GDDP  
**Decision:** Job failure uses a dedicated disposal path (`mark_job_failed` + durable reason/receipt). Do not use `node_status` and do not mutate graph truth for disposal.  
**Why it matters:** Separates runtime job bookkeeping from graph/node truth.

## D03 — No silent system-python eval fallback
**Project:** GDDP  
**Decision:** If project `.venv` is missing, do not fall back to system Python. Report `probe_unavailable` unless the project declares an alternate evaluation environment.  
**Why it matters:** Prevents false-green evidence from wrong dependencies.

## D04 — `agent` is literal, not wildcard
**Project:** GDDP  
**Decision:** Allowed mode `agent` is compared literally. It is not a wildcard. No executor-inheritance or wildcard-permission machinery.  
**Why it matters:** Stops “clever” permission expansion; node allow-lists mean exactly what they say.

## D05 — Empty allow-list → operator / default executor
**Project:** GDDP  
**Decision:** When a node has not constrained executors, the operator’s explicit pick wins. `auto` resolves to configured `default_executor`.  
**Why it matters:** Operator authority is the point of the allow-list; empty list must not strand dispatch.

## D06 — Bookkeeping mismatch is evidence, not a hard block
**Project:** GDDP  
**Decision:** Safeguards that only catch runtime bookkeeping mismatch (not genuinely unsafe action) should surface as evaluation evidence, not hard-reject usable work.  
**Why it matters:** Protects momentum; commit/HEAD bookkeeping churn must not force full node reruns by default.

## D07 — Human is last provisional gate
**Project:** GDDP  
**Decision:** Evaluator is second-to-last gate; human is last on provisional nodes. Reject returns the node to `ready` for retry.  
**Why it matters:** Defines acceptance authority and retry semantics.

## D08 — Reject revokes dependent admission
**Project:** GDDP  
**Decision:** Rejecting a provisional node must revoke dependent admission (token revoke-on-reject) so dependents re-block.  
**Why it matters:** Doctrine: rejection must not leave downstream work still admitted.

## D09 — Nodes enter graphs only via import tool
**Project:** GDDP  
**Decision:** Nodes enter graphs only through the import tool. No hand-authored graph mutation shortcuts.  
**Why it matters:** One write path; prevents silent graph drift and review bypass.

## D10 — No merge-to-main by default on acceptance
**Project:** GDDP  
**Decision:** Executor results live on worktree/result-branch. Acceptance does not merge to `main` by default.  
**Why it matters:** Keeps main clean; acceptance ≠ land.

## D12 — Prefer flow-on-provisional unless strict canary
**Project:** GDDP  
**Decision:** Default preference is flow-on-provisional (momentum; review can lag execution). Strict canary (`frontier_auto_advance: false`) only when explicitly flipped.  
**Why it matters:** Chooses speed-with-review-lag over stop-the-line canary as the normal mode.

## D13 — Prove pass-write and reject-revoke before mission scale
**Project:** GDDP  
**Decision:** Before mission-scale work depends on the gate system, run one tiny live heartbeat node and prove both: pass → admission token written; reject → token revoked and dependents blocked again.  
**Why it matters:** Cheap dress rehearsal so the first real proof is not a full mission.

## D14 — Khoj corpus composition
**Project:** MyAPI / Khoj  
**Decision:** Curated Khoj corpus = existing project docs/notes (~687) + hand-picked session digests. Not bulk dump of ~4k raw transcripts.  
**Why it matters:** Signal over volume for semantic retrieval.

## D15 — Graphify structural, Khoj semantic
**Project:** MyAPI / Pi / GDDP  
**Decision:** Graphify (`graph.json`, reports, `graphify query` paths) stays the structural layer. Khoj is the semantic answer layer over normalized notes, including these decision notes.  
**Why it matters:** Agents need path structure *and* answered meaning; neither replaces the other alone.

## D16 — Decision scan order
**Project:** MyAPI / ops  
**Decision:** Scan session transcripts for decisions last-2-weeks first, then widen to full history.  
**Why it matters:** Newest operator intent first; full archive is phase 2.

## D17 — Read code before new machinery
**Project:** Pi / agent ops  
**Decision:** Verify each claim against live code before designing workarounds. Reject new machinery when correcting a config word fixes the problem.  
**Why it matters:** Stops assumption→workaround→load-bearing architecture loops.

## D18 — No load-bearing unverified assumptions
**Project:** Pi / agent ops  
**Decision:** Unverified assumptions must not become load-bearing architecture.  
**Why it matters:** Companion rule to D17; compounds with multi-agent proposal chains.

---

## Dropped

- **D11** — “Local Pi GDDP lane is the chosen foundation for fleet-building” — **N** (Sab rejected).

## Next

1. Normalize/sanitize hand-picked session digests (separate from these 17).  
2. Ingest this file + ~687 docs into Khoj.  
3. Widen decision scan beyond last 2 weeks.
