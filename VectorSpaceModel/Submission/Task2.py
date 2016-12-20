import glob
import operator
import os
import traceback
import math

# dictionary of the documents and their corresponding token counts
TOKEN_COUNT= {}
# dictionary of the document names and their corresponding document IDs
DOCNAME_DOCID_DICT = {}
# total number of documents
NO_OF_DOCS = 1000

# creates inverted index for unigrams
def inverted_index_unigram():

    inverted_index = {}
    DOC_ID = 0

    try:
        dir_name = os.getcwd()
        path = os.path.join(dir_name,'corpus')
        for filename in glob.glob(os.path.join(path, '*.txt')):
            with file(filename) as f:
                DOC_ID += 1
                doc = f.read()
                file_key = str(filename).split ('corpus\\')[1][:-4]
                print "Generating index for " + file_key
                TOKEN_COUNT[file_key] = len(doc.split())
                DOCNAME_DOCID_DICT.update({file_key:DOC_ID})
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

    except:
        print "Error in try block of inverted_index_unigram!"
        print traceback.format_exc()

    return inverted_index

def rank_docs(query,inverted_index):

    # list of unique query terms
    query_term_list = []
    # inverted index of query terms having normlized tf
    normalized_term_freq_dict = {}
    # inverted index of query terms having tf*idf
    tf_idf_dict = {}
    # index of relevant documents with corresponding tf*idf of query terms
    doc_tf_idf_dict ={}
    # dictionary of tf*idf for the query
    tf_idf_dict_query = {}
    # dictionary of document scores
    doc_scores = {}
    # dictionary of document vector magnitudes
    doc_vector_mag_dict = {}

    for term in query.split():
        if term not in query_term_list:
            query_term_list.append(term)

    for term in query_term_list:
        if term in inverted_index:
            normalized_term_freq_dict[term] = inverted_index[term]
        else:
            normalized_term_freq_dict[term] = {}

    for term in normalized_term_freq_dict:
        doc_dict = normalized_term_freq_dict[term]
        for doc in doc_dict:
            doc_dict[doc] = float(doc_dict[doc]) / float(TOKEN_COUNT[doc])

    tf_idf_dict = normalized_term_freq_dict.copy()
    for term in tf_idf_dict:
        doc_dict = tf_idf_dict[term]
        for doc in doc_dict:
            idf = 1 + math.log((float(NO_OF_DOCS)) / float(len(normalized_term_freq_dict[term])+1))
            doc_dict[doc] = doc_dict[doc] * idf

    for term in tf_idf_dict:
        doc_dict = tf_idf_dict[term]
        for doc in doc_dict:
            if not doc_tf_idf_dict.has_key(doc):
                term_dict = {term : doc_dict[doc]}
                doc_tf_idf_dict[doc] = term_dict
            else:
                term_dict = {term : doc_dict[doc]}
                doc_tf_idf_dict[doc].update(term_dict)

    # initial query vector square sum
    query_vector_square_sum = 0

    for term in query_term_list:
        tf = termFrequency(term,query)
        idf = 1 + math.log((float(NO_OF_DOCS)) / float(len(normalized_term_freq_dict[term])+1))
        tf_idf = tf * idf
        query_vector_square_sum += math.pow(tf_idf,2)
        tf_idf_dict_query[term] = tf_idf

    query_vector_mag = math.sqrt(query_vector_square_sum)

    for doc in doc_tf_idf_dict:
        doc_vector_square_sum = 0
        for term in inverted_index:
            doc_dict = inverted_index[term]
            if doc_dict.has_key(doc):
                tf = float(doc_dict[doc]) / float(TOKEN_COUNT[doc])
                idf = 1 + math.log((float(NO_OF_DOCS)) / float(len(inverted_index[term])+1))
                tf_idf = tf * idf
                doc_vector_square_sum += math.pow(tf_idf,2)
        doc_vector_mag = math.sqrt(doc_vector_square_sum)
        doc_vector_mag_dict[doc] = doc_vector_mag

    for doc in doc_tf_idf_dict:
        term_dict = doc_tf_idf_dict[doc]
        cosine_score = 0
        for term in tf_idf_dict_query:
            if term_dict.has_key(term):
                cosine_score += (float(term_dict[term]) * float(tf_idf_dict_query[term])) / (float (query_vector_mag) * float (doc_vector_mag_dict[doc]))
        doc_scores [doc] = cosine_score

    sorted_doc_scores = sorted(doc_scores.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_doc_scores

def print_ranked_list(inverted_index):

    try:
        file_query= open('QueryFile.txt', 'r')

        for line in file_query.readlines():
            query_array = line.split(' ')
            query_id = query_array[0]
            query_string = " ".join(query_array[1:])[:-1].lower()
            print "The query is: " + query_string
            print "Generating ranked list..."
            sorted_docs = rank_docs(query_string, inverted_index)

            if (len(sorted_docs) == 0):
                print "No matching documents found!!"
            else:
                print "Printing ranked list..."
                file_doc_list= open("Ranked_doc_list_VSM.txt",'a')
                for counter in range (min (len(sorted_docs), 100)):
                    rank = counter + 1
                    file_doc_list.write(str(query_id) + " Q0 " + str(sorted_docs[counter][0]) + "(docID" + str(DOCNAME_DOCID_DICT[str(sorted_docs[counter][0])])+ ") " + str(rank) + " " + str(sorted_docs[counter][1]) + " VSM")
                    file_doc_list.write("\n")
                file_doc_list.close()

    except:
        print "Error in try block of print_ranked_list!"
        print traceback.format_exc()


def termFrequency(query_term, query):
    normalizeQuery = query.lower().split()
    return normalizeQuery.count(query_term.lower()) / float(len(normalizeQuery))


# main function
def main():

    print "Generating inverted index..."
    index_unigram = inverted_index_unigram()
    print_ranked_list(index_unigram)

if __name__ == "__main__": main()
