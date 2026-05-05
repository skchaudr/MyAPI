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

