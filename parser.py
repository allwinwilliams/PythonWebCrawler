from bs4 import BeautifulSoup
import urllib2, sys
import time
from lxml import html
import requests

from page import Page
"""
.. module:: for parsing a given url from web
.. note:: used by crawler to get page and check if url is a available or not
.. moduleauthor:: Allwin Williams <allwinwilliams.info@gmail.com>
"""
def parseAddress(url):
    """
     check if url is http or https, if not add http:// to the front
    """
    if url[:8] == "https://" or url[:7] == "http://":
        return url
    return "http://" + url

def validateUrl(site_url, sub_url):
    """
         **validate the url by**
         - remove anthing starts with #
         - if start with / , add site url to the front
    """
    if sub_url.endswith('/'):
        s=sub_url[:-1]
    else:
        s=sub_url
    if site_url == sub_url:
        return sub_url
    if site_url is None or sub_url is None:
        return ""

    if s.startswith('#'):
        return ""
    elif s.startswith(site_url):
        return s
    elif s.startswith('./'):
        return site_url+s[2:len(s)]
        # actually need to get page from which link is obtained and get.. but for now, because most of the timev/ framework
    elif s.startswith('/'):
        return site_url+s[1:len(s)]
    else:
        return ""

def get_site(url):
    """
        get website base url from a url inside the site
    """
    if url[:4] == "http":
        url_parts = url.split('/',3)
        if url_parts[2] == "":
            return None
        website_url = url_parts[0]+"//"+url_parts[2]+"/"
        return website_url
    return None

def isUrl(website_url, url):
    """
        check if the url is available in internet
    """
    time.sleep(1)
    if url is None or url == "":
        return False
    if website_url is None or website_url == "":
        return False
    full_url = str(validateUrl(website_url, url))
    if full_url is None or full_url == "":
        return False
    site=requests.get(full_url)
    if site is not None:
        if site.status_code==200:
            return True
    return False

def full_url(path, website_url):
    if not path.startswith('/') or path.startswith('.'):
        return path
    if path is None or website_url is None:
        return None
    return website_url+path[1:]

def getPage(website_url, myUrl):
    """
        get whole page with content, title, links in the page from a url given
    """
    url=parseAddress(myUrl)
    address = validateUrl(website_url, url)
    if isUrl(website_url, address) != True:
        return None
    website_html=requests.get(address).content
    soup = BeautifulSoup(website_html, 'lxml')
    page = Page(address, getArticle(soup), getLinks(soup))
    return page

def getArticle(soup):
    """
        get title and content from a html page
    """
    return {'title':soup.title.string, 'content': soup.get_text().replace('\n', '').replace('\r', '').replace('\t', '')}

def getLinks(soup):
    """
        get links from a html page
    """
    links=[]
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links
