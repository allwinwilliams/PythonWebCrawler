dict={}
dict['https://mashable.com/']={
    'content-tags':{
        "content": "article-content",
        "heading": "strong",
        "title":"",
        "image": [],
        "sub-heading": [],
        "quotes": [],
        "highlights": ["markup--code", "markup--li-code"],
        "text": ["graf graf--p" "graf-after--h3"],
        "links": ["markup--anchor", "markup--li-anchor"],
        "others": [],
        "author": []
    },
    'links':{

    },
    'weight': {

    }
}
dict['https://medium.com/']={
    'content-tags':{
        "content": "postArticle-content",
        "heading": "graf",
        "title":"",
        "image": [],
        "sub-heading": [],
        "quotes": [],
        "highlights": ["markup--code", "markup--li-code"],
        "text": ["graf graf--p", "graf-after--h3"],
        "links": ["markup--anchor", "markup--li-anchor"],
        "others": [],
        "author": []
    },
    'links':{

    },
    'weight': {

    }
}

"""
.. module:: provides website links
.. note::   gives website link to crawl through
.. moduleauthor:: Allwin Williams <allwinwilliams.info@gmail.com>
"""

def init_list():
    return dict

def set_list(new_dict):
    dict = new_dict
