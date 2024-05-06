from typing import Protocol


class ResponseLike(Protocol):
    status_code: int

    def json(self) -> dict:
        ...

# > response: ResponseLike = requests.get('https://example.com')
# > response.json()
# > response.status_code

class ClientGetFunction(Protocol):
    def __call__(self, url: str, timeout: float) -> ResponseLike:
        ...

# > def call_url(url: str, timeout: float) -> ResponseLike:
# >     return requests.get(url, timeout=timeout)
# > func: ClientGetFunction = call_url # OK
