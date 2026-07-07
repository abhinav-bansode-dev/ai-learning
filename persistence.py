#Unit Testing
"""project/
├─ APIWeatherProject.py        # main script (imports fetch_weather)
├─ weather_client.py           # fetch_weather(city) -> dict
├─ persistence.py              # save_read(record)
└─ tests/
   └─ test_weather_client.py
"""

import sqlite3
from datetime import datetime
from typing import Dict

DB = "weather_history.db"

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS reads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temp REAL,
            description TEXT,
            ts TEXT
        )""")

def save_read(record: Dict):
    with sqlite3.connect(DB) as conn:
        conn.execute(
            "INSERT INTO reads (city, temp, description, ts) VALUES (?, ?, ?, ?)",
            (record["city"], record["temp"], record["description"], datetime.utcnow().isoformat())
        )
