from collections.abc import Callable
from typing import Any

import requests
from remote_logger import RemoteLogger


def add_logging(
    description: str, *, level: int = 0
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def inner(func: Callable[..., Any]) -> Callable[..., Any]:
        logger = RemoteLogger(func.__name__, description, level)

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger.send_log(args=args, kwargs=kwargs)
            result = func(*args, **kwargs)
            logger.send_log(result=result)
            return result

        return wrapper

    return inner


@add_logging('http client', 0)
def call_url(url: str) -> Any:
    return requests.get(url)


call_url('https://www.example.com/')
