from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """Функция принимает строку, содержащую тип и номер карты или счета и возвращает ее же в замаскированном виде"""
    card_or_account_list = card_or_account.split(" ")
    card_or_account_list_new = []
    acceptable_words = [
        "Visa",
        "Maestro",
        "MasterCard",
        "Classic",
        "Gold",
        "Platinum",
        "Signature",
        "Infinite",
        "Счет",
    ]
    if (
        not 2 <= len(card_or_account_list) <= 3
        or not card_or_account_list[0] in acceptable_words
        or not card_or_account_list[-1].isdigit()
    ):
        raise ValueError("Введены неверные данные")
    if len(card_or_account_list[-1]) == 16 or len(card_or_account_list[-1]) == 20:
        for el in card_or_account_list:
            if el.isdigit() and len(el) == 16:
                masked_card_number = get_mask_card_number(el)
                card_or_account_list_new.append(masked_card_number)
            elif el.isdigit() and len(el) == 20:
                masked_account_number = get_mask_account(el)
                card_or_account_list_new.append(masked_account_number)
            elif el.isalpha() and el in acceptable_words:
                card_or_account_list_new.append(el)

    else:
        raise ValueError("Введены неверные данные")
    result = " ".join(card_or_account_list_new)
    return result


def get_date(unformatted_date: str) -> str:
    """Функция принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407' и возвращает строку с датой в
    формате 'ДД.ММ.ГГГГ'"""
    date_and_time_list = unformatted_date.split("T")
    date_list = date_and_time_list[0].split("-")
    if len(date_list) != 3:
        raise ValueError("Некорректная дата")
    if not 1990 <= int(date_list[0]) <= 2024 or not 0 < int(date_list[1]) <= 12 or not 0 < int(date_list[2]) <= 31:
        raise ValueError("Некорректная дата")
    result = f"{unformatted_date[8:10]}.{unformatted_date[5:7]}.{unformatted_date[:4]}"
    return result
