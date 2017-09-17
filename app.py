import os
from flask import Flask, jsonify, request

from bs4 import BeautifulSoup
import urllib, sys
import time

page_list={}
def parseAddress(input):
        if input[:7] != "http://":
                if input.find("://") != -1:
                        print( "Error: Cannot retrive URL, address must be HTTP")
                        return None
                else:
                        input = "http://" + input
        return input

def retrieveWebPage(address):
        try:
            web_handle = urllib.request.urlopen(address)
        except:
            print( "Cannot retrieve URL: unknown error")
            return urllib.urlopen("http://citinnoviz.in")
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
            if not website_html:
                return "{'message' : 'error, cannot fetch'}"
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


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route('/test',methods=['GET'])
def test_func():
    return jsonify("Hello, World!")

@app.route('/request',methods=['GET'])
def request_func():
    x = request.args.get('q')
    return jsonify(str({'query':x}))


@app.route('/spider',methods=['GET'])
def spider():
    x = request.args.get('url')
    if x:
        return jsonify(getPageList(x))
    return jsonify("no url")

@app.route('/parser',methods=['GET'])
def request_parserfunc():
    x = request.args.get('url')
    if x:
        return jsonify(getPage(x))
    return jsonify("no url")



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
