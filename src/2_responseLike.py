from typing import Protocol

import httpx


class ResponseLike(Protocol):
    status_code: int


response: ResponseLike = httpx.get('https://examples.com/')
assert response.status_code == 200


import requests

response: ResponseLike = requests.get('https://examples.com/')
assert response.status_code == 200
