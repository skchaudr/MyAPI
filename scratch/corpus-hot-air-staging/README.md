# corpus-hot pass-1 (sab-air)

Host: **sab-air.local** · Date: 2026-07-29  
Write root: `~/repos/MyAPI/scratch/corpus-hot/`  
Constraint: read-heavy harvest only — **no** commit/push, reindex, full `.pi` ingest, secret values.

## Quality table

| Project | Brief quality | Biggest gap |
|---------|---------------|-------------|
| **myapi** | **ok** (operator solid; product tip via `main` not working tree) | Working tree on `feat/corpus-v1-normalization` — PROJECT-BRIEF / goldens / MCP / `.handoffs/029` need `git show main:` or pull; few fresh MyAPI-titled agent sessions vs vault |
| **gddp** | **solid** | Live production queue/intake/secrets are **mini** (TOPOLOGY); air has docs+handoffs+sessions but not control-plane state; graphify ≠ project graph |
| **pi-needle-gemma** | **solid** (scoped) | Must not full-ingest `~/.pi`; Camber upload/train still Sab-gated; mini↔air model/serve live-state not diffed service-level |

## Air-only / air-strong sources (summary)
- Obsidian: `Corpus v1.0/` buckets; SSD MyAPI normalization notes; Needle Gemma plan/postmortem; GDDP flashcards
- Full `~/.pi` tree with needle-gemma-v1 bundle + ledger
- gddp-runtime + gddp-config clones on `main` with rich `.handoffs/`
- Claude projects for gddp + pi/needle; Codex rollout summaries for gddp/needle/myapi-vertex

## Pass-1 checklist
- [x] Each project: SOURCES ≥5, QUERIES ≥8, BRIEF-DRAFT non-empty + ≥3 real paths, GAPS
- [x] No secret values; env **names** only
- [x] No side quests (no Khoj reindex, no graph rebuild, no commits)

## Idle status
**air pass-1 complete — three briefs written; idle for merge review.**
