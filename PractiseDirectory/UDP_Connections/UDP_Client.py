import socket
import threading
import time

host = socket.gethostbyname(socket.gethostname())
port = 5008

message = "Hi this is the UDP Client Requesting for Connection"

print("[Socket initiated Successfully]")
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.bind(("0.0.0.0",0))

client.sendto("This is Client Requesting For connection".encode("utf-8"),(host,port))

addr = None

def recvMsg():
    global addr
    while True:
        try:
            msg,sender_addr = client.recvfrom(1024)
            addr = sender_addr
            print(f"[Message] received from {addr} : {msg.decode('utf-8')}")
            print("Enter the message : ", end="", flush=True)
        except Exception as e:
            print(e)
def sendMsg():
    while True:
        try:
            if addr:
                msg = input("Enter the message : ")
                client.sendto(msg.encode("utf-8"),(addr[0],addr[1]))
            else:
                print("[Waiting for server response]")
                time.sleep(1)

        except Exception as e:
            print(e)

recv = threading.Thread(target=recvMsg,daemon=True)
recv.start()

sendMsg()


