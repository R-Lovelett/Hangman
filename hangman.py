import random
import string
from words import words

def get_valid_words(words):

    word = random.choice(words) # Randomly chooses something from list of provided words

    while '-' in word or ' ' in word:
        word == random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word) # Letters in the chosen word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # What the user has guesssed

    lives = 6

    # Getting user input, main gameplay loop
    while len(word_letters) > 0 and lives > 0:
        print("\nYou have ", lives, " lives left. You have used the letters: ", " ".join(used_letters))

        #what the current word is (ie W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", "".join(word_list))
        
        user_letter = input("guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in the word, please try again.")

        elif user_letter in used_letters:
            print("You have already guessed this letter, please guess again.")

        else:
            print("Invalid character. Please try again.")

    # Once user runs out of lives, or guesses the word, end the game
    if lives == 0:
        print("\nYou died, sorry. The word was: ", word)

    else:
        print("You guessed the word ", word, "!!")

hangman()