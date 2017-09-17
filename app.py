from flask import Flask, request, jsonify

import os

from parser import *
from spider import getPageList

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route('/test',methods=['GET'])
def test_func():
    return jsonify("Hello, World!")

# @app.route('/crawler/api/v1.0/get-page', methods=['GET'])
# def pageParse():
#     page_url = request.args.get('url')
#     if page_url:
#         page = getPage(page_url)
#         print(str(page))
#         return jsonify(page)
#     return jsonify("no url sent")
#
#
# @app.route('/crawler/api/v1.0/get-list', methods=['GET'])
# def pageList():
#     page_url = request.args.get('url')
#     if page_url:
#         pages = getPageList(page_url)
#         print(str(pages))
#         return jsonify(pages)
#     return jsonify("no url attribute")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
