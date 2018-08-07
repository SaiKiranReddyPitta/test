'''
************************
Author: Sai Kiran Reddy Pitta
Date: 7 August 2018
Encoding: utf - 8
************************
'''

def gcditer(a_num, b_num):
    '''
    calling function
    '''
    low = min(a_num, b_num)
    while low > 0:
        if ((a_num % low == 0) and (b_num % low == 0)):
            return low
        low = low - 1
        #while b:
        #a, b = b, a%b
        #return a
def main():
    '''
    main function
    '''
    data = input()
    data = data.split()
    print(gcditer(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
