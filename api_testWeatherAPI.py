import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 18.5204,   # Pune
    "longitude": 73.8567,
    "current_weather": True
}

response = requests.get(url, params=params)

print (f"Request URL: {response.url}")

if response.status_code == 200:
    data = response.json()
    print("Temperature:", data["current_weather"]["temperature"], "°C")
else:
    print("Error:", response.status_code)
