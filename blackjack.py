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

    #self.cardsInDeck = cardsInDeck[:]

    def __str__(self): #Only used as a debugger
        return 'The Deck has ' +str(len(self.cardsInDeck)) + ' cards left.'

    def dealCard(self):
        card = random.choice(self.cardsInDeck)
        self.cardsInDeck.remove(card)
        return card



class Dealer(object):
    def __init__(self, hand):
        self.hand = hand


class Player(object):
    def __init__(self, hand, balance=0):
        self.balance = balance
        self.hand = hand

    def add_money(self, amount):
        self.balance += amount

