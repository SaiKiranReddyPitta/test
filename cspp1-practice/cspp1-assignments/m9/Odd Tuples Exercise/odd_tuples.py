'''
************************
Author: Sai Kiran Reddy Pitta
Date: 8 August 2018
Encoding: utf - 8
************************
'''
#Write a python function oddTuples(aTup) that takes a some numbers in the tuple as input and returns a tuple in which contains odd index values in the input tuple  

def oddTuples(atup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    sum_alt_str = ()
    for i in range(0, len(atup)+1, 2):
        sum_alt_str = sum_alt_str + (atup[i],)
    return sum_alt_str

    #return atup[::2]

def main():
    data = input()
    data = data.split()
    atup=()
    for j in range(len(data)):
        atup += ((data[j]),)
    print(oddTuples(atup))

if __name__ == "__main__":
    main()
