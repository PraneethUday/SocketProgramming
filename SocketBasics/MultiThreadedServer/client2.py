import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 5002
client = socket.socket()

try:
    client.connect((host,port))
except socket.error as e:
    print(str(e))

recvMsg = client.recv(1024).decode("utf-8")
print(recvMsg)

while True:
    sendMsg = input("Enter message to send : ")
    client.send(sendMsg.encode("utf-8"))
    response = client.recv(1024)
    print(response.decode("utf-8"))

client.close()




