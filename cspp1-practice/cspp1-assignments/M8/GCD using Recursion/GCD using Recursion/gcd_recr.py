'''
************************
Author: Sai Kiran Reddy Pitta
Date: 7 August 2018
Encoding: utf - 8
************************
'''
def gcdrecur(a_num, b_num):
    '''
    calling function
    '''
    if b_num == 0:
        return a_num
    return gcdrecur(b_num, (a_num % b_num))

def main():
    '''
    main function
    '''
    data = input()
    data = data.split()
    print(gcdrecur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
    