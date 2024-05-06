from collections.abc import Callable
from typing import Concatenate, ParamSpec, Protocol

import requests
from remote_logger import RemoteLogger

P = ParamSpec('P')


class ResponseLike(Protocol):
    status_code: int


def add_logging(
    description: str, *, level: int = 0
) -> Callable[
    [Callable[Concatenate[RemoteLogger, P], ResponseLike]], Callable[P, ResponseLike]
]:
    def inner(
        func: Callable[Concatenate[RemoteLogger, P], ResponseLike],
    ) -> Callable[P, ResponseLike]:
        logger = RemoteLogger(func.__name__, description, level)

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> ResponseLike:
            logger.send_log(args=args, kwargs=kwargs)
            result = func(logger, *args, **kwargs)
            logger.send_log(status_code=result.status_code)
            return result

        return wrapper

    return inner


@add_logging('http client', level=0)
def call_url(logger: RemoteLogger, url: str, timeout: int = 5) -> ResponseLike:
    logger.send_log(message='in call_url')
    return requests.get(url, timeout=timeout)


call_url('https://www.example.com/')
