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
   def __init__(self, threadID, website_url, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.website_url = website_url
      self.counter = counter

   def run(self):
      print "Starting........ " + self.website_url
      crawler.crawl(self.website_url)
      print "Exiting......... " + self.website_url


# threadName.exit()

website_threads=[]
i=0

for page in spider.page_list:
    time.sleep(1)
    website_threads.append(WebsiteThread(1, page, 1))
    website_threads[i].start()
    i += 1

print "Exiting Main Thread"
