---
title: My_DevInfra System Anchor
aliases:
  - My_DevInfra
  - developer infrastructure
  - personal knowledge system
source: obsidian
document_kind: synthesized_note
type: anchor
status: active
projects:
  - myapi
  - context-refinery
  - my-devinfra
tags:
  - project-identity
  - developer-infrastructure
  - retrieval-anchor
benchmark_targets:
  - retrieval-benchmark-v0/Q1
related:
  - khoj-deployment-indexing-anchor
  - vm-tailscale-ssh-access-anchor
  - current-system-end-to-end-anchor
---

# My_DevInfra System Anchor

## What This Is

My_DevInfra is the personal developer infrastructure that turns raw work — code sessions, conversations, notes, terminal output — into retrievable operational memory. It is not one application. It is the system formed by MyAPI, Context Refinery, Khoj, the Obsidian corpus, the retrieval benchmark, and a GCP VM runtime, all working together in a capture-normalize-index-query-benchmark-refine loop.

This note is the canonical answer to "What is My_DevInfra?"

## Core Components

- **MyAPI** — the application repo (`/Users/saboor/repos/MyAPI`). Contains the Context Refinery service, retrieval pipeline, triage CLI, source adapters, normalization scripts, and benchmark harness.
- **Context Refinery** — FastAPI service (port 8000) that classifies queries, runs hybrid retrieval (Khoj semantic + local keyword), applies document-kind priors, reranks, groups, and returns structured results via `/query`.
- **Khoj** — vector search / RAG backend (port 42110). Indexes the full note corpus (~3,200 docs across Obsidian, ChatGPT, Claude, Codex sources). Context Refinery calls Khoj for semantic search.
- **Obsidian corpus** — the human-owned knowledge layer. Notes follow V4 vault schema with frontmatter (type, status, area, project, concepts, tags). Normalized by batch scripts, judgment fields set by V4 triage CLI.
- **Retrieval benchmark** — 18-query harness (`scripts/run_query_benchmark.py`) covering project identity, temporal recall, source-specific recall, cross-source synthesis, operational recall. Results drive a refinement queue that identifies which anchor notes are missing or weak.
- **VM runtime** — GCP `instance-20260418-024637` (e2-highmem-4, us-central1-a). Persistent `/data` disk. 6-hour auto-shutdown. Runs Khoj and Context Refinery as systemd services.

## Operating Loop

```
capture → normalize → index → query → benchmark → refine
```

1. **Capture**: raw work lands as Obsidian notes, ChatGPT/Claude exports, Codex sessions, CLI transcripts.
2. **Normalize**: batch normalizer (`scripts/normalize_vault_schema_v4.py`) handles structural metadata; V4 triage CLI handles judgment fields (type, project, concepts, tags).
3. **Index**: notes are pushed to Khoj via multipart API (`PUT /api/content` first batch, `PATCH` subsequent).
4. **Query**: Context Refinery `/query` classifies intent, runs hybrid retrieval, applies source-aware and document-kind-aware priors, reranks, returns results.
5. **Benchmark**: 18-query harness measures which notes win for which queries.
6. **Refine**: benchmark misses generate a refinement queue → owner writes or strengthens source-of-truth anchor notes → reindex → rerun benchmark.

## Current State

As of 2026-04-23:

- Pipeline is live and queryable end-to-end on VM.
- Corpus: ~3,200 non-empty docs indexed across 5 source families (obsidian, chatgpt, claude, claude-code, codex).
- Retrieval quality improvements shipped: source-aware ranking priors, document-kind priors (synthesized notes beat raw logs for overview queries), daily note penalty, clickbait filtering.
- V4 triage CLI operational with modular passes (type, status, project, concepts, tags, related, V4 schema validation).
- Benchmark-driven refinement loop in progress: building source-of-truth anchor notes for queries where raw logs currently win.

## Decisions Made

- Retrieval quality is a product metric measured by benchmark, not a subjective feeling.
- Benchmark misses drive refinement work. No unbounded vault passes.
- Canonical anchor notes should win overview/identity/operational queries. Raw Claude/Codex/ChatGPT logs are evidence, not ideal retrieval winners.
- Context Refinery is the orchestration layer; Khoj is the search backend. They are separate concerns on the same VM.
- V4 schema splits work: batch normalizer handles high-confidence structural metadata, CLI handles judgment fields requiring human input.

## Benchmark Relevance

This note targets **Q1: "What is My_DevInfra?"** in the 18-query retrieval benchmark. Before this anchor, Q1 was won by a mix of generic Obsidian notes (`obsidian-usr-anchor.md`, `obsidian-identity.md`) and raw Claude session dumps. This note should appear in the top 3 and provide a direct, complete answer.

## Important Files

- `context_refinery/retrieval.py` — query classification, hybrid retrieval, reranking, document-kind priors
- `scripts/run_query_benchmark.py` — 18-query retrieval benchmark runner
- `scripts/benchmark_to_refinement_queue.py` — converts benchmark misses into refinement queue
- `scripts/normalize_vault_schema_v4.py` — batch vault normalizer (structural metadata)
- `scripts/build_v4_owner_queue.py` — builds owner-pass queue from normalizer confidence output
- `context_refinery/triage/runner.py` — V4 triage CLI entry point
- `project-docs/retrieval-benchmark-v0/refinement-queue-2026-04-20.md` — current refinement queue

## Failure Modes / Gotchas

- Raw operational logs outrank synthesized notes when no strong anchor exists for the topic. The fix is to build the anchor, not to demote the logs further.
- A note can be factually relevant but still lose as a retrieval winner if it is a transcript, scratchpad, or daily note — document-kind priors handle this.
- Bulk triage without benchmark targets burns time. Always check which queries the work is meant to improve.
- Project identity queries drift into noise when no direct project anchor exists.

## Source Evidence

- `project-docs/retrieval-benchmark-v0/Harness evaluation/run-2026-04-19-source-aware-priors.md` — latest benchmark run
- `project-docs/retrieval-benchmark-v0/refinement-queue-2026-04-20.md` — active refinement queue
- `project-docs/VM-MIGRATION-HANDOFF.md` — VM migration context
- `project-docs/V4-TRIAGE-CLI-BRIEF.md` — V4 CLI spec
