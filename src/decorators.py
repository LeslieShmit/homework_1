import os.path

from typing import Callable, Any

from config import path

def log(filename: str | bool=None) -> Callable:
    """Декоратор принимает название файла в формате 'name.txt', и записывает в него результаты или возникшие ошибки.
    Если имя файла не задано - логи выводятся в консоль."""
    def inner(func: Callable):
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            global log
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                log = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
            else:
                log = f"{func.__name__} ok\n"
            finally:
                if filename:
                    with open(os.path.join(path, filename), "a", encoding="utf-8") as f:
                        f.write(log)
                        return result
                else:
                    print(log)
                    return result
        return wrapper
    return inner
