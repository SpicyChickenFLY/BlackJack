import multiprocessing
from multiprocessing import Process, Queue, Pipe


from web import ServerUDP
from game import GameManager

"""
The format of standard message:
{
    "type": connect/pulse/disconnect/command/load/chat/info/warn/sys,
    "content": 
}
The content will be different
pulse: None
connect: None
disconnect: None
command: Index of Command
load: None
chat: message
"""

class System():
    def __init__(self):
        self.receive_queue = Queue()
        self.send_queue = Queue()
        self.clients = []
        self.server = ServerUDP()
        self.game_manager = GameManager()
        self.message_process = None
        self.receive_process = None
        self.send_process = None

    def startup(self):
        self.message_process = Process(
            target=self.message_func, args=())
        self.receive_process = Process(
            target=self.receive_func, args=())
        self.send_process = Process(
            target=self.send_func, args=())
        self.message_process.start()
        self.receive_process.start()
        self.send_process.start()

    def shutdown(self):
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
                if data["type"] == "connect" or data["type"] == "disconnect" :
                    # new client connected
                    self.clients.append(addr)
                    response_data = {
                        "type": data["type"],
                        "content": ""
                    }
                    self.send_queue.put([addr, data])
                if data["type"] == "command":
                    # client make command
                    pass
                

    def receive_func(self):
        while True:
            addr, data = self.server.receive()
            self.receive_queue.put([addr, data])

    def send_func(self):
        while True:
            message = self.send_queue.get(True)
            self.server.send(message[0], message[1])
            

if __name__ == "__main__":
    multiprocessing.freeze_support() # Should be placed at the entrance of program
    system = System()

