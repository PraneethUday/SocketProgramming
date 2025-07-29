import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 9005

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))

clients = set()

def HandleClients():
    while True:
        try:
            msg, addr = server.recvfrom(1024)
            if addr not in clients:
                clients.add(addr)
                print(f"New client added {addr}")
            print(f"Message from client {addr}: {msg.decode()}")
            # Relay message to all other clients
            for clientAddr in clients:
                if clientAddr != addr:
                    server.sendto(msg, clientAddr)
        except Exception as e:
            print(e)

thread = threading.Thread(target=HandleClients, daemon=True)
thread.start()
print("Server ready to ACT as relay")

thread.join()
