# MyAPI Part 2 — planning brief (assembled 2026-08-19, all claims live-verified)

Companion file: scratch/part2-eval-verdicts-2026-08-19.md (full evaluator digest).
Governing memo: gddp-config/docs/GDDPvMyAPI-Part2.md (335 lines; read first — it owns intent).

## 1. Mission (one paragraph)
Part 2 tests which durable source classes actually improve context retrieval. Six source
classes (decisions, handoffs, anchor, git, graphify, + Part-1 control) get normalized into
layers -> corpus variants -> a frozen evaluation ruler -> six controlled treatments ->
convergence finding. GDDP gates whether the experiment was EXECUTED correctly, never
whether the hypothesis won.

## 2. Verified live state
Graph (gddp-config graphs/myapi-part2/, 18 nodes):
- provisional (eval pass): 01 evidence-contract, 01b contract-review, 04 inventory-decisions
- ready w/ failed attempts: 02 chat-path-scorer, 03 validate-anchor, 05 inventory-handoffs,
  06 git-evidence, 07 graphify-evidence  (retry budget 0/3 spent on current job rows)
- pending: 08-18
Baseline (Part 1 control): complete, all 13 nodes. Local chat baseline re-run 2026-08-18:
Khoj now on the mini (localhost:42110, local postgres), chat via OpenRouter
google/gemini-2.5-flash. q1/q2 correct+cited, q3 hedged-abstain, q4 traced D18<->D17
companion, q5 clean abstain. Capture: MyAPI codex/myapi-decision-plan@4267673.

## 3. Execution landscape (changed since the crash)
- Orchestrator v1 (gddp-runtime 33a2a19): read-only Pi (read/bash/grep/find/ls/subagent
  only, no edit/write). Loop: observe -> dispatch -> monitor -> report. Boundary steering
  only; no steer channel; stuck-detection via staleness/PID; REPORTS, never cancels.
- Persistent per-project orchestrator session (fork A, f1b6783); ONE git worktree per
  session, not per attempt (ed0407b); batched packets (7221c66); idle grace 12h (ceee600).
- Executor preamble: "You are the EXECUTOR" — orchestration is structural, not per-node.
- Models available: gemini-3.1-pro + gemini-3.6-flash (abundant), deepseek-v4-pro +
  deepseek-v4-flash (abundant), grok-4.6, glm-5.2 (some), qwen (some). Codex lane OUT
  (usage limit, ~4 days from 08-16).
- Cancel primitive: NOT landed — `gddp jobs set failed` is unsafe (late-result
  resurrection); handoff 102 proposes `gddp jobs cancel`; orchestrator has no
  termination authority yet.

## 4. Evaluator verdicts (full digest in companion file)
- PASS: 01 (conf .97), 01b (.94), 04 (.96)
- FAIL 02 (contradicted): the only genuine execution failure — scope. Real work landed
  but only 1 of 4 ACs (metadata-behavior.md); scorer-mechanics.md absent; chat path was
  HTTP 500 then and was parked "out of this lane" instead of filed as a continuation
  proposal. Chat path NOW WORKS locally, so node-02's remaining scope shrank to scorer
  + probe capture.
- FAIL 03/06/07 + NEEDS-HUMAN-REVIEW 05 (block): all four are empty result commits —
  the SYMPTOM of one bug, not four problems. Root cause: the adapter spawned a headless
  executor per attempt and KILLED IT at agent_end (finally block), discarding all context
  and momentum — the disposable-executor pattern Sab had been told was already gone
  (gap first flagged 2026-08-14, recorded in handoff 098). Aborted/never-executed
  sessions were then wrapped as returncode-0 empty commits. Node-05 additionally died
  on Codex usage limit mid-flight. Sab halted the run on discovering the kill was still
  live: no forward progress until persistence was properly fixed.

## 5. Prerequisites before re-dispatch
1. THE BUG (disposable executor / kill-at-agent_end) IS FIXED — persistence landed:
   per-project persistent orchestrator (fork A f1b6783), one worktree per session
   (ed0407b), batch turns (handoff 100), idle grace 12h (ceee600), executor preamble
   separated from orchestrator (33a2a19).
2. Residual gap verified 2026-08-19: no zero-diff gate exists in pi_rpc_adapter or
   reconciler (grepped). A dead session can still be wrapped as an empty returncode-0
   result commit — the detection/reporting layer for the old bug's symptom is missing.
3. Cancel primitive (handoff 102) unlanded — stuck attempts still need manual surgery.
4. Orchestrator lane: Codex out; a replacement orchestrator model must be chosen
   (see open questions).

## 6. Current node contracts for the re-spec layer
node-02 chat-path-scorer | deps: 01b | artifacts: probe/metadata-behavior.md (DONE),
  probe/scorer-mechanics.md (MISSING) | AC: one-shot-answer-works, evidence-capture-proven,
  metadata-behavior-recorded (delivered), scorer-mechanics-ready
node-03 validate-anchor | deps: 01b | artifact: layers/anchor/anchor-assessment.md |
  AC: anchor-assessed, no-competing-brief, extension-bounded
node-05 inventory-handoffs | deps: 01b | artifact: layers/handoffs/handoff-manifest.jsonl |
  AC: manifest-complete (29 known + VM-only/dup/moved), inclusion-reproducible,
  chronology-preserved
node-06 git-evidence | deps: 01b | artifact: layers/git/ + build_git_export script |
  AC: export-created, reproducible (byte-identical rerun + sha256), absolute-dates
node-07 graphify-evidence | deps: 01b | artifact: layers/graphify/graphify-inventory.md |
  AC: capabilities-inventoried, dual-representation, distinction-documented
node-08 build-source-layers | deps: 03+04+05+06+07 | artifact: layers/ | AC:
  five-layers-built, provenance-intact, independently-composable

## 7. Open decision points for the planning session
A. Node-02: shrink to scorer-mechanics + probe capture (chat path proven), or re-run
   full four-AC contract for a clean receipt?
B. 03/05/06/07: re-run as-is once the empty-commit gate lands, or re-spec (merge 06/07
   as "structural evidence layer"? split 05's 29-handoff census into sub-units?)?
C. Who owns the residual zero-diff gate + cancel primitive — a gddp-runtime graph
   node (dogfood), or direct operator work? The root bug is fixed; these are the
   remaining detection/safety seams.
D. Orchestrator model with Codex out: gemini-3.1-pro vs deepseek-v4-pro for the
   observe/dispatch/report loop; worker pool: grok-4.6 / gemini-3.6-flash / ds-v4-flash.
E. Evaluator checker timeout (node-05, 1200s): cap evidence surface in the node contract,
   or raise/budget the checker?
F. frontier_auto_advance stays true with the empty-commit risk, or flip to strict canary
   until the gate lands?
G. Does node-11-part1-control consume the new local chat baseline (4267673) as its
   control measurement, or re-measure at its own HEAD per the contract?
