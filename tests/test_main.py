from unittest.mock import patch

from main import main


@patch("builtins.input", side_effect=["1", "EXECUTED", "да", "по возрастанию", "да", "да", "перевод"])
def test_main_executed(mock_input):
    # Вызови здесь свою функцию main
    main()


@patch("builtins.input", side_effect=["1", "CANCELED", "да", "по возрастанию", "да", "да", "перевод"])
def test_main_canceled(mock_input):
    # Вызови здесь свою функцию main
    main()


@patch("builtins.input", side_effect=["1", "PENDING", "да", "по возрастанию", "да", "да", "перевод"])
def test_main_pending(mock_input):
    # Вызови здесь свою функцию main
    main()
