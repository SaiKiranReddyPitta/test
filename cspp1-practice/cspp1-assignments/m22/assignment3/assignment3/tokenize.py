'''
Author: Sai Kiran Reddy Pitta
Date: 25-08-2018
'''
import re
def tokenize(string):
    '''
    sub function
    '''
    our_dict = {}

    string_lines = input()
    string_1 = ''
    for i in string:
        string_1 = re.sub('[^A-Za-z0-9]', '', string.lower())
        string_1 = input().split()
    return string_1
            
def main():
    '''
    Main function
    '''

    string = input()
    print(tokenize(string))
    

if __name__ == '__main__':
    main()

