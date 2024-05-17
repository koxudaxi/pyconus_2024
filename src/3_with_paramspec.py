from collections.abc import Callable
from typing import ParamSpec, Protocol

import requests
from remote_logger import RemoteLogger

P = ParamSpec('P')


class ResponseLike(Protocol):
    status_code: int


def add_logging(
        group: str, *, level: int = 0
) -> Callable[[Callable[P, ResponseLike]], Callable[P, ResponseLike]]:
    def inner(func: Callable[P, ResponseLike]) -> Callable[P, ResponseLike]:
        logger = RemoteLogger(func.__name__, group, level)

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> ResponseLike:
            logger.send_log(args=args, kwargs=kwargs)
            result = func(*args, **kwargs)
            logger.send_log(status_code=result.status_code)
            return result

        return wrapper

    return inner


@add_logging('http client', level=0)
def call_url(url: str, timeout: int = 5) -> ResponseLike:
    return requests.get(url, timeout=timeout)


call_url('https://examples.com/', 10) # OK
call_url(10, 'https://examples.com/') # NG
