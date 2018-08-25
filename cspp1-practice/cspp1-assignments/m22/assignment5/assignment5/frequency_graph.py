'''
Author: Sai Kiran Reddy Pitta
Date: 25-08-2018
'''

def frequency_graph(dictionary):
    '''
    sub function
    '''
    keys = sorted(dictionary.keys())
    for key in keys:
        print(key, '-', dictionary[key]*('#'))


def main():
    '''
    main function
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
