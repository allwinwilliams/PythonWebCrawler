import threading
import time
import spider
import crawler

"""
.. module:: website_thread
.. note:: for multithreading crawling of each website from spider
.. moduleauthor:: Allwin Williams <allwinwilliams.info@gmail.com>
"""

# exitFlag = 0
class WebsiteThread (threading.Thread):
   def __init__(self, threadID, website_url, tags, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.website_url = website_url
      self.tags = tags
      self.counter = counter
   def run(self):
      print "Starting........ " + self.website_url
      crawler.crawl(self.website_url, self.tags)
      print "Exiting......... " + self.website_url


# threadName.exit()
def main():
    """main function to create threads for each websites"""
    website_threads=[]
    i=0
    for page, value in spider.page_list.iteritems():
        time.sleep(1)
        website_threads.append(WebsiteThread(1, page, value['content-tags'], 1))
        website_threads[i].start()
        i += 1

    print "Exiting Main Thread"

if __name__=="__main__":
    main()
