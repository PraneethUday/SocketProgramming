import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 6062

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def recvMsg():
    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                break
            print(f"\n[Chat] {msg.decode()}")
        except Exception as e:
            break

def sendMsg():
    while True:
        msg = input()
        if msg.lower() == 'exit':
            break
        client.sendall(msg.encode())
    client.close()

threading.Thread(target=recvMsg, daemon=True).start()
sendMsg()
