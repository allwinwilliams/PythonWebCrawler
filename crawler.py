import time

import parser
import db_services
from classifier import *

from page import Page
import spider

"""
.. module:: crawl through a website
.. note:: uses crawl function
.. moduleauthor:: Allwin Williams <allwinwilliams.info@gmail.com>
"""

def crawl(website_url):
    """
        crawl function gets a website_url as input,
        get links in the page from the parser and go to that page and so on...
        after getting the page it calls classify and store function in classifier
    """
    time.sleep(1)
    while True:
        pages=spider.page_list[website_url]["links"]
        key=""
        url=""
        page=parser.getPage(website_url, website_url)
        if page is None:
            print {'message' : 'error'}
            return
        print page.links
        for url in page.links:
            if parser.isUrl(website_url, url):
                if url not in list(pages.keys()):
                    pages[url] = 0
                    print "\n\n new url added........."
                    print url
                    print "pages"
                    print pages
                    print "pages list"
                    print spider.page_list
                else:
                    pages[url] += 1
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
