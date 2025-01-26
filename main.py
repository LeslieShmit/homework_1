from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.readers import transaction_reader_csv, transaction_reader_excel
from src.utils import get_transactions_list, transaction_filter
from src.widget import get_date, mask_account_card


def main():
    """Основная функция, связывающая функциональности между собой и отвечающая за логику проекта"""
    while True:
        print("""Привет! Добро пожаловать в программу работы 
    с банковскими транзакциями. 
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла""")
        user_input = input()
        if user_input == "1":
            print("Для обработки выбран JSON-файл.")
            transaction_list = get_transactions_list("data/operations.json")
            break
        elif user_input == "2":
            print("Для обработки выбран CSV-файл.")
            # Приведение формата словаря, получаемого из csv-файла в соответствие с таковым, получаемым из JSON.
            transaction_list_unformatted = transaction_reader_csv("data/transactions.csv")
            transaction_list = []
            for transaction_dict_unformatted in transaction_list_unformatted:
                transaction_dict_formatted = {"id": transaction_dict_unformatted["id"],
                                              "state": transaction_dict_unformatted["state"],
                                              "date": transaction_dict_unformatted["date"],
                                              "operationAmount": {"amount": transaction_dict_unformatted["amount"],
                                                                  "currency": {"name": transaction_dict_unformatted[
                                                                      "currency_name"],
                                                                               "code": transaction_dict_unformatted[
                                                                                   "currency_code"]}},
                                              "description": transaction_dict_unformatted["description"],
                                              "to": transaction_dict_unformatted["to"]}
                if transaction_dict_unformatted["from"] != 0:
                    transaction_dict_formatted["from"] = transaction_dict_unformatted["from"]
                transaction_list.append(transaction_dict_formatted)
            break
        elif user_input == "3":
            print("Для обработки выбран XLSX-файл.")
            # Приведение формата словаря, получаемого из XLSX-файла в соответствие с таковым, получаемым из JSON.
            transaction_list_unformatted = transaction_reader_excel("data/transactions_excel.xlsx")
            transaction_list = []
            for transaction_dict_unformatted in transaction_list_unformatted:
                transaction_dict_formatted = {"id": transaction_dict_unformatted["id"],
                                              "state": transaction_dict_unformatted["state"],
                                              "date": transaction_dict_unformatted["date"],
                                              "operationAmount": {"amount": transaction_dict_unformatted["amount"],
                                                                  "currency": {"name": transaction_dict_unformatted[
                                                                      "currency_name"],
                                                                               "code": transaction_dict_unformatted[
                                                                                   "currency_code"]}},
                                              "description": transaction_dict_unformatted["description"],
                                              "to": transaction_dict_unformatted["to"]}
                if transaction_dict_unformatted["from"] != 0:
                    transaction_dict_formatted["from"] = transaction_dict_unformatted["from"]
                transaction_list.append(transaction_dict_formatted)
            break
        else:
            print("Введенные данные некорректны. Введите число от 1 до 3.")
    while True:
        print("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        user_input = input()
        if user_input.upper() == "EXECUTED":
            chosen_state = "EXECUTED"
            break
        elif user_input.upper() == "CANCELED":
            chosen_state = "CANCELED"
            break
        elif user_input.upper() == "PENDING":
            chosen_state = "PENDING"
            break
        else:
            print(f"Статус операции '{user_input}' недоступен")
    transactions_filtered_by_state = filter_by_state(transaction_list, chosen_state)
    while True:
        print("Отсортировать операции по дате? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            while True:
                print("Отсортировать по возрастанию или по убыванию?")
                user_input = input().lower()
                if user_input == "по возрастанию":
                    transactions_filtered_and_sorted = sort_by_date(transactions_filtered_by_state, False)
                    break
                elif user_input == "по убыванию":
                    transactions_filtered_and_sorted = sort_by_date(transactions_filtered_by_state)
                    break
                else:
                    print("Введенные данные некорректны. Введите 'по возрастанию' или 'по убыванию'.")
            break
        elif user_input == "нет":
            transactions_filtered_and_sorted = transactions_filtered_by_state
            break
        else:
            print("Введенные данные некорректны. Введите 'да' или 'нет'.")
    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            transactions_filtered_by_currency = list(filter_by_currency(transactions_filtered_and_sorted, "RUB"))
            break
        elif user_input == "нет":
            transactions_filtered_by_currency = transactions_filtered_and_sorted
            break
        else:
            print("Введенные данные некорректны. Введите 'да' или 'нет'.")
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            user_input = input("Введите слово, по которому необходимо отфильтровать транзакции.")
            transactions_filtered_by_user_data = transaction_filter(transactions_filtered_by_currency, user_input)
            break
        elif user_input == "нет":
            transactions_filtered_by_user_data = transactions_filtered_by_currency
            break
        else:
            print("Введенные данные некорректны. Введите 'да' или 'нет'.")
    print("Распечатываю итоговый список транзакций...")
    if transactions_filtered_by_user_data:
        print(f"Всего банковских операций в выборке: {len(transactions_filtered_by_user_data)}")
        for transaction in transactions_filtered_by_user_data:
            if "from" in transaction:
                formatted_date = get_date(transaction["date"])
                masked_source = mask_account_card(transaction["from"])
                masked_destination = mask_account_card(transaction["to"])
                print(f"""{formatted_date} {transaction["description"]}
{masked_source} -> {masked_destination}
Сумма: {transaction["operationAmount"]["amount"]} {transaction["operationAmount"]["currency"]["name"]}""")
            else:
                formatted_date = get_date(transaction["date"])
                masked_destination = mask_account_card(transaction["to"])
                print(f"""{formatted_date} {transaction["description"]}
{masked_destination}
Сумма: {transaction["operationAmount"]["amount"]} {transaction["operationAmount"]["currency"]["name"]}""")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

