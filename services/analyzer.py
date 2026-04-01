def analyze_logs(logs):
    logs = logs.lower()

    if "connection refused" in logs:
        return "Possible DB connection issue"

    elif "timeout" in logs:
        return "Service timeout detected"

    elif "out of memory" in logs:
        return "Memory issue detected"

    elif "error" in logs:
        return "Generic application error"

    return "No obvious issue detected"