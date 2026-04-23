---
title: My_DevInfra System Anchor
aliases:
  - My_DevInfra
  - Personal Briefing & Capture System
  - developer infrastructure
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
  - knowledge-system
benchmark_targets:
  - retrieval-benchmark-v0/Q1
related:
  - khoj-deployment-indexing-anchor
  - vm-tailscale-ssh-access-anchor
  - current-system-end-to-end-anchor
---

# My_DevInfra System Anchor

## What This Is

My_DevInfra is the working project identity for the personal developer infrastructure system around MyAPI, Context Refinery, Khoj, Obsidian, benchmark-driven retrieval, VM operations, and agent-assisted project work.

The system is not just one app. It is the loop that captures raw work, normalizes it into useful notes, indexes it into Khoj, evaluates retrieval quality, and turns project history into actionable context.

## Current State

As of 2026-04-20, the live runtime is on Google Cloud VM `instance-20260418-024637` in project `project-ab32182e-5782-4a9c-939`.

Current core pieces:

- MyAPI repo: application and pipeline code
- Context Refinery: FastAPI service for query, enrichment, triage, and retrieval orchestration
- Khoj: RAG/search backend indexing the Obsidian/agent-note corpus
- Obsidian corpus: the human-owned knowledge layer
- Retrieval benchmark: the measurement harness for whether the right notes win
- VM runtime: the remote compute host with persistent `/data` storage

## Decisions Made

- Treat retrieval quality as a product metric, not a vague feeling.
- Use benchmark misses to drive refinement work.
- Prefer canonical source-of-truth anchor notes over raw command/session dumps.
- Keep raw Claude, Codex, ChatGPT, and terminal logs as evidence, while letting synthesized notes win general retrieval queries.
- Use Context Refinery as the bridge between messy source data and Khoj-ready Markdown.

## Important Commands or Files

- `context_refinery/retrieval.py`: query classification, hybrid retrieval, reranking, document-kind priors.
- `scripts/run_query_benchmark.py`: runs the retrieval benchmark against Context Refinery.
- `scripts/benchmark_to_refinement_queue.py`: converts benchmark misses into an owner-pass queue.
- `project-docs/retrieval-benchmark-v0/refinement-queue-2026-04-20.md`: current benchmark-driven refinement queue.
- `project-docs/retrieval-benchmark-v0/Harness evaluation/run-2026-04-19-daily-note-penalty.md`: current baseline benchmark.

## Failure Modes / Gotchas

- Raw operational logs can rank higher than synthesized notes if no strong anchor exists.
- A note can be factually relevant but still be a poor retrieval winner if it is a transcript, scratchpad, or daily note.
- Project identity queries need a direct project anchor; otherwise retrieval drifts into whatever file contains the right words.
- Bulk triage can burn time without improving benchmark targets.

## Related Notes

- `khoj-deployment-indexing-anchor`
- `vm-tailscale-ssh-access-anchor`
- `context-refinery-architecture-anchor`
- `retrieval-benchmark-methodology-anchor`
- `current-system-end-to-end-anchor`

## Source Evidence

- `project-docs/retrieval-benchmark-v0/Harness evaluation/run-2026-04-19-daily-note-penalty.md`
- `project-docs/retrieval-benchmark-v0/refinement-queue-2026-04-20.md`
- `project-docs/VM-MIGRATION-HANDOFF.md`
- `project-docs/VM-MIGRATION-SPRINT.md`
- `project-docs/HANDOFF-hybrid-search.md`
- `project-docs/STATUS_AND_NEXT_STEPS.md`
