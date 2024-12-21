import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions
)


def test_filter_by_currency(transactions):
    expected_result = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert result == expected_result


def test_filter_by_currency_no_valid_data(transactions_no_valid_currency):
    expected_result = []
    result = list(filter_by_currency(transactions_no_valid_currency, "USD"))
    assert expected_result == result


def test_filter_by_currency_empty_list():
    expected_result = []
    result = list(filter_by_currency([], "USD"))
    assert expected_result == result


def test_filter_by_currency_some_not_valid_data(transactions_some_not_valid_currency):
    expected_result = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]
    result = list(filter_by_currency(transactions_some_not_valid_currency, "USD"))
    assert expected_result == result


def test_transaction_descriptions(transactions):
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_transaction_descriptions_unexpected(transactions_not_valid_description):
    generator = transaction_descriptions(transactions_not_valid_description)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_card_number_generator():
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"


def test_card_number_generator_start_more_than_end():
    with pytest.raises(ValueError) as exc_info:
        next(card_number_generator(5, 1))
    assert str(exc_info.value) == "Ошибка. Начальное значение больше конечного"


@pytest.mark.parametrize(
    "start, stop", [(-1, 5), (-5, 0), (9999999999999995, 10000000000000000), (10000000000000000, 10000000000000005)]
)
def test_card_number_generator_unexpected_value(start, stop):
    with pytest.raises(ValueError) as exc_info:
        next(card_number_generator(start, stop))
    assert str(exc_info.value) == "Ошибка. Оба значения должны находиться в диапазоне от 1 до 9999999999999999"
