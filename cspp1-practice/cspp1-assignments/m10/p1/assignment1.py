'''
************************
Author: Sai Kiran Reddy Pitta
Date: 9 August 2018
Encoding: utf - 8
************************
'''
def get_available_letters(letters_guessed):
    '''
    calling function
    '''
    output = list('abcdefghijklmnopqrstuvwxyz')
    for i in letters_guessed:
        output.remove(i)
    return ''.joins(output)


def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))


if __name__ == "__main__":
    main()
