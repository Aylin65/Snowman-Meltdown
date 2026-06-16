from ascii_art import *
import random


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """ Display the snowman stage for the current number of mistakes."""
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    """Function to get the secret word,
    validate the input, loop to check if letter is in secret word,
    loop until snowman melted,
    saved or all letter guessed right """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    # For now, display the initial game state.
    while mistakes < len(STAGES) - 1:

        display_game_state(mistakes, secret_word,guessed_letters)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in secret_word:
            if guess not in guessed_letters:
                guessed_letters.append(guess)
        else:
            mistakes += 1
            print("You guessed:", guess)
            print(f"{guess} not in the secret word")
        word_guessed = True

        for letter in secret_word:
            if letter not in guessed_letters:
                word_guessed = False
                break

        if word_guessed:
            print("You saved the snowman")
            break
    if mistakes >= len(STAGES) - 1:
        display_game_state(mistakes, secret_word, guessed_letters)
        print("The snowman melted!")
        print(f"The secret wird was : {secret_word} ")
