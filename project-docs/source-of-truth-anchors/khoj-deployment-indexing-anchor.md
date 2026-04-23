---
title: Khoj Deployment and Indexing Anchor
aliases:
  - Khoj deployment
  - Khoj indexing
  - Khoj reindex
  - Context Refinery retrieval backend
source: obsidian
document_kind: synthesized_note
type: anchor
status: active
projects:
  - myapi
  - context-refinery
  - khoj
tags:
  - khoj
  - indexing
  - deployment
  - retrieval
  - vm
benchmark_targets:
  - retrieval-benchmark-v0/Q10
  - retrieval-benchmark-v0/Q12
related:
  - my-devinfra-system-anchor
  - vm-tailscale-ssh-access-anchor
  - current-system-end-to-end-anchor
---

# Khoj Deployment and Indexing Anchor

## What This Is

This note is the source-of-truth anchor for the Khoj deployment and indexing path used by Context Refinery.

Khoj is the search/RAG backend. Context Refinery calls Khoj for semantic search, merges that with local keyword search, applies filters and reranking, then returns benchmarkable results through the `/query` API.

## Current State

As of 2026-04-20:

- VM: `instance-20260418-024637`
- GCP project: `project-ab32182e-5782-4a9c-939`
- Zone: `us-central1-a`
- Machine type: `e2-highmem-4`
- Tailscale IP: `100.85.100.52`
- Khoj service: `khoj.service`
- Khoj health endpoint: `http://localhost:42110/api/health`
- Context Refinery service: `context-refinery.service`
- Context Refinery health endpoint: `http://localhost:8000/health`
- Context Refinery query endpoint: `http://localhost:8000/query`
- Data disk: `/data`, `197G` filesystem, about `174G` free after resize
- Root disk: `/`, `49G` filesystem, about `42G` free after resize

Verified service state:

- `khoj.service`: active
- `context-refinery.service`: active
- Khoj health response: `{"email": "default@example.com"}`
- Context Refinery health response: `{"status":"ok","model":"gemini-1.5-flash"}`
- `/query` returns classified operational results

## Decisions Made

- Keep Khoj and Context Refinery on the same VM for the current phase.
- Store persistent data under `/data`.
- Use `KHOJ_URL=http://localhost:42110` for Context Refinery on the VM.
- Use `KHOJ_NOTES_DIR=/home/saboor/khoj-data/notes` for the keyword-search sidecar.
- Use source-aware and document-kind-aware ranking so synthesized notes can beat raw logs.
- Use benchmark-driven reindex loops instead of open-ended corpus work.

## Important Commands or Files

Run on Mac:

```bash
gcloud compute ssh instance-20260418-024637 --zone us-central1-a --project project-ab32182e-5782-4a9c-939
```

Run in VM shell:

```bash
systemctl is-active khoj.service context-refinery.service
```

Run in VM shell:

```bash
curl -sS http://localhost:42110/api/health
```

Run in VM shell:

```bash
curl -sS http://localhost:8000/health
```

Run in VM shell:

```bash
curl -sS -X POST http://localhost:8000/query -H "Content-Type: application/json" -d '{"q":"What notes mention Khoj deployment or indexing?","n":3}'
```

Important repo files:

- `context_refinery/retrieval.py`
- `scripts/reindex_khoj_safe.py`
- `scripts/khoj_reindex_resume_index.py`
- `scripts/khoj_index_diff.py`
- `scripts/run_query_benchmark.py`
- `/etc/systemd/system/khoj.service`
- `/etc/systemd/system/context-refinery.service`

## Failure Modes / Gotchas

- Context Refinery can be healthy while `/query` fails if `KHOJ_URL` points at an old IP.
- Khoj direct search can work while Context Refinery query fails if environment variables are stale.
- Systemd units can fail after repo relocation if `WorkingDirectory` still points at `/home/saboor/MyAPI` instead of `/data/repos/MyAPI`.
- Raw operational logs can win Q10/Q12 until a stronger Khoj deployment anchor is indexed.
- The root disk and data disk are separate; root exhaustion and `/data` exhaustion require different fixes.

## Related Notes

- `my-devinfra-system-anchor`
- `vm-tailscale-ssh-access-anchor`
- `retrieval-benchmark-methodology-anchor`
- `api-deployment-status-anchor`

## Source Evidence

- `project-docs/VM-MIGRATION-HANDOFF.md`
- `project-docs/VM-MIGRATION-SPRINT.md`
- `project-docs/HANDOFF-situational-summary.md`
- `project-docs/retrieval-benchmark-v0/Harness evaluation/run-2026-04-19-daily-note-penalty.md`
- Session repair on 2026-04-20: VM changed to `e2-highmem-4`, `/data` expanded to `197G`, `/` expanded to `49G`, services restored.
