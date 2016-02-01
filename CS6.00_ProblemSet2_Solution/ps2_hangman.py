# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words_ps3.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
def available_letters(guessed):
    available_letters = ''
    for letter in string.lowercase:
        if letter not in guessed:
            available_letters += letter
    return available_letters

def partial_word(selected_word,guessed):
    result = ''
    for letter in selected_word:
        if letter in guessed:
            result += letter
        else:
            result += '_'

    return result

def hangman():
    selected_word = choose_word(wordlist).lower() 
    assert selected_word is not None

    guessed = ''
    number_guesses = 8
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is %d letters long.' %(len(selected_word))
    print selected_word
    while(number_guesses):
        print '---------------'
        print 'You have %d guesses left' %(number_guesses)
        print 'Available letters:' + available_letters(guessed)
        guessing = raw_input('please guess a letter:')
        if guessing in guessed:
            print 'Opps, you have guessed it and please select one from available letters: ' + partial_word(selected_word,guessed)
        elif guessing in selected_word: 
            guessed += guessing
            print 'Good guessing: ' + partial_word(selected_word,guessed)
        else:
            guessed += guessing
            number_guesses -= 1
            print 'Opps, you get wrong guessing: ' + partial_word(selected_word,guessed)
              
        if selected_word in guessed:
            print 'Congra, you win'
            break

    if number_guesses == 0:
        print 'you lost the game'
            

if __name__=='__main__':
    words_list = load_words()
    print words_list
