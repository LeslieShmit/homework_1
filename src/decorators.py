import os.path
from typing import Any, Callable

from config import path


def log(filename: str | None = None) -> Callable:
    """Декоратор принимает название файла в формате 'name.txt', и записывает в него результаты или возникшие ошибки.
    Если имя файла не задано - логи выводятся в консоль."""

    def inner(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            global log
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                log = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
            else:
                log = f"{func.__name__} ok"
            finally:
                if filename:
                    with open(os.path.join(path, filename), "a", encoding="utf-8") as f:
                        f.write(f"{log}\n")
                        return result
                else:
                    print(log)
                    return result

        return wrapper

    return inner
