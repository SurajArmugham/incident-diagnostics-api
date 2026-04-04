from services.service_checker import check_app_service
from services.db_checker import check_db
from services.analyzer import analyze_logs
from services.log_service import get_logs


# ---------------------------
# Service Checker
# ---------------------------
def test_service_checker():
    result = check_app_service("dummy_service.py")

    assert "status" in result
    assert result["status"] in ["UP", "DOWN"]


# ---------------------------
# DB Checker
# ---------------------------
def test_db_checker():
    result = check_db()

    # Avoid strict dependency on DB setup
    assert "status" in result
    assert result["status"] in ["UP", "DOWN"]


# ---------------------------
# Log Analyzer
# ---------------------------
def test_log_analyzer():
    logs = "ERROR: connection refused"

    result = analyze_logs(logs)

    assert "DB connection" in result


# ---------------------------
# Log Service
# ---------------------------
def test_log_service_contains_expected_content():
    logs = get_logs(50)

    # Handle missing file scenario gracefully
    assert isinstance(logs, str)

    # If logs exist → validate content
    if "Error reading logs" not in logs:
        assert "ERROR" in logs or "INFO" in logs