#hangman game
# skipped the ascii art print

import random
from re import A

word_list = ["ardvark", "cyclops", "kraken"]

chosen_word = random.choice(word_list)
guess_list = ["_"] * len(chosen_word) 

attempts_remaining = 6

while guess_list.count("_") > 0:
    if attempts_remaining == 0:
        print("You lose!")
        break;
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:
        attempts_remaining -= 1
    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            guess_list[letter] = guess
    print(guess_list)
    if guess_list.count("_") == 0:
        print("You win!")