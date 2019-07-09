import multiprocessing
from multiprocessing import Process, Queue, Pipe


from web import ClientUDP
from game import GameManager

class System():
    def __init__(self):
        self.receive_queue = Queue()
        self.send_queue = Queue()
        self.client_pipe, self.game_pipe = Pipe()
        self.client = ClientUDP()
        self.client.connect('127.0.0.1', 23333)
        self.game_manager = GameManager()
        self.message_process = Process(
            target=self.message_func, args=())
        self.receive_process = Process(
            target=self.receive_func, args=())
        self.send_process = Process(
            target=self.send_func, args=())
        self.message_process.start()
        self.receive_process.start()
        self.send_process.start()

    def __del__(self):
        self.client.disconnect()
        if self.message_process != None:
            self.message_process.terminate()
        if self.receive_process != None:
            self.receive_process.terminate()
        if self.send_process != None:
            self.send_process.terminate()

    def message_func(self):
        while True:
            if not self.receive_queue.empty():
                message = self.receive_queue.get(True)
                addr = message[0]
                data = message[1]
                response_data = {
                    "type": data["type"],
                    "content": ""
                }
                if data["type"] == "connect" or data["type"] == "disconnect":  # server connected/disconnected
                    self.clients.append(addr)
                if data["type"] == "command":  # server reply command
                    try:
                        if data["content"] == "fail":
                            self.client_pipe.send(int(data["content"]))
                    except Exception as e:
                        response_data["content"] = "fail"
                if data["type"] == "load":  # client ask for a copy of game
                    self.server_pipe.send()
                    self.server_pipe.receive()
                if data["type"] == "chat":  # broadcast chat message
                    pass
                    self.send_queue.put([addr, response_data])

    def receive_func(self):
        while True:
            addr, data = self.server.receive()
            self.receive_queue.put([addr, data])

    def send_func(self):
        while True:
            message = self.send_queue.get(True)
            self.server.send(message[0], message[1])
