
from typing import TypeAlias

Url: TypeAlias = str

def get_status(url: Url) -> int:
    ...


type Url = str

def get_status(url: Url) -> int:
    ...


from typing import TypeVar

T = TypeVar('T')
def multiply(x: T, y: int) -> T:
    ...

def multiply[T](x: T, y: int) -> T:
    ...

