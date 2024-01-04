import requests
from bs4 import BeautifulSoup
import re
from PIL import Image
from io import BytesIO
from urllib.parse import urlparse


def take_one_picture(list_urls: list) -> str:
    image_urls_list_dic = [{'url': '', 'width': 0, 'height': 0}]
    for url in list_urls:
        response = requests.get(url)
        if response.status_code == 200:  # Проверяем успешность запроса
            img_data = response.content
            img = Image.open(BytesIO(img_data))  # Открываем картинку используя PIL
            width, height = img.size
            url_width_height = {'url': url, 'width': width, 'height': height}
            image_urls_list_dic.append(url_width_height)
        else:
            print("Не удалось загрузить картинку")  # Если запрос не удался
    max_picture = max(image_urls_list_dic, key=lambda x: x['width'])
    return max_picture['url']


def extract_img_urls(domain: str, tag: object) -> list:
    tag_string = str(tag)
    # 1 вариант выделения урла картинки
    urls_1 = re.findall('https?://\S+?.jpe?g', tag_string)
    # 2 вариант выделения урла картинки
    urls_short = re.findall(r'(/wp-content/uploads.*?\.(jpe?g))', tag_string)
    urls_2 = [domain + url[0] for url in urls_short]
    # 3 вариант выделения урла картинки / может домен накладываться и делать картинку битой, но в некоторых случаях единственный определяет
    urls_short = re.findall(r'src="([^"]+\.jp?g)"', tag_string)
    urls_3 = [domain + url for url in urls_short]
    # 4 вариант выделения урла картинки
    urls_4 = re.findall(r'<img.*?src="(https://[^"]*)"', tag_string)
    # 5 вариант выдления урла картинки
    urls_short = re.findall(r'<img.*?src="([^"]*)"', tag_string)
    urls_5 = [domain + url for url in urls_short]
    if urls_1:
        return urls_1
    elif urls_2:
        return urls_2
    elif urls_3:
        return urls_3
    elif urls_4:
        return urls_4
    elif urls_5:
        return urls_5
    else:
        print('картинка не взялась из тэга img')
        return []


def delete_tag_a_img(tag: object) -> object:
    all_tag_a = tag.findAll('a')
    for tag_a in all_tag_a:
        tag_a.find('a')
        tag_text = tag_a.get_text()
        tag_a.replace_with(tag_text)

    all_tag_img = tag.findAll('img')
    for tag_img in all_tag_img:
        tag_img.find('img')
        tag_img.replace_with('')
    return tag


def create_list_tags(url: str) -> list[str]:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    domain = 'https://' + domain
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
               'Accept': '*/*'}
    r = requests.get(url, headers=headers).text
    soup = BeautifulSoup(r, 'html.parser')
    h1_tag = soup.find('h1')
    h2_tag = soup.find('h2')
    list_article = []
    next_elements = h2_tag.find_next_siblings()
    for tag in next_elements:
        if tag.name in ['h2']:
            list_article.append(f'<h2>{tag.get_text()}</h2>')
        if tag.name in ['h3']:
            list_article.append(f'<h3>{tag.get_text()}</h3>')
        if tag.name in ['p']:
            if tag.findChildren('img'):
                # print(tag)
                list_urls_in_tag = extract_img_urls(domain, tag.find('img'))
                list_article.append(f'<img src="{take_one_picture(list_urls_in_tag)}">')
            else:
                list_article.append(f'<p>{clean_text(tag.get_text())}</p>')
        if tag.name in ['div']:
            if tag.findChildren('img'):
                list_urls_in_tag = extract_img_urls(domain, tag.find('img'))
                list_article.append(f'<img src="{take_one_picture(list_urls_in_tag)}">')
            else:
                # list_article.append(f'<p>{tag.get_text()}</p>')
                pass
        if tag.name in ['blockquote']:
            list_article.append(tag)
        if tag.name in ['ol']:
            new_tag = delete_tag_a_img(tag)
            list_article.append(clean_text(str(new_tag)))
        if tag.name in ['ul']:
            new_tag = delete_tag_a_img(tag)
            list_article.append(clean_text(str(new_tag)))
        if tag.name in ['table']:
            new_tag = delete_tag_a_img(tag)
            list_article.append(new_tag)
    list_article.insert(0, f'<h2>{h2_tag.text}</h2>')
    return list_article


def find_element_with_char(lst, char) -> list:
    indices = [i for i, s in enumerate(lst) if char in s]
    return indices


def split_list_by_indices(lst, indices) -> tuple:
    result = []
    start = 0
    for index in indices:
        result.append(tuple(lst[start:index]))
        start = index
    result.append(tuple(lst[start:]))
    return result


def create_cortage_tags(data: list) -> tuple:
    character = 'h2'
    my_indices = find_element_with_char(data, character)
    cortage_tags = split_list_by_indices(data, my_indices)
    return cortage_tags


def clean_text(input_string: str):
    cleaned_string = input_string.replace("\n", "").replace("\r", "").replace("\t", "").replace("\xa0", "").strip()
    return cleaned_string

# можешь попереключать урлы
# url = 'https://fructberry.com/yagody/chernika/mesta-proizrastaniya'
# url = 'https://fructberry.com/yagody/chernika/mesta-proizrastaniya'
# url = 'https://spardostavka.ru/blog/sovety-pokupatelyam/chto-mozhno-sest-na-noch/?ysclid=lqmqv2hs4w609549115'
# url = 'https://foodandhealth.ru/info/regulyarniy-dnevnoy-son-sohranyaet-molodost-mozga/'
# url = 'https://vkusmus.ru/blog/paslen-chernyj-opisanie-svojstva-i-ispolzovanie-solanum-nigrum/'
# url = 'https://www.ayzdorov.ru/lechenie_bessonica_40_prodyktov.php'
# url = 'https://polzaivrededy.ru/kak-otlichit-chagu-ot-trutovika-sovety-i-rekomendatsii-po-sboru/'
# url = 'https://style.rbc.ru/health/606e97389a7947f4ef64a9e8'
# for el in create_list_tags(url):
#     print(type(el), el, end='\n\n')  # класс li

# data = create_list_tags(url)  # список всех тэгов страницы
# print(create_cortage_tags(data))  # список кортежей