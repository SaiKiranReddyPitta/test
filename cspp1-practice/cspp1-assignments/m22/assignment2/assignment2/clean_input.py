'''
Author: Sai Kiran Reddy Pitta
Date: 25-08-2018
'''
import re
def clean_string(string):
    string_input = ''
    for _ in string:
        string_input = re.sub('[^A-Za-z0-9]', '', string.lower())
    return string_input
def main():
    '''
    main function
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
