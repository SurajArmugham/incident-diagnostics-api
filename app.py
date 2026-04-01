from flask import Flask
from routes.health import health_bp
from routes.incident import incident_bp

app = Flask(__name__)

app.register_blueprint(health_bp)
app.register_blueprint(incident_bp)


if __name__ == "__main__":
    app.run(port=8000)