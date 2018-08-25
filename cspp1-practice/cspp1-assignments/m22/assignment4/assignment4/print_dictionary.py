'''
Author: Sai Kiran Reddy Pitta
Date: 25-08-2018
'''

def print_dictionary(dictionary):
    '''
    sub string
    '''
    keys = sorted(dictionary.keys())
    for key_d in keys:
        print(key_d, '-', dictionary[key_d])

def main():
    '''
    main string
    '''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
