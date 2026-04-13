# Jules Task: Codex CLI Session Adapter

## Summary
Build an adapter that ingests structured Codex CLI session artifacts from `~/.codex/command-logs/` and converts them to `CanonicalDoc` objects for the Context Refinery pipeline.

## Data Source
Codex sessions are already pre-processed into structured artifacts by `codex-log-backfill`. Each session lives in `~/.codex/command-logs/YYYY-MM-DD/<session-id>/` with these files:

### `session-meta.json`
```json
{
  "session_id": "019d6994-61d2-7ea1-b362-74754ce48479",
  "started_at": "2026-04-07T20:13:45Z",
  "ended_at": "2026-04-07T20:34:34Z",
  "cwd": "/Users/saboor/repos/gddp-config",
  "model": "gpt-5.4",
  "cli_version": "0.0.0",
  "title": "...",
  "first_user_message": "...",
  "git_branch": "feat/openclaw-nodes",
  "git_sha": "abc123",
  "git_origin_url": "https://github.com/..."
}
```

### `summary.json`
```json
{
  "session_id": "...",
  "started_at": "...",
  "ended_at": "...",
  "title": "short title",
  "initial_intent": "what the user asked first",
  "prompt_count": 3,
  "command_count": 22,
  "top_keywords": ["openclaw", "brew", "config"],
  "sample_commands": ["which openclaw", "brew info openclaw-cli"],
  "outcome_hint": "what happened at the end",
  "final_assistant_message": "full final response"
}
```

### `summary.md`
Human-readable markdown summary with sections: Intent, Outcome Hint, Keywords, Sample Commands, Final Answer.

### `prompts.jsonl`
One line per user prompt: `{"logged_at": "...", "prompt": "full text", "session_id": "..."}`

### `commands.jsonl`
One line per shell command: `{"logged_at": "...", "command": "git status", "output_preview": "...", "session_id": "..."}`

## Requirements

### 1. Create `context_refinery/adapters/codex.py`

**Function signature:**
```python
def parse_codex_session(session_dir: str) -> dict:
    """
    Reads a Codex session directory and returns a dict
    mapping to the CanonicalDocument schema.
    """
```

**Mapping to CanonicalDoc:**
| CanonicalDoc field | Source |
|---|---|
| `id` | `session-meta.json` → `session_id` |
| `title` | `summary.json` → `title` (fall back to first 80 chars of `initial_intent`) |
| `source.system` | `"codex"` |
| `source.type` | `"json"` |
| `source.original_file_name` | relative path from `~/.codex/command-logs/` |
| `timestamps.created_at` | `session-meta.json` → `started_at` |
| `timestamps.updated_at` | `session-meta.json` → `ended_at` |
| `timestamps.ingested_at` | current UTC ISO timestamp |
| `author` | `"codex-cli"` |
| `status` | `"scratchpad"` (default per taxonomy) |
| `doc_type` | `"conversation"` |
| `tags` | `summary.json` → `top_keywords` (already a list of strings) |
| `projects` | Infer from `cwd` — extract repo name from path (e.g., `/Users/saboor/repos/gddp-config` → `"gddp-config"`) |
| `content.raw_text` | Read `summary.md` as-is |
| `content.cleaned_markdown` | Read `summary.md` as-is (it's already clean markdown) |
| `content.summary` | `summary.json` → `initial_intent` + " → " + `outcome_hint` |
| `quality.is_noisy` | `True` if `prompt_count == 0` or `command_count == 0` |
| `quality.warnings` | Add `"no-prompts"` if prompt_count is 0, `"no-commands"` if command_count is 0 |

### 2. Create a batch scanner function

```python
def scan_codex_sessions(root: str = "~/.codex/command-logs") -> list[dict]:
    """
    Walk the command-logs directory tree and parse all sessions.
    Returns a list of CanonicalDocument dicts.
    """
```

This should:
- Recursively find all directories containing `session-meta.json`
- Call `parse_codex_session()` on each
- Skip sessions that fail to parse (log warning, continue)
- Sort results by `created_at` descending (newest first)

### 3. Add API endpoint

Add to `api/routers/imports.py`:
```python
@router.post("/import/codex")
```

Accepts: `{"root": "~/.codex/command-logs"}` (optional, defaults to standard path)
Returns: list of `CanonicalDocumentResponse` objects

### 4. Tests

Add `tests/test_codex.py`:
1. `test_parse_codex_session` — create a temp dir with mock session files, verify output schema
2. `test_parse_codex_session_missing_files` — gracefully handle missing summary.json
3. `test_scan_codex_sessions` — mock directory with 3 sessions, verify all parsed
4. `test_project_extraction_from_cwd` — verify `/Users/saboor/repos/gddp-config` → `"gddp-config"`

## Key files to reference (don't modify)
- `context_refinery/adapters/obsidian.py` — follow this pattern exactly
- `context_refinery/adapters/chatgpt.py` — follow this pattern exactly
- `api/schemas.py` — `CanonicalDocumentResponse` schema
- `docs/01-taxonomy.md` — valid values for status, doc_type

## Do NOT
- Modify the Codex log files or logwrap scripts
- Add new dependencies
- Change the existing adapters
- Read from `~/.codex/sessions/` directly (use the pre-processed `command-logs/` only)
