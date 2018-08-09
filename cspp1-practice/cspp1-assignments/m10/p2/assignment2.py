'''
************************
Author: Sai Kiran Reddy Pitta
Date: 9 August 2018
Encoding: utf - 8
************************
'''

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def get_available_letters(letters_guessed):
    ''' letters that are not present are '''
    temp_stng = "abcdefghijklmnopqrstuvwxyz"
    for each_char in letters_guessed:
        temp_stng = temp_stng.replace(each_char, "")
    return temp_stng

def is_word_guessed(secret_word, letters_guessed):
    ''' Checking the characterws if present or not '''
    for each_char in letters_guessed:
        secret_word = secret_word.replace(each_char, "")
        return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    temp_stng = secret_word
    for each_char in letters_guessed:
        temp_stng = temp_stng.replace(each_char, "")

    for each_char in temp_stng:
        if each_char != "_":
            secret_word = secret_word.replace(each_char, "_")
    return secret_word

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!!")
    letguesbyuser = ''
    numguess = 8
    print("---------------------------------------------------------------")
    while numguess>0:
        print("you have" + str(numguess) + "guesses left")
        print("available letters: " + get_available_letters(letguesbyuser))
        guess = input("Please guess a letter:")
        if guess in secretWord and guess not in letguesbyuser:
            letguesbyuser += guess
            print("Good Guess: " + get_guessed_word(secretWord, letguesbyuser))

        elif guess in letguesbyuser:
            print("Opps! The letter is selected before" + get_guessed_word(secretWord, letguesbyuser))

        else:
            letguesbyuser += guess 
            print("Opps! The wrong letter is selected" + get_guessed_word(secretWord, letguesbyuser))
            numguess -= 1

        print("---------------------------------------------------------------")

        if secretWord == get_guessed_word(secretWord, letguesbyuser):
            return ("yoo! yo won the game"+ get_guessed_word(secretWord, letguesbyuser))
            
        if numguess <= 0:
            print("Sorry, play again!!")
            break
        




def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = chooseWord(wordlist).lower()
    print(hangman(secretWord))

    

if __name__ == "__main__":
    main()
