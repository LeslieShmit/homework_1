import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [("1234567891234567", "1234 56** **** 4567"),
                                                   ("9876543219876543", "9876 54** **** 6543")
                                                   ])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

def test_get_mask_card_number_invalid_format():
    assert get_mask_card_number("123456qwerasdf78") == ("Ошибка. Номер карты может содержать только цифры и не может"
                                                        " быть пустым.")

def test_get_mask_card_number_invalid_length():
    assert get_mask_card_number("123456789") == "Ошибка. Номер карты должен состоять из 16 цифр"

    assert get_mask_card_number("") == "Ошибка. Номер карты может содержать только цифры и не может быть пустым."


@pytest.mark.parametrize("account_number, expected", [("12345678912345678912", "**8912"),
                                                   ("98765432198765432198", "**2198")
                                                   ])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected

def test_get_mask_account_invalid_format():
    assert get_mask_account("123456qwerasdf789123") == ("Ошибка. Номер счета может содержать только цифры и не может"
                                                        " быть пустым.")

def test_get_mask_account_invalid_length():
    assert get_mask_account("12345678912") == "Ошибка. Номер счета должен состоять из 20 цифр"

    assert get_mask_account("") == "Ошибка. Номер счета может содержать только цифры и не может быть пустым."