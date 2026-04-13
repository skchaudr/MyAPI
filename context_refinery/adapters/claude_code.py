import os
import json
import logging
from datetime import datetime, timezone
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

def parse_claude_session(filepath: str) -> Dict[str, Any]:
    """
    Reads a Claude Code JSONL session file and returns a dict
    mapping to the CanonicalDocument schema.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    events = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass

    if not events:
        raise ValueError(f"Empty or invalid JSONL file: {filepath}")

    first_event = events[0]
    session_id = first_event.get("sessionId", "unknown")
    cwd = first_event.get("cwd", "")
    git_branch = first_event.get("gitBranch", "")
    claude_version = first_event.get("version", "")
    forked_from = first_event.get("forkedFrom", {})
    forked_from_session = forked_from.get("sessionId") if isinstance(forked_from, dict) else None

    custom_title = None
    user_messages = []
    assistant_messages = []

    first_user_event = None
    last_event_timestamp = first_event.get("timestamp")

    markdown_parts = []

    # Message counts
    user_count = 0
    assistant_count = 0

    for event in events:
        event_type = event.get("type")
        timestamp = event.get("timestamp")
        if timestamp:
            last_event_timestamp = timestamp

        if event_type == "custom-title":
            custom_title = event.get("title")
        elif event_type == "user":
            user_count += 1
            if not first_user_event:
                first_user_event = event

            message = event.get("message", {})
            content_blocks = message.get("content", [])
            text_content = ""
            for block in content_blocks:
                if block.get("type") == "text":
                    text_content += block.get("text", "")

            if text_content:
                if markdown_parts:
                    markdown_parts.append("---")
                markdown_parts.append(f"**User:** {text_content.strip()}")
                user_messages.append(text_content.strip())

        elif event_type == "assistant":
            assistant_count += 1
            message = event.get("message", {})
            content_blocks = message.get("content", [])
            text_content = ""
            for block in content_blocks:
                if block.get("type") == "text":
                    text_content += block.get("text", "")

            if text_content:
                markdown_parts.append(f"**Assistant:** {text_content.strip()}")
                assistant_messages.append(text_content.strip())

    raw_text = "\n\n".join(markdown_parts)

    warnings = []
    if len(raw_text) > 50000:
        raw_text = raw_text[:50000]
        warnings.append("truncated")

    if user_count == 1:
        warnings.append("single-prompt")
    if user_count > 50:
        warnings.append("very-long")

    first_user_text = user_messages[0] if user_messages else ""

    if custom_title:
        title = custom_title
    else:
        title = first_user_text[:80] if first_user_text else "Untitled Claude Session"

    # Tags extraction
    tags = []
    if cwd:
        cwd_lower = cwd.lower()
        if "myapi" in cwd_lower:
            tags.append("myapi")
        if "obsidian" in cwd_lower:
            tags.append("obsidian")
    if git_branch:
        tags.append(git_branch.lower())

    tags = list(set(tags))[:5] # Max 5 tags

    # Projects extraction
    projects = []
    if cwd:
        project_name = os.path.basename(os.path.normpath(cwd))
        if project_name:
            projects.append(project_name)

    created_at = first_user_event.get("timestamp") if first_user_event else first_event.get("timestamp")
    updated_at = last_event_timestamp
    ingested_at = datetime.now(timezone.utc).isoformat()

    summary = first_user_text[:300] if first_user_text else ""

    doc = {
        "id": session_id,
        "title": title,
        "source": {
            "system": "claude",
            "type": "json",
            "original_file_name": os.path.basename(filepath)
        },
        "timestamps": {
            "created_at": created_at,
            "updated_at": updated_at,
            "ingested_at": ingested_at
        },
        "author": "claude-code",
        "status": "scratchpad",
        "doc_type": "conversation",
        "tags": tags,
        "projects": projects,
        "content": {
            "raw_text": raw_text,
            "cleaned_markdown": raw_text,
        },
        "quality": {
            "is_noisy": user_count < 2,
            "warnings": warnings
        },
        "provenance": {
            "forked_from_session": forked_from_session,
            "cwd": cwd,
            "git_branch": git_branch,
            "claude_version": claude_version,
            "message_count": {"user": user_count, "assistant": assistant_count}
        }
    }

    if summary:
        doc["content"]["summary"] = summary

    return doc

def scan_claude_sessions(root: str = "~/.claude/projects") -> List[Dict[str, Any]]:
    """
    Walk the projects directory tree and parse all session JSONL files.
    Returns a list of CanonicalDocument dicts.
    """
    root_path = os.path.expanduser(root)
    documents = []

    if not os.path.exists(root_path):
        logger.warning(f"Claude projects directory not found: {root_path}")
        return documents

    for dirpath, dirnames, filenames in os.walk(root_path):
        # Exclude subagents and vercel-plugin
        dirnames[:] = [d for d in dirnames if d not in ("subagents", "vercel-plugin")]

        for filename in filenames:
            if filename.endswith(".jsonl"):
                filepath = os.path.join(dirpath, filename)
                try:
                    doc = parse_claude_session(filepath)
                    documents.append(doc)
                except Exception as e:
                    logger.warning(f"Failed to parse Claude session {filepath}: {e}")

    # Sort results by created_at descending
    def get_created_at(doc):
        ts = doc.get("timestamps", {}).get("created_at")
        if not ts:
            return ""
        return ts

    documents.sort(key=get_created_at, reverse=True)
    return documents
