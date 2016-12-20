import glob
import operator
import os
import traceback


# creates inverted index for unigrams
def inverted_index_unigram():

    inverted_index = {}
    token_count= {}

    try:
        dir_name = os.getcwd()
        path = os.path.join(dir_name,'corpus')
        for filename in glob.glob(os.path.join(path, '*.txt')):
            with file(filename) as f:
                doc = f.read()
                file_key = str(filename).split ('corpus\\')[1][:-4]
                print "Generating index for " + file_key
                token_count[file_key] = len(doc.split())
                for word in doc.split():
                    if not inverted_index.has_key(word):
                        doc_dict = {file_key : 1}
                        inverted_index[word] = doc_dict
                    elif  inverted_index[word].has_key(file_key):
                        doc_dict = inverted_index[word]
                        value = doc_dict.get(file_key)
                        value= value + 1
                        doc_dict[file_key]= value
                    else:
                        doc_dict = {file_key : 1}
                        inverted_index[word].update(doc_dict)
            f.close()
        print "--------------------------------------------------------------------------------"
        print "Token count statistics:"
        print token_count

    except:
        print "Error in try block of inverted_index_unigram!"
        print traceback.format_exc()


    return inverted_index


# creates inverted index for bigrams
def inverted_index_bigram():

    inverted_index = {}
    token_count= {}

    try:
        dir_name = os.getcwd()
        path = os.path.join(dir_name,'corpus')
        for filename in glob.glob(os.path.join(path, '*.txt')):
            with file(filename) as f:
                doc = f.read()
                file_key = str(filename).split ('corpus\\')[1][:-4]
                print "Generating index for " + file_key
                word_list = doc.split()
                token_count[file_key] = len(word_list) - 1
                for i in range(len(word_list) - 1) :
                    word = word_list[i] + " " + word_list[i+1]
                    if not inverted_index.has_key(word):
                        doc_dict = {file_key : 1}
                        inverted_index[word] = doc_dict
                    elif  inverted_index[word].has_key(file_key):
                        doc_dict = inverted_index[word]
                        value = doc_dict.get(file_key)
                        value= value + 1
                        doc_dict[file_key]= value
                    else:
                        doc_dict = {file_key : 1}
                        inverted_index[word].update(doc_dict)
            f.close()
        print "--------------------------------------------------------------------------------"
        print "Token count statistics:"
        print token_count

    except:
        print "Error in try block of inverted_index_bigram!"
        print traceback.format_exc()

    return inverted_index


# creates inverted index for trigrams
def inverted_index_trigram():

    inverted_index = {}
    token_count= {}

    try:
        dir_name = os.getcwd()
        path = os.path.join(dir_name,'corpus')
        for filename in glob.glob(os.path.join(path, '*.txt')):
            with file(filename) as f:
                doc = f.read()
                file_key = str(filename).split ('corpus\\')[1][:-4]
                print "Generating index for " + file_key
                word_list = doc.split()
                token_count[file_key] = len(word_list) - 2
                for i in range(len(word_list) - 2) :
                    word = word_list[i] + " " + word_list[i+1] + " " + word_list[i+2]
                    if not inverted_index.has_key(word):
                        doc_dict = {file_key : 1}
                        inverted_index[word] = doc_dict
                    elif  inverted_index[word].has_key(file_key):
                        doc_dict = inverted_index[word]
                        value = doc_dict.get(file_key)
                        value= value + 1
                        doc_dict[file_key]= value
                    else:
                        doc_dict = {file_key : 1}
                        inverted_index[word].update(doc_dict)
            f.close()
        print "--------------------------------------------------------------------------------"
        print "Token count statistics:"
        print token_count

    except:
        print "Error in try block of inverted_index_trigram!"
        print traceback.format_exc()

    return inverted_index


# generates term frequency for any inverted index and sorts them from most to least frequent
def generate_term_freq_table(inverted_index, ngram):

    term_freq = {}

    for key in inverted_index:
        freq = 0
        doc_dict = inverted_index[key]
        for inner_key in doc_dict:
            freq = freq + doc_dict.get(inner_key)
        term_freq[key] = freq

    sorted_term_freq = sorted(term_freq.items(), key=operator.itemgetter(1), reverse=True)
    write_term_freq(sorted_term_freq, ngram)
    return sorted_term_freq


# generates file with term frequency table
def write_term_freq(sorted_term_freq, ngram):

    try:
        print "Writing term frequency table..."
        file_name= "term_freq_table" + "_" + str(ngram) + ".txt"
        file_term_freq_table= open(file_name, 'w')
        for list in sorted_term_freq:
            file_term_freq_table.write(str(list[0])+ " ")
            file_term_freq_table.write(str(list[1]))
            file_term_freq_table.write("\n")
        file_term_freq_table.close()
    except:
        print "Error in try block of write_doc_freq!"
        print traceback.format_exc()



# generates doc frequency for any inverted index and sorts them lexicographically based on term
def generate_doc_freq_table(inverted_index, ngram):

    doc_freq = {}

    for key in inverted_index:
        doc_list = []
        doc_dict = inverted_index[key]
        for inner_key in doc_dict:
            doc_list.append(inner_key)
        doc_freq[key] = doc_list

    sorted_doc_freq = sorted(doc_freq.items(), key=operator.itemgetter(0))
    write_doc_freq(sorted_doc_freq, ngram)
    return sorted_doc_freq


# generates file with doc frequency table
def write_doc_freq(sorted_doc_freq_dict, ngram):

    try:
        print "Writing document frequency table..."
        file_name= "doc_freq_table" + "_" + str(ngram) + ".txt"
        file_doc_freq_table= open(file_name, 'w')
        for list in sorted_doc_freq_dict:
            file_doc_freq_table.write(str(list[0])+ " ")
            file_doc_freq_table.write(str(list[1])+ " ")
            list_length = len (list[1])
            file_doc_freq_table.write(str(list_length))
            file_doc_freq_table.write("\n")
        file_doc_freq_table.close()
    except:
        print "Error in try block of write_doc_freq!"
        print traceback.format_exc()


# main function
def main():

    n = raw_input ('Enter value of n for n-grams: ')

    if int(n)==1:
        index_unigram = inverted_index_unigram()
        #print "---------------------------------------------------------------------------"
        #print "Inverted Index for unigram:"
        #print index_unigram
        term_freq_table_unigram = generate_term_freq_table(index_unigram, "unigram")
        doc_freq_table_unigram = generate_doc_freq_table(index_unigram, "unigram")
    elif int(n)==2:
        index_bigram = inverted_index_bigram()
        #print "---------------------------------------------------------------------------"
        #print "Inverted Index for bigram:"
        #print index_bigram
        term_freq_table_bigram = generate_term_freq_table(index_bigram, "bigram")
        doc_freq_table_bigram = generate_doc_freq_table(index_bigram, "bigram")
    elif int(n)==3:
        index_trigram = inverted_index_trigram()
        #print "---------------------------------------------------------------------------"
        #print "Inverted Index for trigram:"
        #print index_trigram
        term_freq_table_trigram = generate_term_freq_table(index_trigram, "trigram")
        doc_freq_table_trigram = generate_doc_freq_table(index_trigram, "trigram")
    else:
        print "Please enter either 1 or 2 or 3!"


if __name__ == "__main__": main()
