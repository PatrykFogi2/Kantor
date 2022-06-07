from Cantor import Cantor
from bs4 import BeautifulSoup as soup
import requests


def get_objects() -> list:
    html_response = requests.get('https://www.najlepszekonto.pl/lista-kantorow-internetowych')
    bank_rate = html_response.json().get('name')
    '''html_txt = soup(html_response.text, 'html.parser')
    for a in html_txt.find_all("name"):
        print(a)'''


get_objects()