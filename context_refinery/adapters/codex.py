import json
import logging
import os
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

def _get_project_name(cwd: str) -> str:
    """Extract project name from cwd path."""
    if not cwd or cwd == "/":
        return "unknown"
    return os.path.basename(os.path.normpath(cwd))

def parse_codex_session(session_dir: str) -> dict:
    """
    Reads a Codex session directory and returns a dict
    mapping to the CanonicalDocument schema.
    """
    meta_path = os.path.join(session_dir, "session-meta.json")
    summary_json_path = os.path.join(session_dir, "summary.json")
    summary_md_path = os.path.join(session_dir, "summary.md")

    if not os.path.isfile(meta_path):
        raise FileNotFoundError(f"Missing session-meta.json in {session_dir}")

    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    summary = {}
    if os.path.isfile(summary_json_path):
        with open(summary_json_path, "r", encoding="utf-8") as f:
            summary = json.load(f)

    markdown_content = ""
    if os.path.isfile(summary_md_path):
        with open(summary_md_path, "r", encoding="utf-8") as f:
            markdown_content = f.read()

    session_id = meta.get("session_id", "unknown-id")
    started_at = meta.get("started_at")
    ended_at = meta.get("ended_at")
    cwd = meta.get("cwd", "")

    title = summary.get("title")
    initial_intent = summary.get("initial_intent", "")
    if not title:
        title = initial_intent[:80] if initial_intent else "Untitled Session"

    tags = summary.get("top_keywords", [])

    project = _get_project_name(cwd)
    projects = [project] if project != "unknown" else []

    outcome_hint = summary.get("outcome_hint", "")
    content_summary = ""
    if initial_intent and outcome_hint:
        content_summary = f"{initial_intent} → {outcome_hint}"
    elif initial_intent:
        content_summary = initial_intent
    elif outcome_hint:
        content_summary = outcome_hint

    prompt_count = summary.get("prompt_count", 0)
    command_count = summary.get("command_count", 0)

    is_noisy = prompt_count == 0 or command_count == 0
    warnings = []
    if prompt_count == 0:
        warnings.append("no-prompts")
    if command_count == 0:
        warnings.append("no-commands")

    original_file_name = session_dir
    if "~/.codex/command-logs" in session_dir:
        original_file_name = session_dir.split("~/.codex/command-logs/")[-1]
    elif "/.codex/command-logs" in session_dir:
        original_file_name = session_dir.split("/.codex/command-logs/")[-1]

    canonical_doc = {
        "id": session_id,
        "title": title,
        "source": {
            "system": "codex",
            "type": "json",
            "original_file_name": original_file_name
        },
        "timestamps": {
            "created_at": started_at,
            "updated_at": ended_at,
            "ingested_at": datetime.now(timezone.utc).isoformat()
        },
        "author": "codex-cli",
        "status": "scratchpad",
        "doc_type": "conversation",
        "tags": tags,
        "projects": projects,
        "content": {
            "raw_text": markdown_content,
            "cleaned_markdown": markdown_content,
        },
        "quality": {
            "is_noisy": is_noisy,
            "warnings": warnings
        }
    }

    if content_summary:
        canonical_doc["content"]["summary"] = content_summary

    return canonical_doc

def scan_codex_sessions(root: str = "~/.codex/command-logs") -> list[dict]:
    """
    Walk the command-logs directory tree and parse all sessions.
    Returns a list of CanonicalDocument dicts sorted by created_at descending.
    """
    expanded_root = os.path.expanduser(root)
    results = []

    if not os.path.isdir(expanded_root):
        logger.warning(f"Codex command-logs root not found: {expanded_root}")
        return results

    for dirpath, dirnames, filenames in os.walk(expanded_root):
        if "session-meta.json" in filenames:
            try:
                doc = parse_codex_session(dirpath)
                results.append(doc)
            except Exception as e:
                logger.warning(f"Failed to parse session at {dirpath}: {e}")

    # Sort results by created_at descending
    def get_created_at(d):
        created_at = d.get("timestamps", {}).get("created_at")
        if created_at:
            return created_at
        return ""

    results.sort(key=get_created_at, reverse=True)
    return results
