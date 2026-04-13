import os
import json
import tempfile
import pytest
from context_refinery.adapters.claude_code import parse_claude_session, scan_claude_sessions

def create_temp_jsonl(events):
    fd, path = tempfile.mkstemp(suffix=".jsonl")
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        for event in events:
            f.write(json.dumps(event) + '\n')
    return path

def test_parse_claude_session():
    events = [
        {"type": "user", "sessionId": "123", "timestamp": "2023-01-01T00:00:00Z", "cwd": "/repo/MyAPI", "gitBranch": "main", "message": {"content": [{"type": "text", "text": "Hello"}]}},
        {"type": "assistant", "timestamp": "2023-01-01T00:01:00Z", "message": {"content": [{"type": "text", "text": "Hi there"}]}}
    ]
    path = create_temp_jsonl(events)
    try:
        doc = parse_claude_session(path)
        assert doc["id"] == "123"
        assert doc["title"] == "Hello"
        assert doc["source"]["system"] == "claude"
        assert doc["source"]["type"] == "json"
        assert doc["timestamps"]["created_at"] == "2023-01-01T00:00:00Z"
        assert doc["timestamps"]["updated_at"] == "2023-01-01T00:01:00Z"
        assert "myapi" in doc["tags"]
        assert "main" in doc["tags"]
        assert "MyAPI" in doc["projects"]
        assert doc["content"]["raw_text"] == "**User:** Hello\n\n**Assistant:** Hi there"
        assert "single-prompt" in doc["quality"]["warnings"]
    finally:
        os.remove(path)

def test_parse_claude_session_with_fork():
    events = [
        {"type": "user", "sessionId": "123", "forkedFrom": {"sessionId": "abc"}, "message": {"content": [{"type": "text", "text": "Fork"}]}}
    ]
    path = create_temp_jsonl(events)
    try:
        doc = parse_claude_session(path)
        assert doc["provenance"]["forked_from_session"] == "abc"
    finally:
        os.remove(path)

def test_conversation_reconstruction():
    events = [
        {"type": "user", "message": {"content": [{"type": "text", "text": "A"}]}},
        {"type": "assistant", "message": {"content": [{"type": "text", "text": "B"}]}},
        {"type": "user", "message": {"content": [{"type": "text", "text": "C"}]}}
    ]
    path = create_temp_jsonl(events)
    try:
        doc = parse_claude_session(path)
        expected = "**User:** A\n\n**Assistant:** B\n\n---\n\n**User:** C"
        assert doc["content"]["raw_text"] == expected
    finally:
        os.remove(path)

def test_skip_thinking_blocks():
    events = [
        {"type": "user", "message": {"content": [{"type": "text", "text": "Help"}]}},
        {"type": "assistant", "message": {"content": [{"type": "thinking", "thinking": "Internal thought"}, {"type": "text", "text": "Answer"}]}}
    ]
    path = create_temp_jsonl(events)
    try:
        doc = parse_claude_session(path)
        assert "Internal thought" not in doc["content"]["raw_text"]
        assert "Answer" in doc["content"]["raw_text"]
    finally:
        os.remove(path)

def test_custom_title():
    events = [
        {"type": "user", "message": {"content": [{"type": "text", "text": "Initial"}]}},
        {"type": "custom-title", "title": "My Custom Title"}
    ]
    path = create_temp_jsonl(events)
    try:
        doc = parse_claude_session(path)
        assert doc["title"] == "My Custom Title"
    finally:
        os.remove(path)

def test_truncation():
    long_text = "A" * 55000
    events = [
        {"type": "user", "message": {"content": [{"type": "text", "text": long_text}]}},
        {"type": "assistant", "message": {"content": [{"type": "text", "text": "B"}]}},
        {"type": "user", "message": {"content": [{"type": "text", "text": "C"}]}}
    ]
    path = create_temp_jsonl(events)
    try:
        doc = parse_claude_session(path)
        assert len(doc["content"]["raw_text"]) <= 50000
        assert "truncated" in doc["quality"]["warnings"]
        assert doc["quality"]["is_noisy"] is False
    finally:
        os.remove(path)

def test_scan_claude_sessions(tmp_path):
    root = tmp_path / "projects"
    root.mkdir()

    # Valid project
    proj = root / "proj"
    proj.mkdir()
    with open(proj / "sess1.jsonl", "w") as f:
        f.write(json.dumps({"type": "user", "timestamp": "2023-01-01T00:00:00Z", "message": {"content": [{"type": "text", "text": "A"}]}}) + "\n")

    # Subagents (should be ignored)
    subagents = root / "subagents"
    subagents.mkdir()
    with open(subagents / "sess2.jsonl", "w") as f:
        f.write(json.dumps({"type": "user", "message": {"content": [{"type": "text", "text": "B"}]}}) + "\n")

    docs = scan_claude_sessions(str(root))
    assert len(docs) == 1
    assert docs[0]["title"] == "A"
