'''
Author Name: Sai Kiran Reddy Pitta
Date: 04-08-2018
'''
def main():
    '''
    Here we have to Print Fizz for Numbers divisible by 3 Similarly Buzz for 5 and Both for 3 and 5
    '''
    int_n = int(input())
    i = 1
    while i <= int_n:
        if i%15 == 0:
            print("Fizz")
            print("Buzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
        i = i +1

if __name__ == "__main__":
    main()
  