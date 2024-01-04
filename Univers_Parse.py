from Cort import cort
import requests
from bs4 import BeautifulSoup
import bs4
from PIL import Image
from io import BytesIO
from Get_Image_Size import get_image_size
import re


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



def get_image_height(url):
    try:
        # Получаем содержимое изображения по URL
        response = requests.get(url)
        response.raise_for_status()  # Проверяем наличие ошибок при запросе

        # Читаем изображение с использованием библиотеки Pillow
        image = Image.open(BytesIO(response.content))

        # Получаем высоту изображения
        height = image.height

        return height

    except Exception as e:
        print(f"Error: {e}")
        return None




def end_url(url): #--> True
    s = url.endswith(('.jpeg', '.png', '.jpg', 'webp'))
    if s:
        return True

def univers_parse(url: str)-> list:    # return clear text of article
    print('Включен Универсальный Парсер для', url)
    string = ''
    list_corteg = []
    # print('Универсальный Парсер. Работаем с урлом - ', url)
    # Исправленный текст для очистки от лишних тегов   **************************************************************
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
               'Accept': '*/*'}
    r = requests.get(url, headers=headers).text

    soup = BeautifulSoup(r, 'html.parser')

    tags = soup.find_all()
    for tag in tags:
        if tag.name == 'div':
            tag.unwrap()


    # Находим тег <h2> и открываем все внутренние
    h2s = soup.find_all('h2')
    for h2 in h2s:
        tags = h2.find_all('p')
        for tag in tags:
            print(' ddd', tag)
            tag.unwrap()


    # h1_tag = soup.find('h1')
    # print(h1_tag)
    # # list_tags_before_h1 = h1_tag.find_all_next()
    # list_tags_before_h1 = h1_tag.find_next_siblings()

    h2_first = soup.find('h2')
    list_tags_after_h2 = h2_first.find_next_siblings()
    print('УП-2')
    # закрыл т.к. идет дублирование тегов
    # h1_tag = soup.find('h1')
    # next_tags = h1_tag.find_all_next()

    content_before_h1 = ', '.join(map(str, list_tags_after_h2))
    # print(content_before_h1)

    try:
        content_article = bs4.BeautifulSoup(content_before_h1, "lxml")
        div_tags = content_article.find_all('div')
        # Удаляем теги div и оставляем их содержимое
        for div_tag in div_tags:
            div_tag.unwrap()
    except:
        pass

    # Найти тег по части значения атрибута class
    desired_class_part = 'table of content'
    tag = content_article.find('div', class_=lambda value: value and desired_class_part in value)

    # Вывести текст найденного тега
    if tag:
        tag.decompose()


    print('УП-3')
    try:
        # УДАЛЕНИЕ ТЕГОВ SPAN ВЕЗДЕ
        # Заменяем каждый тег <span> его содержимым
        span_tags = content_article.find_all('span')
        for span_tag in span_tags:
            span_tag.replace_with_children()
    except:
        pass

    # # УДАЛЯЕМ ПУСТЫЕ Н2
    # h2s = content_article.find_all(['h2','h3'])
    # for h2 in h2s:
    #     if h2.text == '':
    #         h2.decompose()



    print('УП-4')
    try:
        # УДАЛЕНИЕ ПУСТЫХ P
        p_all = content_article.find_all('p')
        for p in p_all:
            if len(p.get_text(strip=True)) == 0:
                p.extract()
    except:
        pass

    # # УДАЛЕНИЕ ТЕГОВ STRONG В P
    try:
        p_all = content_article.find_all('p')
        for p in p_all:
            strongs_tags = p.find_all('strong')
            for strong_tag in strongs_tags:
                strong_tag.replaceWithChildren()
    except:
        pass

    print('УП-5')
    # # УДАЛИТЬ ОКРУЖАЮЩИЙ ТЕГ P У IMG ЕСЛИ НЕТ ТЕКСТА У Р (! задача подвисла)
    try:
        img_all = content_article.find_all('img')
        for img in img_all:
            try:

                img.find_parent('p').unwrap()
                img.attrs.pop('alt', None)
            except:
                pass
    except:
        pass

    # # УДАЛИТЬ ОКРУЖАЮЩИЙ ТЕГ A У IMG
    try:
        img_all = content_article.find_all('img')
        for img in img_all:
            try:
                img.find_parent('a').unwrap()
                img.attrs.pop('alt', None)
            except:
                pass
    except:
        pass
    print('УП-6')

    # # УДАЛИТЬ ОКРУЖАЮЩИЙ ТЕГ P У IFRAME
    try:
        img_all = content_article.find_all('iframe')
        for img in img_all:
            img.find_parent('p').unwrap()
    except:
        pass
    print('УП-7')

    # # H2 Очистить и вставить текст
    h2s = content_article.find_all('h2')
    for h2 in h2s:
        p_tags_inside_h2 = h2.find_all('p')

        for p in p_tags_inside_h2:
           p.replace_with_children()


    # ЗАМЕНА ТЕГОВ DIV SHORTCODE НА BLOCKQUOTE
    try:
        div_shorts = content_article.find_all('div', class_='shortcodestyle')
        for div_short in div_shorts:
            div_short.name = 'blockquote'
    except:
        pass
    print('УП-8')

    # УДАЛЕНИЕ ОДНОГО ТЕГА DIV КЛАССУ
    try:
        div_tag = content_article.find("div", class_="tptn_counter")
        div_tag.decompose()
    except:
        pass

    # УДАЛЕНИЕ МНОЖЕСТВА ТЕГОВ DIV
    try:
        div_tags = content_article.find_all("div")
        for div_tag in div_tags:
            div_tag.decompose()
    except:
        pass
    print('УП-9')
    # УДАЛЕНИЕ ТЕГОВ A В P
    try:
        p_all = content_article.find_all('p')
        for p in p_all:
            aa = p.find_all('a')
            for a in aa:
                a.replace_with(a.contents)
    except:
        pass

    # УДАЛЕНИЕ МНОЖЕСТВА ТЕГОВ SCRIPT
    try:
        div_tags = content_article.find_all("script")
        for div_tag in div_tags:
            div_tag.decompose()
    except:
        print('Универсальный Парсер. ошибка в поиске тега 9.1')
    print('УП-10')

    # УДАЛЕНИЕ МНОЖЕСТВА ТЕГОВ BR
    try:
        div_tags = content_article.find_all("br")
        for div_tag in div_tags:
            div_tag.decompose()
    except:
        print('Универсальный Парсер. ошибка в поиске тега 9.2')

    # УДАЛЕНИЕ МНОЖЕСТВА ТЕГОВ INS
    try:
        div_tags = content_article.find_all("ins")
        for div_tag in div_tags:
            div_tag.decompose()
    except:
        print('Универсальный Парсер. ошибка в поиске тега 9.2')

    try:
        # Находим все теги <A> (ссылки) и удаляем их
        a_tags = content_article.find_all('a')
        for a_tag in a_tags:
            # Заменяем тег <a> на его текстовое содержимое
            a_tag.replace_with(a_tag.text)
    except:
        pass
    print('УП-11')

    try:
        # Находим все теги <SUP> оставляя содержимое
        sup_tags = content_article.find_all('sup')
        for sup_tag in sup_tags:
            # Заменяем тег <sup> на его текстовое содержимое
            sup_tag.replace_with(sup_tag.text)
    except:
        pass

    try:
        # ИЩЕМ МАКСИМАЛЬНЫЙ УРЛ У КАРТИНКИ IMG И ДЕЛАЕМ ЗАМЕНУ В АТРИБУТАХ
        img_tags = content_article.find_all('img')
        for img_tag in img_tags:
            list_urls_in_tag = extract_img_urls(url, img_tag)
            s = take_one_picture(list_urls_in_tag)
            img_tag.attrs = {"src":s}
            print(img_tag, 'УП -11- img', s)
    except:
        pass

    print('УП-12')
    # # УДАЛЕНИЕ ТЕГОВ С МАЛЕНЬКИМИ КАРТИНКАМИ И GIF
    # try:
    #     img_tags = content_article.find_all('img')
    #
    #
    #     for img_tag in img_tags:
    #         list_urls_in_tag = extract_img_urls(url, content_article.find('img'))
    #         print('-0-0-0- ', list_urls_in_tag)
    #
    #         find = False
    #         # print('У П. Урл картинки ', img_tag)
    #
    #         # Пошли по атрибутам
    #         for k, v in img_tag.attrs.items():
    #             # if '/' in v:
    #             print('vvv ', k, ' ', v)
    #             ls_src = list(v.split(','))
    #
    #             # Пошли по урлам внутри атрибута
    #             for l in ls_src:
    #                 img_src = l.strip().split(' ')[0]
    #                 image_height = get_image_height(img_src)
    #                 if image_height > 800:
    #                     # print(f"The height of the image is: {image_height} pixels")
    #                     find = True
    #                     # print('url_img', img_src)
    #                     img_tag.attrs = {"src": img_src}
    #                     break
    #                 else:
    #                     # print("Failed to get the image height.")
    #                     find = False
    #             if find == True:
    #                 pass
    #                 break
    #         if find == False:
    #             img_tag.decompose()
    # except:
    #     pass

    # Находим все теги <noscript>
    try:
        noscript_tags = content_article.find_all('noscript')
        # Удаляем каждый тег <noscript> вместе с его содержимым
        for noscript_tag in noscript_tags:
            noscript_tag.decompose()
    except:
        pass


    try:
        # КОД УДАЛЯЕТ АТРИБУТЫ У ТЕГА
        ts = content_article.find_all(['ul', 'p', 'h2'])
        for t in ts:
            t.attrs = {}
    except:
        pass


    # закрыл для тестирования картинки
    tags = content_article.find_all(['h2', 'h3', 'p', 'ul', 'ol', 'table', 'img', 'blockquote', 'iframe'])
    # tags = content_article.find_all(['h2', 'img'])
    # print(content_article)
    # print('Универсальный Парсер =======', tags)
    # tags - список тегов объектов bs4
    print(type(tags[0]))

    # ДОБАВИТЬ ПЕРЫЙ Н2 В СПИСОК ТЕГОВ
    tags.insert(0, h2_first)

    # # Посмотреть какие находит теги после чистки
    for tag in tags:
        pass
        print('----> ', tag)

    # str_tags = []
    # for tag in tags:
    #     str_tags.append(str(tag))


    # СОЗДАНИН КОРТЕЖА H2 - TAGS
    list_corteg = cort(tags)

    return list_corteg

# s = univers_parse('https://polzaivrededy.ru/kak-otlichit-chagu-ot-trutovika-sovety-i-rekomendatsii-po-sboru/')
# s = univers_parse('https://foodandhealth.ru/info/regulyarniy-dnevnoy-son-sohranyaet-molodost-mozga/')
# s = univers_parse('https://style.rbc.ru/health/606e97389a7947f4ef64a9e8')
# s = univers_parse('https://fructberry.com/yagody/chernika/mesta-proizrastaniya')
# s = univers_parse('https://Style.RBC.ru/health/606e97389a7947f4ef64a9e8')
# s = univers_parse('https://fructberry.com/frukty/finiki')
# s = univers_parse('https://style.rbc.ru/health/606e97389a7947f4ef64a9e8')
# s = univers_parse('https://rskrf.ru/tips/eksperty-obyasnyayut/polza-i-vred-finikov-dlya-organizma/')
# s = univers_parse('https://rskrf.ru/tips/eksperty-obyasnyayut/polza-i-vred-finikov-dlya-organizma/')
# print('__________ИТОГОВЫЙ КОД___блок универсальный парсинг_______')
# print(s)

