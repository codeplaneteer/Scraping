import requests
from bs4 import BeautifulSoup
from lxml import etree


class Scraper:
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

    def __init__(self):
        self.__pages = list()

    @property
    def pages(self) -> list:
        return self.__pages

    @pages.setter
    def pages(self, page: object):
        self.__pages.append(page)

    @pages.deleter
    def pages(self, page: object):
        self.__pages.remove(page)

    def get_element_text(self, page: object):
        res = requests.get(page.url)
        match page.filter_type:
            case "selector":
                soup = BeautifulSoup(res.content, 'html.parser')
                element = soup.select(page.element)[0].text
            case "xpath":
                soup = BeautifulSoup(res.content, 'lxml')
                soup_lxml = etree.HTML(str(soup))
                element = soup_lxml.xpath(page.element)[0].text
        return element
