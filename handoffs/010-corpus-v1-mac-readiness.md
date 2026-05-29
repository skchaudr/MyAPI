# 010 — Corpus v1 Mac readiness: shard export wired and scanned

Date: 2026-05-29
Branch: feat/corpus-v1-normalization

## Empirical reality

Mac is the current source for the full ChatGPT export slice and the broad local agent-session corpus.

The repo is on `feat/corpus-v1-normalization`. The relevant normalization code paths are:

- `context_refinery/normalization_schema.py`
- `scripts/normalize_corpus.py`
- `tests/test_normalization_schema.py`
- `tests/test_normalize_corpus.py`

The May 22 ChatGPT export is extracted at:

```text
corpus_v1/chatgpt-may-22-to-be-normalized/
```

It contains 20 `conversations-*.json` shards and 1,918 conversations.

`scripts/normalize_corpus.py` now accepts a ChatGPT export directory containing `conversations*.json` shards, in addition to the previous single JSON file and zip forms. This removes the blocker where the May 22 export existed on disk but could not be scanned directly as one input.

Focused verification:

```text
venv/bin/pytest tests/test_normalization_schema.py tests/test_normalize_corpus.py
42 passed
```

The focused test coverage includes:

- ChatGPT export shard directories are accepted by scan/copy loading.
- ChatGPT shard order is deterministic.
- CLI session copy paths include a stable entry fingerprint so duplicate titles/unknown ids do not overwrite each other.

Fresh Mac scan:

```text
venv/bin/python scripts/normalize_corpus.py scan --obsidian /Users/saboor/Obsidian/SoloDeveloper --chatgpt corpus_v1/chatgpt-may-22-to-be-normalized --claude-web _archive/claude-ALL-conversation-history.zip
```

Manifest written:

```text
corpus_v1/manifests/scan-2026-05-29.jsonl
```

Scan totals:

```text
rows: 4932
by source:
  obsidian: 1714
  repo_docs: 63
  claude_code: 744
  codex: 149
  chatgpt: 1918
  claude_web: 344
by source_type:
  note: 77
  daily_note: 160
  project_doc: 1043
  reference: 483
  anchor: 4
  handoff: 10
  cli_session: 893
  conversation: 2262
```

## Important distinction

`corpus_v1/normalized/` is the older flat `ingest_all.py` / GCS export path. It is not the same thing as the planned v1-stamped `documents/`, `conversations/`, `artifacts/`, and `manifests/` layout produced by `scripts/normalize_corpus.py copy`.

Do not treat `corpus_v1/normalized/` as proof that the v1 corpus copy/materialization pass has completed.

Full materialization:

```text
venv/bin/python scripts/normalize_corpus.py copy --manifest corpus_v1/manifests/scan-2026-05-29.jsonl --chatgpt corpus_v1/chatgpt-may-22-to-be-normalized --claude-web _archive/claude-ALL-conversation-history.zip
```

Copy manifest written:

```text
corpus_v1/manifests/copy-2026-05-29.jsonl
```

Copy totals:

```text
rows copied: 4898
filesystem files under documents/conversations/artifacts: 4898
unique output paths: 4898
duplicate output paths: 0
missing outputs: 0
by source:
  obsidian: 1714
  repo_docs: 63
  claude_code: 710
  codex: 149
  chatgpt: 1918
  claude_web: 344
by source_type:
  note: 77
  daily_note: 160
  project_doc: 1043
  reference: 483
  anchor: 4
  handoff: 10
  cli_session: 859
  conversation: 2262
```

The scan had 4,932 rows, but copy skipped 34 stale `claude_code` source files that disappeared between scan and materialization, mostly under `/Users/saboor/.claude/projects/-private-tmp/`. This is a source freshness issue, not a normalizer crash.

Structural output validation:

```text
all copied manifest paths exist
all 4,898 materialized files start with YAML frontmatter
mixed-source samples present for obsidian, repo_docs, chatgpt, claude_web, claude_code, and codex
```

## Resume point

The next useful step is reviewing content quality in a small mixed sample from the materialized v1 output:

- one Obsidian project doc
- one ChatGPT conversation from the May 22 shards
- one Claude web conversation
- one Claude Code session
- one Codex session

After sample inspection, reranker/source-weighting work can resume against the materialized v1 corpus.

## Tailscale note

Remote `big-ssd` is reachable again from Mac without repeated browser auth after removing a stray quarantine xattr from the local Tailscale preferences plist. The plist was backed up first under `/tmp`.

The practical SSH path is working again. The local Tailscale CLI still reported a preferences-loading error during follow-up status checks, so if future work depends on `tailscale status` specifically, treat that as a separate local Tailscale cleanup task.
