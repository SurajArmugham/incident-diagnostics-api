import os

# ---------------------------
# API Key (Required)
# ---------------------------
# Fail fast with clear error if not set
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY is not set in environment variables")


# ---------------------------
# Base directory
# ---------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------
# Paths
# ---------------------------
DB_PATH = os.path.join(BASE_DIR, "database", "test.db")
LOG_FILE = os.path.join(BASE_DIR, "logs", "app.log")