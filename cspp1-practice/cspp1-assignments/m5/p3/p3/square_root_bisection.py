'''
Author: Sai Kiran Reddy Pitta
Date: 3 Aug 2018
Encoding: UTF-8
'''
def main():
    """ This function computes
    the square root of a given number"""
    numberabc = input()
    epsilon = 0.01
    low = 0
    high = int(number)
    ans = (high + low) / 2.0
    while abs(ans ** 2 - int(number)) >= epsilon:
        if ans ** 2 < int(number):
            low = ans
        else:
            high = ans
        ans = (low + high) / 2.0
    print(ans)
if __name__ == "__main__":
    main()
