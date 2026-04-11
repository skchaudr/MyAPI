import json
import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

MINIMAL_CONVERSATION = {
    "id": "test-id-123",
    "title": "Test Conversation",
    "create_time": 1700000000.0,
    "update_time": 1700000100.0,
    "mapping": {
        "node1": {
            "id": "node1",
            "parent": None,
            "message": {
                "author": {"role": "user"},
                "content": {"parts": ["Hello!"]}
            }
        }
    },
    "current_node": "node1"
}

def test_import_obsidian_valid():
    content = b"---\ntitle: Test Note\n---\nHello world!"
    files = {"file": ("test.md", content, "text/markdown")}
    response = client.post("/import/obsidian", files=files)
    assert response.status_code == 200
    data = response.json()
    assert data["source"]["system"] == "obsidian"
    assert data["title"] == "Test Note"
    assert "Hello world!" in data["content"]["cleaned_markdown"]

def test_import_obsidian_wrong_ext():
    content = b"Hello world!"
    files = {"file": ("test.txt", content, "text/plain")}
    response = client.post("/import/obsidian", files=files)
    assert response.status_code == 400

def test_import_chatgpt_single():
    content = json.dumps(MINIMAL_CONVERSATION).encode()
    files = {"file": ("chat.json", content, "application/json")}
    response = client.post("/import/chatgpt", files=files)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["source"]["system"] == "chatgpt"
    assert data[0]["title"] == "Test Conversation"

def test_import_chatgpt_batch():
    batch = [MINIMAL_CONVERSATION, MINIMAL_CONVERSATION, MINIMAL_CONVERSATION]
    content = json.dumps(batch).encode()
    files = {"file": ("chat.json", content, "application/json")}
    response = client.post("/import/chatgpt", files=files)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3

def test_import_chatgpt_invalid_json():
    content = b"not json"
    files = {"file": ("chat.json", content, "application/json")}
    response = client.post("/import/chatgpt", files=files)
    assert response.status_code == 422
