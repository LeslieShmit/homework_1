from unittest.mock import patch

import pandas as pd

from src.readers import transaction_reader_csv, transaction_reader_exel


@patch("pandas.read_csv")
def test_transaction_reader_csv(mock_read):
    mock_read.return_value = pd.DataFrame({"Yes": [1, 2], "No": [3, 4]})
    assert transaction_reader_csv("test.scv") == [{"Yes": 1, "No": 3}, {"Yes": 2, "No": 4}]


@patch("pandas.read_excel")
def test_transaction_reader_exel(mock_read):
    mock_read.return_value = pd.DataFrame({"Yes": [1, 2], "No": [3, 4]})
    assert transaction_reader_exel("test.xlsx") == [{"Yes": 1, "No": 3}, {"Yes": 2, "No": 4}]
