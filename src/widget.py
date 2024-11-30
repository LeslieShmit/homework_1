from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """Функция принимает строку, содержащую тип и номер карты или счета и возвращает ее же в замаскированном виде"""
    card_or_account_list = card_or_account.split(" ")
    card_or_account_list_new = []
    for el in card_or_account_list:
        if el.isdigit() and len(el) == 16:
            masked_card_number = get_mask_card_number(el)
            card_or_account_list_new.append(masked_card_number)
        elif el.isdigit() and len(el) == 20:
            masked_account_number = get_mask_account(el)
            card_or_account_list_new.append(masked_account_number)
        elif el.isalpha():
            card_or_account_list_new.append(el)
        else:
            continue
    result = " ".join(card_or_account_list_new)
    return result


def get_date(unformatted_date: str) -> str:
    """Функция принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407' и возвращает строку с датой в
    формате 'ДД.ММ.ГГГГ'"""
    result = f"{unformatted_date[8:10]}.{unformatted_date[5:7]}.{unformatted_date[:4]}"
    return result
