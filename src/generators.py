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

def transaction_descriptions(list_of_operations: list[dict]) -> str:
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
