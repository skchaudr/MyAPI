---
title: Corpus v1 live categorization run - 2026-05-05
status: in-progress
projects: [gddp, corpus-v1, context-refinery]
tags: [benchmark, corpus, eval, retrieval-run]
date: 2026-05-05
endpoint: http://100.85.100.52:8000/query
references_events:
  - project-docs/corpus-v1-baseline-candidate-queries.md
  - project-docs/corpus-v1-normalization-readiness.md
---

# Corpus v1 live categorization run - 2026-05-05

Purpose: categorize live retrieval behavior for the new v1 benchmark candidates. This run is diagnostic, not a scored regression run.

## Category labels

- `good_hit`: expected evidence appears in the winner set.
- `good_hit_with_noise`: top answer is useful, but nearby results reveal routing weakness.
- `meta_eclipse`: conversation/meta commentary outranks canonical source/project docs.
- `stale_or_broad_doc_win`: broad or stale summary outranks a sharper source.
- `evidence_absence`: correct behavior should explicitly report missing or weak evidence.
- `needs_owner_judgment`: retrieval is plausible but quality/reliability depends on owner interpretation.

## Q1 - Graph-driven development core concept

```yaml
query: "What is graph-driven development, and what problem is GDDP trying to solve?"
category: good_hit_with_noise
actual_winner: obsidian-gdd-main-thread-summary.md
winner_source: obsidian
winner_score: 0.788
expected_answer_type: project_overview
```

Top result was useful and directly on-topic. The result says the graph is the source of truth, not the agent, which is central to the expected answer.

Issue: ChatGPT conversation chunks occupied most of the remaining top results, including adjacent/meta discussions about Ace Graphs and generic GDD comparisons. That is not fatal for this query, but it shows raw conversations remain too competitive.

Metadata that would improve routing:

- Boost `source_type=anchor` and `source_type=project_doc` for project overview queries.
- Keep high-signal artifact summaries from conversations eligible, but downweight raw conversation chunks.
- Assign `primary_project=gddp` and `work_type=project_work` to the GDDP anchor/control-plane docs.

## Q2 - Bounded GDDP execution

```yaml
query: "How does GDDP turn events into bounded agent work without letting executors freestyle?"
category: unresolved_needs_content_review
actual_winner: chatgpt-gdd-vs-agent-orchestration.md
winner_source: chatgpt
winner_score: 0.707
expected_answer_type: operational_architecture
```

Provisional read: do not grade this as pass or fail until the full winning thread is inspected or the generated answer quality is reviewed.

What is known from the returned snippet: the winning thread appears to be a ChatGPT conversation titled `GDD vs Agent Orchestration`, dated `2026-03-21`, where Saboor asks how similar another agent-orchestration setup is to GDD. The snippet discusses overlap around multi-agent setup, persistent memory, human approval, containerized agents, MCP tools, bounded autonomy, memory, tool access, and supervision.

Why it may be relevant: it is probably a comparative/explanatory thread about how GDD relates to broader agent orchestration patterns, and it may contain the concrete pipeline/contract answer.

Why it may still be the wrong winner: the query asks how GDDP turns events into bounded agent work. That expected answer has direct project-doc evidence in pipeline, graph contract, job schema, and roadmap docs. A comparison thread may be useful supporting context, but it may not be the canonical operating contract.

Grading rule:

- If this thread directly explains the concrete GDDP mechanism, mark `good_hit`.
- If it explains the mechanism conceptually but omits the event-to-job-to-artifact contract, mark `partial_hit`.
- If it only discusses adjacent agent-orchestration ideas, mark `meta_eclipse`.

Metadata that would fix routing:

- For `expected_answer_type=operational_architecture`, boost `source_type=project_doc`, `source_type=anchor`, and `work_type=project_work`.
- Downweight `source_type=conversation` unless query intent asks for conversation, transcript, provenance, or personal thinking.
- Add artifact summaries for high-signal GDDP conversations so extracted decisions can compete without raw thread noise.
- Mark GDDP docs under `GDD-Control-Center/docs/v1/` as `source_type=project_doc`, `temporal_mode=meta`, `primary_project=gddp`, `signal_strength=high`.

Owner question: does this thread contain the actual concrete GDDP pipeline/contract answer, or only an adjacent comparison?

## Batch run snapshot

This snapshot captures the top retrieved files from the first 10-query v1 batch. It is intentionally not fully graded yet.

### Q1

Query: `What is graph-driven development, and what problem is GDDP trying to solve?`

Top results:

1. `obsidian-gdd-main-thread-summary.md` — `obsidian` — `0.788`
2. `chatgpt-ace-graphs-connected.md` — `chatgpt` — `0.714`
3. `chatgpt-gdad-summary-main-thread.md` — `chatgpt` — `0.693`
4. `chatgpt-ai-system-improvement-failures.md` — `chatgpt` — `0.691`
5. `chatgpt-gdd-vs-agent-orchestration.md` — `chatgpt` — `0.478`

### Q2

Query: `How does GDDP turn events into bounded agent work without letting executors freestyle?`

Top results:

1. `chatgpt-gdd-vs-agent-orchestration.md` — `chatgpt` — `0.707`
2. `chatgpt-project-shift-analysis.md` — `chatgpt` — `0.674`
3. `chatgpt-intelligence-harness-execution-layers.md` — `chatgpt` — `0.294`

### Q3

Query: `How many vault schemas have I gone through, and what changed between them?`

Top results:

1. `claude-web-converting-opclaw-to-final-system-repo.md` — `claude` — `0.681`
2. `chatgpt-gdad-summary-main-thread.md` — `chatgpt` — `0.663`
3. `chatgpt-antigravity-remote-dev-usage.md` — `chatgpt` — `0.657`
4. `chatgpt-vault-schema-feedback.md` — `chatgpt` — `0.632`
5. `claude-web-para-system-vault-schema-implementation.md` — `claude` — `0.591`

### Q4

Query: `Based on my Obsidian notes, would Saboor recommend OpenClaw as a tool, or is the evidence more mixed?`

Top results:

1. `obsidian-cline-vs-openclaw-similarities-and-differences.md` — `obsidian` — `0.942`
2. `obsidian-saboor-docs-11-tailored-guides.md` — `obsidian` — `0.939`
3. `obsidian-openclaw-cli-power-user-guide.md` — `obsidian` — `0.939`
4. `obsidian-gdd-openclaw-observed-errors-and-operator-lessons.md` — `obsidian` — `0.937`
5. `chatgpt-merged-jules-wh.md` — `chatgpt` — `0.851`

### Q5

Query: `What topics and goals was I working on around April 27?`

Top results:

1. `claude-web-integrating-claude-code-with-obsidian-vault.md` — `claude` — `0.590`
2. `chatgpt-ai-assisted-development-goals.md` — `chatgpt` — `0.468`
3. `chatgpt-important-3-month-plan.md` — `chatgpt` — `0.456`
4. `chatgpt-accountability-partner-framework.md` — `chatgpt` — `0.454`
5. `chatgpt-project-management-system.md` — `chatgpt` — `0.453`

### Q6

Query: `What roles do Saboor's Mac, Big Pi, and Small Pi play in his developer infrastructure?`

Top results:

1. `chatgpt-bot-identity-and-setup.md` — `chatgpt` — `0.842`
2. `chatgpt-ethernet-vs-wi-fi-pi.md` — `chatgpt` — `0.800`
3. `chatgpt-jules-experiment-insights.md` — `chatgpt` — `0.709`
4. `obsidian-mac-memory-control-playbook-8gb.md` — `obsidian` — `0.692`
5. `chatgpt-merged-jules-wh.md` — `chatgpt` — `0.692`

### Q7

Query: `How has Saboor's arc as a recent UCSC graduate developed episodically since graduation?`

Top results:

1. `chatgpt-career-coaching-plan.md` — `chatgpt` — `0.469`
2. `obsidian-saboor-docs-11-tailored-guides.md` — `obsidian` — `0.442`
3. `obsidian-point-program-meeting-1.md` — `obsidian` — `0.438`
4. `obsidian-vincent-social-interactivity-meeting-2.md` — `obsidian` — `0.434`
5. `obsidian-post-breakup-processing-and-decision-making.md` — `obsidian` — `0.432`

### Q8

Query: `How should I shape Jules tasks now that the gate works?`

Top results:

1. `claude-web-orchestration-mvp-tuning-and-scope-expansion.md` — `claude` — `0.978`
2. `chatgpt-antigravity-remote-dev-usage.md` — `chatgpt` — `0.842`
3. `chatgpt-gdad-summary-main-thread.md` — `chatgpt` — `0.838`
4. `chatgpt-maximizing-ai-task-usage.md` — `chatgpt` — `0.743`
5. `chatgpt-project-shift-analysis.md` — `chatgpt` — `0.652`

### Q9

Query: `Have I actually documented recurring Neovim friction, or is the friction log still only planned?`

Top results:

1. `chatgpt-neovim-time-saversinks-rules.md` — `chatgpt` — `0.714`
2. `chatgpt-neovim-setup-guide-1.md` — `chatgpt` — `0.631`
3. `chatgpt-ai-assisted-development-goals.md` — `chatgpt` — `0.579`
4. `chatgpt-skill-tree-build.md` — `chatgpt` — `0.578`
5. `claude-web-building-a-non-linear-developer-mastery-roadmap.md` — `claude` — `0.578`

### Q10

Query: `How do I inspect what Claude or Codex actually did in a session?`

Top results:

1. `claude-local-command-caveatcaveat-the-messages-below-were-generated-389c7e7b.md` — `claude-code` — `0.706`
2. `chatgpt-claude-workflow-demo.md` — `chatgpt` — `0.692`
3. `chatgpt-ace-graphs-connected.md` — `chatgpt` — `0.668`
4. `chatgpt-merged-jules-wh.md` — `chatgpt` — `0.665`
5. `chatgpt-browser-automation-security.md` — `chatgpt` — `0.661`
