"""
.. module:: term class
.. note:: to manage terms structred term
.. moduleauthor:: Allwin Williams <allwinwilliams.info@gmail.com>
"""

class Page(object):
    """
        Term class with properties url, article and links
    """
    name=""
    weight=0
    related={}
    def __init__(self, name):
        self.name=name
        self.weight=0
