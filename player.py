"""
Author: Chow
Create: 2019/05/30
Last Review: 2019/06/01
"""

import deck

class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        if card.face_up:
            self.cards.append(card)
        else:
            self.cards.insert(0, card)
        
    def pop(self):
        return self.cards.pop()

    def drop(self):
        cards = self.cards
        self.cards = []
        return cards

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

    def show_down(self):
        for card in self.cards:
            if card.face_up:
                card.flip()

    def show(self, check=False):
        for card in self.cards:
            card.show(check)
            print(' ', end='')
        print('')

class Player:  
    def __init__(self, chips=20, name='player', player=True):
        self.hands = [Hand()]
        self.status = []
        self.chips = chips
        self.bets = 0
        self.name = name
        self.player = player

    def split_hand(self, hand_index, card1, card2):
        self.hands[hand_index].show_down()
        self.hands.insert(hand_index + 1, Hand())
        split_card = self.hands[hand_index].pop()
        self.deal_hand(hand_index, card1)
        self.hands[hand_index + 1].add(split_card)
        self.deal_hand(hand_index + 1, card2)
        
    def deal_hand(self, hand_index, card):
        self.hands[hand_index].add(card)

    def drop_hand(self, hand_index):
        cards = self.hands[hand_index].drop()
        self.hands.pop(hand_index)
        return cards

    def add_bet(self, price):
        if self.chips > price:
            self.chips -= price
            self.bets += price
            return True
        else:
            return False
    
    def win(self):
        self.chips += self.bets
        self.bets = 0

    def lose(self):
        self.bets = 0

    def command_1(self, hand_index):
        surrender_allow = True
        add_bet_allow = self.chips > 0
        split_allow = self.hands[hand_index].check_split_allow()
        pass_allow = True
        while True:
            command = input(
                "1.Surrender:{0}, 2.Raise_bet:{1}, 3:Split:{2}, 4:Pass:{3}\n".format(
                    surrender_allow, add_bet_allow, split_allow, pass_allow
                )
            )
            if (surrender_allow and command == '1') \
                or (add_bet_allow and command == '2') \
                or (split_allow and command == '3') \
                or (pass_allow and command == '4'):
                break
        return command

    def command_2(self, hand_index):
        hit_allow = self.hands[hand_index].calc_total_value()!= 22 \
            and self.hands[hand_index].calc_total_value()!= 21\
            and len(self.hands[hand_index].cards) < 5
        stop_allow = True
        while True:
            command = input(
                "1.Hit:{0}, 2.Stop:{1}\n".format(
                    hit_allow, stop_allow
                )
            )
            if (hit_allow and command == '1') \
                or (stop_allow and command == '2'):
                break
        return command

    def show_hands(self, check=False):
        for hand_index, hand in enumerate(self.hands):
            print("hands-{0}: ".format(hand_index), end='')
            hand.show(check)

if __name__ == "__main__":
    dealer = Player(40)
    dealer.deal_hand(0, deck.Card(12, 'spade'))
    dealer.deal_hand(0, deck.Card(1, 'spade', True))
    dealer.deal_hand(0, deck.Card(2, 'heart', True))
    dealer.show_hands()