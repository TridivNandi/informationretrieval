import urllib2
import re
import time
import traceback
from bs4 import BeautifulSoup

#Global Variables:
#FILE_INDEX stores the index of the files starting from 1 till 1000(at most)
#The first file is named as file_1(file_FILE_INDEX).... nth file name is file_n
FILE_INDEX = 1
#This dictionary stores the file name and the corresponding URL as (key, vaue) pair
FILENAME_URL_MAP = { }
#MAXIMUM_DEPTH determines the maximum level till which the crawler will crawl.
#The seed starts with a depth value 1
MAXIMUM_DEPTH = 5
#Maximum number of pages allowed to crawl
MAXIMUM_NUMBER_OF_PAGES = 1000

def web_spider(seed_url):
    pages_to_crawl = [seed_url]
    pages_crawled = []
    next_depth = []
    depth = 1
    while pages_to_crawl and len(pages_crawled) < MAXIMUM_NUMBER_OF_PAGES and depth <= MAXIMUM_DEPTH:
        page=pages_to_crawl.pop(0)
        if page not in pages_crawled:
            #implementation of politeness policy
            time.sleep(1)
            urls = get_all_urls(page)
            union(next_depth,urls)
            pages_crawled.append(page)
            if not pages_to_crawl:
                pages_to_crawl, next_depth = next_depth, []
                depth =+1
    return pages_crawled


def union(list1, list2):
    for element in list2:
        if element not in list1:
            list1.append(element)


def write_contents(page, html_content):
    global FILE_INDEX
    filename= 'file_' + str(FILE_INDEX) + '.txt'
    file_content = open(filename, 'w')
    #storing the URL long with the page content
    file_content.write(page + "\n" + html_content)
    global FILENAME_URL_MAP
    FILENAME_URL_MAP.update({'"'+filename+'"' : '"'+page+'"'})
    file_url_list= open('crawled_urls.txt', 'a')
    file_url_list.write(str(FILE_INDEX) + "." + " "+ page + "\n")
    FILE_INDEX +=1
    file_content.close()
    file_url_list.close()


def get_all_urls(page):
    list_url=[ ]
    base_url = "https://en.wikipedia.org"
    try:
        handle= urllib2.urlopen(page)
        soup=BeautifulSoup(handle, "html.parser")
        write_contents(page, soup.prettify().encode("utf-8"))
        data = soup.findAll('div', attrs={'id':'bodyContent'})
        for div in data:
            for link in div.findAll('a',{'href' : re.compile('^/wiki/')}):
                href = link.get('href')
                #not crawling the administrative pages having ':' in their link
                if ':' in href:
                    continue
                #url = base_url + extension
                url = base_url + href
                #if we have '#' in url, extract the link upto '#'
                if '#' in url:
                    url = url[:url.index('#')]
                list_url.append(url.encode("utf-8"))
    except:
        print "Error in try block of get_all_urls!"
        print traceback.format_exc()
    return list_url

#main method
def main():
    print "The crawler is running with seed url as " + "https://en.wikipedia.org/wiki/Sustainable_energy"
    #calling the web_spider method with the given seed. It returns a list of
    #crawled urls
    my_list = web_spider("https://en.wikipedia.org/wiki/Sustainable_energy")
    #printing the list of crawled urls
    print my_list
    #printing the dictionary which maps the file name with their corresponding URL
    print FILENAME_URL_MAP


if __name__ == "__main__": main()
