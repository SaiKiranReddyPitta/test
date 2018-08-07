'''
************************
Author: Sai Kiran Reddy Pitta
Date: 7 August 2018
Encoding: utf - 8
************************
'''

def iterpower(base, exp):
    '''
    calling function
    '''
    power = 1
    j = 1
    while j <= exp:
        power = power * base
        j = j + 1
    return power

def main():
    '''
    Main Function
    '''
    data = input()
    data = data.split()
    print(iterpower(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
