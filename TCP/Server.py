import socket
import time
header = 10
ADDR = socket.gethostbyname(socket.gethostname())
PORT = 6060

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Server has started")
server.bind((ADDR,PORT))
server.listen(5)
print("server listening for connections")

while True:
    clientSocket,addr = server.accept()
    print(f"Connection from {addr} has been established")

    while True:
        time.sleep(3)
        msg = "Hi How are you"
        msg = f'{len(str(msg)):<{header}}' + msg

        clientSocket.send(msg.encode("utf-8"))





