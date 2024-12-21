from mypy.server.objgraph import Iterable


def filter_by_currency(list_of_operations: list[dict], currency: str) -> Iterable:
    """Функция принимает на вход список словарей, представляющих транзакции и возвращает итератор, который поочередно
    выдает транзакции, где валюта операции соответствует заданной"""
    try:
        for dictionary in list_of_operations:
            value = dictionary["operationAmount"]["currency"]["code"]  # noqa: F841
    except KeyError:
        list_of_operations.remove(dictionary)  # noqa

    filtered_data = filter(
        lambda operation: operation["operationAmount"]["currency"]["code"] == currency, list_of_operations
    )
    return filtered_data


def transaction_descriptions(list_of_operations: list[dict]) -> Iterable:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for dictionary in list_of_operations:
        try:
            value = dictionary["description"]  # noqa: F841
        except KeyError:
            list_of_operations.remove(dictionary)
    for operation in list_of_operations:
        yield operation["description"]
    while True:  # pragma: no cover
        pass  # pragma: no cover


def card_number_generator(start: int, stop: int) -> Iterable:
    """Функция генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX, где X
    — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    if start > stop:
        raise ValueError("Ошибка. Начальное значение больше конечного")
    if start > 9999999999999999 or stop > 9999999999999999:
        raise ValueError("Ошибка. Оба значения должны находиться в диапазоне от 1 до 9999999999999999")
    if start <= 0 or stop <= 0:
        raise ValueError("Ошибка. Оба значения должны находиться в диапазоне от 1 до 9999999999999999")
    for i in range(start, stop + 1):
        count_0 = "0" * (16 - len(str(i)))
        number = count_0 + str(i)
        yield f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"
