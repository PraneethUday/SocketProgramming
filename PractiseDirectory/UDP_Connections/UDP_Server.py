import socket
import threading
import time

host = socket.gethostbyname(socket.gethostname())
port = 5008

message = "Acknowledge call back Postive -- [Connection Successful]"

print("[Starting the server]")
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((host,port))
print("[Server listening for Connections]")

clients = set()

def recvMsg():
    while True:
        try:
            msg,sender_addr = server.recvfrom(1024)
            if sender_addr not in clients:
                clients.add(sender_addr)
                greetingMsg = f"[Connection Successfull -- Server Response] from [{host}]".encode("utf-8")
                server.sendto(msg,sender_addr)
            print(f"[Message] received from {sender_addr} : {msg.decode('utf-8')}")
            print("Enter the message : ", end="", flush=True)
        except Exception as e:
            print(e)
def sendMsg():
    while True:
        try:
            msg = input("Enter the message : ")
            for addr in clients:
                server.sendto(msg.encode("utf-8"),addr)
            else:
                print("[Waiting for server response]")
                time.sleep(1)
        except Exception as e:
            print(e)

recv = threading.Thread(target=recvMsg,daemon=True)
recv.start()

sendMsg()


