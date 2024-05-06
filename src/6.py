
from typing import TypeAlias, TypeVar

T = TypeVar('T')

Url: TypeAlias = str

def get_status(url: Url) -> T:
    ...


type Url = str

def get_status[T](url: Url) -> T:
    ...
