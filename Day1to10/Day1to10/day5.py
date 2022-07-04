#password generator

import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbols = ['!','#','$','%','&','(',')','*','+']
numbers = ['0','1','2','3','4','5','6','7','8','9']

print("Welcome to the Python Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

combined_list = []

for nr in range(0, nr_letters):
    if random.randint(0, 1) == 1:
        combined_list.append(letters[random.randint(0, len(letters)-1)].upper())
    else:
        combined_list.append(letters[random.randint(0, len(letters)-1)])

for nr in range(0, nr_symbols):
    combined_list.append(symbols[random.randint(0,len(symbols)-1)])

for nr in range(0, nr_numbers):
    combined_list.append(numbers[random.randint(0, len(numbers)-1)])

print(combined_list)

password = ""

while len(combined_list) > 0:
    random_index = random.randint(0, len(combined_list) - 1 )
    password += str(combined_list[random_index])
    combined_list.pop(random_index)

print(f"Your new password is {password}")



