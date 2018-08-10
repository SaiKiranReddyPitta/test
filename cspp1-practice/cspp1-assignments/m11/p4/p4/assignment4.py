'''
Author: Sai Kiran Reddy Pitta
Date: 10 August 2018
Encoding: utf - 8
'''
def calculatehandlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    sum_in = 0
    for values in hand.values():
        sum_in = sum_in + values
    return sum_in

def main():
    '''
    main function
    '''
    n_input = input()
    adict = {}
    for i in range(int(n_input)):
        data = input()
        l_in = data.split()
        adict[l_in[0]] = int(l_in[1])
    print(calculatehandlen(adict))

if __name__ == "__main__":
    main()
