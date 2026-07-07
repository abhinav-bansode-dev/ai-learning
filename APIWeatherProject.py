#!/usr/bin/env python3
# Minimal weather fetcher for learners

import os
import requests
from requests.exceptions import RequestException, HTTPError

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city: str) -> str:
    if not API_KEY:
        raise SystemExit("Set OPENWEATHER_API_KEY environment variable and rerun.")
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        resp = requests.get(BASE_URL, params=params, timeout=8)
        resp.raise_for_status()
        data = resp.json()
        name = data.get("name", city)
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"{name}: {temp}°C, {desc}"
    except HTTPError as e:
        return f"HTTP error for {city}: {e}"
    except (KeyError, ValueError):
        return f"Unexpected response for {city}."
    except RequestException as e:
        return f"Network error for {city}: {e}"

if __name__ == "__main__":
    cities = ["Aurangabad", "Mumbai", "InvalidCityName"]
    for c in cities:
        print(fetch_weather(c))
