'''
************************
Author: Sai Kiran Reddy Pitta
Date: 10 August 2018
Encoding: utf - 8
************************
'''
def updatehand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function

    hand = list(word)
    for i in hand:
        if i in list(hand.keys()):
            hand[i] -= 1
    return hand

def main():
    '''
    main function
    '''
    n_input = input()
    adict = {}
    for i in range(int(n_input)):
        i = i+1
        data = input()
        l_l = data.split()
        adict[l_l[0]] = int(l_l[1])
    data1 = input()
    print(updatehand(adict, data1))

if __name__ == "__main__":
    main()
