---
title: Corpus v1 baseline candidate queries
status: owner-revised-draft
projects: [gddp, corpus-v1, context-refinery]
tags: [benchmark, corpus, eval, obsidian]
date: 2026-05-05
references_events:
  - project-docs/corpus-v1-normalization-readiness.md
---

# Corpus v1 baseline candidate queries

Source pass: `/home/sab-ssd/obsidian/SoloDeveloper`

Admission rule: every query below is either grounded in observed vault notes or is a realistic user/agent question where absence of evidence should be handled explicitly.

Owner feedback applied:

- Replaced MyAPI cold-start and system-overview questions with GDDP questions, because MyAPI is too recent in the vault to be a fair historical baseline.
- Added GDDP definition and bounded-execution questions grounded in March 2026 project notes.
- Removed the retrieval-failure-mode query as not good.
- Replaced vault-schema-decision query with a concrete schema-count/history query.
- Replaced CLI-session query with an OpenClaw recommendation query.
- Narrowed the April 27 query to topics/goals, not active-thread inventory.
- Strengthened machine-routing query into a role question.
- Added a post-UCSC episodic career-arc query.
- Carried forward Jules task sizing and Neovim evidence-absence checks to preserve 10 candidates.

## 1. Graph-driven development core concept

```yaml
query: "What is graph-driven development, and what problem is GDDP trying to solve?"
admission_basis: corpus_grounded
expected_answer_type: project_overview
evidence_expectation: documented
fair_after: 2026-03-12
corpus_state_required: GDDP anchor, main thread summary, and v1 graph docs visible in the vault
```

Why this is realistic: this is the first question a clean agent or reviewer would ask before touching GDDP. It tests whether retrieval understands the project as a methodology and architecture, not just a folder name or generic graph idea.

Evidence:

- `/home/sab-ssd/obsidian/SoloDeveloper/01 Projects/GDDP/GDD - agentic or autonomous dispatch pipeline anchor.md:13` through `:19` defines the objective as an autonomous software developer pipeline using graph nodes as source of project truth, with time, security, and scope limits as non-negotiables.
- `/home/sab-ssd/obsidian/SoloDeveloper/01 Projects/GDDP/GDD Main Thread Summary.md:38` through `:53` distinguishes Graph-Driven Development from Graph-Driven Agentic Development.
- `/home/sab-ssd/obsidian/SoloDeveloper/01 Projects/GDDP/GDD Main Thread Summary.md:190` through `:208` defines GDD as project progress driven by a structured capability graph, where agents move nodes through blocked, ready, running, and complete states.
- `/home/sab-ssd/obsidian/SoloDeveloper/01 Projects/GDDP/GDD-Control-Center/docs/v1/10-project-graph.md:13` says the graph keeps OpenClaw from inventing the project.
- `/home/sab-ssd/obsidian/SoloDeveloper/01 Projects/GDDP/GDD-Control-Center/docs/three-layer-model.md:17` through `:39` defines the blueprint, graph, and execution layers.

Expected benchmark behavior: answer should say GDDP makes the graph the source of project truth. Humans author capabilities, dependencies, boundaries, acceptance conditions, and priorities; agents perform bounded execution against ready graph nodes. The answer should not collapse GDDP into a generic graph database, ticket tracker, or vague agent workflow.

## 2. Bounded GDDP execution

```yaml
query: "How does GDDP turn events into bounded agent work without letting executors freestyle?"
admission_basis: corpus_grounded
expected_answer_type: operational_architecture
evidence_expectation: documented
fair_after: 2026-03-12
corpus_state_required: GDDP v1 pipeline, project graph, roadmap, and review-checkpoint docs visible in the vault
```

Why this is realistic: this is a practical "how" RAG question. An agent deciding whether to dispatch work needs to understand the actual control loop, not just retrieve a definition.

Evidence:

- `/home/sab-ssd/obsidian/SoloDeveloper/01 Projects/GDDP/GDD-Control-Center/docs/v1/00-pipeline-overview.md:15` through `:32` describes the full loop from GitHub event through normalization, classification, scope check, job creation, executor choice, validation, artifacts, and graph/GitHub update.
- `/home/sab-ssd/obsidian/SoloDeveloper/01 Projects/GDDP/GDD-Control-Center/docs/v1/00-pipeline-overview.md:34` through `:35` states the critical invariant that webhook payloads never directly trigger execution.
- `/home/sab-ssd/obsidian/SoloDeveloper/01 Projects/GDDP/GDD-Control-Center/docs/v1/10-project-graph.md:25` through `:30` lists what OpenClaw decides after the human-authored graph constrains the project.
- `/home/sab-ssd/obsidian/SoloDeveloper/01 Projects/GDDP/GDD-Control-Center/docs/v1/10-project-graph.md:57` through `:75` shows acceptance criteria, constraints, allowed execution modes, and required artifacts inside a node schema.
- `/home/sab-ssd/obsidian/SoloDeveloper/01 Projects/GDDP/GDD-Control-Center/docs/roadmap.md:13` through `:17` defines the graph-driven control system and safety rule.
- `/home/sab-ssd/obsidian/SoloDeveloper/01 Projects/GDDP/GDD-Control-Center/docs/roadmap.md:173` through `:177` states the invariant that no executor freestyles and every action traces back to a node.

Expected benchmark behavior: answer should describe a contract-bound pipeline: events are normalized, classified, checked against the project graph, turned into jobs, routed to allowed executors, validated against node acceptance criteria, and recorded as artifacts before graph state advances. It should explicitly mention the anti-freestyle invariant.

Live v0 smoke observation from `2026-05-05`:

```yaml
actual_winner: chatgpt-gdd-vs-agent-orchestration.md
failure_mode: meta-eclipse
why_winner_won: adjacent conversation language about bounded autonomy outranked direct GDDP pipeline and roadmap docs
metadata_that_would_fix_routing: boost source_type=project_doc and work_type=project_work for operational_architecture queries; downweight raw conversation unless the query asks for conversation provenance
```

## 3. Vault schema history

```yaml
query: "How many vault schemas have I gone through, and what changed between them?"
admission_basis: corpus_grounded
expected_answer_type: historical_synthesis
evidence_expectation: documented
fair_after: 2026-04-26
corpus_state_required: V2, V3, and V4 schema notes visible in the vault
```

Why this is realistic: this tests whether retrieval can summarize a real evolution across related schema notes instead of returning only the latest reference.

Evidence:

- `/home/sab-ssd/obsidian/SoloDeveloper/09 Utilities/_Vault System/VLT_ Vault Schema V2.md:19` names Vault Schema V2 as finalized.
- `/home/sab-ssd/obsidian/SoloDeveloper/00 Inbox/vlt_ Vault Schema V3 -- introduces Concepts.md:17` names Formalized Schema V3.
- `/home/sab-ssd/obsidian/SoloDeveloper/00 Inbox/vlt_ Vault Schema V3 -- introduces Concepts.md:98` through `:111` shows V3 introducing concepts as the graph layer.
- `/home/sab-ssd/obsidian/SoloDeveloper/09 Utilities/_Vault System/_V4_Vault_Schema_ .md:14` names Vault Schema V4.
- `/home/sab-ssd/obsidian/SoloDeveloper/09 Utilities/_Vault System/_V4_Vault_Schema_ .md:21` through `:27` defines V4's three-layer mental model.
- `/home/sab-ssd/obsidian/SoloDeveloper/09 Utilities/_Vault System/Vault Schema V4 Reference.md:19` through `:21` gives the V4 core principle.

Expected benchmark behavior: answer should likely identify at least V2, V3, and V4 from the evidence, while admitting if V1 is not clearly documented in the sampled corpus.

## 4. OpenClaw recommendation

```yaml
query: "Based on my Obsidian notes, would Saboor recommend OpenClaw as a tool, or is the evidence more mixed?"
admission_basis: corpus_grounded
expected_answer_type: judgment_from_evidence
evidence_expectation: documented
fair_after: 2026-03-02
corpus_state_required: OpenClaw struggle/recovery notes plus known-good state available
```

Why this is realistic: this is a personal recommendation question that requires weighing positive strategic fit against operational pain.

Evidence:

- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/OpenClaw 2026- Updates.md:20` describes OpenClaw as a universal AI agent gateway.
- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/OpenClaw 2026- Updates.md:22` says it is highly relevant to Saboor's multi-device, multi-agent setup.
- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/OpenClaw 2026- Updates.md:92` through `:104` proposes an accountability/coding-assistant architecture and says it is doable with the current setup.
- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/OpenClaw 2026- Updates.md:123` says the accountability workflow is worth prototyping.
- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/Developer Infrastructure/OpenClaw/OpenClaw broke again, exhaustion from running the same loop trying to fix it.md:24` through `:33` lists failure modes.
- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/Developer Infrastructure/OpenClaw/OpenClaw broke again, exhaustion from running the same loop trying to fix it.md:202` captures frustration after config hardening broke things further.
- `/home/sab-ssd/obsidian/SoloDeveloper/09 Utilities/Reports/OpenClaw_Known_Good_State.md:7` through `:10` records a later verified connected known-good state.

Expected benchmark behavior: the answer should be mixed. Saboor appears interested and invested for his own infra, but the notes do not support a blanket recommendation without caveats around reliability, config complexity, and operator burden.

## 5. Recent topics and goals

```yaml
query: "What topics and goals was I working on around April 27?"
admission_basis: corpus_grounded
expected_answer_type: temporal_synthesis
evidence_expectation: documented
fair_after: 2026-04-27
corpus_state_required: sprint-goal and active-session notes available
```

Why this is realistic: this is the practical form of "what was I working on then?" without forcing a specific active-thread inventory.

Evidence:

- `/home/sab-ssd/obsidian/SoloDeveloper/01 Projects/one-month-launchpad/Active Sessions for 2026 Apri Career Sprint.md:31` through `:39` lists session topics around April 23-27.
- `/home/sab-ssd/obsidian/SoloDeveloper/01 Projects/one-month-launchpad/Active Sessions for 2026 Apri Career Sprint.md:46` through `:52` lists themes still in play: Bailey site, Vault V4, dotfiles, and Neovim.
- `/home/sab-ssd/obsidian/SoloDeveloper/00 Inbox/sprint-goal.md:28` says the sprint goal was to ship MyAPI, ship GDDP, document both, broadcast both, and maintain Bailey.
- `/home/sab-ssd/obsidian/SoloDeveloper/00 Inbox/sprint-goal.md:144` through `:150` gives weekly targets across MyAPI, GDDP, Bailey, portfolio, LinkedIn, and retrospective work.

## 6. Mac, Big Pi, and Small Pi roles

```yaml
query: "What roles do Saboor's Mac, Big Pi, and Small Pi play in his developer infrastructure?"
admission_basis: corpus_grounded
expected_answer_type: operational_architecture
evidence_expectation: documented
fair_after: 2026-02-28
corpus_state_required: job-class matrix and execution topology notes available
```

Why this is realistic: an agent needs this before dispatching work or proposing background execution.

Evidence:

- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/Developer Infrastructure/Job Class Matrix (Mac + Big Pi + Small Pi).md:13` through `:18` maps job classes to Mac, Small Pi, Big Pi, or explicit approval.
- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/Developer Infrastructure/Job Class Matrix (Mac + Big Pi + Small Pi).md:20` through `:25` lists routing rules.
- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/Developer Infrastructure/OpenClaw/EXECUTION_TOPOLOGY_V1.md:24` through `:41` describes the MacBook Air as control plane and personal knowledge hub.
- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/Developer Infrastructure/OpenClaw/EXECUTION_TOPOLOGY_V1.md:45` through `:62` describes Big Pi as stable always-on automation node.
- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/Developer Infrastructure/OpenClaw/EXECUTION_TOPOLOGY_V1.md:66` through `:77` describes Small Pi as experimental/test node.
- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/Developer Infrastructure/OpenClaw/OpenClaw broke again, exhaustion from running the same loop trying to fix it.md:65` through `:80` also frames Big Pi as brain, Mac as hands, and Small Pi as edge.

## 7. Post-UCSC episodic arc

```yaml
query: "How has Saboor's arc as a recent UCSC graduate developed episodically since graduation?"
admission_basis: corpus_grounded
expected_answer_type: episodic_synthesis
evidence_expectation: documented
fair_after: 2026-05-01
corpus_state_required: profile/career identity, sprint, portfolio, and weekly job-target evidence available
```

Why this is realistic: this is a high-level personal/career synthesis question that a human might ask when preparing a portfolio, interview narrative, or career positioning note.

Evidence:

- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/Global Claude.md:120` through `:124` identifies Saboor as a recent UCSC CS graduate focused on software engineering, agentic AI usage, infrastructure, and data engineering.
- `/home/sab-ssd/obsidian/SoloDeveloper/09 Utilities/Reports/PR_feat-portfolio-content-update_Decision.md:51` through `:62` frames his portfolio identity as a UCSC CS grad building AI-orchestrated systems from physical constraints and turning adaptation into methodology.
- `/home/sab-ssd/obsidian/SoloDeveloper/00 Inbox/sprint-goal.md:28` through `:31` shows a concrete shipping-and-broadcast career sprint posture.
- `/home/sab-ssd/obsidian/SoloDeveloper/01 Projects/Portfolio/LinkedIn Sprint V2 for 2026 is arc-defining.md:15` through `:25` ties outreach to having real projects and portfolio proof first.
- `/home/sab-ssd/obsidian/SoloDeveloper/04 Periodic/01 Weeklys/2026-W18.md:246` through `:287` shows the career target narrowing toward agentic runtime, AI infra, semantic search, data infrastructure, and early-career AI/product roles.
- `/home/sab-ssd/obsidian/SoloDeveloper/04 Periodic/01 Weeklys/2026-W18.md:318` through `:343` continues that target list with AI-native startups, NVIDIA AI infrastructure, and Anthropic inference/RL roles.

Expected benchmark behavior: answer should be episodic, not just biographical. It should connect graduation identity, physical constraints, agentic-development methodology, shipping artifacts, portfolio/LinkedIn readiness, and AI-infra/new-grad job targeting.

## 8. Jules task sizing

```yaml
query: "How should I shape Jules tasks now that the gate works?"
admission_basis: corpus_grounded
expected_answer_type: decision_plus_guidance
evidence_expectation: documented
fair_after: 2026-04-14
corpus_state_required: Jules/OpenClaw task-sizing note available after normalization
```

Why this is realistic: this is a high-value agent-orchestration question before dispatching background coding tasks.

Evidence:

- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/Developer Infrastructure/MVP-Finetuning-OC-Jules-loop-with-Claude-and-ChatGPT-input.md:74` through `:82` says the gate works and the task model should shift from tiny diffs to validated deliverables.
- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/Developer Infrastructure/MVP-Finetuning-OC-Jules-loop-with-Claude-and-ChatGPT-input.md:84` through `:94` recommends feature-sized tasks, test coverage, and richer task prompts.

## 9. Neovim friction evidence check

```yaml
query: "Have I actually documented recurring Neovim friction, or is the friction log still only planned?"
admission_basis: realistic_user_or_agent_question
expected_answer_type: evidence_absence_check
evidence_expectation: intentionally_unknown
fair_after: 2026-04-27
corpus_state_required: sprint-goal and active-session notes available; dedicated friction log may be absent
```

Why this is realistic: this is the corrected benchmark shape. It should not assume the friction log exists.

Evidence:

- `/home/sab-ssd/obsidian/SoloDeveloper/00 Inbox/sprint-goal.md:130` lists `Neovim Friction Log` as a planned capture during real sessions.
- `/home/sab-ssd/obsidian/SoloDeveloper/01 Projects/one-month-launchpad/Active Sessions for 2026 Apri Career Sprint.md:51` says Neovim config is not yet locked and a dedicated session is pending.

Expected benchmark behavior: returning only setup/tutorial notes would be a weak or wrong answer unless the system clearly says no dedicated recurring-friction log was found.

## 10. CLI session evidence

```yaml
query: "How do I inspect what Claude or Codex actually did in a session?"
admission_basis: corpus_grounded
expected_answer_type: operational_recall
evidence_expectation: documented
fair_after: 2026-04-14
corpus_state_required: CLI log-history/hook notes available in the vault
```

Why this is realistic: this is exactly what an agent or human asks when checking whether a session changed code, ran commands, or produced an artifact.

Evidence:

- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/Exports/CLI/Codex and Claude log history + hooks.md:8` through `:15` explains Claude hook logging versus Codex wrapper reconstruction.
- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/Exports/CLI/Codex and Claude log history + hooks.md:124` through `:157` lists practical uses and example questions for Claude and Codex artifacts.
- `/home/sab-ssd/obsidian/SoloDeveloper/02 Areas/Exports/CLI/Codex and Claude log history + hooks.md:203` through `:221` says both systems end in queryable structured logs, readable summaries, per-session directories, and a future-friendly normalization path.

## Initial coverage

These 10 candidates cover:

- graph-driven development definition
- bounded agent execution
- vault schema history
- personal recommendation from mixed evidence
- temporal goals/topics
- developer infrastructure roles
- episodic career arc
- agent task sizing
- evidence-absence checking
- CLI session provenance
