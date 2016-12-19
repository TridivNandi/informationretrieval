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

#web spider crawls web using depth-first algorithm
def web_spider(seed_url, keyword):
    #the initial_depth of the given seed url is set to 1
    initial_depth = 1
    #the depth is getting appended at the end of the url
    seed_url_string = str(seed_url) + str(initial_depth)
    pages_to_crawl = [seed_url_string]
    pages_crawled = []
    while pages_to_crawl and len(pages_crawled) < MAXIMUM_NUMBER_OF_PAGES:
        string_page=pages_to_crawl.pop(0)
        string_length= len(string_page)
        #extracting the url of the page
        page= string_page[:string_length-1]
        #extracting the depth of the page
        present_depth= int(string_page[-1])
        if page not in pages_crawled:
            #if the depth of the page is more than the MAXIMUM_DEPTH, we skip
            #the page
            if present_depth > MAXIMUM_DEPTH:
                continue
            present_depth +=1
            # maintaining the politeness policy
            time.sleep(1)
            urls = get_all_urls(page, keyword, present_depth)
            union(pages_to_crawl,urls)
            pages_crawled.append(page)
    return pages_crawled


def union(list1, list2):
    pos=0
    for element in list2:
            list1.insert(pos,element)
            pos+=1


def write_contents(page, html_content):

    global FILE_INDEX
    filename= 'file_' + str(FILE_INDEX) + '.txt'
    file_content = open(filename, 'w')
    #storing the URL long with the page content
    file_content.write(page + "\n" +html_content)
    global FILENAME_URL_MAP
    FILENAME_URL_MAP.update({'"'+filename+'"' : '"'+page+'"'})
    file_url_list= open('crawled_urls.txt', 'a')
    file_url_list.write(str(FILE_INDEX) + "." + " "+ page + "\n")
    FILE_INDEX +=1
    file_content.close()
    file_url_list.close()

def get_all_urls(page, keyword, depth):
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
                anchor_text = link.text.encode("utf-8")
                # not crawling the administrative pages having ':' in their links
                if ':' in href:
                    continue
                url = base_url + href
                #if we have '#' in url, extract the link upto '#'
                if '#' in url:
                    url = url[:url.index('#')]
                # regular expression for the link matching the given keyword
                link_regex=r'.*'+re.escape(keyword)+r'.*'
                anchor_regex=r'.*'+re.escape(keyword)+r'.*'
                link_match = re.search(link_regex, '"'+str(url)+'"', re.IGNORECASE)
                anchor_text_match = re.search(anchor_regex,'"'+anchor_text+'"', re.IGNORECASE)
                #if the keyword is not in the anchor text as well as the URL,
                #the flow goes to the next iteration
                if (not anchor_text_match) and (not link_match):
                    continue
                url = url + str(depth)
                list_url.append(url.encode("utf-8"))
    except:
        print "Error in try block of get_all_urls!"
        print traceback.format_exc()
    return list_url

#main method
def main():
    keyword = raw_input ('Enter the keyword: ')
    print ("The crawler is running with seed url as " + "https://en.wikipedia.org/wiki/Sustainable_energy")
    #calling the web spider with the given seed and keyword given by user. It returns a list of
    #crawled urls
    my_list = web_spider("https://en.wikipedia.org/wiki/Sustainable_energy", str(keyword))
    # printing the list of crawled urls
    print my_list
    #printing the dictionary which maps the file name with their corresponding URL
    print FILENAME_URL_MAP


if __name__ == "__main__": main()
