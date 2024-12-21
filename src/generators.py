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

