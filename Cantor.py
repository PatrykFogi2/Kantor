from fastapi import FastAPI
from typing import Optional
from typing import List
from fastapi import responses

import requests


class Cantor():
    def __init__(self, name: str, link: str):
        self.name = name
        self.link = link

    def get_value(self, link):
        value_list = ['eur', 'gbp', 'nok', 'chf', 'usd']
        list_get_value = []
        for value in value_list:
            print(link + value + '/')
            response = requests.get(link + value + '/')
            rate = response.json().get('rates')
            list_get_value.append(rate[0].get('mid'))
        return list_get_value

Test = Cantor('xxx', 'http://api.nbp.pl/api/exchangerates/rates/a/')
print(Test.name)
print(Test.get_value('http://api.nbp.pl/api/exchangerates/rates/a/'))