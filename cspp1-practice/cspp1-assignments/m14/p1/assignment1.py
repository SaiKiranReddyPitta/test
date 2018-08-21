'''
Author: Sai Kiran Reddy Pitta
Date: 22-08-2018
'''
import string
class cipher:
    def __init__(self, value):
        self.value = value
    def __len__(self):
        count = 0
        for i in self.value:
            count += 1
        return count

    def shift(self, shift_number):
        small_alphabet = ""
        upper_alphabet = ""
        small_alphabet = "" + string.ascii_lowercase + string.ascii_lowercase
        upper_alphabet = "" + string.ascii_uppercase + string.ascii_uppercase
        shift_string = ""
        l = len(self.value)
        for i in range(0, l):
            if self.value[i] in small_alphabet:
                shift_string += small_alphabet[small_alphabet.index(self.value[i]) + shift_number]
            elif self.value[i] in upper_alphabet:
                shift_string += upper_alphabet[upper_alphabet.index(self.value[i]) + shift_number]
            else:
                shift_string += self.value[i]
        return shift_string

def main():
    '''
    main function
    '''
    data_input = input()
    shift_number = int(input())
    cipher_object = cipher(data_input)
    print(cipher_object.shift(shift_number))


if __name__ == "__main__":
    main()
