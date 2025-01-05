import json
import os


def get_transactions_list(path_to_file: str) -> list[dict]:
    try:
        with open(path_to_file, "r", encoding="utf-8") as transaction_file:
            transaction_list = json.load(transaction_file)
    except FileNotFoundError:
        transaction_list = []
    except json.decoder.JSONDecodeError:
        transaction_list = []
    if type(transaction_list) != list:
        transaction_list = []
    return transaction_list
