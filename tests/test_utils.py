from unittest.mock import mock_open, patch

from src.utils import (
    get_transactions_list,
    transaction_counter_by_categories,
    transaction_filter
)


def test_get_transactions_list():
    mocked_open = mock_open(read_data='[{"id": 1, "amount": "100.0"}]')
    with patch("builtins.open", mocked_open):
        result = get_transactions_list("../data/operations.json")
        assert result == [{"id": 1, "amount": "100.0"}]


def test_get_transactions_list_not_list():
    mocked_open = mock_open(read_data="Hello")
    with patch("builtins.open", mocked_open):
        result = get_transactions_list("../data/operations.json")
        assert result == []


def test_get_transactions_list_decoder_error():
    mocked_open = mock_open(read_data="(1, 2, 3)")
    with patch("builtins.open", mocked_open):
        result = get_transactions_list("../data/operations.json")
        assert result == []


def test_get_transactions_list_file_not_found():
    assert get_transactions_list("../data/nonexistent.json") == []


def test_transaction_filter(transactions):
    expected_result = [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]
    result = transaction_filter(transactions, "перевод с карты")
    assert result == expected_result


def test_transaction_counter_by_categories(transactions):
    expected_result = {"Перевод организации": 2, "Перевод с карты на карту": 1}
    result = transaction_counter_by_categories(
        transactions, ["Перевод с карты на карту", "Перевод организации", "Международный перевод"]
    )
    assert expected_result == result
