import subprocess
from utils.config import LOG_FILE

def get_logs(lines=500):
    try:
        result = subprocess.run(
            ["tail", "-n", str(lines), LOG_FILE],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return f"Error reading logs: {result.stderr}"

        return result.stdout

    except Exception as e:
        return f"Error reading logs: {str(e)}"