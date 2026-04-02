# ---------------------------
# Health: API
# ---------------------------
def test_health_app(client):
    res = client.get("/health/app")

    assert res.status_code == 200
    assert res.json["status"] == "UP"


# ---------------------------
# Health: Service (pgrep)
# ---------------------------
def test_health_service(client):
    res = client.get("/health/dependency/service")

    assert res.status_code == 200
    assert "status" in res.json
    assert res.json["status"] in ["UP", "DOWN"]


# ---------------------------
# Health: DB
# ---------------------------
def test_health_db(client):
    res = client.get("/health/dependency/db")

    assert res.status_code == 200
    assert res.json["status"] in ["UP", "DOWN"]


# ---------------------------
# Incident API
# ---------------------------
def test_incident_analyze(client, auth_headers):
    payload = {
        "incident_id": "INC12345",
        "service_name": "dummy_service.py"
    }

    res = client.post("/incident/analyze", json=payload, headers=auth_headers)

    assert res.status_code == 200

    data = res.json

    assert "incident_id" in data
    assert "service_status" in data
    assert "db_status" in data
    assert "possible_cause" in data
    assert "overall_status" in data


def test_incident_analyze_unauthorized_without_secret(client):
    payload = {
        "incident_id": "INC12345",
        "service_name": "dummy_service.py"
    }

    res = client.post("/incident/analyze", json=payload)

    assert res.status_code == 401
    assert res.json["error"] == "Unauthorized"
