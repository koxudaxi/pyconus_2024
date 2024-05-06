from typing import TypeVar, TypeVarTuple

T = TypeVar("T")
Ts = TypeVarTuple("Ts")


def move_first_element_to_last(tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
    return (*tup[1:], tup[0])

move_first_element_to_last((1, 2, 3)) # Expected: (2, 3, 1)
#                           ↑  ↑  ↑
#                           T  *Ts
