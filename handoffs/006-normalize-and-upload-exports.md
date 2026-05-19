# Handoff 006: Normalize Exports → Upload to GCS

## Goal
Run `ingest_all.py` to convert raw ChatGPT/Claude/Codex exports into normalized markdown, then upload to GCS bucket.

## Raw Export Locations
- **ChatGPT:** `_archive/chatgpt_ALL_CONVOS-2026-02-01/conversations.json`
- **Claude Web:** `_archive/claude-ALL-conversation-history.zip`
- **Codex CLI:** `~/.codex/command-logs/` (scanned automatically)
- **Claude Code:** `~/.claude/projects/` (scanned automatically)

## Steps

```bash
cd /Users/saboor/repos/MyAPI

# 1. Create output directory
mkdir -p corpus_v1/normalized

# 2. Run normalization (reads raw exports, writes .md files)
python3 ingest_all.py \
  --chatgpt _archive/chatgpt_ALL_CONVOS-2026-02-01/conversations.json \
  --claude-web _archive/claude-ALL-conversation-history.zip \
  --output corpus_v1/normalized/

# 3. Upload normalized markdown to GCS
gsutil -m rsync -r corpus_v1/normalized/ gs://sb-myapi-corpus/exports/
```

## Notes
- GCP project: `sb-genai-2026`
- Bucket: `gs://sb-myapi-corpus`
- Branch: `feat/corpus-v1-normalization`
- If ingest_all.py errors on missing deps, run `pip install -r requirements.txt` first
- Commit any new files to the branch after successful normalization
