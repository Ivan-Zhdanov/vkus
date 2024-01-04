import requests
import xmltodict
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def check_block_domains_list(domain):  # проверка есть ли выбранный домен в блок-листе
    with open('Blocks_domains.txt', 'r') as f:
        lines: list = f.read().splitlines()
        if lines.count(domain):
            return True  # домен в блок-листе
    return False  # домен не в блок-листе


def check_url(url):
    domain = urlparse(url).netloc
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0', 'Accept': '*/*'}
    r = requests.get(url, headers=headers)
    try:
        if check_block_domains_list(domain):  # проверка текущего домена на нахождение в блок-листе
            return False
        if r.status_code != 200:
            return False
        soup = BeautifulSoup(r.text, 'html.parser')
        count_h2 = len(soup.find_all('h2'))
        count_symbols = len(soup.body.get_text())
        if count_symbols < 2000:
            return False
        if count_h2 < 1:
            return False
    except:
        pass

    return True


def parsing_google(search_response: str) -> list:
    headers = {'Content-Type': 'application/xml'}
    resp = requests.get(f"http://xmlriver.com/search/xml?user=10523&key=aaac4e5ac50226e36818e376b4d8a9898dac9b57&query={search_response}", headers=headers)
    dict_data = xmltodict.parse(resp.content)
    list_urls = []
    for i in dict_data['yandexsearch']['response']['results']['grouping']['group']:
        el = i['doc']['url']
        try:
            if check_url(el) == False:
                pass
            else:
                list_urls.append(el)  # последний элемент содержит None
        except:
            pass
    return list_urls[:2]


def parsing_yandex(search_response: str) -> list:
    list_urls = []
    headers = {'Content-Type': 'application/xml'}
    resp = requests.get(f"http://xmlriver.com/search_yandex/xml?user=10523&key=aaac4e5ac50226e36818e376b4d8a9898dac9b57&query={search_response}", headers=headers)
    dict_data = xmltodict.parse(resp.content)
    for i in dict_data['yandexsearch']['response']['results']['grouping']['group']:
        el = i['doc']['url']
        print(el)
        try:
            if check_url(el) == False:
                pass
            else:
                list_urls.append(el)  # последний элемент содержит None
        except:
            pass
    # УСТАНОВКА КОЛИчЕСТВА ВЗЯТЫХ ДЛЯ АНАЛИЗА УРЛОВ
    return list_urls[:3]


# print(check_url('https://agro-him.com.ua/index.php?route=information/news/news&news_id=8'))
# print(parsing_google('гниль малины'))


# print(check_url('https://countryhouse.pro/peresadka-smorodiny/'))
# print(parsing_google('гниль малины'))

# print(parsing_yandex('гниль малины'))