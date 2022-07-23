#blackjack project
import random

card_values = {
    "K": 10,
    "Q": 10,
    "J": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "A": 11
}

player_hand = []
dealer_hand = []

player_pot = 100
MINIMUM_BET = 5

game_continue = True

#natural == blackjack == ace + face on first deal
#dealer pays 1.5*pot for naturals

def deal_cards():
    player_hand.append(random.choice(list(card_values.keys())))
    player_hand.append(random.choice(list(card_values.keys())))
    dealer_hand.append(random.choice(list(card_values.keys())))
    dealer_hand.append(random.choice(list(card_values.keys())))

def hit(hand):
    hand.append(random.choice(list(card_values.keys())))

def determine_value(hand):
    for card in hand:
        total_value += card

# deal_cards()
# print(determine_value(player_hand))

print(card_values.keys())