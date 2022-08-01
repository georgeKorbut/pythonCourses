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

player_pot = 100
minimum_bet = 5

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

def cards_to_string(hand):
    cards = ' '.join(str(e) for e in hand)
    return cards


print("Welcome to the blackjack table!")
while game_continue:
    bet = int(input(f"How much do you wish to bet? Minimum is {minimum_bet} and you have {player_pot}: "))
    if bet < minimum_bet:
        print(f"That is less than the minimum bet. Your bet is {minimum_bet} for this round")
    deal_cards()
    print(f"Player hand is {cards_to_string(player_hand)}")
    print(f"Dealer hand visible card is {dealer_hand[0]}")
    if determine_value(player_hand) == 21 and determine_value(dealer_hand) != 21:
        print(f"Blackjack! Player wins. Your bot is now {player_pot + bet}")
    elif determine_value(player_hand) == 21 and determine_value(dealer_hand) == 21:
        print(f"Player and dealer both have blackjack! Draw. Player pot remains {player_pot}")
    while (determine_value(player_hand) < 21):
        choice = input(f"Do you wish to hit or stand? hit:stand ")
        if choice == "hit":
            hit(player_hand)
            print(f"Player hand is {cards_to_string(player_hand)}")
            if determine_value(player_hand) > 21:
                print(f"Bust! Player pot is {player_pot - bet}")
                play_again = input("Do you want to play another round? y:n ")
                if play_again == "n":
                    break


