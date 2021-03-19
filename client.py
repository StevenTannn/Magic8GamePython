import socket
import os
import argparse


class Send ():

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port

    def start(self):
        while True:
            sock = socket.socket()
            sock.connect((self.host, self.port))
            ques = input("Ask a question:")
            if ques == "quit" :
                sock.close()
                print('Connection to server closed, exiting app')
                os._exit(0)
            else :
                dataOut = ques.encode()
                sock.send(dataOut)
                dataRes = sock.recv(1024)
                res = dataRes.decode()
                print("Result : %s" % res)
                sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Magic 8 Game')
    parser.add_argument('host', help='Port IP Server')
    parser.add_argument('-quit', help='To close server connection')
    parser.add_argument('-p', metavar='PORT', type=int,
                        default=8080, help='TCP port (default 8080)')
    args = parser.parse_args()

    client = Send(args.host, args.p)
    client.start()