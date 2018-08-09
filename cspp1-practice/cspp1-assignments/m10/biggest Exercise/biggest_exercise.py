'''
************************
Author: Sai Kiran Reddy Pitta
Date: 9 August 2018
Encoding: utf - 8
************************
'''
def biggest(adict):
    '''
    calling function
    '''
    all_values = list(adict.values())
    max_values = max(all_values)
    for i in adict:
        if adict[i] == max_values:
            return i
    
def main():
    '''
    Main function for the given program
    '''
def main():
    n_input = int(input())
    adict={}
    for i in range(int(n_input)):
        s_enter=input()
        l=s_enter.split()
        if l[0][0] not in adict:
            adict[l[0][0]]=[l[1]]
        else:
            adict[l[0][0]].append(l[1])
    print(biggest(adict))


if __name__ == "__main__":
    main()
