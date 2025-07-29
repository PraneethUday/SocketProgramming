import socket
import threading
import sys

addr = "172.20.10.3"
port = 8001
print("[Server starting]")
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((addr,port))
clientAddr = None
def recvMsg():
    global clientAddr
    while True:
        data,clientAddr = server.recvfrom(4096)
        print(f"\n[CLIENT] from [{clientAddr}] : {data.decode("utf-8")}")
        print("Enter the Message : ",end="",flush=True)
def sendMsg():
    while True:
        if clientAddr:
            msg = input("Enter the message : ")
            server.sendto(msg.encode("utf-8"),clientAddr)


recv = threading.Thread(target=recvMsg, daemon=True)
recv.start()

send = threading.Thread(target=sendMsg)
send.start()


