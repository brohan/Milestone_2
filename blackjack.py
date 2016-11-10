#! /usr/bin/python3

import random


class Card(object):
    def __init__(self, suit, value, isHidden):
        self.suit = suit
        self.value = value
        self.isHidden = isHidden

        if self.value == 'A':
            self.pointValue = 11
        elif self.value in ['K', 'Q', 'J']:
            self.pointValue = 10
        elif value in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            self.pointValue = int(value)

    def __str__(self):
        if self.isHidden:
            return '[XX]'
        else:
            return '[' + str(self.value) + self.suit + ']'

    def getSuite(self):
        return self.suit

    def getValue(self):
        return self.value

    def getPointValue(self):
        return self.pointValue

    def setPointValue(self, pointValue):
        self.pointValue = pointValue

    def isHidden(self):
        return self.isHidden

    def hideCard(self):
        self.isHidden = True

    def revealCard(self):
        self.isHidden = False

    def isAce(self):
        return self.value == 'A'


class Deck(object):
    def __init__(self):
        cardsInDeck = []
        suits = ['S', 'H', 'D', 'C']
        values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        for suit in suits:
            for value in values:
                cardsInDeck.append(Card(suit,value, False))

        self.cardsInDeck = cardsInDeck[:]

    def __str__(self):  #Only used as a debugger
        return 'The Deck has ' + str(len(self.cardsInDeck)) + ' cards left.'

    def dealCard(self):
        card = random.choice(self.cardsInDeck)
        self.cardsInDeck.remove(card)
        return card


class Dealer(object):
    def __init__(self):
        pass

class Player(object):
    def __init__(self, balance=0):
        self.balance = balance


    def add_money(self, amount):
        self.balance += amount

    def subtract_money(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

deck = Deck()
player1 = Player()
dealer = Dealer()

print('Welcome to the game of BlackJack, do you feel lucky?')
while True:
    try:
        player1Balance = int(input(('How much $ would you like to put in your account? ')))
    except:
        continue
    else:
        break
player1.add_money(player1Balance)
print('Your account balance is now ${} '.format(player1.get_balance()))

