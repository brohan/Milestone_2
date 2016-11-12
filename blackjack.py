#! /usr/bin/python3

import random


class Card(object):
    pointValue = 0
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


class Hand(object):

    hasAce = False
    dealtPair = False

    def __init__(self, deck):
        self.hand = []
        self.cardValue = []
        self.card1 = deck.dealCard()
        self.score = self.card1.pointValue
        self.cardValue.append(self.card1.getValue())
        self.card2 = deck.dealCard()
        self.score += self.card2.pointValue
        self.cardValue.append(self.card2.getValue())
        self.hand.append(self.card1)
        self.hand.append(self.card2)


    def add_card(self, deck):
        self.newCard = deck.dealCard()



'''
Process for dealing cards:
 initialize with getting 2 cards, check for pairs, return pair flag, sum score, set Ace flag, add cards to hand list

Have to have way to:
    add another card to hand: which would update score, if score is over 21 check for ace, if ace, adjust score for ace = 1
    print hand (for i in hand print i' ')

'''

class PairDealt(object):
    def __init(self, hand):
        self.hand1 = self.hand[0]
        self.hand1 = self.hand[1]




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
playerHand = Hand(deck)
dealerHand = Hand(deck)
dealerHand.card2.hideCard()

print(*playerHand.hand, sep=' ')


print('Welcome to the game of BlackJack, do you feel lucky? \n')
while True:
    try:
        player1Balance = int(input('How much $ would you like to put in your account? '))
    except:
        print('Invalid entry, try again ')
        continue
    else:
        break
player1.add_money(player1Balance)
print('Your account balance is now ${} \n'.format(player1.get_balance()))

while True:
    while True:
        try:
            bet = int(input('How much would you like to bet? '))
        except:
            print('Invalid entry, try again ')
            continue
        else:
            if bet > player1Balance:
                print('Not enough funds available!')
                continue
            else:
                break





'''
 FINISH DOUBLES HERE

    if pvalue == 21:
        dcard2.revealCard()
        print('Your cards:      Dealer cards:')
        print(str(pcard1) + ' ' + str(pcard2) + '         ' + str(dcard1) + ' ' + str(dcard2))

        if pvalue == dvalue:
            print('Push: Bet returned \n')
        else:
            continue

        if dvalue >= 17:
            player1Balance += bet
            print('You win! Your balance is now {} \n'.format(player1Balance))
        else:

'''

