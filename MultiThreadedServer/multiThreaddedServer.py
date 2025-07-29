import socket
from _thread import *

host = socket.gethostbyname(socket.gethostname())
port = 5002
threadCount = 0
encodeFormat = "utf-8"

server = socket.socket()

try:
    server.bind((host,port))
except Exception as e:
    print(e)

print("[Server has Started]")
print("[Waiting for connection]")
server.listen(5)

def clientThread(client):
    client.send("Welcome the Server".encode(encodeFormat))
    while True:
        msg = client.recv(1024)
        if not msg:
            break
        recMsg = msg.decode(encodeFormat)
        sendMsg = f"Hello I am Server from the IP {host}.You said : {recMsg}".encode("utf-8")
        client.sendall(sendMsg)
    client.close()

while True:
    client,clientAddr = server.accept()
    print(f"[Client has been added] : {clientAddr[0]}")
    start_new_thread(clientThread,(client,))
    threadCount+=1
    print("ThreadNumber = ",threadCount)







