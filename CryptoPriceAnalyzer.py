import requests
import csv
import datetime

# Step 1: Fetch API Data (BTC + ETH)
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    btc_price = data["bitcoin"]["usd"]
    eth_price = data["ethereum"]["usd"]
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"Bitcoin: ${btc_price}, Ethereum: ${eth_price} at {date}")

    # Step 2: Save to CSV
    with open("crypto_prices.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, btc_price, eth_price])

    # Step 3: Read Back & Analyze
    btc_prices, eth_prices = [], []
    with open("crypto_prices.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                btc_prices.append(float(row[1]))
                eth_prices.append(float(row[2]))

    if btc_prices and eth_prices:
        print("\n--- Analysis ---")
        print(f"BTC → Avg: ${sum(btc_prices)/len(btc_prices):.2f}, High: ${max(btc_prices):.2f}, Low: ${min(btc_prices):.2f}")
        print(f"ETH → Avg: ${sum(eth_prices)/len(eth_prices):.2f}, High: ${max(eth_prices):.2f}, Low: ${min(eth_prices):.2f}")
else:
    print("Error fetching crypto data:", response.status_code)
