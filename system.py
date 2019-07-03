from multiprocessing import Process, Queue

from game import PlayerManager, GameManager

class System():
    def __init__(self):
        self.player_manager = PlayerManager()
        self.game_manager = GameManager()

    def startup(self):
        pass

    def shutdown(self):
        pass