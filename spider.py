import parser
import link_provider

page_list=link_provider.init_list()
print page_list


def check_and_add_urls(urls):
    for url in urls:
        if parser.isUrl(url):
            if url not in list(page_list.keys()):
                page_list[url] = 0
                print "\n\n new url added"
                print url
            else:
                page_list[url] += 1
