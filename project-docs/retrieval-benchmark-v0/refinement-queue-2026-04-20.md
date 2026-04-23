# Benchmark-Driven Refinement Queue

Source benchmark: `project-docs/retrieval-benchmark-v0/Harness evaluation/run-2026-04-19-daily-note-penalty.md`

Purpose: convert retrieval benchmark misses into a small owner-pass queue for source-of-truth anchor notes.

Operating loop:

1. Normalize deterministic metadata.
2. Owner/refiner writes or strengthens the target anchor.
3. Reindex Khoj.
4. Rerun the same benchmark.
5. Compare whether the anchor now wins.

## Anchor Targets

### Q1: What is My_DevInfra?

- Intent: `project_overview`
- Desired anchor: `my-devinfra-system-anchor.md`
- Problem: Project identity still depends on a mix of one useful Obsidian note and raw Claude evidence.
- Owner action: Create or strengthen the canonical My_DevInfra identity note with current scope, components, and source evidence.
- Benchmark goal: The My_DevInfra anchor should appear in the top 3 and raw dumps should sit below it.
- Current top results: obsidian:obsidian-usr-anchor.md, claude-code:claude-local-command-caveatcaveat-the-messages-below-were-generated-6d8ab6da.md, obsidian:obsidian-identity.md, obsidian:obsidian-talon-voice-control-for-coding-neovim.md, obsidian:obsidian-writing-in-your-own-words-is-the-real-second-brain.md

Owner-pass notes:

- 

### Q7: What was I learning about retrieval systems?

- Intent: `synthesis`
- Desired anchor: `retrieval-rag-learning-anchor.md`
- Problem: Retrieval-learning queries surface plausible ChatGPT notes, but no synthesized learning anchor clearly wins.
- Owner action: Create a concise retrieval/RAG learning anchor that names embeddings, indexing, RAG, reranking, and benchmark lessons.
- Benchmark goal: The retrieval/RAG anchor should appear in the top 3 for retrieval-learning questions.
- Current top results: chatgpt:chatgpt-web-stack-and-bun-overview.md, chatgpt:chatgpt-gdad-summary-main-thread.md, obsidian:obsidian-evaluating-the-johnny-decimal-project-management-system.md, chatgpt:chatgpt-llamaindex-overview.md, chatgpt:chatgpt-blog-posts-for-dev-portfolio.md

Owner-pass notes:

- 

### Q8: What did I decide about the vault schema?

- Intent: `decision`
- Desired anchor: `obsidian-vault-schema-anchor.md`
- Problem: Vault-schema decisions are scattered across ChatGPT and Obsidian notes.
- Owner action: Create a vault schema decision anchor with folder logic, frontmatter rules, note kinds, and current tradeoffs.
- Benchmark goal: The schema anchor should appear in the top 3 for vault-schema decision queries.
- Current top results: chatgpt:chatgpt-llamaindex-overview.md, chatgpt:chatgpt-dispatch-pipeline-handoff.md, chatgpt:chatgpt-system-architecture-overview.md, chatgpt:chatgpt-gdad-summary-main-thread.md, chatgpt:chatgpt-claude-co-work-overview.md

Owner-pass notes:

- 

### Q10: What notes mention Khoj deployment or indexing?

- Intent: `operational`
- Desired anchor: `khoj-deployment-indexing-anchor.md`
- Problem: Khoj deployment/indexing queries are still won by raw operational logs.
- Owner action: Create a Khoj deployment/indexing anchor with VM, data disk, service, reindex, and verification state.
- Benchmark goal: The Khoj anchor should appear above Claude/Codex raw logs for operational indexing queries.
- Current top results: claude-code:claude-local-command-caveatcaveat-the-messages-below-were-generated-a476a891.md, codex:codex-looking-at-the-handoff-doc-can-you-help-me-configure-why-the-019d73f6.md, obsidian:obsidian-20260412.md

Owner-pass notes:

- 

### Q12: What is the status of the API deployment?

- Intent: `operational`
- Desired anchor: `api-deployment-status-anchor.md`
- Problem: API deployment status is partly answered by system-status briefing, but raw logs still dominate.
- Owner action: Create or refine the current API deployment status anchor with service paths, health checks, and known failure modes.
- Benchmark goal: The API status anchor should appear in the top 3 and answer the status question directly.
- Current top results: claude-code:claude-local-command-caveatcaveat-the-messages-below-were-generated-2a98a9e1.md, obsidian:obsidian-system-status-briefing.md, claude-code:claude-local-command-caveatcaveat-the-messages-below-were-generated-a476a891.md, codex:codex-looking-at-the-handoff-doc-can-you-help-me-configure-why-the-019d73f6.md, obsidian:obsidian-20260412.md

Owner-pass notes:

- 

### Q16: What notes are tied to Tailscale, SSH, or VM access?

- Intent: `operational`
- Desired anchor: `vm-tailscale-ssh-access-anchor.md`
- Problem: VM/Tailscale/SSH access queries surface raw command sessions instead of an access runbook.
- Owner action: Create a VM access anchor with Tailscale IPs, gcloud SSH syntax, service checks, disk layout, and recovery notes.
- Benchmark goal: The VM access anchor should appear above raw command logs for Tailscale, SSH, and VM access queries.
- Current top results: claude-code:claude-local-command-caveatcaveat-the-messages-below-were-generated-a476a891.md, chatgpt:chatgpt-antigravity-remote-dev-usage.md, codex:codex-looking-at-the-handoff-doc-can-you-help-me-configure-why-the-019d73f6.md, obsidian:obsidian-20260412.md

Owner-pass notes:

- 

### Q18: What docs should I use to understand the current system end to end?

- Intent: `synthesis`
- Desired anchor: `current-system-end-to-end-anchor.md`
- Problem: End-to-end system understanding lacks one canonical overview result.
- Owner action: Create a system overview anchor that connects MyAPI, Context Refinery, Khoj, Obsidian corpus, benchmark loop, and VM runtime.
- Benchmark goal: The system overview anchor should appear in the top 3 for end-to-end docs queries.
- Current top results: chatgpt:chatgpt-dispatch-pipeline-handoff.md, chatgpt:chatgpt-opencode-overview.md, chatgpt:chatgpt-dashboard-setup-guide.md, chatgpt:chatgpt-walletconnect-resolv-overview.md, claude:claude-web-task-system-integration-handoff-document.md

Owner-pass notes:

- 

## Batch Normalizer Scope

Safe deterministic fields:

- `title`
- `aliases`
- `source`
- `document_kind`
- `type`
- `status`
- `projects`
- `tags`
- `created`
- `modified`
- `benchmark_targets`

Owner-controlled fields:

- `summary`
- `decisions`
- `failure_modes`
- `source_evidence`
- `related`

## First Pilot Batch

- `my-devinfra-system-anchor.md`
- `khoj-deployment-indexing-anchor.md`
- `vm-tailscale-ssh-access-anchor.md`
