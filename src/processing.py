def filter_by_state(list_of_dicts: list, chosen_state: str = "EXECUTED") -> list | str:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию
    'EXECUTED') и возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    new_list_of_dicts = []
    for dictionary in list_of_dicts:
        if dictionary.get("state") == chosen_state:
            new_list_of_dicts.append(dictionary)
    if not new_list_of_dicts:
        result = []
    else:
        result = new_list_of_dicts
    return result


def sort_by_date(list_of_dicts: list, is_reverse: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) и возвращает новый список, отсортированный по дате (date)."""
    for el in list_of_dicts:
        date_and_time_list = el["date"].split("T")
        date_list = date_and_time_list[0].split("-")
        if not 1990 <= int(date_list[0]) <= 2024 or not 0 < int(date_list[1]) <= 12 or not 0 < int(date_list[2]) <= 31:
            raise ValueError("Некорректная дата")
    sorted_list = sorted(list_of_dicts, key=lambda dictionary: dictionary["date"], reverse=is_reverse)
    return sorted_list
