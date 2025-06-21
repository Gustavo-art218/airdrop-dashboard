# utils.py

from config import WALLETS_FILE

def load_wallets():
    """Load wallet addresses from a file."""
    with open(WALLETS_FILE, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def log_result(result):
    """Log result to console."""
    print(f"Wallet: {result['wallet']} | Eligible: {result['eligible']}")
