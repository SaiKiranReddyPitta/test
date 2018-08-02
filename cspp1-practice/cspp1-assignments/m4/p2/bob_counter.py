'''
Author Name: Sai Kiran Reddy Pitta
Date: 02-08-2018
'''

def main():
    '''
    This function gives Total number of times word "bob" got repeated in the String
    '''
    s_1 = input()
    s_2 = "bob"
    l_1 = len(s_1)
    count = 0
    for i in range(0, l_1, 1):
        if s_1[i:i+3] == s_2:
            count = count + 1
    print(count)

if __name__ == "__main__":
    main()
