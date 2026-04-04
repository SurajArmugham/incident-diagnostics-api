import requests
import pytest
import os
from dotenv import load_dotenv

# ---------------------------
# Load environment variables
# ---------------------------
load_dotenv()

BASE_URL = "http://localhost:8000"

# ---------------------------
# API Key (from env)
# ---------------------------
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY not found in environment")

HEADERS = {
    "X-API-Key": API_KEY   # ✅ match auth.py
}


# ---------------------------
# Helper: Check if server is running
# ---------------------------
def is_server_up():
    try:
        res = requests.get(f"{BASE_URL}/health/app", timeout=2)
        return res.status_code == 200
    except Exception:
        return False


# ---------------------------
# Health: API
# ---------------------------
@pytest.mark.skipif(not is_server_up(), reason="API server not running")
def test_health_app_requests():
    res = requests.get(f"{BASE_URL}/health/app", timeout=2)

    assert res.status_code == 200
    assert res.json()["status"] == "UP"


# ---------------------------
# Incident API (Authorized)
# ---------------------------
@pytest.mark.skipif(not is_server_up(), reason="API server not running")
def test_incident_analyze_requests():
    payload = {
        "incident_id": "INC12345",
        "service_name": "dummy_service.py"
    }

    res = requests.post(
        f"{BASE_URL}/incident/analyze",
        json=payload,
        headers=HEADERS,
        timeout=3
    )

    assert res.status_code == 200

    data = res.json()
    assert data["incident_id"] == "INC12345"
    assert "overall_status" in data


# ---------------------------
# Incident API (Unauthorized)
# ---------------------------
@pytest.mark.skipif(not is_server_up(), reason="API server not running")
def test_incident_analyze_requests_unauthorized():
    payload = {
        "incident_id": "INC12345",
        "service_name": "dummy_service.py"
    }

    res = requests.post(
        f"{BASE_URL}/incident/analyze",
        json=payload,
        timeout=3
    )

    assert res.status_code == 401