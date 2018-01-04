dict={}
dict['https://mashable.com/']={
    'tags':{
        "content": ["section-content"],
        "heading": ["graf", "graf--h3", "graf--leading", "graf--title"],
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

    }
}
dict['https://medium.com/']={
    'tags':{
        "content": ["section-content"],
        "heading": ["graf", "graf--h3", "graf--leading", "graf--title"],
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
