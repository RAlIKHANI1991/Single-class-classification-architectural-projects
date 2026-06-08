# tests/test_health.py
from fastapi.testclient import TestClient
from api.app import app


client = TestClient(app)


def test_health_endpoint():

    response = client.get("/health")

    assert response.status_code == 200

    result = response.json()

    assert result["status"] == "healthy"