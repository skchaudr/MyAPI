# MyAPI-Rebuild Corpus Freshness Audit - 2026-07-01

## Short answer

MyAPI-rebuild's intended corpus is fresher than Corpus v1.0 alone, but the current code defaults are not aligned with the intended live sources.

The plan points at durable handoffs built from live Obsidian, Corpus v1.0, old MyAPI docs/handoffs/graph, Codex sessions, Claude projects, and Pi/Needle traces. The live sources exist and are mostly fresh enough for a raw audit pass. The stale gap is ingestion wiring: `ingest_all.py` still defaults Codex to `/Users/sab-mini/.codex/command-logs`, defaults Obsidian to missing `/Users/sab-mini/Obsidian/SoloDeveloper`, and has no default path for `/Users/sab-mini/.pi` traces. No `khoj-ready-bundle` exists in MyAPI-rebuild today.

Inspected repo docs:
- `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/REBUILD-CONTEXT-ANCHOR.md`
- `/Users/sab-mini/repos/MyAPI-rebuild/IMPLEMENTATION-PLAN.md`
- `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/ARCHITECTURE.md`

## Actual read defaults observed

Static code inspection only; no ingestion or indexing was run.

| Component | Current default read path or endpoint | Freshness / fit |
|---|---|---|
| `ingest_all.py --obsidian` | Defaults to `/Users/sab-mini/Obsidian/SoloDeveloper` if present | Missing on sab-air. Intended live vault is `/Users/sab-mini/Obsidian/SSD`, so Obsidian will be skipped unless explicitly passed. |
| `context_refinery/adapters/codex.py` | `/Users/sab-mini/.codex/command-logs` | Exists, latest file `2026-06-22 20:32:58 -0700`, but intended/current source is `/Users/sab-mini/.codex/sessions`, latest `2026-07-01 18:46:36 -0700`. |
| `context_refinery/adapters/claude_code.py` | `/Users/sab-mini/.claude/projects` | Exists and fresh; latest JSONL `2026-07-01 17:38:30 -0700`. |
| `context_refinery/retrieval.py` | Khoj URL default `http://100.107.147.16:42110`; keyword dir default `/home/sbkchaudry_gmail_com/khoj-data/notes` | This is a deployed/VM-era retrieval path, not a local corpus v2 read path. |
| `scripts/reindex_khoj_safe.py` | `~/khoj-data/notes`, `http://localhost:42110` | Useful for Khoj reindexing, but not proof that MyAPI-rebuild has a fresh local bundle. |
| Bundle outputs | `/Users/sab-mini/repos/MyAPI-rebuild/khoj-ready-bundle`, `/Users/sab-mini/repos/MyAPI-rebuild/exports/khoj-ready-bundle` | Both missing. |

## Source audit

| Source family | Source path inspected | Exists | Freshness signal | Likely role | Risks / gaps | Recommended next ingestion or audit action |
|---|---:|---:|---|---|---|---|
| Live vault | `/Users/sab-mini/Obsidian/SSD` | Yes | 2,367 `.md`; latest note-like file `/Users/sab-mini/Obsidian/SSD/04 Periodic/00 Dailys/2026.07.01.md` modified `2026-07-01 18:04:15 -0700`; latest project note `/Users/sab-mini/Obsidian/SSD/01 Projects/GDDP/GDD - pass one strategy - overnight runs, aa-cli, thinking bigger.md` modified `2026-07-01 17:40:27 -0700`. | Current person/project truth, preferences, decisions, active project anchors. Best source for `get_person_context`. | Current ingest default misses it because it looks for `/Users/sab-mini/Obsidian/SoloDeveloper`. Vault system files also update frequently, so freshness checks should focus on `.md`, not `.obsidian` or `.smart-env`. | Run the next raw pass with explicit `--obsidian /Users/sab-mini/Obsidian/SSD`, then audit copied files for source identity, frontmatter preservation, and duplicate filename collisions. |
| Corpus v1.0 | `/Users/sab-mini/repos/MyAPI/Corpus v1.0` | Yes | 3,000 `.md`; content latest `/Users/sab-mini/repos/MyAPI/Corpus v1.0/June 17 SitRep on API & MCP Path.md` modified `2026-06-17 07:53:14 -0700`; Obsidian/plugin metadata modified `2026-06-21 23:56:47 -0700`. | Baseline substrate: 22 PARA-ish buckets, prior normalized sessions, source counts, old retrieval corpus. | Stale relative to live vault and live session logs. Session buckets are older: Codex/Claude/ChatGPT session corpus files last touched around `2026-06-09`. Good baseline, not enough as "today." | Treat as baseline/reference, not the only source. Diff it against live vault and live session directories before v2 extraction. |
| Corpus v1.0 session buckets | `/Users/sab-mini/repos/MyAPI/Corpus v1.0/60-sessions-and-conversations/{codex,claude-code,claude-web,chatgpt}` | Yes | Codex 53 `.md`, latest `2026-06-09 04:33:26 -0700`; Claude Code 526 `.md`, latest `2026-06-09 04:33:22 -0700`; Claude Web 108 `.md`, latest `2026-06-09 04:33:30 -0700`; ChatGPT 170 `.md`, latest `2026-06-09 04:33:37 -0700`. | Historic session corpus and benchmark baseline. | Not fresh for late-June/July agent work; v0 issue remains possible: sessions exist but are not shaped into durable traces. | Use for regression baselines and source-family tests; refresh from live Codex/Claude paths before judging current recall. |
| Old MyAPI repo docs | `/Users/sab-mini/repos/MyAPI/project-docs` | Yes | 55 files; latest docs `/Users/sab-mini/repos/MyAPI/project-docs/corpus-v1-vault-v1.0-implementation-plan.md` modified `2026-06-08 00:33:32 -0700`, `/Users/sab-mini/repos/MyAPI/project-docs/corpus-v1-obsidian-substrate-architecture.md` modified `2026-06-08 00:25:22 -0700`. | Project origin, v1 architecture, old substrate decisions, Khoj/Vertex deployment context. | Useful but stale against rebuild direction from `2026-06-21+`. Should not override rebuild anchor. | Ingest as project-history/reference docs with lower freshness priority than rebuild anchors and live handoffs. |
| Old MyAPI handoffs | `/Users/sab-mini/repos/MyAPI/handoffs` and `/Users/sab-mini/repos/MyAPI/Corpus v1.0/70-artifacts-and-reference/handoffs` | Yes | `/Users/sab-mini/repos/MyAPI/handoffs` has 13 `.md`; latest `/Users/sab-mini/repos/MyAPI/handoffs/012-macbook-acp-claude-vault-run.md` modified `2026-06-08 00:33:32 -0700`. Anchor-mentioned `/Users/sab-mini/repos/MyAPI/.handoffs` does not exist. | Early durable-handoff instinct and evidence for v0/v1 evolution. | Path mismatch: anchor names `/Users/sab-mini/repos/MyAPI/.handoffs/025-web-ui-agent-pt-2.md`, but live old repo has `/Users/sab-mini/repos/MyAPI/handoffs` and Corpus has `70-artifacts-and-reference/handoffs`; the rebuild repo has `.handoffs/025-web-ui-agent-pt-2.md`. | Normalize handoff path references before ingestion. Prefer `/Users/sab-mini/repos/MyAPI-rebuild/.handoffs` for rebuild handoffs and `/Users/sab-mini/repos/MyAPI/handoffs` for old repo history. |
| Rebuild handoffs | `/Users/sab-mini/repos/MyAPI-rebuild/.handoffs` | Yes | 15 `.md`; latest `/Users/sab-mini/repos/MyAPI-rebuild/.handoffs/022-situational-summary.md` modified `2026-06-23 22:13:47 -0700`. `/Users/sab-mini/repos/MyAPI-rebuild/handoffs` exists but has 0 `.md`. | Best current durable-handoff corpus inside rebuild. Includes copied/continued handoff numbers up to `025-web-ui-agent-pt-2.md`. | Two handoff dirs exist; root `AGENTS.md` says `.handoffs` is canonical, so empty `handoffs/` should not be treated as missing handoffs. | Ingest `.handoffs` first as privileged traces; ignore empty `handoffs/` unless intentionally populated later. |
| Old MyAPI Graphify graph | `/Users/sab-mini/repos/MyAPI/graphify-out/graph.json` | Yes | File size 888,104 bytes; modified `2026-06-12 15:23:29 -0700`. | Code/rationale graph baseline referenced by anchor and plan. | Stale for any code changed after June 12; mostly code/rationale, not fresh prose relationships. | Reuse as baseline, then regenerate/compare graph before porting graph logic. |
| Rebuild Graphify graph | `/Users/sab-mini/repos/MyAPI-rebuild/graphify-out/graph.json` | Yes | File size 29,357 bytes; modified `2026-06-23 13:13:32 -0700`. | Current rebuild repo structure map. | Much smaller than old MyAPI graph; should not be mistaken for the full old substrate graph. | Keep as rebuild-code graph only; pair with old graph and prose corpus rather than replacing them. |
| Codex sessions | `/Users/sab-mini/.codex/sessions` | Yes | 419 `.jsonl`; latest `/Users/sab-mini/.codex/sessions/2026/07/01/rollout-2026-07-01T18-45-35-019f2080-bca6-77a2-92ae-6ee329db7ef9.jsonl` modified `2026-07-01 18:46:36 -0700`. | Fresh operational traces for Codex work, including rebuild/GDDP/Pi continuity. Anchor explicitly points here for event-trace verification. | Current adapter ignores this tree and reads `/Users/sab-mini/.codex/command-logs` instead. Rollout JSONL needs a parser distinct from old `session-meta.json` command logs. | Add or run a sessions JSONL adapter for `/Users/sab-mini/.codex/sessions`; prioritize June 19-21 and current July 1 traces for rebuild-night and current-state handoffs. |
| Legacy Codex command logs | `/Users/sab-mini/.codex/command-logs` | Yes | 208 files; latest `/Users/sab-mini/.codex/command-logs/2026-06-22/019ef288-92b3-7541-8959-318d2da4487b/session-meta.json` modified `2026-06-22 20:32:58 -0700`. | What the current Codex adapter can read today. | Older and incomplete relative to `/Users/sab-mini/.codex/sessions`; relying on it misses current Codex work. | Keep for backwards compatibility only. Update default/source docs so "Codex sessions" means `/Users/sab-mini/.codex/sessions`. |
| Claude projects | `/Users/sab-mini/.claude/projects` | Yes | 237 `.jsonl`, 244 `.md`; latest `/Users/sab-mini/.claude/projects/-Users-sab-mini-Obsidian-SSD/9d6a59dd-548c-441a-a452-43810696dcef.jsonl` modified `2026-07-01 17:38:30 -0700`. | Fresh Claude Code session traces and project continuity evidence. Current adapter supports this path. | Includes memory files and project folders; source-family filtering must avoid over-weighting generated memory next to sessions. | Use current adapter, then audit counts by project folder and sample parsed provenance fields. |
| Pi / Needle traces | `/Users/sab-mini/.pi`, especially `/Users/sab-mini/.pi/needle`, `/Users/sab-mini/.pi/agent/sessions`, `/Users/sab-mini/.pi/harness/sessions`, `/Users/sab-mini/.pi/.handoffs`, `/Users/sab-mini/.pi/agent/handoffs` | Yes | `/Users/sab-mini/.pi/agent/sessions` has 70 `.jsonl`, latest `2026-07-01 02:29:05 -0700`; `/Users/sab-mini/.pi/needle` has 7 `.jsonl`, latest `/Users/sab-mini/.pi/needle/shadow/2026-06-30.jsonl` modified `2026-06-29 21:22:15 -0700`; `.pi/.handoffs` has recent attachments modified `2026-06-29 22:00:39 -0700`. | Agent/runtime traces, Needle router evidence, Pi operational handoffs. Important for cross-agent continuity and runtime provenance. | No current MyAPI-rebuild adapter/default for this family. `.pi` is large; naive ingestion would pull cache/code/generated artifacts. | Do a scoped Pi source map first: only `.pi/agent/sessions`, `.pi/needle`, `.pi/.handoffs`, `.pi/agent/handoffs`, and selected harness reports. Then write a dedicated adapter or raw extractor. |

## Freshness judgment

Fresh enough for a raw corpus v2 audit:
- `/Users/sab-mini/Obsidian/SSD`
- `/Users/sab-mini/.codex/sessions`
- `/Users/sab-mini/.claude/projects`
- scoped `/Users/sab-mini/.pi` traces
- `/Users/sab-mini/repos/MyAPI-rebuild/.handoffs`

Fresh enough only as baseline/reference:
- `/Users/sab-mini/repos/MyAPI/Corpus v1.0`
- `/Users/sab-mini/repos/MyAPI/project-docs`
- `/Users/sab-mini/repos/MyAPI/handoffs`
- `/Users/sab-mini/repos/MyAPI/graphify-out/graph.json`

Not usable as current local output:
- `/Users/sab-mini/repos/MyAPI-rebuild/khoj-ready-bundle` - missing
- `/Users/sab-mini/repos/MyAPI-rebuild/exports/khoj-ready-bundle` - missing

## Recommended next action

Do one read-only/raw extraction audit before any full ingest:

1. Patch or wrap `ingest_all.py` so the sab-air defaults are explicit:
   - Obsidian: `/Users/sab-mini/Obsidian/SSD`
   - Codex: `/Users/sab-mini/.codex/sessions`
   - Claude Code: `/Users/sab-mini/.claude/projects`
   - Pi/Needle scoped roots: `/Users/sab-mini/.pi/agent/sessions`, `/Users/sab-mini/.pi/needle`, `/Users/sab-mini/.pi/.handoffs`, `/Users/sab-mini/.pi/agent/handoffs`
2. Generate a dry-run manifest only: source family, path, file count, newest file, parser available yes/no, sample parsed metadata.
3. Ingest `.handoffs` and live vault anchors first, then live sessions, then Corpus v1.0 as baseline.
4. Keep old MyAPI graph and Corpus v1.0 as regression fixtures, not proof of current context freshness.

## Validation

Initial status:

```text
## main...origin/main
 M .gitignore
```

Only intended changed path from this worker:

```text
project-documents/corpus-freshness-audit-2026-07-01.md
```
