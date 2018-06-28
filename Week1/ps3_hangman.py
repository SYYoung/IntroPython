# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if lettersGuessed.empty():
        return False
    for w in secretWord:
        if w not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    outList = list(secretWord)
    for i in range(len(outList)):
        if (outList[i] not in lettersGuessed):
            outList[i] = '_'
    outStr = ' '.join(outList)
    return outStr



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    allLettersList = list(string.ascii_lowercase)
    for i in lettersGuessed:
        del(allLettersList[allLettersList.index(i)])
    outStr = ''.join(allLettersList)
    return outStr
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * 1. At the start of the game, let the user know how many 
      letters the secretWord contains.

    * 2. Ask the user to supply one guess (i.e. letter) per round.

    * 3. The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * 4. After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    # step 1
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is ", len(secretWord), " letters long.")
    mistakesMade = 0
    lettersGuessed = []
    win = False
    while ((mistakesMade <= 8) and isWordGuessed(secretWord, lettersGuessed)) :
        print("------------")
        print("You have ", str(8-mistakesMade), " guesses left.")
        print("Available letters: ", getAvailableLetters(lettersGuessed))
        ch = input('Please guess a letter: ')
        if (ch in lettersGuessed):
            print("Ooops! You've already guessed that letter: ",
                  getGuessedWord(secretWord, lettersGuessed))
        elif (ch in secretWord):
            lettersGuessed.append(ch)
            print('Good guess: ', getGuessedWord(secretWord,lettersGuessed))
            if (isWordGuessed(secretWord, lettersGuessed)):
                win = True
                break
        else:
            lettersGuessed.append(ch)
            mistakesMade -= 1
            print('Oops! That letter is not in my word: ',
                  getGuessedWord(secretWord,lettersGuessed))
    print('----------')
    if (win):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ', secretWord)





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

# test code
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#result = isWordGuessed(secretWord, lettersGuessed)
#print(getGuessedWord(secretWord, lettersGuessed))
import string
#print(getAvailableLetters(lettersGuessed))

