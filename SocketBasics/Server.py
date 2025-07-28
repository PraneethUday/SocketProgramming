import socket

ADDR = socket.gethostbyname(socket.gethostname())
PORT = 6060

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Server has started")
server.bind((ADDR,PORT))
server.listen(5)
print("server listening for connections")



