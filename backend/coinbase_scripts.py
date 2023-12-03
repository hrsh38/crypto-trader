from coinbase.wallet.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

def get_total_balance(api_key, api_secret):
    # Initialize the client with your API credentials
    client = Client(api_key, api_secret)

    # Initialize total balance
    total_balance = 0.0

    # Get all accounts
    accounts = client.get_accounts()

    # Loop through accounts and sum up the balances
    for wallet in accounts.data:
        balance = wallet.balance
        # Convert balance to a float and add it to total balance
        total_balance += float(balance.amount)

    return total_balance

h = get_total_balance(api_key, api_secret)
print(h)