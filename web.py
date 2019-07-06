import socket
import sys
import json

def str_to_byte(string):
    byte = bytes(string, encoding='utf-8')
    return byte

def byte_to_str(byte):
    string = str(byte, encoding="utf-8")
    return string

class ServerUDP:
    def __init__(self):
        self.new_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __del__(self):
        self.new_socket.close()

    def host(self, host, port):
        self.new_socket.bind((host, port))

    def receive(self):
        data, addr = self.new_socket.recvfrom(1024)
        data = json.loads(byte_to_str(data))
        print('Request data from {0}: {1}'.format(addr, data))
        return addr, data

    def send(self, addr, data):
        print('Response data to {0}: {1}'.format(addr, data))
        json.dumps(data)
        self.new_socket.sendto(str_to_byte(data), addr)
        
class ClientUDP:
    def __init__(self):
        self.new_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __del__(self):
        self.new_socket.close()

    def connect(self, host, port):
        self.new_socket.connect((host, port))
    
    def send(self, message):
        self.new_socket.send(message)

    def receive(self):
        return self.new_socket.recv(1024)

if __name__ == "__main__":
    if  len(sys.argv) > 1 and sys.argv[1] == 'client':
        client = ClientUDP()
        client.connect('127.0.0.1', 23334)
        response = client.send(str_to_byte('test1'))
        print(byte_to_str(response))
    else:
        server = ServerUDP()
        server.host('127.0.0.1', 23334)
        server.receive()
