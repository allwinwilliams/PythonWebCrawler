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
                print( "Cannot retrieve URL: HTTP Error Code", e.code)
                sys.exit(1)
        except urllib2.URLError as e:
                print( "Cannot retrieve URL: " + e.reason[1])
                sys.exit(1)
        except:
                print( "Cannot retrieve URL: unknown error")
                sys.exit(1)
        return web_handle

def parseURL(site_url, sub_url):
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

def getPage(myUrl):
    var = parseURL(myUrl, myUrl)
    address=parseAddress(var)
    website=retrieveWebPage(address)
    website_html = website.read()
    soup = BeautifulSoup(website_html, 'html.parser')

    URL = {'url': address,'title': soup.title.string, 'content':soup.get_text()}
    return URL
