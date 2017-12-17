from db_services import *

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
