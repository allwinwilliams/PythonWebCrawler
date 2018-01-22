"""
.. module:: page class
.. note:: to store structred page
.. moduleauthor:: Allwin Williams <allwinwilliams.info@gmail.com>
"""

class Page(object):
    """
        Page class with properties url, article and links
    """

    url=""
    article=""
    links=[]
    related={}
    def __init__(self, url, article, links):
        self.url = url
        self.article = article
        self.links = links
