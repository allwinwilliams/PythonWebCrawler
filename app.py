import os
from flask import Flask, jsonify, request

from bs4 import BeautifulSoup
import urllib, sys
import time


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
            return None
        return web_handle

def parseURL(site_url, sub_url):

    if sub_url.endswith('/'):
        s=sub_url[:-1]
    else:
        s=sub_url
    if s.startswith('#'):
        return None
    if s.startswith(site_url):
        return s
    if s.startswith('./'):
        s=site_url+s[1:len(s)]
        return s
    elif s.startswith('/'):
        s=site_url+s
        return s
    else:
        return None

def getPage(myUrl):
    var = parseURL(myUrl, myUrl)
    if var is None:
        return None
    address=parseAddress(var)
    if address is None:
        return None
    website=retrieveWebPage(address)
    if website is None:
        return None
    website_html = website.read()
    soup = BeautifulSoup(website_html, 'html.parser')

    URL = {'url': address,'title': soup.title.string, 'content': soup.get_text()}
    return URL


def getList(myUrl):

    request_url = myUrl
    print("request url"+str(request_url))

    var = parseURL(myUrl, myUrl)
    print("parsed url"+str(var))
    if var is None:
        return None

    address=parseAddress(var)
    request_address=str(address)

    print("address :"+str(request_address))
    if address is None:
        return None

    website=retrieveWebPage(address)
    if website is None:
        return None

    website_html = website.read()
    soup = BeautifulSoup(website_html, 'html.parser')

    page_list={}
    page_list[str(address)]=0
    key=""
    url=""
    i=0
    data=[]

    while True:

        for key in list(page_list.keys()):

            if page_list[key] != 0:
                page_list[key] += 1
                continue

            page_list[key] += 1
            address=parseAddress(key)

            if address is None:
                continue

            website=retrieveWebPage(address)
            if website is None:
                continue

            website_html = website.read()

            if not website_html:
                return "{'message' : 'error, cannot fetch'}"

            soup = BeautifulSoup(website_html, 'html.parser')

            for link in soup.find_all('a'):

                print("href:"+str(link.get('href')))

                url=parseURL(request_address, str(link.get('href')))
                print("url:"+str(url))

                if url is None:
                    continue

                address=parseAddress(url)
                print("address:"+str(address))

                if address is None:
                    continue
                else:
                    if address not in list(page_list.keys()):
                        print("...........address added..........")
                        page_list[str(address)]=0
                    else:
                        page_list[str(address)]+=1
                        print("...........weight added..........")

        i=0

        for key in list(page_list.keys()):
            if page_list[key] != 0:
                i+=1

        if i>=len(list(page_list.keys())):
            break


    for key, value in page_list.items():
        data.append({ 'url': key, 'weight': str(value) })

    response = { 'url': request_url, 'count': str(len(data)), 'data' : data }
    return response


def getPageList(myUrl):

    request_url = myUrl
    print("request url"+str(request_url))

    var = parseURL(myUrl, myUrl)
    print("parsed url"+str(var))
    if var is None:
        return None

    address=parseAddress(var)
    request_address=str(address)

    print("address :"+str(request_address))
    if address is None:
        return None

    website=retrieveWebPage(address)
    if website is None:
        return None

    website_html = website.read()

    if not website_html:
        return "{'message' : 'error, cannot fetch'}"

    soup = BeautifulSoup(website_html, 'html.parser')

    page_list={}
    page_list[str(address)]=0
    key=""
    url=""
    data=[]

    for link in soup.find_all('a'):

        print("href:"+str(link.get('href')))

        url=parseURL(request_address, str(link.get('href')))
        print("url:"+str(url))

        if url is None:
            continue

        address=parseAddress(url)
        print("address:"+str(address))

        if address is None:
            continue
        else:
            if address not in list(page_list.keys()):
                print("...........address added..........")
                page_list[str(address)]=0
            else:
                page_list[str(address)]+=1
                print("...........weight added..........")

    for key, value in page_list.items():
        data.append({ 'url': key })

    response = { 'url': request_url, 'count': str(len(data)), 'data' : data }
    return response


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
        response = jsonify(getList(x))
        if response is None:
            return jsonify({'error': "error on fetching data from url "+str(x)})
        return response
    return jsonify("no url attribute given")

@app.route('/get-links',methods=['GET'])
def getLinks():
    x = request.args.get('url')
    if x:
        response = jsonify(getPageList(x))
        if response is None:
            return jsonify({'error': "error on fetching data from url "+str(x)})
        return response
    return jsonify("no url attribute given")

@app.route('/parser',methods=['GET'])
def request_parserfunc():
    x = request.args.get('url')
    if x:
        response = jsonify(getPage(x))
        if response is None:
            return jsonify({'error': "error on fetching data from url "+str(x)})
        return response
    return jsonify("no url attribute given")



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
