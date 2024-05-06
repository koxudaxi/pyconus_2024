import httpx
from httpx import Response

response: Response = httpx.get('https://examples.com/')
assert response.status_code == 200


import requests
from requests import Response

response: Response = requests.get('https://examples.com/')
assert response.status_code == 200
