# Задача сделать так, чтобы кортеж был на основе деления по абзацам
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from Get_url_Img_from_WP import take_url_img_from_wp
from GPT3_other_tags import th_list, Chat_converstaion_p, Chat_converstaion_ul_ol, Chat_converstaion_table, Chat_converstaion_quote, Chat_converstaion_ppp
import concurrent.futures
import time
import threading
def check_img_url(url):
    return urlparse(url).netloc



def merge_4_links(urls: list) -> list:
    big_article_list = []
    for url in urls:
        big_article_list = big_article_list + get_h2_text_image(url)
    return big_article_list



def get_h2_text_image( url: str):    # return clear text of article
    string = ''
    print('работаем с урлом - ', url)
    # Исправленный текст для очистки от лишних тегов   **************************************************************
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
               'Accept': '*/*'}
    r = requests.get(url, headers=headers).text

    soup0 = BeautifulSoup(r, 'html.parser')
    # print('.', soup0)
    # поиск тега h1
    h1_tag = soup0.h1
    # поиск всех тегов
    content = soup0.find_all()

    # объект Beautiful Soup
    # предыдущий парсинг
    # content_article = soup0.find("div", class_='article')
    # content_article = soup0.find("div", class_='entry-content')
    content_article = soup0.find("div", class_='post-content')


    # УДАЛЕНИЕ ТЕГОВ SPAN В H2
    try:
        h2_all = content_article.find_all('h2')
        for h2 in h2_all:
            span_tags = h2.find_all('span')
            for span_tag in span_tags:
                span_tag.decompose()
            # удаление всех атрибутов тега
            for attr in list(h2.attrs):
                del h2[attr]
    except:
        pass

    # УДАЛЕНИЕ ТЕГОВ SPAN ВЕЗДЕ
    try:
        span_tags = content_article.find_all('span')
        for span_tag in span_tags:
            span_tag.decompose()
    except:
        pass

    # # УДАЛЕНИЕ ПУСТЫХ P
    # p_all = content_article.find_all('p')
    # for p in p_all:
    #     if len(p.get_text(strip=True)) == 0:
    #         p.extract()


    # # УДАЛЕНИЕ ТЕГОВ STRONG В P
    try:
        p_all = content_article.find_all('p')
        for p in p_all:
            strongs_tags = p.find_all('strong')
            for strong_tag in strongs_tags:
                strong_tag.replaceWithChildren()
    except:
        pass

    # УДАЛЕНИЕ ТЕГОВ SPAN В H3
    try:
        h3_all = content_article.find_all('h3')
        for h3 in h3_all:
            span_tags = h3.find_all('span')
            for span_tag in span_tags:
                span_tag.decompose()
            # удаление всех атрибутов тега
            for attr in list(h3.attrs):
                del h3[attr]
    except:
        pass

    # # УДАЛИТЬ ОКРУЖАЮЩИЙ ТЕГ P У IMG
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

    # # УДАЛИТЬ ОКРУЖАЮЩИЙ ТЕГ P У IFRAME
    try:
        img_all = content_article.find_all('iframe')
        for img in img_all:
            img.find_parent('p').unwrap()
    except:
        pass

    # ЗАМЕНА ТЕГОВ DIV SHORTCODE НА BLOCKQUOTE
    try:
        div_shorts = content_article.find_all('div', class_='shortcodestyle')
        for div_short in div_shorts:
            div_short.name = 'blockquote'
    except:
        pass

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
        print('ошибка в поиске тега 9.1')

    # УДАЛЕНИЕ МНОЖЕСТВА ТЕГОВ INS
    try:
        div_tags = content_article.find_all("ins")
        for div_tag in div_tags:
            div_tag.decompose()
    except:
        print('ошибка в поиске тега 9.2')

    # Находим все теги <A> (ссылки) и удаляем их
    a_tags = content_article.find_all('a')
    for a_tag in a_tags:
        # Заменяем тег <a> на его текстовое содержимое
        a_tag.replace_with(a_tag.text)


    # Находим все теги <SUP> оставляя содержимое
    sup_tags = content_article.find_all('sup')
    for sup_tag in sup_tags:
        # Заменяем тег <sup> на его текстовое содержимое
        sup_tag.replace_with(sup_tag.text)



    # закрыл для тестироания картинки
    tags = content_article.find_all(['h2', 'h3', 'p', 'ul', 'ol', 'table', 'img', 'blockquote', 'iframe'])
    # tags = content_article.find_all(['h2', 'img'])
    # print(soup)
    print('=======', type(tags))
    print(type(tags[0]))

    # Посмотреть какие находит теги после чистки
    for tag in tags:
        print('----> ', tag)

    # breakpoint()

    # # создание списка кортежей
    # h2 = ""
    # abzac_str = ""
    # all_article_list = []
    # cort_h2_tags = (h2, abzac_str)
    # # Сформировать кортеж Н2 и Tags
    # for tag in tags:
    #
    #     cort_h2_tags = (h2, abzac_str)
    #     if tag.name == 'h2':
    #         h2 = str(tag)
    #         all_article_list.append(cort_h2_tags)
    #     else:
    #         abzac_str = abzac_str + str(tag)
    #         print('--', abzac_str)

    # print('****', all_article_list)

    # return all_article_list

    # breakpoint()
    #
    # # По три штуки берем и создаем три потока
    # for i in range(0, len(tags), 3):
    #     chunk = tags[i:i + 3]
    #     print('чанки -> ', chunk)
    #     thread1 = threading.Thread(target=Chat_converstaion_ppp, args=(chunk[0],))
    #     thread2 = threading.Thread(target=Chat_converstaion_ppp, args=(chunk[1],))
    #     thread3 = threading.Thread(target=Chat_converstaion_ppp, args=(chunk[2],))
    #
    #     thread1.start()
    #     thread2.start()
    #     thread3.start()
    #
    #     string = string + thread1
    #     string = string + thread2
    #     string = string + thread3
    #
    #     thread1.join()
    #     thread2.join()
    #     thread3.join()

    # h2_tags = ()
    # for tag in tags:
    #     if

    # breakpoint()

    # ЕСЛИ МЫ ОТПРАВЛЯЕТ ОБЪЕКТ ТЭГ, А ТАМ УЖЕ ЕГО ПРОВЕРЯЕМ НА ТО ИЛИ ИНОЕ
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        # Запуск функции process_data в пуле потоков и передача данных из списка
        results = list(executor.map(Chat_converstaion_ppp, tags))
        print('пауза на основном потоке 5с')
        time.sleep(5)
    print(results)
    # Распаковка созданного списка
    for res in results:
        string = string + res
    # закрыть все потоки которые есть
    executor.shutdown(wait=True)

    # очистка списка
    th_list.clear()

    return string



    # # СДЕЛАТЬ СПИСОК ТЕКСТОВЫЙ  ******************************
    # tags_text = []
    #
    # for num, tag in enumerate(tags):
    #     # if tag.name == 'h2' or tag.name == 'h3':
    #     #     h2 = tag.text
    #     #     tags_text.append(h2)
    #
    #     if tag.name == 'p':
    #         abzac_str = tag.text
    #         # r1 = Chat_converstaion_p(abzac_str)
    #         # print(r1)
    #         # html = html + '<p>' + r1 + '</p>'
    #         tags_text.append(abzac_str)
    #
    # print(tags_text)
    # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    #     # Запуск функции process_data в пуле потоков и передача данных из списка
    #     results = list(executor.map(Chat_converstaion_ppp, tags_text))
    #
    # print(results)
    # exit()




    # h2 = ''
    # abzac_str = ''
    # img_str = ''
    # html = ''
    # for num, tag in enumerate(tags):
    #     print(num, ' ======= ', tag)
    #
    #     # корректировка Н2 или Н3 берется как заголовок
    #     if tag.name == 'h2' or tag.name == 'h3':
    #         h2 = tag.text
    #         print(h2)
    #         html = html + '<h2>' + h2 + '</h2>'
    #
    #     elif tag.name == 'p':
    #         abzac_str = tag.text
    #         r1 = Chat_converstaion_p(abzac_str)
    #         print(r1)
    #         html = html + '<p>' + r1 + '</p>'
    #
    #     elif tag.name == 'ul' or tag.name == 'ol':
    #         r2 = Chat_converstaion_ul_ol(tag)
    #         print(tag, ' ---> ', r2)
    #         html = html + r2
    #
    #     elif tag.name == 'table':
    #         r3 = Chat_converstaion_table(tag)
    #         print(tag, ' ---> ', r3)
    #         html = html + r3
    #
    #     elif tag.name == 'blockquote':
    #         r4 = Chat_converstaion_quote(tag)
    #         print(tag, ' ---> ', r4)
    #         html = html + r4
    #
    #     elif tag.name == 'img':
    #         print('------_', tag)
    #         src_value = None
    #         src_list = ['src', 'data-src', 'src-lazy']
    #         print('________', src_value)
    #         for s in src_list:
    #             print('ssssssss', s)
    #             src_value = tag.get(s)
    #             print('valueeeeeeeee', src_value)
    #             # нашли первый src
    #             if src_value:
    #                 break
    #         if src_value:
    #             print('valuee intooooo', src_value)
    #             full_url = requests.compat.urljoin(url, src_value)
    #             print(full_url)
    #             img_str = full_url
    #             # Добавление тега с картиной с урлом
    #             try:
    #                 img_str = take_url_img_from_wp(full_url)
    #             except:
    #                 img_str = ""
    #             print('полученный адрес картинки', img_str)
    #         html = html + '<img class="alignnone size-medium wp-image-29881" src="' + img_str + '"/>'
    #
    #     elif tag.name == 'iframe':
    #         print(tag, ' ---> ')
    #         html = html + str(tag)
    #
    #     else:
    #         print('тег не найден')

    # return html
# s = get_h2_text_image('https://vsepolezno.com/drugoe/rejtingi/5-jakoby-vrednyh-produktov-pitanija-i-ih-realnaja-polza/')
# s = get_h2_text_image('https://foodandhealth.ru/info/regulyarniy-dnevnoy-son-sohranyaet-molodost-mozga/')
# print('__________ИТОГОВЫЙ КОД__________')
# print(s)