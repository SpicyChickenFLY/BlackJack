import multiprocessing
from multiprocessing import Process, Queue, Pipe


from web import ServerUDP
from game import GameManager


class System():
    def __init__(self):
        self.receive_queue = Queue()
        self.send_queue = Queue()
        self.clients = []
        self.server = ServerUDP()
        self.game_manager = GameManager()
        self.receive_process = None
        self.send_process = None

    def startup(self):
        self.receive_process = Process(
            target=self.receive_func, args=(self.receive_queue,))
        self.send_process = Process(
            target=self.send_func, args=(self.send_queue,))
        self.message_process.start()
        self.receive_process.start()
        self.send_process.start()

    def shutdown(self):
        if self.receive_process != None:
            self.receive_process.terminate()
        if self.send_process != None:
            self.send_process.terminate()

    def receive_func(self, queue):
        while True:
            addr, data = self.server.receive()
            queue.put([addr, data])

    def send_func(self, queue):
        while True:
            message = queue.get(True)
            self.server.send(message[0], message[1])
            

if __name__ == "__main__":
    multiprocessing.freeze_support() # Should be placed at the entrance of program
    system = System()

