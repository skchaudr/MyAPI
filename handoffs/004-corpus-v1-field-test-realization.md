# 004 — Corpus v1 field-test realization

Date: 2026-05-05
Branch: main

## Empirical Reality

Scope touched:
- Created `project-docs/corpus-v1-normalization-readiness.md` — corpus v1 readiness and strategy note. Captures that this is now a corpus architecture pass, not a retrieval-weight tweak pass.
- Created `project-docs/corpus-v1-baseline-candidate-queries.md` — 10 candidate v1 benchmark questions grounded in the Solo Developer Vault, with `fair_after` / `corpus_state_required` metadata.
- Created `project-docs/corpus-v1-live-categorization-2026-05-05.md` — first live batch snapshot of the 10 v1 candidate queries against `/query`.
- Started VM `instance-20260418-024637` in `us-central1-a`, project `project-ab32182e-5782-4a9c-939`; endpoint health passed at `http://100.85.100.52:8000/health`.
- Ran the 10-query batch against `/query` and saved top-5 winners in the live categorization note.
- VM-dependent work is complete. Sab planned to shut VM down after the batch.

Current state:
- Git status at checkpoint time: three untracked docs:
  - `project-docs/corpus-v1-baseline-candidate-queries.md`
  - `project-docs/corpus-v1-live-categorization-2026-05-05.md`
  - `project-docs/corpus-v1-normalization-readiness.md`
- No commits made this session.
- Existing handoff numbering continues from `003-final-v0-benchmark-run.md`.

Key project decision:
- The v1 benchmark baseline pivoted away from MyAPI historical questions and toward GDDP / graph-driven development.
- Reason: MyAPI is the active/recent project and did not have fair historical vault evidence until `2026-04-14`, stronger after `2026-04-25`.
- GDDP is fair earlier: observed GDDP anchor/control-plane evidence begins around `2026-03-11` and becomes dense across `2026-03-12` through `2026-03-16`.

Two-audience endpoint framing:
- The API endpoint is for **agents** and **the human operator**.
- Agent-facing use case: cold-start context for Claude Code, Codex, Jules, Pi workers, OpenClaw/GDDP executors. Agents should ask the endpoint what project truth, constraints, status, decisions, and prior work they need before acting.
- Human-facing use case: recall, inspection, synthesis, and judgment over the corpus. Sab asks what he decided, what he worked on, what evidence supports a claim, what thread something happened in, or whether the corpus actually documents something.
- Sources are not audiences. Obsidian, ChatGPT, Claude, Codex, Claude Code are input corpora. The endpoint serves agent action and human recall/judgment.

Benchmark realization:
- The current 10-query benchmark is a useful **lab test**, but not the final proof of endpoint usefulness.
- The real field test has to happen in the field:
  - Fresh cold-start agents, with no memory/handoff beyond “use MyAPI first,” run real tasks against real projects.
  - Human users, including Sab and potentially a few others, ask real questions and judge whether the answers are grounded, useful, and not misleading.
- Lab retrieval can categorize likely issues, but the final arbiter is whether retrieved evidence lets a user or agent do the real job correctly.
- Important correction: do not grade a result as bad just because it is a ChatGPT/Claude conversation instead of an anchor/project doc. If the messy conversation contains the exact answer, it is a pass.
- Healthy v1 routing should let canonical docs win for canonical truth questions and conversations win for thought process, history, or idea-development questions.

Live benchmark batch snapshot:
- Q1 `What is graph-driven development, and what problem is GDDP trying to solve?`
  - Winner: `obsidian-gdd-main-thread-summary.md` (`obsidian`, `0.788`)
  - Preliminary read: useful top hit; noisy ChatGPT neighbors.
- Q2 `How does GDDP turn events into bounded agent work without letting executors freestyle?`
  - Winner: `chatgpt-gdd-vs-agent-orchestration.md` (`chatgpt`, `0.707`)
  - Preliminary read corrected to unresolved. It may be a pass if the thread contains the concrete GDDP pipeline/contract.
- Q3 vault schema history
  - Winner: `claude-web-converting-opclaw-to-final-system-repo.md` (`claude`, `0.681`)
- Q4 OpenClaw recommendation
  - Winner: `obsidian-cline-vs-openclaw-similarities-and-differences.md` (`obsidian`, `0.942`)
- Q5 April 27 topics/goals
  - Winner: `claude-web-integrating-claude-code-with-obsidian-vault.md` (`claude`, `0.590`)
- Q6 Mac/Big Pi/Small Pi roles
  - Winner: `chatgpt-bot-identity-and-setup.md` (`chatgpt`, `0.842`)
- Q7 post-UCSC arc
  - Winner: `chatgpt-career-coaching-plan.md` (`chatgpt`, `0.469`)
- Q8 Jules task shaping
  - Winner: `claude-web-orchestration-mvp-tuning-and-scope-expansion.md` (`claude`, `0.978`)
- Q9 Neovim friction log
  - Winner: `chatgpt-neovim-time-saversinks-rules.md` (`chatgpt`, `0.714`)
- Q10 inspect Claude/Codex session
  - Winner: `claude-local-command-caveatcaveat-the-messages-below-were-generated-389c7e7b.md` (`claude-code`, `0.706`)

Critical grading rule going forward:
- Content-first, source-second.
- For each query, inspect the retrieved evidence and ask: can a correct, grounded answer be produced from this?
- Grade as:
  - `pass`
  - `partial`
  - `fail`
  - `unfair_question`
  - `needs_more_context`
- Then record why, including whether the problem is query wording, missing evidence, stale source, meta/source mismatch, or corpus metadata gap.

Implication for corpus v1 normalization:
- Do not normalize toward “anchors always win.”
- Normalize toward honest routing:
  - canonical project docs/anchors should win for source-of-truth and operational-contract questions;
  - conversations should win when the question asks for development history, thought process, comparisons, or what Sab was thinking;
  - artifact summaries should represent high-signal conversations so raw thread noise does not have to carry every answer;
  - null/no-evidence answers must count as valid when the corpus lacks documentation.

Resume point:
- Sab fills the second half of this handoff.
- Then begin corpus v1 normalization from the preserved realization above.
- First practical next step: classify the 10 live batch results by reading enough evidence to decide content quality, not just source type.
- Second practical next step: implement/extend normalization around `source_type`, `work_type`, `temporal_mode`, conversation `thread_type`, `primary_project`, `outcome`, `signal_strength`, and `review_status`.
- Keep VM off unless another live endpoint run is required. The captured batch is enough for offline analysis.

## Narrative / Trajectory

Intent:  Get a feel for where our RAG engine was weak and where to focus our V1 corpus normalization 

Interpretation: Meta commentary and meta conversations around the questions we are asking are showing up but that doesn't necessarily mean that they are not fully answering the question that was being asked. That is why earlier when we were given the opportunity to specify what document records this specific information rather than asking about the specific information, so honestly I think it did fairly well 

Tension: All of that being said, there is going to be benefit from canonical documents and source of truth paper trails but I think that we shouldn't invent authority. We shouldn't reinvent history. We shouldn't recreate or fabricate episodic history 

Momentum: I'm unsure where we're going. It might be the right move to do this corpus normalization so that we can all just have a cleaner baseline and keep moving closer towards reliability 

### Per Sab Instructions: Codex Sitrep Post README And Repo Going Live

The question captured here was not "what should the public onboarding eventually become?" It was: what is actually true in the repo right now if someone grabs it and tries to use their own exported ChatGPT or Claude conversation data?

Current reality: extraction is mostly programmatic. `ingest_all.py` can take a ChatGPT export zip or `conversations.json` and a Claude.ai conversation export zip, run source adapters, reconstruct readable conversations, stamp basic YAML metadata, default imported chats to `scratchpad` / `conversation`, and write one markdown file per thread into a Khoj-ready bundle. That gets a user from raw export to searchable scratchpad corpus without hand-extracting messages.

Current limitations: the hand/judgment layer is still significant. The repo does not yet automatically decide which threads are important, assign meaningful project taxonomy for generic ChatGPT or Claude web exports, create artifact summaries, filter sensitive/private material, dedupe repeated exports robustly, split long threads into smaller topic docs, promote raw chats into trusted memory, or add the corpus-v1 routing fields. The honest split is: searchability is automated; authority and curation are mostly manual.

What should exists as direction, not current state. Public users should eventually upload an export, get immediate low-trust search, then curate high-signal threads incrementally through a review queue: exclude/private, summarize, assign project, mark outcome, promote, and choose whether the raw thread ranks normally, is downweighted, or is retained mainly for provenance.

First corpus-v1 normalization steps from here: define shared metadata fields (`source_type`, `work_type`, `temporal_mode`, plus conversation fields like `thread_type`, `primary_project`, `outcome`, `signal_strength`, `artifact_summary`, `raw_thread_weight`, and `review_status`); build a dry-run scanner/manifest for ChatGPT, Claude, Claude Code, Codex, and Obsidian inputs; add an inspect/review command for one conversation at a time; generate artifact-summary templates for high-signal threads; and only after that wire retrieval weights so canonical docs win for source-of-truth questions while conversations still win for history/thought-process questions.

Recent Git history is intentionally not part of the technical evidence for this assessment. The analysis is based on repo behavior and code paths, not portfolio cleanup or public-release hygiene.

### Per Sab Instructions: Claude Code Sitrep Post README And Repo Going Live

The question for this section, parallel to Codex's: what is actually true *right now* about the orchestration layer that just shipped MyAPI's public README — not what it should eventually become.

The dispatch loop is real and end-to-end-verified on real work this session. The MyAPI README finalize batch (10 mechanical edits, the Author rewrite, LICENSE creation, PR #29 opened on `chore/readme-finalize`) all rode the same path: operator types intent → `pi-intake` drafts a packet YAML → schema-validate plus `pi-packet validate` gate → dispatch executes → `pi-verify-run` reads the artifact dir and surfaces structured pass/fail evidence → operator reviews diff. The PR exists, the LICENSE exists at repo root, the canonical A1/A7 paragraph reconciles three contradictory claims into one. That is real work, not a synthetic demo.

Cross-machine reads from Big Pi to Mac via SSH (`saboor@saboors-macbook-air`) are verified working. Earlier this session, Pi made 41 SSH calls into the Mac to analyze gddp-runtime/config and produce a 132-line strategic recommendation. The same primitive can read MyAPI sources for future agent-context-layer work without any new orchestration code.

Pi's default routing flipped from OpenRouter to Codex Subscription (`gpt-5.5` via `openai-codex`), removing per-token cost on typical dispatches. Required `SESSION_TAGGER_DISABLE=1` because the `session_id` field that `session-tagger.ts` injects into the provider request payload is strict-rejected by the Codex API. Smoke-noop verified the loop end-to-end after the toggle. The cost-tracker output reports nonzero "cost" on Codex Subscription runs — that is theoretical (API-platform rates applied retroactively to flat-rate traffic), not actual. Future fix: provider-aware billing model in `cost-tracker.ts`.

What still requires operator hands at the orchestration layer: `pi-intake`'s drafter occasionally produces packets that need polish — YAML colon-as-dict parsing edge cases, a `$ARTIFACT_DIR` literal-write bug where the drafter wrote to a literal-name `$ARTIFACT_DIR/` directory under cwd instead of resolving the env var at write time, and a `mutations=false` with `bash`-in-`tools` mismatch that the JSON schema does not enforce but `pi-packet validate` does. Each was caught at a validation gate before dispatch this session — the review step is real, not ceremonial. `pi-verify-run`'s `declared_deliverables_exist` check incorrectly parses verification-command strings for paths and produces false-positive warnings on grep-for-absence patterns; cosmetic, but worth tightening.

Implication for MyAPI as an agent-context-layer customer: both halves of the interaction model already exist. Dispatch — any agent can call `/query` and get reranked evidence with metadata. Verification — Pi's verifier primitive is agent-agnostic; could be Pi, Claude Code, Codex, or any future runtime that can read an artifact directory and emit structured findings. When corpus v1 lands and an orchestrator agent asks MyAPI for cold-start context on a project before walking the code, that path is wired end-to-end. The README that just shipped frames MyAPI for exactly this audience (`/query` returning structured JSON for agents; two-audience explicit; agent cold-start as a first-class use case).

What this session did not touch: MyAPI's corpus-v1 pipeline itself. Ingestion, classification, anchor-authoring, and metadata work remain operator-side per Codex's section above. The acceptance harness state was not re-measured against the live VM; the README cites handoff 003's last numeric claim (6/7 mechanical, A1 known-fail, A7 active investigation). The `myapi-status-anchor.md` that closes A7's subject-scope gap remains the operator's top-of-queue per `STATUS_AND_NEXT_STEPS.md`. Pi's role across this batch was orchestration around MyAPI, not inside it. The only direct mutation to MyAPI from this session is the README finalize commit on PR #29, which is awaiting operator merge.
