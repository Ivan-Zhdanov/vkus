import requests
from bs4 import BeautifulSoup

def tags_creator(html):
    soup = BeautifulSoup(html, "lxml")
    tags = soup.find_all(['h2', 'h3', 'p', 'ul', 'ol', 'table', 'img', 'blockquote', 'iframe'])
    return tags