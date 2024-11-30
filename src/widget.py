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
