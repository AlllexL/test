import time
from typing import Any, Callable


def mark_the_time(func: Callable) -> Any:
    def wrapper():
        start = time.monotonic()
        result = func()
        end = time.monotonic() - start

        print(f'Время выполнения: {end}')

        return result

    return wrapper
