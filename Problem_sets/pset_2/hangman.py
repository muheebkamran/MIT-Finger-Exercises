# Problem Set 2, hangman.py
# Name: MUHEEB KAMRAN
# Collaborators: NO ONE
# Time spent:Started at 5:59pm on 14/09/26 FINISHED ON 

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

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
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    for i in secret_word:
      if i not in letters_guessed:
          return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    guessed = ''
    for i in secret_word:
        if i in letters_guessed:
            guessed += i
        else:
            guessed += '*'
    return guessed


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabets = string.ascii_lowercase 
    x = ''
    for alpha in alphabets:
          if alpha not in letters_guessed:
              x += alpha
    return x

 

# Problem Set 2, hangman.py
# Name: MUHEEB KAMRAN
# Collaborators: NO ONE
# Time spent:Started at 5:59pm on 14/09/26 FINISHED ON 

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

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
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    guessed = ''
    for i in secret_word:
        if i in letters_guessed:
            guessed += i
        else:
            guessed += '*'
    return guessed


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
        letters have not yet been guessed. The letters should be returned in
        alphabetical order
    """
    alphabets = string.ascii_lowercase 
    x = ''
    for alpha in alphabets:
        if alpha not in letters_guessed:
            x += alpha
    return x


def hangman(secret_word, with_help):
    """   
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.
    """
    letters_guessed = []

    consonant = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"

    guesses_left = 10

    print('Welcome to Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')

    while guesses_left > 0 and not has_player_won(secret_word, letters_guessed):

        print('--------------------')
        print('You have', guesses_left, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))

        user_input = input('Please guess a letter: ')

        # Help functionality
        if user_input == '!' and with_help:
            if guesses_left >= 3:
                guesses_left -= 3
                missing_letters = [c for c in set(secret_word) if c not in letters_guessed]
                revealed_letter = random.choice(missing_letters)
                letters_guessed.append(revealed_letter)
                print("Letter revealed:", revealed_letter)
            else:
                print("Oops! Not enough guesses left:", end=' ')

        # Normal letter guess
        else:
            # Check if the user entered a single letter
            if len(user_input) == 1 and (
                'a' <= user_input <= 'z' or
                'A' <= user_input <= 'Z'
            ):

                user_input = user_input.lower()

                # Check if the letter was already guessed
                if user_input in letters_guessed:
                    print("Oops! You've already guessed that letter:", end=' ')

                else:
                    # Remember the guess
                    letters_guessed.append(user_input)

                    # Check if the letter is in the secret word
                    if user_input in secret_word:
                        print('Good guess:', end=' ')

                    else:
                        print('Oops! That letter is not in my word:', end=' ')

                        # Incorrect consonant
                        if user_input in consonant:
                            guesses_left -= 1

                        # Incorrect vowel
                        elif user_input in vowels:
                            guesses_left -= 2

            else:
                print('Oops! That is not a valid letter. Please input a letter from the alphabet:', end=' ')

        print(get_word_progress(secret_word, letters_guessed))

    print('--------------------')
    # Game finished
    if has_player_won(secret_word, letters_guessed):
        print("Congratulations, you won!")
        total_score = (guesses_left + 4 * len(set(secret_word))) + (3 * len(secret_word))
        print("Your total score for this game is:", total_score)

    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word + ".")


if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    # secret_word = choose_word(wordlist)
    # with_help = False
    # hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass
    pass