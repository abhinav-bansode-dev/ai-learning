#API Extract Useful Fields
import requests

url = "https://api.github.com/repos/python/cpython"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Repo:", data["name"])
    print("Stars:", data["stargazers_count"])
    print("Forks:", data["forks_count"])
    print("Open Issues:", data["open_issues_count"])
    print("Last Updated:", data["updated_at"])
else:
    print("Error:", response.status_code)
