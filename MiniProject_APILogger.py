#Mini Project: API Logger [API Integration + File Handling]
import requests

# Step 1: Call an API (Joke API)
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)

if response.status_code == 200:
    joke = response.json()
    joke_text = f"{joke['setup']} - {joke['punchline']}\n"

    # Step 2: Save to file
    with open("api_log1.txt", "w") as file:
        file.write(joke_text)

    print("Joke saved to api_log1.txt")

    # Step 3: Read back from file
    with open("api_log1.txt", "r") as file:
        print("\n--- Saved Jokes ---")
        print(file.read())
else:
    print("Failed to fetch joke")
