#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import schedule
import sys
import time
import pandas as pd
from datetime import datetime
from src.page import Page
from src.scraper import Scraper
from src.telegram import Telegram


def print_page_info(scraper: object, page: object):
    msg = '='*28
    msg += '\n[name]\n'
    msg += f'{page.name}\n\n'
    msg += '[url]\n'
    msg += f'{page.url}\n\n'
    msg += '[filter_type]\n'
    msg += f'{page.filter_type}\n\n'
    msg += '[element]\n'
    msg += f'{page.element}\n\n'
    msg += '[description]\n'
    msg += f'{page.description}\n\n'
    msg += '[message]\n'
    msg += f'{scraper.get_element_text(page)}\n'
    msg += '='*28
    print(msg)


def main(argv):
    """
    Ejecutar de la forma:
    python main.py pages.csv
    """

    start = datetime.now()

    for filename in argv:
        path = f'./{filename}'
        name, extension = os.path.splitext(filename)

        if os.path.exists(path) and extension in ('.csv'):
            msg = f'Procesando archivo {name}'
            print(f'{"*" * len(msg)}\n{msg}\n{"*" * len(msg)}')
            df_pages = pd.read_csv(f"./{path}", sep='|')
        else:
            raise Exception('No encontrado o Extension incorrecta')

    scraper = Scraper()
    for index, row in df_pages.iterrows():
        page = Page(
            name=row['name'],
            url=row['url'],
            filter_type=row['filter_type'],
            element=row['element'],
            description=row['description']
        )
        scraper.pages = page

    # for page in scraper.pages:
    #     print_page_info(scraper, page)

    telegram = Telegram()
    # telegram.send_message()

    stop = datetime.now()
    print(f'\nTiempo => {stop - start}')

if __name__ == '__main__':
    FILENAME = 'pages.csv'
    # main(sys.argv[1:])
    # schedule.every().day.at('06:00').do(main(FILENAME))
    main([FILENAME])
