# if else 
# print("Rollercoaster")
# height = int(input("What is your height in cm? "))

# if height > 120: 
#     print("You can ride this rollercoaster")
#     age = int(input("What is your age?"))
#     if age > 18:
#         print("Please pay $12.")
#     elif age > 12:
#         print("Please pay $7.")
#     else:
#         print("Please pay $5.")    
# else:
#     print("Sorry you must be taller to ride this ride")

#introduce modulo 
# num = int(input("Which number do you want to check?"))

# if num % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

#python pizza
print("Welcome to Python Pizza")
size = input("What size pizza do you want? S, M, or L")
add_pepperoni = input("Do you want Pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
if size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
if size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")