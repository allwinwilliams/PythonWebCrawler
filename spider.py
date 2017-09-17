from bs4 import BeautifulSoup
import urllib, sys
import time

page_list={}
def parseAddress(input):
        if input[:7] != "http://":
                if input.find("://") != -1:
                        print( "Error: Cannot retrive URL, address must be HTTP")
                        sys.exit(1)
                else:
                        input = "http://" + input
        return input

def retrieveWebPage(address):
        try:
                web_handle = urllib2.urlopen(address)
        except urllib2.HTTPError as e:
                #print( "Cannot retrieve URL: " + str(e.code) + ": " + error_desc
                print( "Cannot retrieve URL: HTTP Error Code", e.code)
                return None
        except urllib2.URLError as e:
                print( "Cannot retrieve URL: " + e.reason[1])
                return None
        except:
                print( "Cannot retrieve URL: unknown error")
                return None
        return web_handle

def parseURL(site_url, sub_url):
    if not ( sub_url.startswith(site_url) or sub_url.startswith('./') or sub_url.startswith('#') or sub_url.startswith('/')):
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

def getPageList(myUrl):
    var = parseURL(myUrl, myUrl)
    address=parseAddress(var)
    website=retrieveWebPage(address)
    if website is None:
        return "{'message' : 'error'}"
    website_html = website.read()
    soup = BeautifulSoup(website_html, 'html.parser')

    page_list[str(address)]=0
    key=""
    url=""
    i=1
    while True:
        i=1
        for key in list(page_list.keys()):
            if page_list[key] != 0:
                continue
            page_list[key] += 1
            address=parseAddress(key)
            website=retrieveWebPage(address)
            if website is None:
                return "{'message' : 'error'}"
            website_html = website.read()
            soup = BeautifulSoup(website_html, 'html.parser')
            for link in soup.find_all('a'):
                url=parseURL(var, link.get('href').decode())
                if url != "":
                    if str(url) not in list(page_list.keys()):
                        page_list[str(url)]=0
                    else:
                        page_list[url] += 1
        for key in list(page_list.keys()):
            if page_list[key] == 0:
                i+=1
        if i>=len(list(page_list.keys())):
            break
    return list(page_list.keys())
