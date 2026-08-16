# Query grounding pass 1 — already-stated answers

Grounded in corpus-hot QUERIES categories: **Ownership · Now-state · Evidence · Connect**.

Method: harvest from anchors/briefs/QUERIES/SOURCES/decisions — fluff removed, structure kept.

Goal shape: decisions · golden keywords · context-rich sources · then git map. Sort/index preferred on VM.


## Operating model

- Code graphify = structural path answers (triggered by graph terms).

- This corpus = **semantic graphify**: ownership/now/evidence/connect even when code keywords never fire.

- Golden briefs + **golden keywords** per project = canonical retrieval handles.

- Compress: remove noise, keep self-documenting structure, attach git later.


---
# MYAPI

## Golden keywords (seed)

`vertex-ai-infrastructure-established`, `khoj-deployment-indexing-anchor`, `cleared-context-bare-retrieval`, `query-bank-trust-categorized`, `eval-of-retrieval-benchmark`, `notable-technical-decisions`, `prove-first-durable-handoff`, `rebuild-narrative-recapture`, `the-trust-calibration-model`, `decisions-and-trajectories`, `gddp-first-durable-handoff`, `sessions-and-conversations`, `my-devinfra-system-anchor`, `current-gaps-and-roadmap`, `artifacts-and-reference`, `source-of-truth-anchors`, `vm-tailscale-ssh-access`, `current-system-end-to`, `obsidian-myapi-anchor`, `speed-with-review-lag`, `systems-and-workflows`, `executor-inheritance`, `vm-migration-handoff`, `document-kind-aware`, `flow-on-provisional`, `plausible-but-wrong`, `retrieval-benchmark`, `source-aware-priors`, `wildcard-permission`, `symbolic-full-name`, `the-handoff-system`, `brief-description`, `decision-recovery`, `frontmatter-typed`, `human-find-thread`, `project-documents`, `retrieval-quality`, `trust-categorized`, `agent-cold-start`, `benchmark-driven`

## Ownership

- (PROJECT-BRIEF.md) explicitly stamped durable/canonical or used as baseline/reference. This keeps
- (PROJECT-BRIEF.md) and the handoff inversion; `ARCHITECTURE.md` as the canonical build plan
- (AGENTS.md) delimited. Any command being instructed to run must be placed on its own
- (AGENTS.md) Keep `.handoffs/000-template.md` as the canonical template. Do not overwrite it
- (README.md) Synthesized-note boost (prior for canonical anchors, guarded against chat-dump sources)
- (README.md) Acceptance harness has one bank-evolution question (A1) and one active retrieval investigation (A7).** See *The Trust Calibration Model* for the canonical state and rationale; per-run detail in `handoffs/`.
- (README.md) Four canonical anchor docs in `project-docs/source-of-truth-anchors/`:
- (README.md) These are the canonical context the benchmark queries are tuned against. Agents should query MyAPI for these before grep'ing.
- (README.md) See *The Trust Calibration Model* above for the canonical acceptance state and the per-query interpretation. Per-run scores are recorded in `handoffs/`.
- (README.md) `project-docs/STATUS_AND_NEXT_STEPS.md` — canonical "where are we" doc (last updated 2026-05-02)

## Now-State

- (PROJECT-BRIEF.md) The corpus direction is also sharper now: rebuild around a recent active window,
- (PROJECT-BRIEF.md) Phase:** planning / docs only — 0 implementation code. The planning work
- (PROJECT-BRIEF.md) has landed on `main`; `rebuild` remains a historical/local branch name. The
- (PROJECT-BRIEF.md) with live daily sources becoming the default active corpus
- (PROJECT-BRIEF.md) the live `context_refinery/` Python package — drift risk for new readers
- (AGENTS.md) Planning / docs-first rebuild work is now merged toward `main`. Do not invent
- (AGENTS.md) session being able to start immediately, not for the current session merely
- (AGENTS.md) 1. Run `git status --short --branch` before editing. If it is not clean, stop
- (AGENTS.md) 3. Verify branch and upstream before work: `git branch --show-current`,
- (AGENTS.md) but do not hide meaningful source artifacts just to get a clean status.

## Evidence

- (PROJECT-BRIEF.md) move it across sessions," the handoff is the tool. Two MCP tools
- (PROJECT-BRIEF.md) what matters, why, what the evidence is, what to think next. It is one of
- (PROJECT-BRIEF.md) verify / control / continue in agent-era infrastructure.
- (PROJECT-BRIEF.md) `max_tokens`, and evidence inclusion. The default answer is small and fresh; deeper
- (PROJECT-BRIEF.md) Pulled from `graphify-out/.graphify_analysis.json` (2026-06-21).
- (PROJECT-BRIEF.md) Structure (4 communities):** handoff/AGENTS ecosystem (evals, ingest,
- (PROJECT-BRIEF.md) rag-pipeline sub-agents); context-refinery core (event_trace, handoff
- (PROJECT-BRIEF.md) `../MyAPI/graphify-out/graph.json` (862 nodes, 2186 links) — baseline/reference,
- (PROJECT-BRIEF.md) and the handoff inversion; `ARCHITECTURE.md` as the canonical build plan
- (PROJECT-BRIEF.md) Inherited uncommitted work is part of the evidence trail. The rebuild is about

## Connect

- (PROJECT-BRIEF.md) Personal context engine. A vault of durable handoffs surfaced as context briefs via MCP — not v0's single RAG pool.
- (PROJECT-BRIEF.md) three portfolio pieces (with .pi and GDDP) — together a triptych for
- (PROJECT-BRIEF.md) rag-pipeline sub-agents); context-refinery core (event_trace, handoff
- (PROJECT-BRIEF.md) (four layers L0–L4); two event traces (MyAPI v0 derail; rebuild-night Codex
- (AGENTS.md) context briefs via MCP — not v0's single RAG pool.
- (AGENTS.md) `ingest/`, `rag-pipeline/` (sub-agent contracts)
- (AGENTS.md) If a command depends on `localhost`, `127.0.0.1`, a service port, or a local
- (README.md) Status:** Phase 1 (build the pipeline) is closed and deployed. Phase 2 (trust calibration via benchmark-driven refinement) is the active work.
- (README.md) Same corpus, same retrieval pipeline, different response shapes.
- (README.md) For questions, reach out via GitHub or sbkchaudry@gmail.com.


---
# GDDP

## Golden keywords (seed)

`multi-project-heartbeat-dispatch`, `notable-technical-decisions`, `rebuild-narrative-recapture`, `the-trust-calibration-model`, `dispatch-graph-target-fix`, `current-gaps-and-roadmap`, `source-of-truth-anchors`, `gddp-tui-navigation`, `plausible-but-wrong`, `retrieval-benchmark`, `symbolic-full-name`, `the-handoff-system`, `brief-description`, `executor-agnostic`, `human-in-the-loop`, `project-documents`, `retrieval-quality`, `benchmark-driven`, `context-refinery`, `layout-dependent`, `project-overview`, `synthesized-note`, `durable-handoff`, `formatting-only`, `friend-refinery`, `lowest-leverage`, `meta-narratives`, `SemanticToolbox`, `semi-autonomous`, `bank-evolution`, `context-window`, `high-certainty`, `metadata-aware`, `person-context`, `self-contained`, `benchmark-run`, `candidate-set`, `control-plane`, `gold-document`, `multi-project`

## Ownership

- (README.md) Synthesized-note boost (prior for canonical anchors, guarded against chat-dump sources)
- (README.md) Acceptance harness has one bank-evolution question (A1) and one active retrieval investigation (A7).** See *The Trust Calibration Model* for the canonical state and rationale; per-run detail in `handoffs/`.
- (README.md) Four canonical anchor docs in `project-docs/source-of-truth-anchors/`:
- (README.md) These are the canonical context the benchmark queries are tuned against. Agents should query MyAPI for these before grep'ing.
- (README.md) See *The Trust Calibration Model* above for the canonical acceptance state and the per-query interpretation. Per-run scores are recorded in `handoffs/`.
- (README.md) `project-docs/STATUS_AND_NEXT_STEPS.md` — canonical "where are we" doc (last updated 2026-05-02)
- (AGENTS.md) delimited. Any command being instructed to run must be placed on its own
- (AGENTS.md) Keep `.handoffs/000-template.md` as the canonical template. Do not overwrite it
- (PROJECT-BRIEF.md) explicitly stamped durable/canonical or used as baseline/reference. This keeps
- (PROJECT-BRIEF.md) and the handoff inversion; `ARCHITECTURE.md` as the canonical build plan

## Now-State

- (README.md) Status:** Phase 1 (build the pipeline) is closed and deployed. Phase 2 (trust calibration via benchmark-driven refinement) is the active work.
- (README.md) PYTHONPATH=/path/to/MyAPI uvicorn api.main:app --reload --port 8000
- (README.md) d '{"query": "What is MyAPI and what is its current goal?"}'
- (README.md) [Current Gaps and Roadmap](#current-gaps-and-roadmap)
- (README.md) `main.py`** — three routers: `/enrich`, `/import`, `/query`, plus `/health`.
- (README.md) Project identity** — "What is MyAPI and what is its current goal?"
- (README.md) Operational recall** — "What's broken or blocked in MyAPI right now?"
- (README.md) Synthesis** — "What docs should I use to understand the current system end to end?"
- (README.md) Fixes are tracked in numbered session handoffs (`handoffs/000-004`) and acceptance runs (`scripts/acceptance.py`). The acceptance harness is a mechanical test against the live `/query` endpoint with gold-document assertions per query.
- (README.md) The acceptance harness lives in `scripts/acceptance.py`; per-run details and current state are in `handoffs/` (most recent: `003-final-v0-benchmark-run.md`).

## Evidence

- (README.md) Status:** Phase 1 (build the pipeline) is closed and deployed. Phase 2 (trust calibration via benchmark-driven refinement) is the active work.
- (README.md) PYTHONPATH=/path/to/MyAPI uvicorn api.main:app --reload --port 8000
- (README.md) [The Handoff System](#the-handoff-system)
- (README.md) 1. **Agent-facing:** structured `/query` endpoint returning reranked evidence with confidence scores, source metadata, and timestamps. Designed for cold-start context elimination and inter-agent handoffs.
- (README.md) The benchmark (`project-docs/retrieval-benchmark-v0/Query/benchmark-v0.md`) contains 18 queries across multiple intent classes:
- (README.md) 3. **Corpus gap** — documented evidence doesn't exist
- (README.md) 4. **Retrieval gap** — evidence exists but candidate-set selection or ranking missed it
- (README.md) 5. **Metadata gap** — evidence exists but source/title/tag metadata is insufficient to route correctly
- (README.md) The acceptance harness lives in `scripts/acceptance.py`; per-run details and current state are in `handoffs/` (most recent: `003-final-v0-benchmark-run.md`).
- (README.md) 1. Three retrieval lanes, OR'd, with a synthesized-note prior** (commit `5d713ab`)

## Connect

- (README.md) Status:** Phase 1 (build the pipeline) is closed and deployed. Phase 2 (trust calibration via benchmark-driven refinement) is the active work.
- (README.md) Same corpus, same retrieval pipeline, different response shapes.
- (README.md) For questions, reach out via GitHub or sbkchaudry@gmail.com.
- (AGENTS.md) context briefs via MCP — not v0's single RAG pool.
- (AGENTS.md) `ingest/`, `rag-pipeline/` (sub-agent contracts)
- (AGENTS.md) If a command depends on `localhost`, `127.0.0.1`, a service port, or a local
- (PROJECT-BRIEF.md) Personal context engine. A vault of durable handoffs surfaced as context briefs via MCP — not v0's single RAG pool.
- (PROJECT-BRIEF.md) three portfolio pieces (with .pi and GDDP) — together a triptych for
- (PROJECT-BRIEF.md) rag-pipeline sub-agents); context-refinery core (event_trace, handoff
- (PROJECT-BRIEF.md) (four layers L0–L4); two event traces (MyAPI v0 derail; rebuild-night Codex


---
# PI

## Golden keywords (seed)

`irreversible-without-backup`, `task-packet-template`, `personal-knowledge`, `answer-noise-trim`, `execution-ledger`, `non-interactive`, `project-clients`, `infra-topology`, `stop-condition`, `pointer-style`, `voice-to-text`, `cheap-routes`, `daily-memory`, `git-workflow`, `graphify-out`, `ground-state`, `infra-budget`, `loop-breaker`, `models-store`, `needle-gemma`, `observe-only`, `tracked-file`, `full-ingest`, `hf-datasets`, `local-model`, `project-gdd`, `re-litigate`, `shell-first`, `broad-scan`, `disk-level`, `local-verb`, `mac-needle`, `gemma-cli`, `mini-only`, `on-device`, `one-liner`, `path-only`, `pi-hub-rs`, `one-line`, `pi-route`

## Ownership

- (QUERIES.md) 1. What does Pi own vs Needle vs mac-needle training package?
- (AGENTS.md) Sab owns direction, architecture, priorities, and final judgment.
- (AGENTS.md) TOOLS.md and other docs are pointers, not authority. Before claiming a tool

## Now-State

- (QUERIES.md) 3. Where do model provider settings live vs where weights/checkpoints live?
- (QUERIES.md) 6. Is Needle observe-only or active routing until eval gates clear?
- (QUERIES.md) 7. What are the two active Pi portfolio threads (extensions audit + Needle)?
- (SOURCES.md) | 9 | `/Users/sab-mini/.pi/agent/sessions/` | session dirs (names only sampled) | live |
- (AGENTS.md) Pi is his hands: inspect live state, do the work, verify by doing, report
- (AGENTS.md) Verify by doing: run it, check live state, read the file. Verification is how
- (AGENTS.md) Interactive: push the current branch after commit. Report the hash once.
- (AGENTS.md) Memory is a pointer, not current truth — verify live state before acting.
- (last2w-decisions) D17 — Read code before new machinery: Verify each claim against live code before designing workarounds. Reject new machinery when correcting a config word fixes the problem.
- (last2w-decisions) D18 — No load-bearing unverified assumptions: Unverified assumptions must not become load-bearing architecture.

## Evidence

- (QUERIES.md) 8. Which handoffs document Mac routing decision and cost evidence?
- (QUERIES.md) 12. How does Pi verify peer agents (Hermes/Codex/Claude) in the portfolio triptych with MyAPI + GDDP?
- (QUERIES.md) 15. Path from tools.json registry → router.route → shadow/eval before promotion.
- (BRIEF-DRAFT.md) 7. `/Users/sab-mini/repos/mac-needle/` (dir; checkpoints path only)
- (SOURCES.md) | 12 | `/Users/sab-mini/repos/mac-needle/` | Cactus Needle training package clone; `checkpoints/` (path only) | mini training home |
- (SOURCES.md) HF-related datasets under `~/.pi/agent/data/hf-datasets/functiongemma-*` (path labels only)
- (SOURCES.md) | Full `~/.pi` tree, needle, harness, agent sessions, mac-needle clone | Air clone lag of `.pi` / needle; air Vertex operator path stronger historically |
- (SOURCES.md) | launchd plist path for needle serve | Whether air runs same launchd job |
- (SOURCES.md) Entire graphify-out rebuild of `.pi` (out of scope)
- (AGENTS.md) Pi is his hands: inspect live state, do the work, verify by doing, report

## Connect

- (QUERIES.md) 12. How does Pi verify peer agents (Hermes/Codex/Claude) in the portfolio triptych with MyAPI + GDDP?
- (QUERIES.md) 13. How does `pi-route` / `NEEDLE_URL` connect orchestrator to serve.py daemon?
- (AGENTS.md) concisely — conversationally when interactive, via artifacts in a packet run.
- (AGENTS.md) When Sab signals looping: load the `loop-breaker` skill via read tool, or ask
- (AGENTS.md) Browser automation via Playwright + Chromium, verified surfaces only. Verify


---
# Sources scanned

- `myapi`: `/Users/sab-mini/repos/MyAPI/PROJECT-BRIEF.md`
- `myapi`: `/Users/sab-mini/repos/MyAPI/AGENTS.md`
- `myapi`: `/Users/sab-mini/repos/MyAPI/README.md`
- `myapi`: `/Users/sab-mini/repos/MyAPI/IMPLEMENTATION-PLAN.md`
- `myapi`: `/Users/sab-mini/repos/MyAPI/project-docs/source-of-truth-anchors/khoj-deployment-indexing-anchor.md`
- `myapi`: `/Users/sab-mini/repos/MyAPI/project-docs/source-of-truth-anchors/myapi-status-anchor.md`
- `myapi`: `/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/QUERIES.md`
- `myapi`: `/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/BRIEF-DRAFT.md`
- `myapi`: `/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/myapi/SOURCES.md`
- `myapi`: `/Users/sab-mini/repos/MyAPI/Corpus v1.0/40-decisions-and-trajectories/2026-08-08-last2w-decisions.md`
- `myapi`: `/Users/sab-mini/repos/MyAPI/Corpus v1.0/20-projects/MyAPI/MyAPI Anchor.md`
- `gddp`: `/Users/sab-mini/repos/MyAPI/README.md`
- `gddp`: `/Users/sab-mini/repos/MyAPI/AGENTS.md`
- `gddp`: `/Users/sab-mini/repos/MyAPI/PROJECT-BRIEF.md`
- `gddp`: `/Users/sab-mini/repos/gddp-runtime/README.md`
- `gddp`: `/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/gddp/QUERIES.md`
- `gddp`: `/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/gddp/BRIEF-DRAFT.md`
- `gddp`: `/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/gddp/SOURCES.md`
- `gddp`: `/Users/sab-mini/repos/MyAPI/Corpus v1.0/20-projects/GDDP/GDDP Anchor.md`
- `pi`: `/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/pi-needle-gemma/QUERIES.md`
- `pi`: `/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/pi-needle-gemma/BRIEF-DRAFT.md`
- `pi`: `/Users/sab-mini/repos/MyAPI/scratch/corpus-hot/pi-needle-gemma/SOURCES.md`
- `pi`: `/Users/sab-mini/.pi/agent/AGENTS.md`

---
# Next compress steps (VM-friendly)

1. Keep only notes that bind to a QUERIES bullet.

2. One golden brief per project answering all four categories.

3. Golden keyword frontmatter on those briefs + anchors.

4. Session `#great/#good` → decision lines only → link `git` SHA when known.

5. Eval: run QUERIES against `/query`.
