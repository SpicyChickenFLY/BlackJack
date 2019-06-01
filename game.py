"""
Author: Chow
Create: 2019/05/30
Last Review: 2019/05/31
"""

from player import Player
from deck import Deck

def check_player():
    pass

def compare_hands(dealer_hand, player_hand):
    pass

def game():
    '''Check all players and dealer are ready'''
    
    players = [Player(20, 'Alice'), Player(30, 'Bob'),  Player(30, 'charlie')]
    dealer = Player(70, 'Chow')

    deck = Deck(2)
    deck.show(True)

    round_num = 0
    while True:
        '''New round'''
        round_num += 1
        print(round_num)

        '''Every player devide their bet'''
        for player_index in range(len(players)):
            players[player_index].add_bet(5)
            print(
                'Player-{0} bet {1}'.format(
                    players[player_index].name, 
                    players[player_index].bets
                )
            )
        print("Game Start")

        '''Deal card for dealer and each player'''
        for player_index in range(len(players)):
            players[player_index].deal(0, deck.deal(True))
            players[player_index].deal(0, deck.deal())
            print('Player-{0}: '.format(players[player_index].name))
            players[player_index].show_hands(True)
        dealer.deal(0, deck.deal(True))         
        dealer.deal(0, deck.deal())
        print('Dealer-{0}: '.format(dealer.name))
        dealer.show_hands(True)
        print()

        '''Each player make a decision'''
        for player in players:
            hand_index = 0
            while hand_index < len(player.hands):
                command = player.command_1(hand_index)
                if command == 1:
                    player.lose()
                    dropped_hand = player.drop_hand()
                    for card in dropped_hand:
                        deck.drop(card)
                elif command == 2:
                    pass
                elif command == 3:
                    pass
                else:
                    pass
                hand_index += 1
            
        '''Dealer make a decision '''

    
if __name__ == "__main__":
    game()


