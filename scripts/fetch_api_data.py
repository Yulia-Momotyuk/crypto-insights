import requests
import pandas as pd
from datetime import datetime, timezone
import os

# 1. Parameters
coins = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    "solana": "SOL",
    "ripple": "XRP",
    "cardano": "ADA"
}

# 2. Function to fetch data via API
def fetch_coin_data(coin_id, symbol):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": "usd", "days": "365"}
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        # Check if prices exist
        if "prices" not in data:
            print(f"⚠️ No data for {coin_id}: {data}")
            return pd.DataFrame()
        
        prices = data["prices"]
        market_caps = data.get("market_caps", [])
        volumes = data.get("total_volumes", [])
        
        df = pd.DataFrame({
            "date": [datetime.fromtimestamp(x[0] / 1000, tz=timezone.utc).date() for x in prices],
            "coin_id": coin_id,
            "symbol": symbol,
            "price_usd": [x[1] for x in prices],
            "market_cap_usd": [x[1] for x in market_caps] if market_caps else [None]*len(prices),
            "volume_usd": [x[1] for x in volumes] if volumes else [None]*len(prices)
        })
        return df
    except Exception as e:
        print(f"❌ Error for {coin_id}: {e}")
        return pd.DataFrame()

# 3. Fetching and merging data for all coins
all_data = pd.concat([fetch_coin_data(cid, sym) for cid, sym in coins.items()],
                     ignore_index=True)

# 4. Save CSV
os.makedirs("data", exist_ok=True)
all_data.to_csv("data/crypto_market.csv", index=False)

print("✅ Done! File crypto_market.csv saved in data folder")
all_data.head()