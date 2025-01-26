import pandas as pd


def transaction_reader_csv(path_to_file: str) -> list[dict]:
    """Функция принимает на вход путь до файла .csv и возвращает содержимое в виде списка словарей."""
    transaction_df = pd.read_csv(path_to_file, sep=";")
    transaction_df = transaction_df.fillna(0)
    transaction_list = transaction_df.to_dict("records")
    return transaction_list


def transaction_reader_excel(path_to_file: str) -> list[dict]:
    """Функция принимает на вход путь до файла exel и возвращает содержимое в виде списка словарей."""
    transaction_data_exel = pd.read_excel(path_to_file)
    transaction_data_exel = transaction_data_exel.fillna(0)
    transaction_list = transaction_data_exel.to_dict("records")
    return transaction_list
