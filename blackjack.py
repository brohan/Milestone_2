#! /usr/bin/python3

import random


class Card:

    def __init__(self, suit, value, is_hidden):
        self.point_value = 0
        self.suit = suit
        self.value = value
        self.is_hidden = is_hidden

        if self.value == 'A':
            self.point_value = 11
        elif self.value in ['K', 'Q', 'J']:
            self.point_value = 10
        elif value in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            self.point_value = int(value)

    def __str__(self):
        if self.is_hidden:
            return '[XX]'
        else:
            return '[' + str(self.value) + self.suit + ']'

    def hide_card(self):
        self.is_hidden = True

    def reveal_card(self):
        self.is_hidden = False


class Deck:
    def __init__(self):
        cards_in_deck = []
        suits = ['S', 'H', 'D', 'C']
        values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        for suit in suits:
            for value in values:
                cards_in_deck.append(Card(suit, value, False))

        self.cards_in_deck = cards_in_deck[:]

    def __str__(self):  # Only used as a debugger
        return 'The Deck has ' + str(len(self.cards_in_deck)) + ' cards left.'

    def deal_card(self):
        card = random.choice(self.cards_in_deck)
        self.cards_in_deck.remove(card)
        return card


class Hand:
    def __init__(self, deck):
        self.pair_dealt = False
        self.hand = []
        self.hand_values = []
        self.num_of_aces = 0
        self.card1 = deck.deal_card()
        self.score = self.card1.point_value
        self.hand_values.append(self.card1.value)
        if self.card1.value == 'A':
            self.num_of_aces += 1
        self.card2 = deck.deal_card()
        self.score += self.card2.point_value
        self.hand_values.append(self.card2.value)
        if self.card2.value == 'A':
            self.num_of_aces += 1
        self.hand.append(self.card1)
        self.hand.append(self.card2)
        if self.hand_values[0] == self.hand_values[1]:
            self.pair_dealt = True

    def deal_card(self, deck):
        self.new_card = deck.deal_card()
        self.score +=self.new_card.point_value
        self.hand_values.append(self.new_card.value)
        self.hand.append(self.new_card)
        if self.score > 21:
            if self.num_of_aces:
                self.score -=10
                self.num_of_aces -=1
'''
Have to have way to:
    add another card to hand: which would update score, if score is over 21 check for ace, if ace, adjust score for ace = 1
'''


def split_deal(hand, deck):
    hand1 = hand[0]
    hand2 = hand[1]

def hit_or_stay(answer, hand, deck):
    pass # Add items to take a hit

def set_wager(balance):
    while True:
        try:
            wager = int(input('How much would you like to wager? '))
        except(ValueError, TypeError):
            print('Invalid entry, try again ')
            continue
        else:
            break
    if wager <= balance:
        return wager
    else:
        print('Your wager is too high.')
        set_wager(balance)


print('Welcome to the game of BlackJack, do you feel lucky? \n')
while True:
    try:
        player1_balance = int(input('How much $ would you like to put in your account? '))
    except:
        print('Invalid entry, try again ')
        continue
    else:
        break
print('Your account balance is now ${} \n'.format(player1_balance))

while True:
    new_deck = Deck()
    player_hand = Hand(new_deck)
    dealer_hand = Hand(new_deck)
    dealer_hand.card2.hide_card()

    if player1_balance > 0:
        wager = set_wager(player1_balance)
        print("\nDealer hand is: ", end='')
        print(*dealer_hand.hand, sep=' ')
        print('Your hand is: ', end = '')
        print(*player_hand.hand, sep=' ')
        if player_hand.pair_dealt == False:
            hit_or_stay = input('Would you like to (h)it or (s)tay? h or s ')
    else:
        print('You have no funds to bet, good-bye.')
        break