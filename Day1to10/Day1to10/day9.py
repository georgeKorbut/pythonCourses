#day 9 - dictionaries

#STUDENT GRADES
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermoine": 99,
#     "Draco": 74,
#     "Neville": 62
# }

# student_grades = {}

# for key in student_scores:
#     if student_scores[key] > 90:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] > 80:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Failing"

# for key in student_grades:
#     print(f"{key}'s grade is {student_grades[key]}\n")


#TRAVEL LOG
# def add_new_country(country, cities, total_visits):
#     travel_log.append({"country": country,
#         "visits": total_visits,
#         "cities" : cities
#     })

# travel_log = [
# {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]

# new_country = input("Which country did you travel to?\n")
# visits = int(input("How many times have you been there?\n"))

# cities_visited = []
# cities = ""

# while cities != "done":
#     cities = input("Which cities have you been to? Enter 'done' when you've listed them all\n")
#     if cities == "done":
#         break
#     cities_visited.append(cities)

# add_new_country(new_country, cities_visited, visits)

# print(travel_log)

#SECRET AUCTION
import os
from turtle import clear #used to clear terminal when entering additional bidders

bid_dict = {}

def add_to_bids(name, bid):
    bid_dict[name] = bid

def winner(bid_dict):
    highest_bidder_name = ""
    highest_bidder_bid = 0
    for key in bid_dict:
        if bid_dict[key] > highest_bidder_bid:
            highest_bidder_name = key
            highest_bidder_bid = bid_dict[key]
    
    print(f"Congradulations {highest_bidder_name} you win with your bid of ${highest_bidder_bid}")

print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))
add_to_bids(name, bid)
other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")


while other_bidders == 'yes':
    os.system('cls')
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    add_to_bids(name, bid)
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no':")
    while other_bidders != "yes" and other_bidders != "no":
        other_bidders = input("That's not a valid response. Are there other bidders? Type 'yes' or 'no':")
winner(bid_dict)