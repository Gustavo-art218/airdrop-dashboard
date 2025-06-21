import json
from web3 import Web3
from config import RPC_URL, CONTRACT_ADDRESS, ABI_FILE, CLAIM_INDEX_FILE

def load_abi():
    with open(ABI_FILE) as f:
        return json.load(f)

def load_claim_indices():
    with open(CLAIM_INDEX_FILE) as f:
        return json.load(f)

def main():
    web3 = Web3(Web3.HTTPProvider(RPC_URL))
    abi = load_abi()
    contract = web3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=abi)
    claims = load_claim_indices()

    for wallet, index in claims.items():
        claimed = contract.functions.isClaimed(index).call()
        status = "✅ Already Claimed" if claimed else "🟢 Eligible to Claim"
        print(f"{wallet} | Index: {index} | {status}")

if __name__ == "__main__":
    main()
