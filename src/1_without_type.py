from typing import Any

import requests
from remote_logger import RemoteLogger


def add_logging(description, level=0):
    def inner(func):
        logger = RemoteLogger(func.__name__, description, level)

        def wrapper(*args, **kwargs):
            logger.send_log(args=args, kwargs=kwargs)
            result = func(*args, **kwargs)
            logger.send_log(result=result)
            return result

        return wrapper

    return inner


@add_logging('http client', 0)
def call_url(url: str) -> Any:
    return requests.get(url)


call_url('https://www.example.com/')
# {"name": "call_url", "description": "http client", "level": 0, "args": ["https://www.example.com/"], "kwargs": {}}
# {"name": "call_url", "description": "http client", "level": 0, "result": 200}
