from collections.abc import Callable
from typing import Protocol, TypeAlias


class ResponseLike(Protocol):
    status_code: int


def call_url(url: str, *, timeout: float = 5) -> ResponseLike:
    ...


GetStatus: TypeAlias = Callable[[int, float], ResponseLike]


class GetStatus(Protocol):
    def __call__(self, url: str, timeout: float = 5) -> ResponseLike:
        ...
