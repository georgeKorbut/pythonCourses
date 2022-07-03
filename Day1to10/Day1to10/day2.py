#tip calculator project

#bmi calculator
# height = input("enter your height in m:")
# weight = input("enter your weight in kg:")

# print(type(height))
# print(type(weight))

# height_float = float(height)
# weight_float = float(weight)

# print(height_float, weight_float)

# bmi = weight_float / (height_float ** 2)
# print(int(bmi))

#day 2.3 life in weeks, f-string exercise
# age = input("What is your current age?")
# years_remaining = 90 - int(age)
# weeks_in_year = 52
# months_in_year = 12
# days_in_year = 365

# #math
# days_remaining = years_remaining * days_in_year
# weeks_remaining  = years_remaining * weeks_in_year
# months_remaining = years_remaining * months_in_year

# print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")

#tip calculator, day 2 final project
print("Welcome to the tip calculator")
bill_no_tip = int(input("What was the total bill?"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
num_people = int(input("How many people to split the bill?"))

bill_with_tip = bill_no_tip * (1 + tip_percent / 100)
bill_per_person = bill_with_tip / num_people

print("Each person should pay: ${:.2f}"
    .format(bill_per_person))

# test_format_float = 123.456789
# print("{:.2f}"
#     .format(test_format_float))


