from app.detector.rules import analyze_login_attempts
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from pathlib import Path
from app.collector.file_monitor import start_file_monitor
from app.collector.system_collector import collect_system_info
from app.database.db import (
    initialize_database,
    save_system_snapshot,
    get_system_snapshots,
    get_security_events
)

app = FastAPI(
    title="CyberShield SIEM",
    description="Python-based Security Information and Event Management System",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
initialize_database()


@app.get("/")
def home():
    return {
        "project": "CyberShield",
        "status": "Online",
        "message": "CyberShield SIEM is running!",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "CyberShield API"
    }


@app.get("/system-info")
def system_info():
    data = collect_system_info()
    save_system_snapshot(data)

    return {
        "message": "System information collected and saved successfully",
        "data": data
    }

@app.get("/live-system-info")
def live_system_info():
    return collect_system_info()
@app.get("/snapshots")
def view_snapshots():
    records = get_system_snapshots()

    return {
        "total_records": len(records),
        "snapshots": records
    }

@app.get("/simulate-login")
def simulate_login(attempts: int = 5, source: str = "192.168.1.10"):
    result = analyze_login_attempts(attempts, source)

    return {
        "test": "Brute Force Detection",
        "attempts": attempts,
        "detection_result": result
    }

@app.get("/security-events")
def view_security_events():
    events = get_security_events()

    return {
        "total_alerts": len(events),
        "security_events": events
    }

# File Integrity Monitoring configuration

FIM_DIRECTORY = (
    Path(__file__).resolve().parent.parent
    / "logs"
    / "fim_test"
)

FIM_DIRECTORY.mkdir(parents=True, exist_ok=True)

file_observer = None


@app.post("/fim/start")
def start_fim():
    global file_observer

    if file_observer is not None and file_observer.is_alive():
        return {"status": "already_running"}

    file_observer = start_file_monitor(str(FIM_DIRECTORY))

    return {
        "status": "started",
        "monitoring_directory": str(FIM_DIRECTORY)
    }


@app.post("/fim/stop")
def stop_fim():
    global file_observer

    if file_observer is None or not file_observer.is_alive():
        return {"status": "not_running"}

    file_observer.stop()
    file_observer.join(timeout=5)
    file_observer = None

    return {"status": "stopped"}
