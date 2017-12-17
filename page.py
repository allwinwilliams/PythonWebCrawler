
class Page(object):
    url=""
    article=""
    links=[]

    def __init__(self, url, article, links):
        self.url = url
        self.article = article
        self.links = links
