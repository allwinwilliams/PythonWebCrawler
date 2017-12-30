import os
from flask import Flask, jsonify, request

from bs4 import BeautifulSoup

from neo4j.v1 import GraphDatabase

import db_services

import sys
import time


"""
.. module:: provides web interface
.. note:: provides interface through which articles can be retrived under different constraint
.. moduleauthor:: Allwin Williams <allwinwilliams.info@gmail.com>
"""


@app.route('/hello',methods=['GET'])
def request_hello():
    return jsonify("hello world")


@app.route('/posts',methods=['GET'])
def getPosts():
    topics = request.args.get('topics')
    return  db_services.getArticles(topics=topics)


if __name__ == "__main__":
    neo4j-driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
