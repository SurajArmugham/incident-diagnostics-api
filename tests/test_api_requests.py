import requests
import pytest

import pytest

pytest.skip("Skipping external API tests in CI", allow_module_level=True)

BASE_URL = "http://localhost:8000"


def is_server_up():
    try:
        requests.get(f"{BASE_URL}/health/app", timeout=1)
        return True
    except:
        return False


@pytest.mark.skipif(not is_server_up(), reason="API server not running")
def test_health_app_requests():
    res = requests.get(f"{BASE_URL}/health/app")
    assert res.status_code == 200

# ---------------------------
# Health: API
# ---------------------------
def test_health_app_requests():
    res = requests.get(f"{BASE_URL}/health/app")

    assert res.status_code == 200
    assert res.json()["status"] == "UP"


# ---------------------------
# Health: Service
# ---------------------------
def test_health_service_requests():
    res = requests.get(f"{BASE_URL}/health/dependency/service")

    assert res.status_code == 200
    assert res.json()["status"] in ["UP", "DOWN"]


# ---------------------------
# Health: DB
# ---------------------------
def test_health_db_requests():
    res = requests.get(f"{BASE_URL}/health/dependency/db")

    assert res.status_code == 200
    assert res.json()["status"] in ["UP", "DOWN"]


# ---------------------------
# Incident API
# ---------------------------
def test_incident_analyze_requests():
    payload = {
        "incident_id": "INC12345",
        "service_name": "dummy_service.py"
    }

    res = requests.post(f"{BASE_URL}/incident/analyze", json=payload)

    assert res.status_code == 200

    data = res.json()

    assert "incident_id" in data
    assert "service_status" in data
    assert "db_status" in data
    assert "possible_cause" in data
    assert "overall_status" in data