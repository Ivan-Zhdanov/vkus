# Задача сделать так, чтобы кортеж был на основе деления по абзацам
import bs4
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from Get_url_Img_from_WP import take_url_img_from_wp
# from GPT3_other_tags import th_list, Chat_converstaion_p, Chat_converstaion_ul_ol, Chat_converstaion_table, Chat_converstaion_quote, Chat_converstaion_ppp
import concurrent.futures
import time
from PIL import ImageFile
import threading
from Cort import cort
from Stream import stream
from Univers_Parse import univers_parse
from Get_Image_Size import get_image_size
from Univers_Parse2 import create_cortage_tags, create_list_tags
def check_img_url(url):
    return urlparse(url).netloc

#  ????? вроде не использую
def end_url(url): #--> True
    s = url.endswith(('.jpeg', '.png', '.jpg', 'webp'))
    if s:
        return True


# ОБЪЕДИНЕНИЕ СПИСКОВ КОРТЕЖЕЙ ПО НЕСКОЛЬКИМ ССЫЛКАМ
def merge_4_links(urls: list) -> list:
    print('merge - 1')
    big_article_list = []
    for url in urls:
        print('merge - 1.2', url)
        big_article_list = big_article_list + univers_parse(url)
        print('merge - 1.3')


    return big_article_list

#
# ls = ['https://fructberry.com/frukty/finiki','https://style.rbc.ru/health/606e97389a7947f4ef64a9e8','https://fructberry.com/yagody/chernika/mesta-proizrastaniya']
# ls = ['https://fructberry.com/frukty/finiki']
# s = merge_4_links(ls)
# print(s)