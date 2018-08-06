
'''
Author : Sai Kiran Reddy
Date : 03 August 2018
Encoding: utf-8

'''
def main():
    ''' This function computes the square root
     of given number using Newton- Rapson method'''
    squareno = int(input())
    epsilon = 0.01
    guess = squareno / 2.0
    while abs(guess**2 - squareno) >= epsilon:
        guess = guess - (((guess ** 2) - squareno) / (2 * guess))
    print(guess)
if __name__ == "__main__":
    main()
