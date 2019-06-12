"""
Author: Chow
Create: 2019/05/30
Last Review: 2019/06/12
"""

class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        if card.face_up:
            self.cards.append(card)
        else:
            self.cards.insert(0, card)
        
    def pop(self, index=-1):
        return self.cards.pop(index)

    def drop(self):
        cards = self.cards
        self.cards = []
        return cards

    def show_down(self):
        for card in self.cards:
            if card.face_up:
                card.flip()

    def show(self, check=False):
        for card in self.cards:
            card.show(check)
            print(' ', end='')
        print('')

class Hand_BlackJack(Hand):
    def check_hit_allow(self):
        return self.calc_total_value() != 22 \
            and len(self.cards) < 5

    def check_split_allow(self):
        return len(self.cards) == 2 and \
            self.cards[0].value == self.cards[1].value
        
    def calc_total_value(self):
        value = 0
        ace_num = 0
        for card in self.cards:
            if card.value == 1:
                ace_num += 1
            elif card.value > 10:
                value += 10
            else:
                value += card.value
            if value > 21:
                return 22
        value += ace_num * 11
        for _ in range(ace_num):
            if value > 21:
                value -= 10
        return 22 if value > 21 else value

if __name__ == "__main__":
    from deck import card
    pass
