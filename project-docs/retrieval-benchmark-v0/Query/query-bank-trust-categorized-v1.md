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

---

## Human Retrieval (H)

### H1. Find the thread where I set up the Khoj VM migration
- **Expected shape**: 1-3 session/note links with dates, ranked by relevance to VM-setup work
- **Good enough**: top result is the migration session or a session-summary note from that week
- **Severity if fails**: annoying — fallback is grep through claude-code exports

### H2. What did I decide about source-aware priors?
- **Expected shape**: decision text + reasoning, plus link to source thread/commit
- **Good enough**: returns either `source-aware-priors` design note OR the commit `0f1155d` context
- **Severity if fails**: annoying — decision is recoverable from git log

### H3. When was I last working on the benchmark harness?
- **Expected shape**: temporal answer — date or date range, optionally with file paths touched
- **Good enough**: surfaces the 2026-04-23 post-anchor run or the harness scripts dir activity
- **Severity if fails**: acceptable — `git log` covers this

### H4. Find notes about the gold-mine Q1 fix
- **Expected shape**: exact-term match on the specific incident (broken exact-match search → fix → recovery)
- **Good enough**: returns the session(s) where exact-term retrieval was diagnosed and patched
- **Severity if fails**: **blocking** — part of the **exact-term regression** sentinel pair (with F5); a single failure on either is one regression, not two crises

### H5. What's been frustrating me about the triage workflow?
- **Expected shape**: 2-4 reflective notes or session segments with concrete friction points
- **Good enough**: surfaces V4 triage feedback, owner-pass complaints, or recent friction logs
- **Severity if fails**: acceptable — reflective queries are exploratory by nature

---

## Agent Retrieval (A)

### A1. What is MyAPI and what is its current goal?
- **Expected shape**: 1-paragraph assertion + 3-5 bullet points (architecture, current phase, immediate goal)
- **Good enough**: top result is `my-devinfra-system-anchor.md`; answer mentions retrieval substrate + agent-cold-start direction
- **Severity if fails**: **blocking** — this is the project-overview baseline; agents can't operate without it
- **Status**: won by anchor in 2026-04-23 run (thin margin: 1.297 vs 1.288)

### A2. What's the current state of the retrieval pipeline end-to-end?
- **Expected shape**: structured: corpus → indexer → Khoj → Context Refinery → benchmark loop, with current health/blockers per stage
- **Good enough**: returns `current-system-end-to-end-anchor.md` (doesn't exist yet)
- **Severity if fails**: **blocking** — Q18 territory, **known corpus gap, not a surprise failure**. Tonight produces a build task, not panic.
- **Status**: known corpus gap, anchor not built

### A3. What is the status of the API deployment?
- **Expected shape**: structured: VM hostname/IP, services running, ports, health-check command, last-known-good timestamp
- **Good enough**: anchors at top, surfaces Tailscale IP + 6-hour auto-shutdown caveat
- **Severity if fails**: **blocking** — operational query, agents need this before touching anything live
- **Status**: won by anchor (Q12)

### A4. What conventions apply when editing Python in this repo?
- **Expected shape**: assertions about no multi-line `-c`, PYTHONPATH requirements, project structure
- **Good enough**: surfaces project `CLAUDE.md` content or equivalent convention notes
- **Severity if fails**: annoying — agents can read CLAUDE.md directly, but corpus should know about it
- **Status**: untested — hypothesis: **corpus gap first** (CLAUDE.md likely not ingested), **metadata gap second** (if it is ingested but mislabeled)
- **Test rule**: if direct retrieval finds CLAUDE.md but labels/surfaces it badly → metadata gap. If retrieval cannot find it at all → corpus gap.

### A5. What anchors exist in this corpus and what queries do they cover?
- **Expected shape**: list of anchor files with their target query IDs
- **Good enough**: returns the 3 existing anchors with Q1/Q10/Q12/Q16 mapping
- **Severity if fails**: annoying — meta-corpus query, not blocking but reveals self-knowledge gap
- **Status**: untested — likely **answer-shape gap** (would need synthesis layer)

### A6. Who else is working on this and on what?
- **Expected shape**: list of agents/collaborators with current scope (Codex on runtime/harness, Claude on framing, Jules for batch tasks)
- **Good enough**: returns multi-agent topology note + recent project-state context
- **Severity if fails**: annoying (not blocking) — surfacing collaboration boundaries matters for handoffs but doesn't gate work
- **Status**: untested — `project_multi_agent.md` exists in memory but not corpus

### A7. What's broken or blocked in MyAPI right now?
- **Expected shape**: list of open issues with severity (Q18 anchor missing, source: "unknown" on anchors, Q1 thin margin)
- **Good enough**: surfaces **either** the post-anchor-v2 run analysis section **or** the refinement queue / status note — not required to be one specific note
- **Severity if fails**: **blocking** — agents need to know what to avoid stepping on
- **Status**: untested — relies on benchmark eval notes being indexed

---

## Failure Probes (F)

### F1. What was I working on the week of April 15, 2026?
- **Type**: time-scoped
- **Expected shape**: filtered list of activity within that date range
- **Good enough**: returns notes/sessions from 2026-04-13 through 2026-04-19
- **Severity if fails**: acceptable — temporal precision is a known weak class
- **Hypothesis**: **retrieval gap** — temporal filtering isn't deeply implemented

### F2. What notes are about Pi but not about the harness?
- **Type**: negation / boolean
- **Expected shape**: filtered list excluding harness-related notes
- **Good enough**: returns Pi-only notes; explicitly does not surface harness packets
- **Severity if fails**: acceptable — negation queries are notoriously hard for vector search
- **Hypothesis**: **intent gap** — classifier likely doesn't recognize negation

### F3. What projects mention both Khoj and Tailscale?
- **Type**: cross-source / multi-entity relationship
- **Expected shape**: list of projects/notes with both entities present
- **Good enough**: surfaces the VM/deployment cluster (anchors + related ops notes)
- **Severity if fails**: annoying — cross-entity queries are common for agents
- **Hypothesis**: hybrid keyword + vector should handle this; if it doesn't, **retrieval gap**

### F4. Did I ever decide against using MCP and why?
- **Type**: decision-recovery / not-taken-path
- **Expected shape**: decision text or note explaining the rejection + reasoning
- **Good enough**: returns relevant decision note OR an explicit "no such decision found"
- **Severity if fails**: acceptable — paths-not-taken are inherently sparse in corpus
- **Hypothesis**: likely **corpus gap** — these decisions often live only in conversation, not notes

### F5. Find the note where I used the term "gold mine"
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
