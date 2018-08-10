'''
Author: Sai Kiran Reddy Pitta
Date: 10 August 2018
Encoding: utf - 8
'''

def isvalidword(word, hand, wordlist):
    """
    Returns True if word is in the wordlist and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordlist.

    word: string
    hand: dictionary (string -> int)
    wordlist: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    count = 0
    i_input = len(word)
    for i in word:
        if i in hand:
            count += 1

    if i_input == count:
        if word in wordlist:
            return True
        return False
    return False


def main():
    '''
    main function
    '''
    word = input()
    n_input = int(input())
    adict = {}
    for i in range(n_input):
        data = input()
        l_inp = data.split()
        adict[l_inp[0]] = int(l_inp[1])
    abc = input().split()
    print(isvalidword(word, adict, abc))

if __name__ == "__main__":
    main()
