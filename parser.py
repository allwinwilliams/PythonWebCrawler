from bs4 import BeautifulSoup
import urllib2, sys
import time
from lxml import html
import requests

from page import Page

def parseAddress(url):
    if url[:8] == "https://":
        return url
    if url[:7] != "http://":
        url = "http://" + url
    return url


def validateUrl(site_url, sub_url):
    if site_url == sub_url:
        print "equal"
        return sub_url

    if site_url is None or sub_url is None:
        print "none........"
        return ""

    if sub_url.endswith('/'):
        s=sub_url
    else:
        s=sub_url+'/'



    if s.startswith('#'):
        return ""
    elif s.startswith(site_url):
        return s
    elif s.startswith('./'):
        return site_url+s[2:len(s)]
    elif s.startswith('/'):
        return site_url+s[1:len(s)]
    else:
        return ""


def get_site(url):
    if url[:4] == "http":
        url_parts = url.split('/',3)
        if url_parts[2] == "":
            return None
        website_url = url_parts[0]+"//"+url_parts[2]+"/"
        return website_url
    return None

def isUrl(url):
    time.sleep(1)
    if url is None or url == "":
        return False
    print url
    site_url=get_site(url)
    print "________________ SITE URL _________________"
    print site_url
    if site_url is None or site_url == "":
        return False
    full_url = str(validateUrl(site_url, url))
    print "????????????? full_url ????????????????"
    print full_url
    if full_url is None or full_url == "":
        return False
    site=requests.get(full_url)
    if site:
        if site.status_code==200:
            return True
    return False

def getPage(myUrl):
    url=parseAddress(myUrl)
    address = validateUrl(url, url)
    if isUrl(address) != True:
        return None
    website_html=requests.get(address).content
    soup = BeautifulSoup(website_html, 'lxml')
    page = Page(address, getArticle(soup), getLinks(soup))
    return page

def getArticle(soup):
    return {'title':soup.title.string, 'content': soup.get_text().replace('\n', '').replace('\r', '').replace('\t', '')}

def getLinks(soup):
    links=[]
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links
