import socket
import threading
import os
import argparse
from random import randint


class Server (threading.Thread):

    def __init__(self, host, port):
        super().__init__()
        self.conn = []
        self.host = host
        self.port = port

    def run(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        soc.bind((self.host, self.port))
        soc.listen()

        while True:
            conn, addr = soc.accept()
            print("Connection from Client: %s" % str(addr))
            dataIn = conn.recv(1024)
            stringIn = dataIn.decode()
            print("Client Question: %s" % stringIn)
            ans = ["It is certain",
                   "Without a doubt",
                   "You may rely on it",
                   "Yes definitely",
                   "It is decidedly so",
                   "As I see it, yes",
                   "Most likely",
                   "Yes",
                   "Outlook good",
                   "Signs point to yes",
                   "Reply hazy try again",
                   "Better not tell you now",
                   "Ask again later",
                   "Cannot predict now",
                   "Concentrate and ask again",
                   "Don't count on it",
                   "Outlook not so good",
                   "My sources say no",
                   "Very doubtful",
                   "My reply is no"]
            stringOut = ans[randint(0, 19)]
            print("Answer for Client: %s" % stringOut)
            dataOut = stringOut.encode()
            conn.send(dataOut)
            conn.close()


def exit(server):
    while True:
        ipt = input('')
        if ipt == 'quit':
            print("Closing Server Connection")
            for conn in server.conn:
                conn.sc.close()
            os._exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Magic 8 Game')
    parser.add_argument('host', help='Port IP Server')
    parser.add_argument('-quit', help='To close server connection')
    parser.add_argument('-p', metavar='PORT', type=int,
                        default=8080, help='TCP port (default 8080)')
    args = parser.parse_args()

    server = Server(args.host, args.p)
    server.start()

    exit = threading.Thread(target=exit, args=(server,))
    exit.start()
