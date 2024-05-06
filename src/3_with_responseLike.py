from collections.abc import Callable
from typing import Any, Protocol, TypeVarTuple

import requests
from remote_logger import RemoteLogger

Ts = TypeVarTuple('Ts')


class ResponseLike(Protocol):
    status_code: int


def add_logging(
    description: str, *, level: int = 0
) -> Callable[[Callable[[*Ts], ResponseLike]], Callable[[*Ts], ResponseLike]]:
    def inner(func: Callable[[*Ts], ResponseLike]) -> Callable[[*Ts], ResponseLike]:
        logger = RemoteLogger(func.__name__, description, level)

        def wrapper(*args: *Ts, **kwargs: Any) -> ResponseLike:
            logger.send_log(args=args, kwargs=kwargs)
            result = func(*args, **kwargs)
            logger.send_log(status_code=result.status_code)
            return result

        return wrapper

    return inner


@add_logging('http client', level=0)
def get_status(url: str):
    return requests.get(url)


get_status('https://www.example.com/')
