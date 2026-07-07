#!/usr/bin/env python3
# Simple CLI: fetch cities or show last N saved reads

import sys
from weather_client import fetch_weather
from persistence import init_db, save_read
import sqlite3

DB = "weather_history.db"

def show_last(n: int):
    with sqlite3.connect(DB) as conn:
        cur = conn.execute("SELECT city, temp, description, ts FROM reads ORDER BY id DESC LIMIT ?", (n,))
        rows = cur.fetchall()
    if not rows:
        print("No saved reads found.")
        return
    for city, temp, desc, ts in rows:
        print(f"{ts} | {city}: {temp}°C, {desc}")

def main(args):
    if not args:
        print("Usage: py APIWeatherProject.py CityName [AnotherCity ...]  OR  py APIWeatherProject.py --last N")
        return
    if args[0] == "--last":
        try:
            n = int(args[1]) if len(args) > 1 else 5
        except ValueError:
            n = 5
        show_last(n)
        return

    init_db()
    for city in args:
        try:
            res = fetch_weather(city)
            print(f"{res['city']}: {res['temp']}°C, {res['description']}")
            save_read(res)
        except Exception as e:
            print(f"Error for {city}: {e}")

if __name__ == "__main__":
    main(sys.argv[1:])
