'''
************************
Author: Sai Kiran Reddy Pitta
Date: 7 August 2018
Encoding: utf - 8
************************
'''
def is_found(low_value, high_value, char, sorted_str):
    '''
    function
    '''
    middle_value = (low_value+high_value)//2
    #print(middle_value)
    if sorted_str[middle_value] == char:
        return "True"
    elif middle_value == low_value or middle_value == high_value:
        return "False"
    else:
        if sorted_str[middle_value] < char:
            return is_found(middle_value, high_value, char, sorted_str)
        return is_found(low_value, middle_value, char, sorted_str)
def isin(char, astr):
    '''
    char: a single character
    astr: an alphabetized string
    returns: True if char is in astr; False otherwise
    '''
    sorted_str = sorted(astr)
    sorted_str = ''.join(sorted_str)
    #print(sorted_str)
    low_value = 0
    high_value = len(sorted_str)
    x_x = is_found(low_value, high_value, char, sorted_str)
    return x_x
def main():
    '''
    main function
    '''
    char_input = input()
    string_input = input()
    if char_input == "" or string_input == "":
        print("no input given")
    else:
        print(isin(char_input, string_input))


if __name__ == "__main__":
    main()
    