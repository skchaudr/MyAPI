import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_enrich_success(mocker):
    mocker.patch(
        "context_refinery.services.GeminiService.enrich",
        return_value={"summary": "test", "doc_type": "note", "tags": ["a"]}
    )
    response = client.post("/enrich", json={"content": "hello"})
    assert response.status_code == 200
    data = response.json()
    assert data["summary"] == "test"
    assert data["doc_type"] == "note"
    assert data["tags"] == ["a"]

def test_enrich_empty_content(mocker):
    mocker.patch(
        "context_refinery.services.GeminiService.enrich",
        return_value={"summary": "empty", "doc_type": "unknown", "tags": []}
    )
    response = client.post("/enrich", json={"content": ""})
    assert response.status_code == 200
    data = response.json()
    assert data["summary"] == "empty"
    assert data["doc_type"] == "unknown"
    assert data["tags"] == []

def test_enrich_missing_body():
    response = client.post("/enrich", json={})
    assert response.status_code == 422

def test_enrich_no_api_key(mocker):
    mocker.patch(
        "context_refinery.services.GeminiService.enrich",
        side_effect=Exception("GEMINI_API_KEY is not set...")
    )
    response = client.post("/enrich", json={"content": "hello"})
    assert response.status_code == 503
    assert "GEMINI_API_KEY not configured" in response.json()["detail"]
