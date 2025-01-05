import pytest
from unittest import mock
from unittest.mock import patch, mock_open
from src.utils import get_transactions_list


def test_get_transactions_list():
    mocked_open = mock_open(read_data='[{"id": 1, "amount": "100.0"}]')
    with patch('builtins.open', mocked_open):
        result = get_transactions_list("../data/operations.json")
        assert result == [{"id": 1, "amount": "100.0"}]


def test_get_transactions_list_not_list():
    mocked_open = mock_open(read_data="Hello")
    with patch('builtins.open', mocked_open):
        result = get_transactions_list("../data/operations.json")
        assert result == []


def test_get_transactions_list_decoder_error():
    mocked_open = mock_open(read_data="(1, 2, 3)")
    with patch('builtins.open', mocked_open):
        result = get_transactions_list("../data/operations.json")
        assert result == []

def test_get_transactions_list_file_not_found():
    assert get_transactions_list("../data/nonexistent.json") == []
