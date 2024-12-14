import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_or_account, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(card_or_account, expected):
    assert mask_account_card(card_or_account) == expected


@pytest.mark.parametrize(
    "card_or_account_wrong_format",
    ["Aaaa 1596837868705199", "Maestro 1596837", "73654108430135874305", "Visa Classic"],
)
def test_mask_account_card_wrong_format(card_or_account_wrong_format):
    with pytest.raises(ValueError):
        mask_account_card(card_or_account_wrong_format)


@pytest.mark.parametrize(
    "unformatted_date, expected",
    [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
    ],
)
def test_get_date(unformatted_date, expected):
    assert get_date(unformatted_date) == expected


@pytest.mark.parametrize(
    "incorrect_input", ["T18:35:29.512364", "2018-06T02:08:58.425572", "9999-99-99T21:27:25.241689"]
)
def test_get_date_incorrect_input(incorrect_input):
    with pytest.raises(ValueError):
        get_date(incorrect_input)
