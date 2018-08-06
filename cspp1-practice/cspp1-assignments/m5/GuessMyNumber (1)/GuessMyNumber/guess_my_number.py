'''
Author: Sai Kiran Reddy Pitta
Date: 6 August 2018
Encoding: UTF-8
'''
def main():
    """This function prints the Secret number
    which the user has guessed """
    max_n = 100
    min_n = 0
    c_h = ''
    while c_h != 'c':
        guess_n = (min_n + max_n)// 2
        print("is your guess "+ str(guess_n))
        c_h = input("Enter your choice: ")
        if c_h == 'l':
            min_n = guess_n
        else:
            max_n = guess_n
    print("The secret number you guessed is "+ str(guess_n))


if __name__ == "__main__":
    main()
