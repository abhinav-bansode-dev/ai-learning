#Weather Translator
#This combines API requests, authentication, JSON parsing, and file handling

#Get Weather Data

import requests
import json

api_key = "73f8ed710635fc29636b16ecf8141b8c"
city = "Mumbai"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()
print(data)

#Parse JSON Response

if response.status_code == 200 and "main" in data:
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    print(f"Weather in {city}: {temp}°C, {desc}, Humidity: {humidity}%")
else:
    print("Error:", data.get("message", "Unknown error"))


# Translate Output
translate_url = "https://libretranslate.de/translate"
payload = {
    "q": f"Weather in {city}: {temp}°C, {desc}, Humidity: {humidity}%",
    "source": "en",
    "target": "hi"   # Hindi
}
translated = requests.post(translate_url, data=payload).json()
print("Translated:", translated["translatedText"])

# Save to File
report = {
    "city": city,
    "temperature": temp,
    "description": desc,
    "humidity": humidity,
    "translated": translated.get("translatedText", "")
}

with open("weather_report.json", "a", encoding="utf-8") as f:
    f.write(json.dumps(report, ensure_ascii=False) + "\n")

