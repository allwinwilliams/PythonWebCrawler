import time

import parser
import db_services
from classifier import *
import link_provider

from page import Page
import spider


key=""
url=""

while True:
    for key, value in spider.page_list.items():
        if value != 0:
            value += 1
            continue
        spider.page_list[key] += 1
        page=parser.getPage(key)
        if page is None:
            print {'message' : 'error'}
            break
        print page.links
        spider.check_and_add_urls(page.links)
        print "...........Page_list............"
        print parser.page_list
        db_services.classify_and_store({'url': page.url, 'article': page.article})
        time.sleep(1)
