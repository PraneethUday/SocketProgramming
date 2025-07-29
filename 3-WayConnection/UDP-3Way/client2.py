import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 9005

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(('0.0.0.0', 0))  # Optional: bind client socket to allow receiving

def recvMsg():
    while True:
        try:
            msg, addr = client.recvfrom(1024)
            print(f"\nMessage Received: {msg.decode()}")
            print("Enter the message to be sent: ", end='', flush=True)
        except Exception as e:
            print(f"Receive error: {e}")
            #break

def sendMsg():
    while True:
        msg = input("Enter the message to be sent: ")
        if msg.lower() == "end":
            print("Client closing connection...")
            break
        client.sendto(msg.encode(), (host, port))
    client.close()

threading.Thread(target=recvMsg, daemon=True).start()
sendMsg()
