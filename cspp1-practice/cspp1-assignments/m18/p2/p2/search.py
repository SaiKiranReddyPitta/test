'''
Author = Sai Kiran Reddy Pitta
Roll number = 20186002
'''
'''
Tiny Search Engine - Part 2 - Search
    In this programming assingment you are given the search index and search queries_list as input.
    Complete the program below to search in the index. Don't worry, it is explained below.
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
    The second input to this program is search queries_list.
    Each search querylist has one or more words
    A search querylist has to be tokenized i.e., the words have to be extracted
    This word may be a key in the search index.
    If the word is a key then collect the values.
    Collect the values from the search index for all the words in the search querylist.
    Make a set using the doc_id present as the first item in the values tuple.
    Return the search results.

    Note: PyLint score need not be 10/10. Anything above 9.5 is good.
'''
def search(search_index, querylist):
    '''
        function to search through the search index and return the results
        split the querylist into lowercase words
        check if the word is in the search_index
        collect all the values for the words that are in the search_index
        make a set of doc_id and return
    '''
    list1 = set()
    querylist = querylist.lower()
    querylist = querylist.split()
    for i in querylist:
        if i in search_index:
            list2 = list(search_index.get(i))
            for j in list2:
                list1.add(j[0])
    return list1
def process_queries_list(search_index, queries_list):
    '''
        function to process the search queries_list
        iterate through all the queries_list and call the search function
        print the results returned by search function
    '''
    for i in queries_list:
        print(search(search_index, i))
def main():
    '''
        main function
    '''
    # This line loads the search index
    search_index = eval(input())
    # read the number of search queries_list
    lines = int(input())
    # read the search queries_list into a list
    queries_list = []
    for i in range(lines):
        queries_list.append(input())
        i += 1
    #print(queries_list)
    # call process queries_list
    process_queries_list(search_index, queries_list)
if __name__ == '__main__':
    main()
