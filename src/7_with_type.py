from __future__ import annotations

from collections.abc import Callable
from typing import Concatenate, Protocol

import httpx
import requests

from .remote_logger import RemoteLogger


class ResponseLike(Protocol):
    status_code: int


type LogFunc[** P, R] = Callable[Concatenate[RemoteLogger, P], R]


def add_logging[** P](
        description: str, *, level: int = 0
) -> Callable[[LogFunc[P, ResponseLike]], Callable[P, ResponseLike]]:
    def inner(func: LogFunc[P, ResponseLike]) -> Callable[P, ResponseLike]:
        logger = RemoteLogger(func.__name__, description, level)

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> ResponseLike:
            logger.send_log(args=args, kwargs=kwargs)
            result = func(logger, *args, **kwargs)
            logger.send_log(status_code=result.status_code)
            return result

        return wrapper

    return inner


@add_logging('http client', level=0)
def download_with_request(
        logger: RemoteLogger, url: str, timeout: float = 5
) -> ResponseLike:
    logger.send_log(message='in download_with_request')
    return requests.get(url, timeout=timeout)


@add_logging('http client', level=0)
def download_with_httpx(
        logger: RemoteLogger, url: str, timeout: float = 5
) -> ResponseLike:
    logger.send_log(message='in download_with_httpx')
    return httpx.get(url, timeout=timeout)


download_with_request('https://examples.com/', timeout=10)
download_with_httpx('https://examples.com/', timeout=10)
