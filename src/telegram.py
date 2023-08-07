import os
import requests
from dotenv import load_dotenv


class Telegram:
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

    def __init__(self):
        load_dotenv()
        self.__api_key = os.environ.get('API_KEY')

    @property
    def api_key(self) -> str:
        return self.__api_key

    def send_message(self):
        query = f'https://api.telegram.org/bot{self.api_key}/functionsss'
        try:
            res = requests.post(query)
            if res.status_code != 200:
                raise Exception(f'Error: status code {res.status_code}')
        except Exception as e:
            msg = f'Error: {e}'
            return msg

