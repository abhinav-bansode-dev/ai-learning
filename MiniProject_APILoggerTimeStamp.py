#Weather Logger Project with timestamp

import requests
from datetime import datetime

# Step 1: Call Weather API (Open-Meteo free API)
url = "https://api.open-meteo.com/v1/forecast?latitude=19.88&longitude=75.32&current_weather=true"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = data['current_weather']
    log_entry = f"{datetime.now()} - Temp: {weather['temperature']}°C, Wind: {weather['windspeed']} km/h\n"

    # Step 2: Save to file
    with open("weather_log.txt", "a") as file:
        file.write(log_entry)

    print("Weather saved to weather_log.txt")

    # Step 3: Read back
    with open("weather_log.txt", "r") as file:
        print("\n--- Weather History ---")
        print(file.read())
else:
    print("Failed to fetch weather")
