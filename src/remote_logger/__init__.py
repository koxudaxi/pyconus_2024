import json


class RemoteLogger:
    def __init__(self, name: str, description: str, level: int) -> None:
        self.name = name
        self.description = description
        self.level = level

    def send_log(self, *args, **kwargs):
        # do some logic to send log
        print(json.dumps({**self.__dict__, **kwargs}))

# logger = RemoteLogger(name='test', description='test logger', level=0)
# logger.send_log(message='hello', user_id=1)
# {"name": "test", "description": "test logger", "level": 0, "message": "hello", "user_id": 1}



