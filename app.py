# ---------------------------
# Load environment variables FIRST
# ---------------------------
from dotenv import load_dotenv
load_dotenv()


# ---------------------------
# Core Flask imports
# ---------------------------
from flask import Flask
import logging


# ---------------------------
# Configure logging
# ---------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)


# ---------------------------
# Import routes (after env is loaded)
# ---------------------------
from routes.health import health_bp
from routes.incident import incident_bp


# ---------------------------
# Create Flask app instance
# ---------------------------
app = Flask(__name__)


# ---------------------------
# Register Blueprints
# ---------------------------
app.register_blueprint(health_bp)
app.register_blueprint(incident_bp)


# ---------------------------
# Entry point
# ---------------------------
if __name__ == "__main__":
    # Run app locally
    app.run(port=8000)