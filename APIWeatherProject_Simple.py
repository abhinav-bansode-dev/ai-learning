#!/usr/bin/env python3
# Simple CLI to fetch weather for one or more cities

import os
import sys
from weather_client import fetch_weather
from persistence import init_db, save_read

def main(args):
    if not args:
        print("Usage: py APIWeatherProject.py CityName [AnotherCity ...]")
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
    # skip the script name
    main(sys.argv[1:])
