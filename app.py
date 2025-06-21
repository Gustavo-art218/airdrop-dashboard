from flask import Flask, render_template
import json
from contract_scanner import load_abi, load_claim_indices
from web3 import Web3
from config import RPC_URL, CONTRACT_ADDRESS

app = Flask(__name__)

@app.route("/")
def index():
    web3 = Web3(Web3.HTTPProvider(RPC_URL))
    abi = load_abi()
    contract = web3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=abi)
    claims = load_claim_indices()
    results = []

    for wallet, index in claims.items():
        claimed = contract.functions.isClaimed(index).call()
        status = "Already Claimed" if claimed else "Eligible to Claim"
        results.append({"wallet": wallet, "index": index, "status": status})

    return render_template("dashboard.html", results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

