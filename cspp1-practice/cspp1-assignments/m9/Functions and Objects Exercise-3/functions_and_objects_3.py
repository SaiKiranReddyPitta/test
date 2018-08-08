'''
************************
Author: Sai Kiran Reddy Pitta
Date: 8 August 2018
Encoding: utf - 8
************************
'''
#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]


def apply_to_each(L, f):
    for i in range(len(L)):
        L[i] = L[i] * L[i]
    print (L)
    

    
def main():
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, int)

if __name__ == "__main__":
    main()
