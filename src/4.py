from collections.abc import Callable
from typing import Concatenate, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

def with_request(f: Callable[Concatenate[Request, P], R]) -> Callable[P, R]:
  def inner(*args: P.args, **kwargs: P.kwargs) -> R:
    return f(Request(), *args, **kwargs)
  return inner

@with_request
def takes_int_str(request: Request, x: int, y: str) -> int:
  # use request
  return x + 7

takes_int_str(1, "A") # Accepted
takes_int_str("B", 2) # Correctly rejected by the type checker
