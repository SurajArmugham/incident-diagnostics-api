from utils.config import DB_PATH
import sqlite3

def check_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("SELECT 1")
        conn.close()

        return {
            "status": "UP",
            "detail": "DB connection successful"
        }

    except Exception as e:
        return {
            "status": "DOWN",
            "error": str(e)
        }