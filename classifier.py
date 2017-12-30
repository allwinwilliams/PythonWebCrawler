from db_services import *

"""
.. module:: classify the articles
.. note:: *has functions*
            - to check if its a articles
            - to check similar article already exists
            - to map articles to topics
.. moduleauthor:: Allwin Williams <allwinwilliams.info@gmail.com>
"""
    
def isArticle(content):
    return True

def classify(content):
    if not isArticle(content):
        return None
    if same_content(content):
        return None
    return content

def same_content(content):
    return False
