'''
************************
Author: Sai Kiran Reddy Pitta
Date: 9 August 2018
Encoding: utf - 8
************************
'''
def how_many(adict):
    '''
    calling function
    '''
    count = 0
    values_of_dict = adict.values()
    for i in values_of_dict:
        for _ in i:
            count += 1
    return count
def main():
    '''
    Main function for the given program
    '''
    n_enter = input()
    adict = {}
    for i in range(int(n_enter)):
        s_enter = input()
        l_e = s_enter.split()
        if l_e[0][0] not in adict:
            adict[l_e[0][0]] = [l_e[1]]
        else:
            adict[l_e[0][0]].append(l_e[1])
    print(how_many(adict))


if __name__ == "__main__":
    main()
