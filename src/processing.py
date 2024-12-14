def filter_by_state(list_of_dicts: list, chosen_state: str = "EXECUTED") -> list | str:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию
    'EXECUTED') и возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    new_list_of_dicts = []
    for dictionary in list_of_dicts:
        if dictionary.get("state") == chosen_state:
            new_list_of_dicts.append(dictionary)
    if not new_list_of_dicts:
        result = "Нет результатов, удовлетворяющих заданным критериям"
    else:
        result = new_list_of_dicts
    return result


def sort_by_date(list_of_dicts: list, is_reverse: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) и возвращает новый список, отсортированный по дате (date)."""
    sorted_list = sorted(list_of_dicts, key=lambda dictionary: dictionary["date"], reverse=is_reverse)
    return sorted_list

