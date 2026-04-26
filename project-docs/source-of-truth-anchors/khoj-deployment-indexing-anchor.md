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

Khoj is the vector search and RAG backend for the My_DevInfra system. It indexes the full note corpus (~3,200 docs across Obsidian, ChatGPT, Claude, Claude Code, and Codex sources) and serves semantic search results. Context Refinery is the orchestration layer that calls Khoj for semantic search, merges that with local keyword search, applies document-kind priors, reranks, and exposes the `/query` API.

This note is the canonical answer to "What notes mention Khoj deployment or indexing?" and "What is the status of the API deployment?"

## Runtime Topology

```
Notes corpus (~/khoj-data/notes/)
    ↓ index via PUT/PATCH /api/content
Khoj (port 42110, khoj.service)
    ↓ semantic search via GET /api/search
Context Refinery (port 8000, context-refinery.service)
    ↓ classify → hybrid search → filter → rerank → group
/query API response
```

All services run on the same GCP VM (`instance-20260418-024637`, e2-highmem-4, us-central1-a).

- **Khoj**: port `42110`, systemd `khoj.service`, runs in `--anonymous-mode`, venv at `/data/khoj-venv`
- **Context Refinery**: port `8000`, systemd `context-refinery.service`, env loaded from `~/MyAPI/.env`
- **KHOJ_URL**: `http://localhost:42110` (set in `~/MyAPI/.env`, used by Context Refinery)
- **KHOJ_NOTES_DIR**: `/home/saboor/khoj-data/notes` (used by keyword search sidecar)
- **Data disk**: `/data` (~197G filesystem), stores repos, venvs, and persistent data
- **Tailscale IP**: `100.85.100.52`

## Current Service State

As of 2026-04-23:

| Service | Port | Health endpoint | Expected response |
|---|---|---|---|
| Khoj | 42110 | `http://localhost:42110/api/health` | `{"email": "default@example.com"}` |
| Context Refinery | 8000 | `http://localhost:8000/health` | `{"status":"ok","model":"gemini-1.5-flash"}` |

Query endpoint: `POST http://localhost:8000/query` with `{"q": "...", "n": 10}`

## Indexing Flow

1. Notes land in `~/khoj-data/notes/` as normalized Markdown with YAML frontmatter.
2. Indexing uses the Khoj multipart API: `PUT /api/content?client=api` for the first batch, `PATCH /api/content?client=api` for subsequent batches.
3. Each file is sent as a multipart form field with the filename as key and file content as value.
4. Batched in groups to avoid timeout — `scripts/reindex_khoj_safe.py` handles batching and error recovery.
5. After indexing, verify with a known-good query through Context Refinery `/query`.

Reindex scripts:

- `scripts/reindex_khoj_safe.py` — full safe reindex with batching
- `scripts/khoj_reindex_resume_index.py` — resume a partial reindex
- `scripts/khoj_index_diff.py` — index only changed files
- `scripts/khoj_repair_index_delta.py` — repair index gaps

## Verification Checks

Run these in order on the VM to confirm the stack is healthy:

```bash
# 1. Are services running?
systemctl is-active khoj.service context-refinery.service

# 2. Can Khoj respond?
curl -sS http://localhost:42110/api/health

# 3. Can Context Refinery respond?
curl -sS http://localhost:8000/health

# 4. Does a known-good query return results?
curl -sS -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"q":"What notes mention Khoj deployment or indexing?","n":3}'
```

If step 4 fails while steps 1-3 pass, check `KHOJ_URL` in `~/MyAPI/.env` — it may point at a stale IP.

## Decisions Made

- Khoj and Context Refinery colocated on the same VM for this phase (no separate search cluster).
- Persistent data under `/data`, not root disk.
- `KHOJ_URL=http://localhost:42110` — local loopback, not Tailscale IP.
- Source-aware and document-kind-aware ranking in Context Refinery so synthesized anchor notes beat raw session dumps for overview queries.
- Benchmark-driven reindex loops: normalize → index → benchmark → refine. No open-ended corpus work.

## Important Commands or Files

Repo files:

- `context_refinery/retrieval.py` — query classification, hybrid retrieval, reranking, document-kind priors
- `scripts/reindex_khoj_safe.py` — batched safe reindex
- `scripts/khoj_reindex_resume_index.py` — resume partial reindex
- `scripts/khoj_index_diff.py` — diff-based reindex
- `scripts/run_query_benchmark.py` — 18-query benchmark runner

VM paths:

- `/etc/systemd/system/khoj.service` — Khoj systemd unit
- `/etc/systemd/system/context-refinery.service` — Context Refinery systemd unit
- `~/MyAPI/.env` — environment variables including `KHOJ_URL`
- `~/khoj-data/notes/` — indexed note corpus

## Failure Modes / Gotchas

- **Stale KHOJ_URL**: Context Refinery health passes but `/query` fails because `KHOJ_URL` in `.env` points at an old Tailscale IP instead of `localhost:42110`. Fix: update `.env`, restart `context-refinery.service`.
- **WorkingDirectory mismatch**: systemd units fail if `WorkingDirectory` still references `/home/saboor/MyAPI` after repo moved to `/data/repos/MyAPI`. Fix: update unit files, `systemctl daemon-reload`.
- **Disk confusion**: root disk (`/`) and data disk (`/data`) are separate. Root exhaustion needs root cleanup; `/data` exhaustion needs `/data` cleanup. They are not the same disk.
- **Reindex timeouts**: large batch uploads can timeout. Use `reindex_khoj_safe.py` which handles batching and retries.
- **Raw logs winning queries**: until this anchor is indexed, Q10 and Q12 are won by raw Claude/Codex session dumps. The fix is indexing this note, not further tuning the retrieval code.

## Source Evidence

- `project-docs/VM-MIGRATION-HANDOFF.md`
- `project-docs/VM-MIGRATION-SPRINT.md`
- `project-docs/retrieval-benchmark-v0/Harness evaluation/run-2026-04-19-source-aware-priors.md`
- `project-docs/retrieval-benchmark-v0/refinement-queue-2026-04-20.md`
- Session repair 2026-04-20: VM changed to e2-highmem-4, disks expanded, services restored
