'''
Author: Sai Kiran Reddy Pitta
Date: 24-08-2018
'''
'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
# helper function to load the stop words from a file
def load_stopwordslist(file_name):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(file_name, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords
def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    str1 = ''
    for i in text:
        for j in i:
            if 'a' <= j <= 'z' or j == ' ':
                str1 += j
    list1 = str1.split()
    extra = load_stopwordslist("stopwords.txt")
    list2 = list1[:]
    for i in list2:
        if i in extra:
            list1.remove(i)
    return list1
def build_search_index(docslist):
    '''
        Process the docslist step by step as given below
    '''
    # initialize a search index (an empty dictionary)
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop
    # clean up doc and tokenize to words list
    # add or update the words of the doc to the search index
    # return search index
    import collections
    len_docslist = len(docslist)
    searchindex = {}
    for i in range(len_docslist):
        docslist[i] = word_list(docslist[i])
        docslist[i] = collections.Counter(docslist[i])
    for i in range(len_docslist):
        for j in docslist[i]:
            if j in searchindex:
                searchindex[j].append((i, docslist[i][j]))
            else:
                searchindex[j] = [(i, docslist[i][j])]
    return searchindex
# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])
# main function that loads the docslist from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input().lower())
        i += 1
    # call print to display the search index
    print_search_index(build_search_index(documents))
if __name__ == '__main__':
    main()
