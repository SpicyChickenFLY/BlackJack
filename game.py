"""
Author: Chow
Create: 2019/05/30
Last Review: 2019/06/01
"""

from player import Player
from deck import Deck

def check_player():
    pass

def compare_hands(dealer_hand, player_hand):
    pass

def game():
    '''Check all players and dealer are ready'''
    
    players = [Player(20, 'Alice'), Player(30, 'Bob'),  Player(30, 'Charlie')]
    dealer = Player(70, 'Chow')

    deck = Deck(2)
    deck.show(True)

    round_num = 0
    if True:
        '''New round'''
        round_num += 1
        print('Round: {0}'.format(round_num))

        '''Every player devide their bet'''
        for player_index in range(len(players)):
            players[player_index].add_bet(5)
            print(
                'Player-{0} bet {1}\n'.format(
                    players[player_index].name, 
                    players[player_index].bets
                )
            )
        print("Game Start")

        '''Deal card for dealer and each player'''
        for player_index in range(len(players)):
            players[player_index].deal_hand(0, deck.deal(True))
            players[player_index].deal_hand(0, deck.deal())
            print('Player-{0}: '.format(players[player_index].name))
            players[player_index].show_hands(True)
        dealer.deal_hand(0, deck.deal(True))         
        dealer.deal_hand(0, deck.deal())
        print('Dealer-{0}: '.format(dealer.name))
        dealer.show_hands(True)
        print()

        '''Each player make a decision'''
        for player_index in range(len(players)):
            hand_index = 0
            while hand_index < len(players[player_index].hands):
                print('Player-{0}: '.format(players[player_index].name), end='')
                command = players[player_index].command_1(hand_index)
                if command == '1': # surrender
                    players[player_index].lose()
                    dropped_hand = players[player_index].drop_hand(hand_index)
                    for card in dropped_hand:
                        deck.drop(card)
                    print('Surrender')
                elif command == '2': # raise_bet
                    bet = 5
                    players[player_index].add_bet(bet)
                    print('Raise_bet:{0}'.format(bet))
                elif command == '3': # split
                    card1 = deck.deal(True)
                    card2 = deck.deal(True)
                    players[player_index].split_hand(hand_index, card1, card2)
                    print('Split')
                elif command == '4': # pass
                    hand_index += 1
                    print('Pass')
                else:
                    print('Do it again')
                
            
        '''Each player make a decision'''


        '''Dealer make a decision '''

    
if __name__ == "__main__":
    game()


