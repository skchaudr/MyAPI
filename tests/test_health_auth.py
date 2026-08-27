import os
import pytest
from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)

def test_health_unauthorized_missing_key():
    # Setup correct server key
    os.environ["HEALTH_API_KEY"] = "secret-key"

    response = client.get("/health")

    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid or missing API Key"}

def test_health_unauthorized_wrong_key():
    os.environ["HEALTH_API_KEY"] = "secret-key"

    response = client.get("/health", headers={"X-API-Key": "wrong-key"})

    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid or missing API Key"}

def test_health_authorized():
    os.environ["HEALTH_API_KEY"] = "secret-key"

    response = client.get("/health", headers={"X-API-Key": "secret-key"})

    # We mock out Gemini API calls in the health check, or just check that it's a 200
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "model" in data

def test_health_server_misconfigured():
    # Remove the server key
    if "HEALTH_API_KEY" in os.environ:
        del os.environ["HEALTH_API_KEY"]

    response = client.get("/health", headers={"X-API-Key": "secret-key"})

    # Should fail securely with 500 and generic error message
    assert response.status_code == 500
    assert response.json() == {"detail": "An internal server error occurred"}
