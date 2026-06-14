import requests

url = "https://httpbin.org/post"
payload = {"name": "AAA", "role": "AI Learner"}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Response JSON:", response.json())
