#rock, paper, scissors game

import random

num_choice = int(input("What do you choose? 0 for rock, 1 for paper, and 2 for scissors"))

options = ["rock", "paper", "scissors"]

human_choice = options[num_choice]
computer_choice = options[random.randint(0,2)]

if human_choice == computer_choice:
    print("Its a draw!")
elif (human_choice == "rock" and computer_choice == "paper") or (human_choice == "paper" and computer_choice == "scissors") or (human_choice == "scissors" and computer_choice == "rock"):
    print("You lose!")
else:
    print("Congradulations you win!")

print(f"You chose {human_choice}, the computer chose {computer_choice}")
