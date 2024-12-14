def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на ввод номер карты в виде числа, проверяет корректность формата и возвращает маску в
    виде строки в формате XXXX XX** **** XXXX"""
    try:
        card_number_int = int(card_number)
    except ValueError:
        result = "Ошибка. Номер карты может содержать только цифры и не может быть пустым."
    else:
        card_number_string = str(card_number_int)
        if len(card_number_string) == 16:
            result = f"{card_number_string[0: 4]} {card_number_string[4: 6]}** **** {card_number_string[-4:]}"
        else:
            result = "Ошибка. Номер карты должен состоять из 16 цифр"
    return result


def get_mask_account(account_number: str) -> str:
    """Функция принимает на ввод номер счета в виде числа, проверяет корректность формата и возвращает маску в
    виде строки в формате **XXXX"""
    try:
        account_number_int = int(account_number)
    except ValueError:
        result = "Ошибка. Номер счета может содержать только цифры и не может быть пустым."
    else:
        account_number_string = str(account_number_int)
        if len(account_number_string) == 20:
            result = f"**{account_number_string[-4:]}"
        else:
            result = "Ошибка. Номер счета должен состоять из 20 цифр"
    return result
