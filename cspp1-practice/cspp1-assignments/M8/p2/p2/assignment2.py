'''
************************
Author: Sai Kiran Reddy Pitta
Date: 7 August 2018
Encoding: utf - 8
************************
'''
def sumofdigits(n_num):
    '''
    calling function
    '''
    if n_num == 0:
        return 0
    return (n_num%10) + sumofdigits(n_num//10)


def main():
    '''
    main function
    '''
    a_num = input()
    print(sumofdigits(int(a_num)))

if __name__ == "__main__":
    main()
