'''
************************
Author: Sai Kiran Reddy Pitta
Date: 7 August 2018
Encoding: utf - 8
************************
'''


def factorial(n_num):
    '''
    this function is used to calculate factorial of given number
    '''
    if n_num in (0, 1):
        return 1
    return n_num*factorial((n_num-1))
def main():
    '''
    main function
    '''
    a_2 = input()
    print(factorial(int(a_2)))
if __name__ == "__main__":
    main()
