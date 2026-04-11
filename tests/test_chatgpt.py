import pytest
from datetime import datetime
from context_refinery.adapters.chatgpt import parse_chatgpt_conversation

def test_parse_chatgpt_conversation_basic():
    # Mock conversation with a single branch
    mock_conversation = {
        "title": "Test Conversation",
        "create_time": 1672531200,  # 2023-01-01 00:00:00 UTC
        "update_time": 1672534800,  # 2023-01-01 01:00:00 UTC
        "current_node": "node3",
        "mapping": {
            "node1": {
                "id": "node1",
                "message": {
                    "author": {"role": "system"},
                    "content": {"parts": ["You are a helpful assistant."]}
                },
                "parent": None
            },
            "node2": {
                "id": "node2",
                "message": {
                    "author": {"role": "user"},
                    "content": {"parts": ["Hello!"]}
                },
                "parent": "node1"
            },
            "node3": {
                "id": "node3",
                "message": {
                    "author": {"role": "assistant"},
                    "content": {"parts": ["Hi there! How can I help?"]}
                },
                "parent": "node2"
            }
        }
    }

    doc = parse_chatgpt_conversation(mock_conversation)

    assert doc["title"] == "Test Conversation"
    assert doc["source"]["system"] == "chatgpt"
    assert doc["doc_type"] == "conversation"

    # Assert timestamps (ignoring ingested_at which is dynamic)
    assert "2023-01-01" in doc["timestamps"]["created_at"]
    assert "2023-01-01" in doc["timestamps"]["updated_at"]

    # Assert markdown output
    markdown = doc["content"]["cleaned_markdown"]
    assert "**System**: You are a helpful assistant." in markdown
    assert "**User**: Hello!" in markdown
    assert "**Assistant**: Hi there! How can I help?" in markdown

def test_parse_chatgpt_conversation_branching():
    # Mock conversation with multiple branches
    # Node1 -> Node2 -> Node3 (abandoned branch)
    #               \-> Node4 (current active branch)
    mock_conversation = {
        "current_node": "node4",
        "mapping": {
            "node1": {
                "id": "node1",
                "message": {
                    "author": {"role": "user"},
                    "content": {"parts": ["What is 2+2?"]}
                },
                "parent": None
            },
            "node2": {
                "id": "node2",
                "message": {
                    "author": {"role": "assistant"},
                    "content": {"parts": ["It is 4."]}
                },
                "parent": "node1"
            },
            "node3": {
                "id": "node3",
                "message": {
                    "author": {"role": "user"},
                    "content": {"parts": ["Wrong branch!"]}
                },
                "parent": "node2"
            },
            "node4": {
                "id": "node4",
                "message": {
                    "author": {"role": "user"},
                    "content": {"parts": ["What is 3+3?"]}
                },
                "parent": "node2"
            }
        }
    }

    doc = parse_chatgpt_conversation(mock_conversation)
    markdown = doc["content"]["cleaned_markdown"]

    assert "**User**: What is 2+2?" in markdown
    assert "**Assistant**: It is 4." in markdown
    assert "**User**: What is 3+3?" in markdown
    # The abandoned branch shouldn't be included
    assert "Wrong branch!" not in markdown

def test_parse_chatgpt_conversation_empty_or_missing_message():
    mock_conversation = {
        "current_node": "node2",
        "mapping": {
            "node1": {
                "id": "node1",
                "message": None,  # Missing message
                "parent": None
            },
            "node2": {
                "id": "node2",
                "message": {
                    "author": {"role": "user"},
                    "content": {"parts": [""]} # Empty string part
                },
                "parent": "node1"
            }
        }
    }

    doc = parse_chatgpt_conversation(mock_conversation)
    # Missing/empty messages should be skipped
    assert doc["content"]["cleaned_markdown"] == ""
