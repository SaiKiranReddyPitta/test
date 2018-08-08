'''
************************
Author: Sai Kiran Reddy Pitta
Date: 8 August 2018
Encoding: utf - 8
************************
'''
#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]


def apply_to_each(L, abs):
    for i in range(len(L)):
        L[i] = abs(L[i])
    print(L)

def main():
    data = input()
    data1 = data.split()
    list1 = []
    for j in data1:
        list1.append(int(j))
    apply_to_each(list1, abs)

if __name__ == "__main__":
    main()
