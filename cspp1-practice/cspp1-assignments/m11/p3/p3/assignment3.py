'''
Author: Sai Kiran Reddy Pitta
Date: 10 August 2018
Encoding: utf - 8
'''

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    count = 0
    i_input = len(word)
    for i in word
    	if i in hand
    		count = count + 1

    if i_input = count
    	if word in wordList
    		return True
    	else:
    		return False
    else:
    		return False


def main():
	word=input()
	n=int(input())
	adict={}
	for i in range(n):
		data=input()
		l=data.split()
		adict[l[0]]=int(l[1])
	l2=input().split()
	print(isValidWord(word,adict,l2))
		


if __name__== "__main__":
	main()