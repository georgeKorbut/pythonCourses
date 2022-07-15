#day 8 of 100 days of python

#prime number check
# import math

# def check_if_prime(n):
#     is_prime = True
#     n_sqrt = math.ceil(math.sqrt(n))
#     first_divisor = 0
#     for num in range(2, n_sqrt+1):
#         if n % num == 0:
#             is_prime = False
#             first_divisor = num    
#             break
#     if is_prime:
#         print(f"{n} is prime!")
#     else:
#         print(f"{n} is not prime. It is divisible by {first_divisor}.")          


# n = int(input("Check if this number is prime:"))
# check_if_prime(n)

#caesar cipher
from platform import system
import string 
import sys

alphabet = string.ascii_lowercase

direction = input("Type 'cipher' to use the encoder\n")

if direction != 'cipher':
    sys.exit("That's not what this program does")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift):
    right_shift_text = ""
    left_shift_text = ""
    index = 0
    for letter in text:
        index = alphabet.index(letter) + shift
        if index > 25:
            index %= 26
        right_shift_text += alphabet[index]  
    for letter in text:
        index = alphabet.index(letter) - shift
        if index < -25:
            index %= 26
        left_shift_text += alphabet[index]  
    print(f"Your right shift text is {right_shift_text} and your left shift text is {left_shift_text}")

# def encrypt(text, shift):
#     decrypted_list = list(text)
#     encrypted_list = []
#     index = 0
#     for letter in decrypted_list:
#         index = alphabet.index(letter) + shift
#         if index > 25:
#             index %= 26
#         encrypted_list.append(alphabet[index])  
#     encrypted_string = ''.join(str(e) for e in encrypted_list)  
#     print(f"Your encrypted text is {encrypted_string}")

# def decrypt(text, shift):
#     encrypted_list = list(text)
#     decrypted_list = []
#     index = 0
#     for letter in encrypted_list:
#         index = alphabet.index(letter) - shift
#         if index < -25:
#             index %= 26
#         decrypted_list.append(alphabet[index])    
#     decrypted_string = ''.join(str(e) for e in decrypted_list)
#     print(f"Your decrypted text is {decrypted_string}") 

caesar(text, shift)







