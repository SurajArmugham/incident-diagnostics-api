import pytest


# ---------------------------
# Health: API
# ---------------------------
def test_health_app(client):
    # No auth required for health endpoint
    res = client.get("/health/app")

    assert res.status_code == 200

    data = res.get_json()
    assert data["status"] == "UP"


# ---------------------------
# Health: Service (pgrep)
# ---------------------------
def test_health_service(client):
    # No auth required for dependency check
    res = client.get("/health/dependency/service")

    assert res.status_code == 200

    data = res.get_json()
    assert "status" in data
    assert data["status"] in ["UP", "DOWN"]


# ---------------------------
# Health: DB
# ---------------------------
def test_health_db(client):
    # No auth required for DB health
    res = client.get("/health/dependency/db")

    assert res.status_code == 200

    data = res.get_json()
    assert data["status"] in ["UP", "DOWN"]


# ---------------------------
# Incident API (Authorized)
# ---------------------------
def test_incident_analyze(client, api_headers):
    payload = {
        "incident_id": "INC12345",
        "service_name": "dummy_service.py"
    }

    res = client.post(
        "/incident/analyze",
        json=payload,
        headers=api_headers
    )

    assert res.status_code == 200

    data = res.get_json()

    # Validate response structure
    assert data["incident_id"] == "INC12345"
    assert "service_status" in data
    assert "db_status" in data
    assert "possible_cause" in data
    assert "overall_status" in data


# ---------------------------
# Incident API (Unauthorized)
# ---------------------------
def test_incident_analyze_unauthorized(client):
    payload = {
        "incident_id": "INC12345",
        "service_name": "dummy_service.py"
    }

    res = client.post("/incident/analyze", json=payload)

    assert res.status_code == 401