#Weather Logger v2 (with JSON + Error Handling)
import requests
import json
from datetime import datetime

try:
    url = "https://api.open-meteo.com/v1/forecast?latitude=19.88&longitude=75.32&current_weather=true"
    response = requests.get(url)
    response.raise_for_status()  # raises HTTPError if status != 200

    data = response.json()
    weather = data['current_weather']

    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": weather['temperature'],
        "windspeed": weather['windspeed']
    }

    # Save JSON log
    with open("weather_log.json", "a") as file:
        file.write(json.dumps(log_entry) + "\n")

    print("Weather saved to weather_log.json")

    # Read back logs
    with open("weather_log.json", "r") as file:
        print("\n--- Weather History ---")
        for line in file:
            print(json.loads(line))

except requests.exceptions.RequestException as e:
    print("API call failed:", e)
except Exception as e:
    print("Unexpected error:", e)
