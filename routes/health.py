from flask import Blueprint, jsonify
from services.service_checker import check_app_service
from services.db_checker import check_db

health_bp = Blueprint("health", __name__)


# ---------------------------
# API Health (SELF)
# ---------------------------
@health_bp.route("/health/app")
def health_self():
    return jsonify({
        "status": "UP",
        "service": "incident-api"
    })


# ---------------------------
# Product Service Check (pgrep)
# ---------------------------
@health_bp.route("/health/dependency/service")
def health_service():
    result = check_app_service("dummy_service.py")
    return jsonify(result)


# ---------------------------
# DB Check
# ---------------------------
@health_bp.route("/health/dependency/db")
def health_db():
    result = check_db()
    return jsonify(result)