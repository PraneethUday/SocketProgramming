import socket
import threading

host = socket.gethostbyname(socket.gethostname())
tcpPort = 6007
udpPort = 6008

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,tcpPort))

def recvMsg():
    while True:
        try:
            data = client.recv(4096)
            if not data:
                print("\nConnection closed by the server.")
                break
            print(f"\n[UDP client said] {data.decode()}")
            print("[You] Enter message: ", end='', flush=True)
        except Exception as e:
            print("\nConnection closed.", e)
            break

def SendMsg():
    while True:
        msg = input("[You] : Enter the Message to Send : ")
        if msg.lower() == "end":
            print("[Connection Closed]".upper())
            break
        try:
            client.send(msg.encode())
        except Exception as e:
            print(e)
    client.close()

threading.Thread(target=recvMsg,daemon=True).start()
SendMsg()

