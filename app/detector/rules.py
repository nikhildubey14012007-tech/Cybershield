
from app.database.db import save_security_event


def detect_brute_force(attempt_count, source):
    if attempt_count >= 5:
        return {
            "detected": True,
            "event_type": "BRUTE_FORCE_ATTEMPT",
            "source": source,
            "description": (
                f"{attempt_count} failed login attempts "
                f"detected from {source}"
            ),
            "severity": "HIGH"
        }

    return {
        "detected": False,
        "message": "No brute-force threshold reached"
    }


def analyze_login_attempts(attempt_count, source):
    result = detect_brute_force(attempt_count, source)

    if result["detected"]:
        save_security_event(
            result["event_type"],
            result["source"],
            result["description"],
            result["severity"]
        )

    return result
