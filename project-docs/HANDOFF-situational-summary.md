# Situational Summary — Context Refinery — 2026-04-15

## What just happened

Full corpus re-ingest completed. 3,368 documents are rsynced to the GCP VM and a Khoj re-index is running via `nohup` (PID on VM, check `/tmp/reindex_khoj.log`). The index runs in 4 batches (PUT 1000, PATCH 1000, PATCH 1000, PATCH 368) and takes ~90 minutes total.

## Corpus breakdown

| Source | Count | Notes |
|---|---|---|
| ChatGPT | 1,683 | Full export (May 2023 → Apr 2026), sharded zip, newly ingested |
| Obsidian vault | ~1,205 | SoloDeveloper vault; 369 notes have Jules-normalized frontmatter, rest are raw |
| Claude.ai web | 344 | Full export (Jul 2023 → Apr 2026) |
| Claude Code CLI | 71 | Local session logs from ~/.claude/projects/ |
| Codex CLI | 65 | Local session logs from ~/.codex/command-logs/ |
| **Total** | **3,368** | |

## What's deployed

- **Khoj** on GCP VM (`100.107.147.16:42110`) — re-indexing 3,368 files right now
- **Context Refinery API** on same VM (`:8000`) — systemd service, includes `/query` endpoint with hybrid search (vector + keyword)
- **Code** is on branch `feat/claude-web-adapter` on the VM (`~/MyAPI`), pushed to `origin`

## What was merged today (SoloDeveloper vault)

8 Jules normalization branches merged into `main` of `skchaudr/SoloDeveloper`:
- `02 Areas/My_DevInfra` (96 files)
- `02 Areas/Health` (81 files)
- `02 Areas/Career` (19 files)
- `01 Projects/CIM` (25 files)
- `02 Areas/Code Problem Solving` (10 files)
- `01 Projects/GDDP` (62 files)
- `02 Areas/Learning` (65 files)
- `01 Projects/SocialXP` (11 files)

Two merge conflicts resolved conservatively (kept Jules frontmatter + main body content).

## What was built/shipped in this session

1. **Claude.ai web adapter** — `context_refinery/adapters/claude.py` + wired into `ingest_all.py`
2. **Hybrid search** — `KeywordSearcher` in `retrieval.py`, keyword matches get 15% reranker boost
3. **Sharded ChatGPT export support** — `ingest_all.py` handles zip with `conversations-000.json` through `conversations-015.json`
4. **Bulk Obsidian vault ingestion** — `ingest_all.py --obsidian ~/Obsidian/SoloDeveloper`
5. **Lazy google.genai import** — unblocks local test runs without SDK installed
6. **Benchmark v0 run** — 18 queries, all returning results after null-handling fix
7. **Triage inbox fix** — `0-9a-z` single-keypress selection for 10+ subfolder menus

## Branches of note (MyAPI repo)

| Branch | Status |
|---|---|
| `feat/claude-web-adapter` | Active development branch, deployed to VM |
| `feat/smart-retrieval-layer` | Merged to main previously |
| `modular-triage-system-*` | Stale, do NOT merge (behind main) |

## What to do when the index finishes

1. Check: `gcloud compute ssh --zone "us-central1-a" "khoj-headless-engine" --tunnel-through-iap --project "gen-lang-client-0824562549" --command 'cat /tmp/reindex_khoj.log'`
2. When it says `DONE`, run the benchmark: `python3 /tmp/run_benchmark.py` (or recreate from `project-docs/retrieval-benchmark-v0/Query/benchmark-v0.md`)
3. Compare results against the previous run — expect `unknown`/`untitled` counts to drop significantly for Obsidian-sourced results

## Open work items

- **Remaining vault normalization** — `03 Resources/Workflows` (168 files), `03 Resources/AI` (60), `03 Resources/NeoVim` (28), `03 Resources/Programming` (17) still need Jules passes
- **Classifier tuning** — 14/18 benchmark queries classify as `factual`; temporal, pattern, and cross-source intents need broader regex triggers
- **Modular triage CLI** — scaffolded with stubs, handoff doc at `project-docs/HANDOFF-modular-triage.md`
- **Older vaults** — coding-tech and personal vaults (2023–2024) not yet ingested; lower priority until current corpus quality stabilizes
- **PR cleanup** — `feat/claude-web-adapter` should be merged to main when ready; several stale Jules branches can be deleted
