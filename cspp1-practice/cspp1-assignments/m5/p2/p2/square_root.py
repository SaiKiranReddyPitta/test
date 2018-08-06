'''
Author : Sai Kiran Reddy Pitta 
Date : 03 August 2018
Encoding: UTF-8
'''
def main():
    ''' This function prints the square root
    of given number using Approximation method'''
    squareno = int(input())
    epsilon = 0.01
    guess = 0.0
    step = 0.1
    while abs(guess**2 - squareno) >= epsilon:
        if guess <= squareno:
            guess += step
        else:
            break
    if abs(guess**2 - squareno) >= epsilon:
        print("Failed")
    else:
        print(guess)
if __name__ == "__main__":
    main()
