import os

from flask import Flask, jsonify, request
from routes.health import health_bp
from routes.incident import incident_bp

app = Flask(__name__)
app.config["API_SECRET_KEY"] = os.getenv("API_SECRET_KEY")


@app.before_request
def validate_api_secret_key():
    """Require X-API-KEY for non-health API endpoints."""
    if request.path.startswith("/health"):
        return None

    configured_secret = app.config.get("API_SECRET_KEY")
    if not configured_secret:
        return jsonify({"error": "API secret key is not configured"}), 500

    request_secret = request.headers.get("X-API-KEY")
    if request_secret != configured_secret:
        return jsonify({"error": "Unauthorized"}), 401

    return None


app.register_blueprint(health_bp)
app.register_blueprint(incident_bp)


if __name__ == "__main__":
    app.run(port=8000)
