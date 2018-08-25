'''
Author: Sai Kiran Reddy Pitta
Date: 25-08-2018
'''

def read_the_input():
    '''
    Sub string
    '''
    given_string = ""
    number_1 = int(input())
    
    for i in range(number_1):
        given_string += input() + '\n'
    print(given_string)

def main():
    '''
    Main function
    '''
    read_the_input()

if __name__ == '__main__':
    main()
