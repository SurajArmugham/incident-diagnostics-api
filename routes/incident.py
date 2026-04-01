from flask import Blueprint, request, jsonify
from services.service_checker import check_app_service
from services.db_checker import check_db
from services.log_service import get_logs
from services.analyzer import analyze_logs
import time

incident_bp = Blueprint("incident", __name__)


@incident_bp.route("/incident/analyze", methods=["POST"])
def analyze_incident():
    data = request.json or {}
    start = time.time()

    service_name = data.get("service_name", "dummy_service.py")

    # ---------------------------
    # Run checks
    # ---------------------------
    service_status = check_app_service(service_name)
    db_status = check_db()
    logs = get_logs(500)
    cause = analyze_logs(logs)

    # ---------------------------
    # Overall status
    # ---------------------------
    overall = "UP"

    if service_status["status"] == "DOWN":
        overall = "DOWN"
    elif db_status["status"] == "DOWN":
        overall = "DEGRADED"

    # ---------------------------
    # Response
    # ---------------------------
    return jsonify({
        "incident_id": data.get("incident_id"),
        "service_checked": service_name,
        "service_status": service_status,
        "db_status": db_status,
        "possible_cause": cause,
        "overall_status": overall,
        "execution_time_ms": round((time.time() - start) * 1000, 2)
    })