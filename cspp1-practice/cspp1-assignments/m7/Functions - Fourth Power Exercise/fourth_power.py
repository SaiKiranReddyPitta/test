'''
Author: Sai Kiran Reddy Pitta
Date: 06 Aug 2018
Encoding: UTF-8
'''

def square(x):
    x = x**2
    return x 

def fourthPower(x):
    x = x**4
    return x

def main():
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if(temp[1] == '0'):
        print(fourthPower(int(float(str(data)))))
    else:
        print(fourthPower(data))

if __name__== "__main__":
    main()
