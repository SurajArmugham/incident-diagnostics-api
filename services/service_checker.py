import subprocess

def check_app_service(service_name="dummy_service.py"):
    try:
        result = subprocess.run(
            ["pgrep", "-f", service_name],
            capture_output=True,
            text=True
        )

        if result.stdout.strip():
            return {
                "status": "UP",
                "detail": f"{service_name} is running"
            }
        else:
            return {
                "status": "DOWN",
                "detail": f"{service_name} not found"
            }

    except Exception as e:
        return {
            "status": "DOWN",
            "error": str(e)
        }