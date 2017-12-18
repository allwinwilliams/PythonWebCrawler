import time

import parser
import db_services
from classifier import *
import link_provider

from page import Page
import spider


def crawl(website_url):
    time.sleep(1)

    pages=link_provider.dict[website_url]

    key=""
    url=""

    time.sleep(1)
    page=parser.getPage(website_url, website_url)
    if page is None:
        print {'message' : 'error'}
        return
    print page.links

    for url in page.links:
        time.sleep(1)
        if parser.isUrl(website_url, url):
            if url not in list(pages.keys()):
                pages[url] = 0
                print "\n\n new url added"
                print url
            else:
                pages[url] += 1

    while True:
        time.sleep(1)
        for key, value in pages.items():
            time.sleep(1)
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
                time.sleep(1)
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
            time.sleep(1)
