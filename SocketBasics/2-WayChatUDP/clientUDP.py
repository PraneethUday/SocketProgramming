import socket
import threading

addr = socket.gethostbyname(socket.gethostname())
port = 8001

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(("0.0.0.0",0))

def recvMsg():
    while True:
        data, clientAddr = client.recvfrom(4096)
        print(f"\n[SERVER] from [{clientAddr}] : {data.decode('utf-8')}")
        print("Enter the Message : ",end="",flush=True)

def sendMsg():
    while True:
        msg = input("Enter the Message to Send : ")
        client.sendto(msg.encode('utf-8'), (addr, port))



recv = threading.Thread(target=recvMsg, daemon=True)
recv.start()

send = threading.Thread(target=sendMsg)
send.start()

