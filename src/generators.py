from mypy.server.objgraph import Iterable


def filter_by_currency(list_of_operations: list[dict], currency: str) -> Iterable:
    try:
        for dictionary in list_of_operations:
            value = dictionary["operationAmount"]["currency"]["code"]  # noqa: F841
    except KeyError:
        filtered_data = []
    else:
        filtered_data = filter(
            lambda operation: operation["operationAmount"]["currency"]["code"] == currency, list_of_operations
        )
    return filtered_data
