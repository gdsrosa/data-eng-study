import os
from dotenv import load_dotenv
import requests

load_dotenv()

def get_btc_price():
    url = f"https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin&x_cg_demo_api_key={os.getenv('COINGECKO_API_KEY')}"
    response = requests.get(url)
    data = response.json()
    return data

print("BTC Price: ", get_btc_price())