'''
************************
Author: Sai Kiran Reddy Pitta
Date: 7 August 2018
Encoding: utf - 8
************************
'''


def recurpower(base, exp):
    '''
 calling function
    '''
    if exp == 1:
        return base
    return base*recurpower(base, (exp - 1))


def main():
    '''
    main
    '''
    data = input()
    data = data.split()
    print(recurpower(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
