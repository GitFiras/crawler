'''
Project: Crawler

    • Crawl: parameter url
    • download webpage: get(url) to get HTML
    • fetch all found links
    • fetch all found links in the links
    • Output: print urls found
    • draw a graph of all pages linked to
        ◦ output links for graphs before parse in the format, saved in a .txt file:
        ◦ routers/ → link1
        ◦ routers/ → link2
        ◦ routers/ → link3
- Use beautiful soup to structure HTML

Instructions
./crawl.py	→ start https://en.wikipedia.org/wiki/Router_(computing)		--max 1000

Precautions:
    • Stay on the same main domain (ie. wikipedia.com)
    • broken links → status code
    • image links (non-HTML ) → content type header
    • Anchor links (pointers that link to the same page as a quick link) → ignore hash with “#…” (ie. #heading2) delete everything beyond href #.
    • De-duplicate webpages


Stopping conditions
    • Define a maximum number of links found and downloaded, based on a counter (--max 1000)
    • Define a maximum depth of steps (2)
        ◦ Queue (Python Queue or Python list)
        ◦ Insert complete url + count of ‘1’ into queue
        ◦ Downloader Processes items from the queue. Download url, Get links, put Links in the queue with count of ‘2’ as a tuple.
        ◦ Hash set, to see every url only once.
'''

import requests
import urllib
from bs4 import BeautifulSoup
import urllib3
import re
# import requests.exceptions from urllib.parse
# import urlsplit from urllib.parse
# import urlparse from collections
# import deque

class Queue:

    def __init__(self):
        self._data = list()

    def enqueue(self, item):
        """
        Add item to the queue.
        """
        self._data.append(item)
        return True

    def dequeue(self):
        """
        Remove item from the queue.
        """
        del self._data[len(self._data) - 1]

    def __len__(self):
        """
        Returns the length of the queue
        """
        return len(self._data)


class Crawler:
    '''
    Setup of Web Crawler. url definition.
    '''
    def __init__(self, max_depth=2):
        # self.url = url
        self.max_depth = max_depth
        self.queue = []
        self.url = 'https://en.wikipedia.org/wiki/Router_(computing)'

    def crawl(self):
        '''
        Crawl function based on GET from url.
        :param url, lists of urls: local, new, processed.
        :return: url status_code, url json
        '''
        local_urls = []
        nextnew_urls =[]
        processed_urls = [set()]

        new_urls = []
        second_urls = []
        page = requests.get(self.url)                                               # get page request
        data = page.text                                                            # page data
        print(f'The crawled url is: {self.url}')                                    # print url
        print(f'The status code of the connection is: {page.status_code}')          # print status code

        content = BeautifulSoup(data, "html.parser")                                # beautiful soup variable
        for link in content.findAll('a', attrs={'href': re.compile("^http://")}, limit=1000):               # limit crawl
            if type is not '.pdf':
                link_found = link.get('href')                                       # link_found
                print(link.get('href'))

        self.queue.append(self.url)                                                 # append first url to queue
        nextnew_urls = requests.get(self.url).text                                  # get page
        del self.queue[len(self.queue) - 1]                                         # dequeue item from end of queue
        self.queue.append(link.get('href'))                                         # append links found to queue

        # for i in nextnew_urls:
        #     if not i in new_urls and not i in processed_urls: new_urls.append(i)
        #     print(new_urls)
# TO DO
# put first url in queue - DONE
# process url in queue - DONE
# for every url, put back in queue - DONE
# repeat





c = Crawler()
c.crawl()



        # soup = BeautifulSoup(data)              #
        # page = urllib3.urlopen(self.url)
        # for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        #     print(link.get('href'))
        # print(soup.prettify())

















    # def constrainsts(self):
    # websitelocal_urls = set()
    # websiteforeign_urls = set()
    # urlsbroken_urls = set()


    # BROKEN URLS
    # try:
    #     response = requests.get(url)
    # except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema):
    # broken_urls.add(url)      add broken urls to it’s own set, then continue
    # continue


# content = BeautifulSoup(response.text, “lxml”)
# for link in content.find_all(‘a’):    # extract link url from the anchor    anchor = link.attrs[“href”] if “href” in link.attrs else ‘’

