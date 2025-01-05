import requests
import os
from dotenv import load_dotenv

def convertion_to_rubles(transaction: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        final_result = transaction["operationAmount"]["amount"]
    else:
        load_dotenv()
        api_key = os.getenv("API_KEY")
        currency = transaction["operationAmount"]["currency"]["code"]
        amount_to_convert = transaction["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount_to_convert}"
        payload = {}
        headers = {
            "apikey": api_key
        }
        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.json()
        final_result = result["result"]
    return float(final_result)
