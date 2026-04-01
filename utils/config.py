import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(BASE_DIR, "database", "test.db")
LOG_FILE = os.path.join(BASE_DIR, "logs", "app.log")