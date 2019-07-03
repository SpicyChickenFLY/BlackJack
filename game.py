"""
Author: Chow
Create: 2019/05/30
Last Review: 2019/06/18
"""

from player import Player_BlackJack, Dealer_BlackJack
from deck import Deck


class PlayerManager():
    def __init__(self):
        pass
    def new_player_connect(self):
        pass

    def player_disconnect(self):
        pass

    def dealer_disconnect(self):
        pass

    def check_player_num(self):
        pass

class GameManager():
    def __init__(self):
        self.round_num = 0
        self.round_score = []
        self.players = []
        self.dealer = None
        self.score_board = []
        self.deck = None
    
    def showScoreBoard(self):
        pass

    def boardcast(self, permission):
        pass

    def player_lose(self, player_index, hand_index):
        dropped_hand, bet = self.players[player_index].lose(hand_index)
        self.round_score[player_index] -= bet
        for card in dropped_hand:
            self.deck.drop(card)
        self.dealer.win(bet)
        self.round_score[-1] += bet
    
    def player_split(self):
        pass

    def player_raise_bet(self):
        pass

    def new_round(self):
        self.round_num += 1
        self.deck = Deck(2)
        
        score = []
        for _ in range(self.check_player_num()):
            score.append(0)

        print('Round: {0}'.format(self.round_num))

        '''Initial Phase'''
        print("--- Initial Phase ---")
        for player_index in range(len(self.players)):
            self.players[player_index].deal_hand(0, deck.deal(True))
            self.players[player_index].deal_hand(0, deck.deal())
            print('Player-{0}: '.format(self.players[player_index].name))
            self.players[player_index].show_hands(True)
        self.dealer.deal_hand(0, deck.deal(True))         
        self.dealer.deal_hand(0, deck.deal())
        print('Dealer-{0}: '.format(self.dealer.name))
        self.dealer.show_hands(True)

        '''Player Phase-1'''
        print("--- Player Phase-1 ---")
        for player_index in range(len(players)):
            hand_index = 0
            while hand_index < len(players[player_index].hands):
                print('Player-{0}: '.format(players[player_index].name))
                players[player_index].show_hands(True)
                '''Initiate Command'''
                command = players[player_index].initial_command(hand_index)
                if command == '1': # surrender
                    print('Surrender')
                    self.player_lose(player_index, hand_index)
                elif command == '2': # raise_bet
                    bet = 5
                    players[player_index].raise_bet(hand_index, bet)
                    print('Raise_bet:{0}'.format(bet))
                elif command == '3': # split
                    print('Split')
                    card1 = deck.deal(True)
                    card2 = deck.deal(True)
                    players[player_index].split_hand(hand_index, card1, card2)
                elif command == '4': # pass
                    print('Pass')
                    hand_index += 1
                else:
                    print('Do it again')

        '''Player Phase-2'''
        print("--- Player Phase-2 ---")
        for player_index in range(len(players)):
            hand_index = 0
            while hand_index < len(players[player_index].hands):
                print('Player-{0}: '.format(players[player_index].name))
                players[player_index].show_hands(True)            
                command = players[player_index].card_command(hand_index)
                if command == '1': # Hit
                    print('Hit')
                    players[player_index].deal_hand(hand_index, deck.deal(True))
                    players[player_index].show_hands(True)
                    if players[player_index].hands[hand_index].calc_total_value() == 22:
                        print('Blast')
                        self.player_lose(player_index, hand_index)
                        
                elif command == '2': # Stop
                    print('Stop')
                    hand_index += 1
                    
                else:
                    print('Do it again')

        '''Dealer Phase'''
        print("--- Dealer Phase ---")
        print('Dealer-{0}: '.format(dealer.name))
        while dealer.hands[0].calc_total_value() < 17:
            dealer.deal_hand(0, deck.deal(True))
            print('Supply')
            dealer.show_hands(True)
        if dealer.hands[0].calc_total_value() == 22:
            print('Blast')
            for player_index in range(len(players)):
                for hand_index in range(len(players[player_index].hands)):
                    dropped_hand, bet = players[player_index].win(hand_index)
                    score[player_index] += bet
                    for card in dropped_hand:
                        deck.drop(card)
                    dealer.lose(bet)
                    score[-1] -= bet
        else:
            while True:
                command = dealer.card_command(0)
                if command == '1': # Hit
                    print('Hit')
                    dealer.deal_hand(0, deck.deal(True))
                    dealer.show_hands(True)
                    if dealer.hands[0].calc_total_value() == 22:
                        print('Blast')
                        for player_index in range(len(players)):
                            for hand_index in range(len(players[player_index].hands)):
                                dropped_hand, bet = players[player_index].win(hand_index)
                                score[player_index] += bet
                                for card in dropped_hand:
                                    deck.drop(card)
                                dealer.lose(bet)
                                score[-1] -= bet
                        break
                elif command == '2': # Stop
                    print('Stop')
                    break
                else:
                    print('Do it again')

        '''Judge Phase'''
        print("--- Judge Phase ---")
        for player_index in range(len(players)):
            for hand_index in range(len(players[player_index].hands)):
                player_hand_value = players[player_index].hands[hand_index].calc_total_value()
                dealer_hand_value = dealer.hands[0].calc_total_value()
                if player_hand_value > dealer_hand_value:
                    dropped_hand, bet = players[player_index].win(hand_index)
                    score[player_index] += bet
                    for card in dropped_hand:
                        deck.drop(card)
                    dealer.lose(bet)
                    score[-1] -= bet
                elif player_hand_value < dealer_hand_value:
                    pass
                else:
                    player_hand_len = len(players[player_index].hands[hand_index].cards)
                    dealer_hand_len = len(dealer.hands[0].cards)
                    if player_hand_len > dealer_hand_len:
                        pass
                    elif player_hand_len < dealer_hand_len:
                        pass
                    else:
                        pass

        '''End Phase'''
        print("--- End Phase ---")
        dropped_hand = dealer.drop_hand(0)
        for card in dropped_hand:
            deck.drop(card)
        print(score)
        score_board.append(score)

def game():
    '''Check all players and dealer are ready'''
    
    players = [Player_BlackJack(20, 'Alice'), Player_BlackJack(30, 'Bob'),  Player_BlackJack(30, 'Charlie')]
    dealer = Dealer_BlackJack(70, 'Chow')
    score_board = []

    deck = Deck(2)
    #deck.show(True)

    
        

if __name__ == "__main__":
    game()


