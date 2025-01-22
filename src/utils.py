import json
import logging
import os
from logging import DEBUG

logger = logging.getLogger("utils")
logger.setLevel(DEBUG)
abs_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../logs", "utils.log"))
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_list(path_to_file: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        logger.info(f"Попытка открыть файл {path_to_file}.")
        with open(path_to_file, "r", encoding="utf-8") as transaction_file:
            transaction_list = json.load(transaction_file)
    except FileNotFoundError:
        logger.error("Ошибка. Файл не найден.")
        transaction_list = []
    except json.decoder.JSONDecodeError:
        logger.error("Ошибка. Некорректный формат данных.")
        transaction_list = []
    if type(transaction_list) is not list:
        logger.error("Ошибка. Некорректный формат данных.")
        transaction_list = []
    if transaction_list:
        logger.info("Программа завершена успешно.")
    return transaction_list
