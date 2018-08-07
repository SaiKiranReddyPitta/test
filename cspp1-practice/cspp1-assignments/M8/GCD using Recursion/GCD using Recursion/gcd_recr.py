'''
************************
Author: Sai Kiran Reddy Pitta
Date: 7 August 2018
Encoding: utf - 8
************************
'''
def gcdRecur(a_num, b_num):
    if b_num == 0:
        return a
    else:
        low = min(a_num, b_num)
        high = max(a_num, b_num)
        return gcdRecur(b_num, (a_num % b_num))

def main():
    data = input()
    data = data.split()
    print(gcdRecur(int(data[0]),int(data[1])))

if __name__== "__main__":
    main()
    