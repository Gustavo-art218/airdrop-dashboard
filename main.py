import json
import requests
from utils import load_wallets, log_result
from config import AIRDROP_API_ENDPOINT, OUTPUT_FILE

def check_airdrop_eligibility(address):
    try:
        response = requests.get(f"{AIRDROP_API_ENDPOINT}/{address}")
        response.raise_for_status()
        data = response.json()
        return data.get("eligible", False), data
    except Exception as e:
        return False, {"error": str(e)}

def main():
    wallets = load_wallets()
    results = []

    for wallet in wallets:
        eligible, data = check_airdrop_eligibility(wallet)
        result = {
            "wallet": wallet,
            "eligible": eligible,
            "data": data
        }
        log_result(result)
        results.append(result)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    main()
