# РАБОТАЮЩАЯ ПРОГРАММА,КОТОРАЯ ПАРСИТ, РЕРАЙТИТ, МЕНЯЕТ API

from Parsing_all_page import call_parsing
# from parsing.take_url import take_url
from Parse_H1 import parse_h1
# from Parsing_Google import search_results

import os
import sys
# from Paragraf4 import merge_4_links
# from Paragraf5 import merge_4_links
from Paragraf6 import get_h2_text_image, merge_4_links

# from Different_Paragraf import agenta
from Parsing_Google2 import parsing_google, parsing_yandex
# from GPT3_openai_4 import Chat_converstaion, results
import time
from log_write import log_write
import threading
from threading import Thread
from operator import itemgetter
import random
import pandas as pd
# from Random_Promts import random_promts
from Article_add import addWordpress
# from Add_tags import add_tag
from Parsing_to_list import parsing_to_list
from HTML_Cleaner import html_cleaner

# def create_article(url_1):
#     # обнуление буфера для статьи
#     html_all = ''
#     h1 = ''
#
#     try:
#         h1 = parse_h1(url_1)  # Парсинг H1 текущего урла, если ошибка то следующий url
#         # if not h1: continue
#         print('Заголовок Н1 базовой статьи', h1)
#
#         start_time = time.time()
#         # Создание статьи
#         html_all = get_h2_text_image(url_1)
#
#         # Почистить теги и скобки
#         html_all2 = html_cleaner(html_all)
#
#         # Добавление статьи на сайт
#         addWordpress(h1, html_all2)
#
#         end_time = time.time()
#         print('Время на создание сатьи:', end_time - start_time)
#
#
#     except:
#         pass
#         # continue

th_list = []
# domain = 'https://polzaivrededy.ru'  # название сайта на основе которого мы хотим сделать ai-сайт
# domain = 'https://foodandhealth.ru'  # название сайта на основе которого мы хотим сделать ai-сайт
domain = 'https://fructberry.com'  # название сайта на основе которого мы хотим сделать ai-сайт
# domain = 'https://kladovaia-krasoti.ru' # название сайта на основе которого мы хотим сделать ai-сайт

# БЛОК ПАРСИНГА ПО ДОМЕНУ - выключил
urls_list = parsing_to_list(domain)
# print('----------- ', urls_list)
print(' метка А')

# Замеряем время работы
start_all_time = time.time()
# if len(sys.argv) <3:
#     low = int(input('введите нижнюю границу'))
#     hight = int(input('ведите верхнюю границу'))
# else:
#     low = int(sys.argv[2])
#     hight = int(sys.argv[3])
# print(f'Границы ({low} {hight}')
# for url_1 in urls_list[low:hight]:  # Иду по urls сайта беру первый урл в списке всех урлов сайта

for url_1 in urls_list[119:]:  # Иду по urls сайта беру первый урл в списке всех урлов сайта

    print('Номер добавленной статьи ----->', urls_list.index(url_1))

    # обнуление буфера для статьи
    html_all = ''
    h1 = ''

    try:
        h1 = parse_h1(url_1)  # Парсинг H1 текущего урла, если ошибка то следующий url
        if not h1:
            continue
        print('Заголовок Н1 базовой статьи', h1)

        start_time = time.time()
        # # список из 4 ссылок похожих по Н1
        # links_4_g = parsing_yandex(h1)
        # print('список ссылок: ', links_4_g)
        # ls = merge_4_links(links_4_g)

        # ----- вывод созданного большого кортежа



        # Создание статьи
        html_all = get_h2_text_image(url_1)
        print("///////////", html_all)

        # Почистить теги и скобки
        html_all2 = html_cleaner(html_all)

        print('--------------- HTML ----------', html_all)
        # Добавление статьи на сайт
        addWordpress(h1, html_all)

        end_time = time.time()
        print('Время на создание сатьи:', end_time - start_time)

        # запись в файл данных по статье
        log_write(urls_list, url_1)
    except:
        continue


end_all_time = time.time()
print('Общее время работы программы: ', end_all_time - start_all_time)
