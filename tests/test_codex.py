import json
import os
import shutil
import tempfile
import pytest

from context_refinery.adapters.codex import parse_codex_session, scan_codex_sessions

@pytest.fixture
def mock_codex_dir():
    # Create a temporary root directory for mock command-logs
    temp_root = tempfile.mkdtemp()

    # Session 1: complete files
    session1_dir = os.path.join(temp_root, "2024-01-01", "session-1")
    os.makedirs(session1_dir, exist_ok=True)
    with open(os.path.join(session1_dir, "session-meta.json"), "w") as f:
        json.dump({
            "session_id": "session-1",
            "started_at": "2024-01-01T10:00:00Z",
            "ended_at": "2024-01-01T10:15:00Z",
            "cwd": "/Users/test/repos/projA"
        }, f)
    with open(os.path.join(session1_dir, "summary.json"), "w") as f:
        json.dump({
            "title": "Title 1",
            "initial_intent": "Intent 1",
            "outcome_hint": "Outcome 1",
            "prompt_count": 2,
            "command_count": 5,
            "top_keywords": ["tag1", "tag2"]
        }, f)
    with open(os.path.join(session1_dir, "summary.md"), "w") as f:
        f.write("# Summary 1")

    # Session 2: missing summary.json
    session2_dir = os.path.join(temp_root, "2024-01-02", "session-2")
    os.makedirs(session2_dir, exist_ok=True)
    with open(os.path.join(session2_dir, "session-meta.json"), "w") as f:
        json.dump({
            "session_id": "session-2",
            "started_at": "2024-01-02T10:00:00Z",
            "ended_at": "2024-01-02T10:15:00Z",
            "cwd": "/Users/test/repos/projB"
        }, f)

    # Session 3: noisy session
    session3_dir = os.path.join(temp_root, "2024-01-03", "session-3")
    os.makedirs(session3_dir, exist_ok=True)
    with open(os.path.join(session3_dir, "session-meta.json"), "w") as f:
        json.dump({
            "session_id": "session-3",
            "started_at": "2024-01-03T10:00:00Z",
            "ended_at": "2024-01-03T10:15:00Z",
            "cwd": "/Users/test/repos/projC"
        }, f)
    with open(os.path.join(session3_dir, "summary.json"), "w") as f:
        json.dump({
            "prompt_count": 0,
            "command_count": 0,
        }, f)

    yield temp_root

    # Clean up
    shutil.rmtree(temp_root)

def test_parse_codex_session(mock_codex_dir):
    session1_dir = os.path.join(mock_codex_dir, "2024-01-01", "session-1")
    doc = parse_codex_session(session1_dir)

    assert doc["id"] == "session-1"
    assert doc["title"] == "Title 1"
    assert doc["source"]["system"] == "codex"
    assert doc["source"]["type"] == "json"
    assert doc["timestamps"]["created_at"] == "2024-01-01T10:00:00Z"
    assert doc["timestamps"]["updated_at"] == "2024-01-01T10:15:00Z"
    assert "ingested_at" in doc["timestamps"]
    assert doc["author"] == "codex-cli"
    assert doc["status"] == "scratchpad"
    assert doc["doc_type"] == "conversation"
    assert doc["tags"] == ["tag1", "tag2"]
    assert doc["projects"] == ["projA"]
    assert doc["content"]["raw_text"] == "# Summary 1"
    assert doc["content"]["cleaned_markdown"] == "# Summary 1"
    assert doc["content"]["summary"] == "Intent 1 \u2192 Outcome 1"
    assert doc["quality"]["is_noisy"] is False
    assert len(doc["quality"]["warnings"]) == 0

def test_parse_codex_session_missing_files(mock_codex_dir):
    session2_dir = os.path.join(mock_codex_dir, "2024-01-02", "session-2")
    doc = parse_codex_session(session2_dir)

    assert doc["id"] == "session-2"
    assert doc["title"] == "Untitled Session"
    assert doc["projects"] == ["projB"]
    assert doc["tags"] == []
    assert doc["content"]["raw_text"] == ""
    assert "summary" not in doc["content"]
    assert doc["quality"]["is_noisy"] is True
    assert "no-prompts" in doc["quality"]["warnings"]
    assert "no-commands" in doc["quality"]["warnings"]

def test_scan_codex_sessions(mock_codex_dir):
    docs = scan_codex_sessions(mock_codex_dir)

    assert len(docs) == 3
    # Check sorting: newest first (session-3 > session-2 > session-1)
    assert docs[0]["id"] == "session-3"
    assert docs[1]["id"] == "session-2"
    assert docs[2]["id"] == "session-1"

def test_project_extraction_from_cwd():
    from context_refinery.adapters.codex import _get_project_name
    assert _get_project_name("/Users/saboor/repos/gddp-config") == "gddp-config"
    assert _get_project_name("") == "unknown"
    assert _get_project_name("/") == "unknown"
    assert _get_project_name("just-a-folder") == "just-a-folder"
