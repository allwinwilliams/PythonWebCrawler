class Website(object):
    name=""
    content_tags={}
    links={}
    weight=0
    related={}
    def __init__(self, name, tags, weight):
        self.name=name
        self.tags=tags
        self.weight=weight
