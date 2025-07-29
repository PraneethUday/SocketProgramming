import socket
import threading


header = 64
port = 5050
bufferSize = 1024
disconnet = "end"
decodeFromat = "utf-8"
server = socket.gethostbyname(socket.gethostname())
addr = (server,port)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(addr)


def sendMsg(msg):
    message = str(msg).encode(decodeFromat)
    msgLength = len(message)
    strLength = str(msgLength).encode(decodeFromat)
    strLength += b' ' * (header - len(strLength))
    client.send(strLength)
    client.send(message)
sendMsg("Hello World!")


