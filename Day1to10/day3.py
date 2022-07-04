# if else 
print("Rollercoaster")
height = int(input("What is your height in cm? "))

if height > 120: 
    print("You can ride this rollercoaster")
    age = int(input("What is your age?"))
    if age > 18:
        print("Please pay $12.")
    elif age > 12:
        print("Please pay $7.")
    else:
        print("Please pay $5.")    
else:
    print("Sorry you must be taller to ride this ride")

#introduce modulo 
# num = int(input("Which number do you want to check?"))

# if num % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")