import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("Currency_Exchange_API_KEY")

amount = input("Enter the amount of money you want to convert: ")
currency = input("Enter the currency you want to convert to, ex. USD to CHF: ")

currency_parts = currency.split(" to ")
if len(currency_parts) != 2:
    print("Invalid format. Please use format 'USD to CHF'")
    exit()

currency_parts = [part.upper() for part in currency_parts]

from_currency = currency_parts[0]
to_currency = currency_parts[1]

response = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}")

if response.status_code != 200:
    print("Error fetching data from the API")
    exit()

data = response.json()

conversion_rate = data["conversion_rates"][to_currency]

converted_amount = float(amount) * conversion_rate
converted_amount = round(converted_amount, 2)

print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")