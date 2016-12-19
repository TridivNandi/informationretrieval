from math import log
import operator

# Global variables:
# inlink_dictionary maintains the dictionary for all the pages and their corresponding inlinks
inlink_dictionary = {}
# outlink_dictionary maintains the dictionary for all the pages and their corresponding number of outlinks
outlink_dictionary = {}
# init_page_rank_dict maintains the initial page rank for all the pages
init_page_rank_dict = {}
# new_page_rank_dict maintains the revised page rank for all the pages
new_page_rank_dict = {}
# page_list is the list of all the pages for which the pagerank is getting calculated
page_list = []
# sink_page_list is the list of all the sink pages (pages that have no links to other pages)
sink_page_list = []
# d stands for PageRank damping/teleportation factor
d = 0.85

# parses the graph file given to it and calls functions to populate all the dictionaries
def parse_graph(graph):
    file_content = open(graph, 'r')
    for line in file_content.readlines():
        words = line.split()
        populate_inlink_dictionary(words)
        populate_page_list(words)
    populate_outlink_dictionary()

# populates the inlink dictionary
def populate_inlink_dictionary(words):
    key = words[0]
    values = words[1:]
    inlink_dictionary[key] = values

# populates the list maintaining all the pages
def populate_page_list(words):
    page_list.insert(0,words[0])

# populates the outlink dictionary
def populate_outlink_dictionary():
    for key in inlink_dictionary.keys():
        for value in inlink_dictionary[key]:
            if outlink_dictionary.has_key(value):
                outlink_dictionary[value] = outlink_dictionary[value] + 1
            else:
                outlink_dictionary[value] = 1

# populates the init_page_rank_dict with the initial page ranks of all pages
def initiate_pagerank():
    number_of_pages = len(page_list)
    for page in page_list:
        init_page_rank_dict[page] =   float (1)/number_of_pages
    initiate_sink_pagelist()

# populates sink_page_list with all the sink pages
def initiate_sink_pagelist():
    for page in page_list:
        if not outlink_dictionary.has_key(page):
            sink_page_list.insert(0,page)

# calculates the perplexity
def perplexity_calculation(dict):
    entropy = 0
    for page in page_list:
        entropy += dict[page]*log(1.0/dict[page],2)
    return 2**entropy

# calculates the page rank
def pagerank_calculation():
    counter = 0
    perplexity = 0
    iteration = 0
    initiate_pagerank()
    while(counter < 4):
        sink_page_rank = 0
        for page in sink_page_list:
            sink_page_rank = sink_page_rank + init_page_rank_dict[page]
        for page in page_list:
            new_page_rank_dict[page] = float (1-d)/len(page_list)
            new_page_rank_dict[page] += d * float (sink_page_rank/len(page_list))
            for inlink_page in inlink_dictionary[page]:
                new_page_rank_dict[page] = new_page_rank_dict[page] + (d * float(init_page_rank_dict[inlink_page]) / float(outlink_dictionary[inlink_page]))
        for page in page_list:
            init_page_rank_dict[page] = new_page_rank_dict[page]
        perplexity_new = perplexity_calculation(init_page_rank_dict)
        if abs(perplexity_new - perplexity) < 1:
            counter +=  1
        else:
            counter = 0
        perplexity = perplexity_new
        iteration += 1
        print("Perplexity for iteration number " + str(iteration) + " is " + str(perplexity_new))

# sorts and prints top 50 pages by their docID and PageRank Score
def sort_page_rank(dict):
    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
    count = 0
    while count <50 and count < len(sorted_dict):
        print sorted_dict[count]
        count += 1

# sorts and prints top 5 pages by their docID and inlink counts
def sort_in_link(dict):
    temp_dict={}
    for page in dict.keys():
        temp_dict[page]=len(dict.get(page))
    sorted_dict = sorted(temp_dict.items(), key=operator.itemgetter(1),reverse=True)
    count = 0
    while count <5 and count < len(sorted_dict):
        print sorted_dict[count]
        count += 1

# counts the number of pages with no in-links (sources) in the given dictionary
def count_sources(inlink_dict):
    counter = 0
    for page in inlink_dict.keys():
        if not inlink_dict[page]:
            counter +=1
    return counter

# main method
def main():
    filename = raw_input ('Enter the filename: ')
    parse_graph(str(filename))
    print "Starting the program..."
    pagerank_calculation()
    print "---------------------PageRank-----------------------"
    print "The top 50 pages as per their PageRank scores are : "
    sort_page_rank(new_page_rank_dict)
    print "--------------------Top Inlink counts---------------"
    print "The top 5 pages as per their in-link counts are : "
    sort_in_link(inlink_dictionary)
    print "---------------------Statistics---------------------"
    print "The total number of pages in the graph are : " + str (len(page_list))
    print "The total number of pages in the graph with no out-links (sinks) are : " + str (len(sink_page_list))
    print "The total number of pages in the graph with no in-links (sources) are : " + str (count_sources(inlink_dictionary))


if __name__ == "__main__": main()
