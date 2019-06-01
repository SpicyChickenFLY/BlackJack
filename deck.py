"""
Author: Chow
Create: 2019/05/30
Last Review: 2019/06/01
"""

import random

SUITS = ['spade', 'club', 'heart', 'diamond']

class Deck:
    def __init__(self, duplicate=1, size='no_joker'): 
        self.cards = []
        self.discard_cards = []
        """
        size: full_size, no_joker, num_only, single_suit
        duplicate >= 1
        """
        for _ in range(duplicate): 
            if size == 'no_joker':
                for suit in SUITS:
                    for value in range(1, 14):
                        self.cards.append(Card(value, suit))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, flip=False):
        deal_card = None
        if len(self.cards) > 0:
            deal_card = self.cards.pop(0)
        else:
            self.recycle()
            deal_card = self.cards.pop(0)
        if flip:
            deal_card.flip()
        return deal_card

    def drop(self, card):
        if not card.face_up:
            card.flip()
        self.discard_cards.append(card)

    def recycle(self):
        for card in self.discard_cards:
            card.flip()
        self.cards.extend(self.discard_cards)
        self.discard_cards = []
        self.shuffle()

    def show(self, check=False):
        print('cards: ')
        for card in self.cards:
            card.show(check)
            print(' ', end='')
        print()
        print('discard_cards: ')
        for card in self.discard_cards:
            card.show(check)
            print(' ', end='')
        print()

class Card:
    def __init__(self, value=1, suit=SUITS[0], face_up=False):
        """
        value: 1~15
        suit: spade, club, heart, diamond, None
        """
        self.value = value
        self.suit = suit
        self.face_up = face_up

    def flip(self):
        self.face_up = not self.face_up

    def show(self, check=False):
        if not self.face_up and not check:
            print('Hidden', end='')
        elif self.value == 15:
            print('Joker(Red)', end='')
        elif self.value == 14:
            print('Joker(Black)', end='')
        elif self.value ==13:
            print('{0}-King'.format(self.suit), end='')
        elif self.value ==12:
            print('{0}-Queen'.format(self.suit), end='')
        elif self.value ==11:
            print('{0}-Jack'.format(self.suit), end='')
        else:
            print('{0}-{1}'.format(self.suit, self.value), end='')

if __name__ == "__main__":
    deck = Deck()
    deck.show(True)
    deck.shuffle()
    card = deck.deal()
    deck.drop(card)
    card = deck.deal()
    card.flip()
    deck.drop(card)
    deck.show(False)
    deck.recycle()
    deck.show(False)