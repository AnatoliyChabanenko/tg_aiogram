import requests
from bs4 import BeautifulSoup
import json
import re

HOST = 'https://nibulon.com/'
URL = 'https://nibulon.com/data/zakupivlya-silgospprodukcii/zakupivelni-cini.html'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    'accept': '*/*'}



def get_html(url , params= None):
    r = requests.get(url, headers = HEADERS, params=params)
    return r



def get_content(html):
    name = []
    price = []
    soup = BeautifulSoup(html.text , 'html.parser')
    for i in soup.find_all('div' , class_= 'culture_item',limit=6):
        prise =(i.a.strong.text.strip())
        name.append(i.a.text.replace(prise, '').strip("\n\r- "))
        price.append(prise.replace('грн/т', ''))
    p = dict(zip(name, price))
    return p


def main():
    d = get_html(URL)
    contetnt = get_content(d)
    json_damp(contetnt)




def json_damp(data):
    with open('data1.json', 'w') as f:
        print(data)
        json.dump(data , f)


if __name__ == '__main__':
    main()
