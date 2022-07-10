#hangman game
# skipped the ascii art print

import random
from re import A

word_list = ["ardvark", "cyclops", "kraken"]

chosen_word = random.choice(word_list)
letter_list = ["_"] * len(chosen_word) 
guesses_list = []

attempts_remaining = 6

game_state = True

while game_state:
    guess = input("Guess a letter:")
    if guess in guesses_list:
        print("You already guessed that letter.")
        continue
    elif guess in chosen_word:
        guesses_list.append(guess)
        for letter in range(len(chosen_word)):
            if guess == chosen_word[letter]:
                letter_list[letter] = guess
        print(letter_list)
    else:
        guesses_list.append(guess)
        print(f"\'{guess}\' is not in the chosen word. You lose a life")
        attempts_remaining -= 1
        if attempts_remaining == 0:
            game_state = False
            print("You lose!")
            continue
        print(letter_list)
 