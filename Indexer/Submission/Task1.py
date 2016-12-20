from bs4 import BeautifulSoup
import os
import operator
import glob
import re
import traceback

# PRESENT_DIR contains the path of the directory where the code base resides
PRESENT_DIR = os.getcwd()

# FILE_NAME_LIST maintains the list of all the file names
FILE_NAME_LIST = []


# fetches the raw wikipedia articles that was downloaded in HW1 and tokenizes them
def fetch_raw_content():

    try:
        path = os.path.join(PRESENT_DIR,'raw_content')
        for filename in glob.glob(os.path.join(path, '*.txt')):
            with file(filename) as f:
                url = f.readline()
                article_name = (url.split("https://en.wikipedia.org/wiki/"))[-1][:-1]
                article_name = article_name.replace ('_', '').replace ('-', '').replace('/','').replace('%', '').replace('(','').replace(')','')
                print "Generating corpus of " + article_name
                content = f.read()
                content = content.lower()
                #print content[:1000]
                if (content.find('<span class="mw-headline" id="see_also">')!=-1):
                    content=content[:content.index('<span class="mw-headline" id="see_also">')]
                    #print "Inside if block"
                elif (content.find('<span class="mw-headline" id="references">')!=-1):
                    content=content[:content.index('<span class="mw-headline" id="references">')]
                    #print "Inside elif block"
                if (content.find('<div class="toc" id="toc">')!=-1):
                    #print "Inside second if block"
                    first_content=content[:content.index('<div class="toc" id="toc">')]
                    second_content=content[content.find('</div>', (content.find('</div>',(content.index('<div class="toc" id="toc">') + 1)) + 1)):]
                    content = first_content+second_content
                #print content
                soup = BeautifulSoup(content, "html.parser")
                soup.prettify().encode("utf-8")
                title_text = soup.find('title').get_text().encode("utf-8")
                header_text = soup.find('h1').get_text().encode("utf-8")
                data = soup.findAll('div', attrs={'id':'bodycontent'})
                body_text= ""
                for div in data:
                    body_text+=div.get_text().encode("utf-8")
                content_text = title_text + header_text + body_text
                processed_text = process_content(content_text)
                write_content(processed_text, article_name)
                f.close()
    except:
        print "Error in try block of fetch_raw_content!"
        print traceback.format_exc()



# perform text transformation on the string provided to it as argument
def process_content(content):

    #content = content.lower()
    content = re.sub(r'[@_!\s^&*?#=+$~%:;\\/|<>(){}[\]"\']' , ' ', content)
    content_word_list = []
    for word in content.split():
        word_length = len(word)
        if word[word_length - 1:word_length] == "-" or word[word_length - 1:word_length] == "," or word[word_length - 1:word_length] == ".":
            word = word[:(len(word)-1)]
            content_word_list.append(remove_preceeding_punctuation(word))
        else:
            content_word_list.append(remove_preceeding_punctuation(word))
    content_word_list = [x for x in content_word_list if x != '']
    content_word_list = " ".join(content_word_list)
    return content_word_list


# removes irrelevant punctuations before a word
def remove_preceeding_punctuation(word):

    while(word[:1] == "-" or word[:1] == "," or word[:1] == "."):
        if re.match(r'^[\-]?[0-9]*\.?[0-9]+$', word):
            return word
        if word[:1] == "-" or word[:1] == "." or word[:1] == ",":
            word = word[1:]
        else:
            return word
    return word


# writes the contents in file
def write_content(content, file_name):

    try:
        index_value=1
        if file_name not in FILE_NAME_LIST:
            FILE_NAME_LIST.insert(0,file_name)
        else:
            while(file_name in FILE_NAME_LIST):
                file_name = file_name+str(index_value)
                index_value = index_value + 1
            FILE_NAME_LIST.insert(0,file_name)
        file_index_terms= open(PRESENT_DIR+"\\"+"corpus"+"\\"+file_name+".txt",'w')
        file_index_terms.write(content)
        file_index_terms.close()
    except:
        print "Error in try block of write_content!"
        print traceback.format_exc()


# main function
def main():

    print "The corpus is getting generated!"
    fetch_raw_content()


if __name__ == "__main__": main()
