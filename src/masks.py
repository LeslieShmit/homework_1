import logging
import os
from logging import DEBUG

logger = logging.getLogger("masks")
logger.setLevel(DEBUG)
abs_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../logs", "masks.log"))
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на ввод номер карты в виде числа, проверяет корректность формата и возвращает маску в
    виде строки в формате XXXX XX** **** XXXX"""
    try:
        logger.info("Проверка входящих данных на соответствие формата.")
        card_number_int = int(card_number)
    except ValueError:
        logger.error("Ошибка. Формат входящих данных некорректен.")
        result = "Ошибка. Номер карты может содержать только цифры и не может быть пустым."
    else:
        card_number_string = str(card_number_int)
        if len(card_number_string) == 16:
            logger.info("Программа завершена успешно.")
            result = f"{card_number_string[0: 4]} {card_number_string[4: 6]}** **** {card_number_string[-4:]}"
        else:
            logger.error("Ошибка. Формат входящих данных некорректен.")
            result = "Ошибка. Номер карты должен состоять из 16 цифр"
    return result


def get_mask_account(account_number: str) -> str:
    """Функция принимает на ввод номер счета в виде числа, проверяет корректность формата и возвращает маску в
    виде строки в формате **XXXX"""
    try:
        logger.info("Проверка входящих данных на соответствие формата.")
        account_number_int = int(account_number)
    except ValueError:
        logger.error("Ошибка. Формат входящих данных некорректен.")
        result = "Ошибка. Номер счета может содержать только цифры и не может быть пустым."
    else:
        account_number_string = str(account_number_int)
        if len(account_number_string) == 20:
            logger.info("Программа завершена успешно.")
            result = f"**{account_number_string[-4:]}"
        else:
            logger.error("Ошибка. Формат входящих данных некорректен.")
            result = "Ошибка. Номер счета должен состоять из 20 цифр"
    return result
