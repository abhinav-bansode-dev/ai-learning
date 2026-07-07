#Unit Testing
"""project/
├─ APIWeatherProject.py        # main script (imports fetch_weather)
├─ weather_client.py           # fetch_weather(city) -> dict
├─ persistence.py              # save_read(record)
└─ tests/
   └─ test_weather_client.py
"""

import os
import requests
from requests.exceptions import RequestException, HTTPError

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city: str) -> dict:
    if not API_KEY:
        raise RuntimeError("OPENWEATHER_API_KEY not set")
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    resp = requests.get(BASE_URL, params=params, timeout=8)
    resp.raise_for_status()
    data = resp.json()
    return {
        "city": data.get("name", city),
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "raw": data
    }
