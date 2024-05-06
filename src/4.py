from collections.abc import Awaitable, Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

def add_logging(f: Callable[P, R]) -> Callable[P, Awaitable[R]]:
  async def inner(*args: P.args, **kwargs: P.kwargs) -> R:
    await log_to_database()
    return f(*args, **kwargs)
  return inner

@add_logging
def takes_int_str(x: int, y: str) -> int:
  return x + 7

await takes_int_str(1, "A") # Accepted
await takes_int_str("B", 2) # Correctly rejected by the type checker
