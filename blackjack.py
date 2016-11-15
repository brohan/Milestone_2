#! /usr/bin/python3

import random
import copy


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
        if self.new_card.value == 'A':
            self.num_of_aces += 1
        self.score += self.new_card.point_value
        self.hand_values.append(self.new_card.value)
        self.hand.append(self.new_card)
        if self.score > 21:
            if self.num_of_aces:
                self.score -= 10
                self.num_of_aces -= 1


def hit_or_stay(player_hand, dealer_hand, deck, wager):
    answer = input('Would you like to (h)it or (s)tay? h or s ')
    if answer.upper() == 'H':
        player_hand.deal_card(deck)
        print('Your new hand is:', end=' ')
        print(*player_hand.hand)
        if player_hand.score > 21:
            print('Your over 21, you BUST')
            wager = int(-wager)
            return wager
        else:
            return hit_or_stay(player_hand, dealer_hand, deck, wager)
    elif answer.upper() == 'S':
        dealer_hand.card2.reveal_card()
        print("Dealer's cards:", end=' ')
        print(*dealer_hand.hand, sep=' ')
        while dealer_hand.score < 17 and dealer_hand.score < 21:
            print("Dealer has less than 17, needs to hit")
            dealer_hand.deal_card(deck)
            print("Dealer's new hand is: ", end=' ')
            print(*dealer_hand.hand)
        if dealer_hand.score > 21:
            print('Dealer busts')
            return wager
        elif dealer_hand.score > player_hand.score:
            print('Dealer wins')
            wager = int(-wager)
            return wager
        elif dealer_hand.score < player_hand.score:
            print('You win!')
            return wager
        else:
            print('Push')
            return 0

    else:
        hit_or_stay(player_hand, dealer_hand, deck, wager)


def split_hit(hand, deck):
    print('Current hand: ')
    print(*hand.hand, sep=' ')
    hand.deal_card(deck)
    print('Your new hand is:', end=' ')
    print(*hand.hand)
    if hand.score > 21:
        print('Your over 21, you BUST')
        return hand
    elif hand == 21:
        print('Current hand = 21')
        return hand
    else:
        while True:
            answer = input('Would you like to (h)it or (s)tay? h or s ')
            if answer.upper() == 'H':
                return split_hit(hand, deck)
            elif answer.upper() == 'S':
                return hand
            else:
                continue


def split_deal(player_hand, dealer_hand, deck, wager):
    hand1 = copy.deepcopy(player_hand)
    hand2 = copy.deepcopy(player_hand)
    hand1.hand.pop()
    hand2.hand.pop(0)
    hand1.deal_card(deck)
    print('Your 1st hand is now:', end=' ')
    print(*hand1.hand, sep=' ')
    hand2.deal_card(deck)
    print('Your 2nd hand is now:', end=' ')
    print(*hand2.hand, sep=' ')
    print('Split deal not fully implemented yet, skipping')
    return 0


def set_wager(balance):
    while True:
        try:
            amount_to_bet = float(input('How much would you like to wager? '))
        except(ValueError, TypeError):
            print('Invalid entry, try again ')
            continue
        else:
            break
    if amount_to_bet <= balance:
        return amount_to_bet
    else:
        print('Your wager is too high.')
        set_wager(balance)


print('Welcome to the game of BlackJack, do you feel lucky? \n')

player_balance = 0

while True:
    try:
        player_balance = float(input('How much $ would you like to put in your account? '))
    except:
        print('Invalid entry, try again ')
        continue
    else:
        break
print('Your account balance is now ${} \n'.format(player_balance))

while True:
    new_deck = Deck()
    player_hand = Hand(new_deck)
    dealer_hand = Hand(new_deck)
    dealer_hand.card2.hide_card()

    if player_balance > 0:
        wager = set_wager(player_balance)
        print("\nDealer hand is: ", end='')
        print(*dealer_hand.hand, sep=' ')
        print('Your hand is: ', end = '')
        print(*player_hand.hand, sep=' ')

        if player_hand.pair_dealt is False:

            if player_hand.score == 21:
                print('You have a natural blackjack!')
                dealer_hand.card2.reveal_card()
                print("Dealer's cards:", end=' ')
                print(*dealer_hand.hand, sep=' ')

                if dealer_hand.score == 21:
                    print("Dealer has 21, it's a push")
                else:
                    winnings = 1.5 * wager
                    print('You win ${}\n'.format(winnings))
                    player_balance += winnings
                    print('You have a new balance of ${}\n'.format(player_balance))
            else:
                result = hit_or_stay(player_hand, dealer_hand, new_deck, wager)
                player_balance += result
                print('You have a new balance of ${}\n'.format(player_balance))

        else:
            result = split_deal(player_hand, dealer_hand, new_deck, wager)
            player_balance += result
            print('You have a new balance of ${}\n'.format(player_balance))

            pass

    else:
        print('You have no funds to bet, good-bye.')
        break