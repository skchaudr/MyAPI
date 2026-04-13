# Jules Task: Claude Code Session Adapter

## Summary
Build an adapter that ingests Claude Code CLI session JSONL files from `~/.claude/projects/` and converts them to `CanonicalDoc` objects for the Context Refinery pipeline.

## Data Source
Claude Code stores each conversation as a JSONL file at:
`~/.claude/projects/<project-slug>/<session-uuid>.jsonl`

Each line is a JSON object with a `type` field. The relevant types are:

### Message types in JSONL

**`type: "user"`** — user message
```json
{
  "type": "user",
  "uuid": "1f3baf91-...",
  "timestamp": "2026-03-12T12:39:43.986Z",
  "sessionId": "3dba20e1-...",
  "cwd": "/Users/saboor/Obsidian/SoloDeveloper/01 Projects/GDDP",
  "gitBranch": "main",
  "message": {
    "role": "user",
    "content": [{"type": "text", "text": "the actual user message"}]
  },
  "forkedFrom": {"sessionId": "4931f07e-...", "messageUuid": "..."}
}
```

**`type: "assistant"`** — assistant response
```json
{
  "type": "assistant",
  "uuid": "9ac802a5-...",
  "timestamp": "2026-03-12T12:39:52.963Z",
  "sessionId": "3dba20e1-...",
  "parentUuid": "1f3baf91-...",
  "message": {
    "role": "assistant",
    "content": [
      {"type": "thinking", "thinking": "..."},
      {"type": "text", "text": "the actual response"},
      {"type": "tool_use", "name": "Read", "input": {...}}
    ]
  }
}
```

**`type: "progress"`** — tool execution events (skip these for content extraction)

**`type: "system"`** — system messages (skip these)

**`type: "custom-title"`** — session title if user set one

### Key metadata fields (present on all message types)
- `sessionId` — unique session identifier
- `timestamp` — ISO 8601
- `cwd` — working directory
- `gitBranch` — current git branch
- `forkedFrom.sessionId` — parent session (causal link)
- `version` — Claude Code version

## Requirements

### 1. Create `context_refinery/adapters/claude_code.py`

**Function signature:**
```python
def parse_claude_session(filepath: str) -> dict:
    """
    Reads a Claude Code JSONL session file and returns a dict
    mapping to the CanonicalDocument schema.
    """
```

**Parsing logic:**
1. Read the JSONL file line by line
2. Filter to `type == "user"` and `type == "assistant"` entries only
3. Extract text content from `message.content[]` blocks where `block.type == "text"`
4. Skip `thinking` and `tool_use` blocks (they're internal)
5. Reconstruct conversation as markdown:
   ```markdown
   **User:** <message text>

   **Assistant:** <response text>

   ---

   **User:** <next message>
   ...
   ```
6. Extract metadata from the first event in the file

**Mapping to CanonicalDoc:**
| CanonicalDoc field | Source |
|---|---|
| `id` | `sessionId` from first event |
| `title` | First user message text, truncated to 80 chars. If `custom-title` event exists, use that instead |
| `source.system` | `"claude"` |
| `source.type` | `"json"` |
| `source.original_file_name` | basename of the JSONL file |
| `timestamps.created_at` | `timestamp` of first `user` event |
| `timestamps.updated_at` | `timestamp` of last event |
| `timestamps.ingested_at` | current UTC ISO timestamp |
| `author` | `"claude-code"` |
| `status` | `"scratchpad"` (default per taxonomy) |
| `doc_type` | `"conversation"` |
| `tags` | Extract from `cwd` path — e.g., if cwd contains "MyAPI" add "myapi", if it contains "Obsidian" add "obsidian". Also add `gitBranch` value if present. Max 5 tags. |
| `projects` | Infer from `cwd` — extract repo/project name from path |
| `content.raw_text` | Full reconstructed conversation markdown |
| `content.cleaned_markdown` | Same as raw_text (already markdown) |
| `content.summary` | First user message (truncated to 300 chars) |
| `quality.is_noisy` | `True` if fewer than 2 user messages |
| `quality.warnings` | Add `"single-prompt"` if only 1 user message, `"very-long"` if >50 exchanges |

**Provenance metadata (store in a `provenance` key for future graph work):**
```python
{
    "forked_from_session": forkedFrom.sessionId (if present),
    "cwd": cwd,
    "git_branch": gitBranch,
    "claude_version": version,
    "message_count": {"user": N, "assistant": M},
}
```

### 2. Create a batch scanner function

```python
def scan_claude_sessions(root: str = "~/.claude/projects") -> list[dict]:
    """
    Walk the projects directory tree and parse all session JSONL files.
    Returns a list of CanonicalDocument dicts.
    """
```

This should:
- Recursively find all `.jsonl` files (exclude `subagents/` and `vercel-plugin/` subdirectories)
- Call `parse_claude_session()` on each
- Skip files that fail to parse (log warning, continue)
- Sort results by `created_at` descending

### 3. Add API endpoint

Add to `api/routers/imports.py`:
```python
@router.post("/import/claude-code")
```

Accepts: `{"root": "~/.claude/projects"}` (optional, defaults to standard path)
Returns: list of `CanonicalDocumentResponse` objects

### 4. Tests

Add `tests/test_claude_code.py`:
1. `test_parse_claude_session` — create temp JSONL with mock user/assistant messages, verify schema
2. `test_parse_claude_session_with_fork` — verify forkedFrom is captured in provenance
3. `test_conversation_reconstruction` — verify markdown output has correct User/Assistant format
4. `test_skip_thinking_blocks` — verify thinking/tool_use content is excluded from text
5. `test_scan_claude_sessions` — mock directory with 2 sessions, verify both parsed
6. `test_custom_title` — verify custom-title event overrides first-message title

## Important: Content filtering
Claude Code sessions can be HUGE (2000+ lines). The adapter must:
- Only extract `text` blocks from `user` and `assistant` messages
- Skip all `progress`, `system`, `tool_result` events
- Truncate the reconstructed conversation to 50,000 characters max (with a `"truncated"` warning)
- This keeps Khoj indexing fast and avoids massive documents

## Key files to reference (don't modify)
- `context_refinery/adapters/obsidian.py` — follow this pattern
- `context_refinery/adapters/chatgpt.py` — follow this pattern
- `context_refinery/adapters/codex.py` — the Codex adapter (being built in parallel)
- `api/schemas.py` — `CanonicalDocumentResponse` schema
- `docs/01-taxonomy.md` — valid values

## Do NOT
- Modify any files in `~/.claude/`
- Read subagent JSONL files (they're internal)
- Include thinking blocks or tool_use details in the conversation text
- Add new dependencies
- Change existing adapters
