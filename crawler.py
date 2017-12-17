import time

import parser
import db_services
from classifier import *
import link_provider

from page import Page
import spider


def crawl(website_url):
    time.sleep(10)
    pages={website_url: 0}
    key=""
    url=""
    while True:
        time.sleep(10)
        for key, value in pages.items():
            time.sleep(10)
            if value != 0:
                value += 1
                continue
            pages[key] += 1
            page=parser.getPage(website_url, key)
            if page is None:
                print {'message' : 'error'}
                break
            print page.links

            for url in page.links:
                time.sleep(10)
                if parser.isUrl(website_url, url):
                    if url not in list(pages.keys()):
                        pages[url] = 0
                        print "\n\n new url added"
                        print url
                    else:
                        pages[url] += 1

            print "...........Page_list............"
            print parser.pages
            db_services.classify_and_store({'url': page.url, 'article': page.article})
            time.sleep(10)
