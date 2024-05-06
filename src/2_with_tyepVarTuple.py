from collections.abc import Callable
from typing import Any, TypeVarTuple

import requests
from remote_logger import RemoteLogger

Ts = TypeVarTuple('Ts')


def add_logging(
    description: str, *, level: int = 0
) -> Callable[[Callable[[*Ts], Any]], Callable[[*Ts], Any]]:
    def inner(func: Callable[[*Ts], Any]) -> Callable[[*Ts], Any]:
        logger = RemoteLogger(func.__name__, description, level)

        def wrapper(*args: *Ts, **kwargs: Any) -> Any:
            logger.send_log(args=args, kwargs=kwargs)
            result = func(*args, **kwargs)
            logger.send_log(result=result)
            return result

        return wrapper

    return inner


@add_logging('http client', level=0)
def call_url(url: str) -> Any:
    return requests.get(url)


call_url('https://www.example.com/')
