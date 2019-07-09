"""
Author: Chow
Create: 2019/05/31
Last Review: 2019/05/31
"""

import unittest

from deck import Card, Deck

class TestDeckFunctions(unittest.TestCase):
    def test_card_init(self):
        for value in range(14):
            for suit in ['spade', 'club', 'heart', 'diamond']:
                card = Card(value, suit, True)
                card.flip()
                card = Card(value, suit, False)
                card.flip()
                card.show()
        card = Card(14, 'none', True)
        card.show()
        card = Card(15, 'none', True)
        card.show()

    def test_deck_init(self):
        deck = Deck()
        card = deck.deal()
        card.show()
        card = deck.deal(True)
        card.show()
        deck.show()
        

class TestPlayerFunction(unittest.TestCase):
    def test_player_init(self):
        pass

if __name__ == "__main__":
    unittest.main()
