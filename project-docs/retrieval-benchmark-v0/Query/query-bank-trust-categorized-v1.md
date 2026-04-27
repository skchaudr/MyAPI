# Query Bank — Trust-Categorized v1

Created: 2026-04-25

This is the canonical query bank for Phase 2 of MyAPI (trust-categorization phase). It supersedes ad-hoc benchmark runs as the *source of queries*. Individual benchmark runs reference these query IDs and live in `../Harness evaluation/`.

## Framework

Every query belongs to one of three categories:

- **Human retrieval (H)** — "find me that thread", "what did I decide about X". Wants source/narrative.
- **Agent retrieval (A)** — "what is the current state of X", "what should I know before touching Y". Wants structured assertions.
- **Failure probe (F)** — designed to map the boundary of trust (time-scoped, negation, relationship, exact-term, decision-recovery).

Every result gets diagnosed with one of seven buckets:

`win` / `weak win` / `corpus gap` / `retrieval gap` / `metadata gap` / `intent gap` / `answer-shape gap`

Severity if the query fails: `blocking` / `annoying` / `acceptable`.

### Query class (added in 2026-04-27 audit)

Beyond category and severity, every query has a **class** that determines what its result actually means:

- **Validator** — user believes the answer is in the corpus and expects it to be findable. A fail is a real regression; investigate.
- **Probe** — user suspects a gap; running the query diagnoses *where* (corpus / retrieval / metadata / intent / answer-shape). A fail is a confirmed build task, not a crisis.
- **Sentinel** — a previously-fixed failure mode. A fail means the fix broke; treat like a regression.

This was added after A4 surfaced as a probe wearing validator clothes ("Good enough: surfaces project CLAUDE.md content" implied success was expected, but the status line acknowledged it was probably a corpus gap). Probes belong in the bank — they shape the roadmap — but they should not be counted as failed acceptance tests when they fail-by-design. Only validators + sentinels gate the trust judgment.

---

## Human Retrieval (H)

### H1. Find the thread where I set up the Khoj VM migration
- **Class**: validator — VM migration happened ~2026-04-18 with active claude-code sessions; user expects those sessions exported into the corpus
- **Expected shape**: 1-3 session/note links with dates, ranked by relevance to VM-setup work
- **Good enough**: top result is the migration session or a session-summary note from that week
- **Severity if fails**: annoying — fallback is grep through claude-code exports

### H2. What did I decide about source-aware priors?
- **Class**: probe — user uncertain whether a standalone design note exists vs. the decision living only in conversation + commit message
- **Expected shape**: decision text + reasoning, plus link to source thread/commit
- **Good enough**: diagnoses whether design notes for code-decisions are in corpus; surfaces a decision note OR the commit context if either exists, else confirms the gap
- **Severity if fails**: annoying — decision is recoverable from git log

### H3. When was I last working on the benchmark harness?
- **Class**: probe — temporal precision is a known weak class; running this maps the temporal-retrieval boundary, not a feature the corpus is expected to fully support yet
- **Expected shape**: temporal answer — date or date range, optionally with file paths touched
- **Good enough**: surfaces the 2026-04-23 post-anchor run or the harness scripts dir activity
- **Severity if fails**: acceptable — `git log` covers this

### H4. Find notes about the gold-mine Q1 fix
- **Class**: sentinel — exact-term regression check; Q1 fix already landed, this query verifies it holds
- **Expected shape**: exact-term match on the specific incident (broken exact-match search → fix → recovery)
- **Good enough**: returns the session(s) where exact-term retrieval was diagnosed and patched
- **Severity if fails**: **blocking** — part of the **exact-term regression** sentinel pair (with F5); a single failure on either is one regression, not two crises

### H5. What's been frustrating me about the triage workflow?
- **Class**: probe — corpus presence and answer-shape both uncertain; reflective queries test whether the corpus carries lived-experience signal at all
- **Expected shape**: 2-4 reflective notes or session segments with concrete friction points
- **Good enough**: surfaces V4 triage feedback, owner-pass complaints, or recent friction logs
- **Severity if fails**: acceptable — reflective queries are exploratory by nature

---

## Agent Retrieval (A)

### A1. What is MyAPI and what is its current goal?
- **Class**: validator — anchor exists (`my-devinfra-system-anchor.md`) and won the 2026-04-23 run; this is the project-overview baseline and we expect it to keep passing
- **Expected shape**: 1-paragraph assertion + 3-5 bullet points (architecture, current phase, immediate goal)
- **Good enough**: top result is `my-devinfra-system-anchor.md`; answer mentions retrieval substrate + agent-cold-start direction
- **Severity if fails**: **blocking** — this is the project-overview baseline; agents can't operate without it
- **Status**: won by anchor in 2026-04-23 run (thin margin: 1.297 vs 1.288)

### A2. What's the current state of the retrieval pipeline end-to-end?
- **Class**: probe — over-promised originally; the canonical anchor doesn't exist yet, so a "fail" was guaranteed. Running A2 surfaces what the corpus *does* have when asked this question, and the gap-shape informs the build task.
- **Expected shape**: structured: corpus → indexer → Khoj → Context Refinery → benchmark loop, with current health/blockers per stage
- **Good enough**: confirms the dedicated anchor is missing and surfaces the closest existing surrogate (`my-devinfra-system-anchor.md` partial, or recent run notes); result is a build-task signal, not pass/fail
- **Severity if fails**: **blocking** — Q18 territory, **known corpus gap, not a surprise failure**. Tonight produces a build task, not panic.
- **Status**: known corpus gap, anchor not built

### A3. What is the status of the API deployment?
- **Class**: validator — anchor exists and won; agents need this routinely; expected to keep passing
- **Expected shape**: structured: VM hostname/IP, services running, ports, health-check command, last-known-good timestamp
- **Good enough**: anchors at top, surfaces Tailscale IP + 6-hour auto-shutdown caveat
- **Severity if fails**: **blocking** — operational query, agents need this before touching anything live
- **Status**: won by anchor (Q12)

### A4. What conventions apply when editing Python in this repo?
- **Class**: probe — confirmed corpus gap on 2026-04-26 blocker pass; CLAUDE.md is repo-internal and doesn't fit any current corpus batch (notes/ai-exports/anchors). The query's purpose is to surface that gap and force the batch-shape decision.
- **Expected shape**: assertions about no multi-line `-c`, PYTHONPATH requirements, project structure
- **Good enough**: diagnoses whether CLAUDE.md is in corpus (gap) or surfaces it / a convention surrogate; produces a fix-shape decision (anchor-equivalent vs. new conventions batch)
- **Severity if fails**: annoying — agents can read CLAUDE.md directly, but corpus should know about it
- **Status**: confirmed **corpus gap** (2026-04-26 run) — CLAUDE.md not in any indexed batch
- **Test rule**: if direct retrieval finds CLAUDE.md but labels/surfaces it badly → metadata gap. If retrieval cannot find it at all → corpus gap.

### A5. What anchors exist in this corpus and what queries do they cover?
- **Class**: probe — meta-corpus query that requires synthesis (listing + cross-referencing); even with anchors present, the answer-shape needs a synthesis layer that doesn't exist
- **Expected shape**: list of anchor files with their target query IDs
- **Good enough**: diagnoses whether the system can self-describe its anchor coverage (likely answer-shape gap → synthesis layer build task)
- **Severity if fails**: annoying — meta-corpus query, not blocking but reveals self-knowledge gap
- **Status**: untested — likely **answer-shape gap** (would need synthesis layer)

### A6. Who else is working on this and on what?
- **Class**: probe — `project_multi_agent.md` lives in memory not corpus, so a fail is the predicted outcome and produces an "ingest agent topology into corpus" task
- **Expected shape**: list of agents/collaborators with current scope (Codex on runtime/harness, Claude on framing, Jules for batch tasks)
- **Good enough**: diagnoses whether multi-agent topology is in corpus; produces a build task to ingest it if not
- **Severity if fails**: annoying (not blocking) — surfacing collaboration boundaries matters for handoffs but doesn't gate work
- **Status**: untested — `project_multi_agent.md` exists in memory but not corpus

### A7. What's broken or blocked in MyAPI right now?
- **Class**: validator — eval notes are indexed (verified 2026-04-26), so the *content* exists; the partial pass on terminology mismatch ("broken/blocked" vs. "known issues") is a real gap to close, not an unmapped probe
- **Expected shape**: list of open issues with severity (Q18 anchor missing, source: "unknown" on anchors, Q1 thin margin)
- **Good enough**: surfaces **either** the post-anchor-v2 run analysis section **or** the refinement queue / status note — not required to be one specific note
- **Severity if fails**: **blocking** — agents need to know what to avoid stepping on
- **Status**: 2026-04-26 partial — classifier + anchors at top, but terminology mismatch with "broken/blocked" verb; bridge needed

---

## Failure Probes (F)

### F1. What was I working on the week of April 15, 2026?
- **Class**: probe — temporal filtering is unimplemented; this query exists to map the gap, not to validate a feature
- **Type**: time-scoped
- **Expected shape**: filtered list of activity within that date range
- **Good enough**: returns notes/sessions from 2026-04-13 through 2026-04-19
- **Severity if fails**: acceptable — temporal precision is a known weak class
- **Hypothesis**: **retrieval gap** — temporal filtering isn't deeply implemented

### F2. What notes are about Pi but not about the harness?
- **Class**: probe — negation isn't recognized by the classifier; this query maps the intent-gap boundary
- **Type**: negation / boolean
- **Expected shape**: filtered list excluding harness-related notes
- **Good enough**: returns Pi-only notes; explicitly does not surface harness packets
- **Severity if fails**: acceptable — negation queries are notoriously hard for vector search
- **Hypothesis**: **intent gap** — classifier likely doesn't recognize negation

### F3. What projects mention both Khoj and Tailscale?
- **Class**: probe — hybrid retrieval *should* handle this; running it tells us whether keyword+vector composition actually works for cross-entity, or if there's a retrieval-gap to close
- **Type**: cross-source / multi-entity relationship
- **Expected shape**: list of projects/notes with both entities present
- **Good enough**: surfaces the VM/deployment cluster (anchors + related ops notes)
- **Severity if fails**: annoying — cross-entity queries are common for agents
- **Hypothesis**: hybrid keyword + vector should handle this; if it doesn't, **retrieval gap**

### F4. Did I ever decide against using MCP and why?
- **Class**: probe — paths-not-taken are inherently sparse; this query maps whether decision-recovery is feasible from the current corpus
- **Type**: decision-recovery / not-taken-path
- **Expected shape**: decision text or note explaining the rejection + reasoning
- **Good enough**: returns relevant decision note OR an explicit "no such decision found"
- **Severity if fails**: acceptable — paths-not-taken are inherently sparse in corpus
- **Hypothesis**: likely **corpus gap** — these decisions often live only in conversation, not notes

### F5. Find the note where I used the term "gold mine"
- **Class**: sentinel — exact-term regression check; Q1 fix landed, plus the 2026-04-26 exact-phrase boost; this query verifies both fixes hold
- **Type**: exact-term / post-Q1-fix verification
- **Expected shape**: exact-string match returning the specific note(s)
- **Good enough**: surfaces the trust-threshold plan or related session
- **Severity if fails**: **blocking** — paired with H4 as the **exact-term regression** sentinel; one failure on either = one regression. F5 is the **regression sentinel** — should be the first query run tonight.
- **Hypothesis**: should be a clean win post-Q1 fix; if it fails, the fix didn't generalize

---

## Run protocol

For each query in this bank:

1. Run through harness (or direct Khoj/Context Refinery query)
2. Capture top 5 results + scores
3. Diagnose with one of the 7 buckets
4. Note severity if failed
5. Group failures by bucket → fix highest-leverage class first
6. Re-run only the affected queries to verify the fix
7. Periodically re-run the full bank as a baseline check

## Distribution

- 5 human retrieval
- 7 agent retrieval
- 5 failure probes
- **17 total** for v1; expand as new query classes surface

## Tonight's run order (per Codex)

1. **F5** — exact-term regression sentinel (run first)
2. **H4** — exact-term regression pair
3. **A1** — project baseline
4. **A3** — live ops baseline
5. **A7** — blocker map
6. **A2** — corpus-build task signal
7. Everything else (A4, A5, A6, H1–H3, H5, F1–F4)

Logic: regression check → project baseline → live ops baseline → blocker map → wider trust boundary.

### Fix tonight if blocking
- A2 (build the end-to-end anchor)
- A7 (improve answer-shape or add anchor)
- exact-term regression if H4/F5 fail

### Test but likely queue for next session
- A4 (test rule decides corpus vs metadata gap)
- A5 (answer-shape work, larger lift)
- A6 (annoying-not-blocking)

## Resolved open questions

1. **Blocking-tonight set**: A2, A7, exact-term regression (H4/F5). Test-but-queue: A4, A5, A6.
2. **A4 diagnosis rule**: retrieval finds CLAUDE.md but mislabels → metadata gap; can't find at all → corpus gap.
3. **F5 verification**: this is the regression sentinel; first query of the night.

---

## Acceptance test set v1 (post-2026-04-27 audit)

After tagging every query as validator / probe / sentinel, only **6 of 17 queries** are true acceptance tests — the ones where a fail means a real regression or a real corpus health issue:

| ID | Class | Severity | Why it gates trust |
|---|---|---|---|
| H1 | validator | annoying | claude-code session exports should carry recent VM-migration work |
| H4 | sentinel | **blocking** | Q1 exact-term fix must hold (paired with F5) |
| A1 | validator | **blocking** | Project-overview anchor must surface for cold-start; baseline already won |
| A3 | validator | **blocking** | Live-ops anchor must surface; agents need this before touching the VM |
| A7 | validator | **blocking** | Issue-tracking notes are indexed; terminology bridge is the close-out |
| F5 | sentinel | **blocking** | Exact-term regression sentinel; runs first |

The remaining **11 queries are probes** (H2, H3, H5, A2, A4, A5, A6, F1, F2, F3, F4). They produce build tasks when they fail, not regressions. They should still be run — they shape the v1 → v2 roadmap — but their fail rate is not a measure of system trust.

### What this changes about pass/fail accounting

Before audit: 6 of 6 blocking-tonight queries closed → "blocker pass"
After audit: 6 of 6 acceptance-set blocking queries closed (5 of 6 cleanly: F5, H4, A1, A3 won; A7 partial via terminology bridge needed). H1 not yet run — should be next session's first validator check.

The 2026-04-26 blocker pass run was correct in conclusion (the system passed its real acceptance set, modulo A7 partial), but the run note treated A2 as a "blocker" when it was actually a probe; the night produced a build task for A2, which was always its purpose, not a fail.

### What enters the bank from this audit

- **Status updates** propagated into A4 and A7 from the 2026-04-26 run
- **Class field** on every query
- **Reframed "Good enough"** for A2, A4, A5, A6 (probes, not validators)

### What stays out (deferred)

- Per-class **diagnosis rubric** evolution (probes don't need the 7-bucket diagnosis if they're already classified by hypothesis); revisit after more probes run
- A new **Conventions corpus batch** decision (touched in A4's "Status" but the ingestion path is its own task)
