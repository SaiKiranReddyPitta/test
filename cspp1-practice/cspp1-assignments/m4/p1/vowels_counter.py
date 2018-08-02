'''
Author Name: Sai Kiran Reddy Pitta
Date: 02-08-2018
'''

def main():
    '''
    This function gives Number of Vowels in a String
    '''
    s_1 = input()
    total_vowels = 0
    for char in s_1:
        if char in 'aeiou':
            total_vowels = total_vowels + 1
    print(total_vowels)


if __name__ == "__main__":
    main()
