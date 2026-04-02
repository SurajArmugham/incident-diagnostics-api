import os

import pytest
import requests

pytest.skip("Skipping external API tests in CI", allow_module_level=True)

BASE_URL = "http://localhost:8000"
API_SECRET_KEY = os.getenv("API_SECRET_KEY", "test-secret-key")
AUTH_HEADERS = {"X-API-KEY": API_SECRET_KEY}


def is_server_up():
    try:
        requests.get(f"{BASE_URL}/health/app", timeout=1)
        return True
    except requests.RequestException:
        return False


# ---------------------------
# Health: API
# ---------------------------
@pytest.mark.skipif(not is_server_up(), reason="API server not running")
def test_health_app_requests():
    res = requests.get(f"{BASE_URL}/health/app")

    assert res.status_code == 200
    assert res.json()["status"] == "UP"


# ---------------------------
# Health: Service
# ---------------------------
@pytest.mark.skipif(not is_server_up(), reason="API server not running")
def test_health_service_requests():
    res = requests.get(f"{BASE_URL}/health/dependency/service")

    assert res.status_code == 200
    assert res.json()["status"] in ["UP", "DOWN"]


# ---------------------------
# Health: DB
# ---------------------------
@pytest.mark.skipif(not is_server_up(), reason="API server not running")
def test_health_db_requests():
    res = requests.get(f"{BASE_URL}/health/dependency/db")

    assert res.status_code == 200
    assert res.json()["status"] in ["UP", "DOWN"]


# ---------------------------
# Incident API
# ---------------------------
@pytest.mark.skipif(not is_server_up(), reason="API server not running")
def test_incident_analyze_requests():
    payload = {
        "incident_id": "INC12345",
        "service_name": "dummy_service.py"
    }

    res = requests.post(f"{BASE_URL}/incident/analyze", json=payload, headers=AUTH_HEADERS)

    assert res.status_code == 200

    data = res.json()

    assert "incident_id" in data
    assert "service_status" in data
    assert "db_status" in data
    assert "possible_cause" in data
    assert "overall_status" in data
