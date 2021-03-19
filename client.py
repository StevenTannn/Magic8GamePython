import socket

while True:
    soc = socket.socket()
    soc.connect(('127.0.0.1',1060))
    ques = input("Ask a question:")
    dataOut = ques.encode()
    soc.send(dataOut)
    dataRes = soc.recv(1024)
    res = dataRes.decode()
    print("Your answer : %s" %res)
    soc.close()