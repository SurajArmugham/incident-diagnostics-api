from flask import Blueprint, request, jsonify
from services.service_checker import check_app_service
from services.db_checker import check_db
from services.log_service import get_logs
from services.analyzer import analyze_logs
from utils.auth import require_api_key

import time
import logging

incident_bp = Blueprint("incident", __name__)

logger = logging.getLogger(__name__)


@incident_bp.route("/incident/analyze", methods=["POST"])
def analyze_incident():
    # ---------------------------
    # Auth check
    # ---------------------------
    require_api_key()

    start = time.time()

    try:
        # ---------------------------
        # Validate request JSON
        # ---------------------------
        if not request.is_json:
            return jsonify({"error": "Invalid JSON request"}), 400

        data = request.get_json()

        incident_id = data.get("incident_id")
        service_name = data.get("service_name", "dummy_service.py")

        logger.info(f"Incident received: {incident_id} for service {service_name}")

        # ---------------------------
        # Run checks
        # ---------------------------
        service_status = check_app_service(service_name)
        db_status = check_db()
        logs = get_logs(500)
        cause = analyze_logs(logs)

        # ---------------------------
        # Determine overall status
        # ---------------------------
        if service_status["status"] == "DOWN":
            overall = "DOWN"
        elif db_status["status"] == "DOWN":
            overall = "DEGRADED"
        else:
            overall = "UP"

        # ---------------------------
        # Build response
        # ---------------------------
        response = {
            "incident_id": incident_id,
            "service_checked": service_name,
            "service_status": service_status,
            "db_status": db_status,
            "possible_cause": cause,
            "overall_status": overall,
            "execution_time_ms": round((time.time() - start) * 1000, 2)
        }

        logger.info(f"Incident processed: {incident_id} → {overall}")

        return jsonify(response)

    except Exception as e:
        logger.exception("Error processing incident")

        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500