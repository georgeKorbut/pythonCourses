#blackjack project (simplified rules)
# unlimited deck
# no jokers
# J/Q/K all count as 10
# Ace is 11 or 1
# equal probaability of drawing all cards
# cards not removed from deck

import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

player_hand = []
dealer_hand = []

game_continue = True

player_pot = 0
minimum_bet = 5
player_bet = 0

def deal_cards():
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))

def hit(hand):
    hand.append(random.choice(cards))

def determine_value(hand):
    value = 0
    for card in hand:
        value += card
        if card == 11 and value > 21:
            value -= 10
    return value

def play_again():
        continue_game = input("Do you wish to play again? y:n")
        if continue_game == "y":
            continue
        else:
            print(f"final player pot is {player_pot}.")
            break

print("Welcome to the blackjack table!")
while game_continue:
    deal_cards()
    if determine_value(player_hand) == 21:
        print("Blackjack! Player wins")
        player_pot += player_bet
        continue_game = input("Do you wish to play again? y:n")
        if continue_game == "y":
            continue
        else:
            print(f"final player pot is {player_pot}.")
            break
    elif determine_value(player_hand) > 21:
        player_pot -= player_bet
        continue_game = input("Do you wish to play again? y:n")
        if continue_game == "y":
            continue
        else:
            print(f"final player pot is {player_pot}.")
            break

deal_cards()
print(player_hand)
print(dealer_hand)
