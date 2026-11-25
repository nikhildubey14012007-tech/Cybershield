
import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).resolve().parent / "cybershield.db"


def initialize_database():
    connection = sqlite3.connect(DB_PATH)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS system_snapshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hostname TEXT,
            operating_system TEXT,
            cpu_usage REAL,
            memory_usage REAL,
            disk_usage REAL,
            timestamp TEXT
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS security_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_type TEXT NOT NULL,
            source TEXT,
            description TEXT,
            severity TEXT,
            timestamp TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_system_snapshot(data):
    connection = sqlite3.connect(DB_PATH)

    connection.execute("""
        INSERT INTO system_snapshots
        (hostname, operating_system, cpu_usage,
         memory_usage, disk_usage, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["hostname"],
        data["operating_system"],
        data["cpu_usage_percent"],
        data["memory_used_percent"],
        data["disk_used_percent"],
        data["timestamp"]
    ))

    connection.commit()
    connection.close()

def get_system_snapshots():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    cursor = connection.execute("""
        SELECT * FROM system_snapshots
        ORDER BY id DESC
    """)

    records = [dict(row) for row in cursor.fetchall()]

    connection.close()
    return records

def save_security_event(event_type, source, description, severity):
    connection = sqlite3.connect(DB_PATH)

    connection.execute("""
        INSERT INTO security_events
        (event_type, source, description, severity, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (
        event_type,
        source,
        description,
        severity,
        datetime.now().isoformat()
    ))

    connection.commit()
    connection.close()

def get_security_events():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    cursor = connection.execute("""
        SELECT * FROM security_events
        ORDER BY id DESC
    """)

    events = [dict(row) for row in cursor.fetchall()]

    connection.close()
    return events
