import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 6062

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

def broadCast(msg,senderConn):
    for client in clients:
        if client!=senderConn:
            try:
                client.send(msg)
            except Exception as e:
                client.close()
                clients.remove(client)


def handleClient(conn,addr):
    print(f"Server Connected by {addr}")
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            print(msg.decode())
            broadCast(msg,conn)
        except Exception as e:
            break
    conn.close()
    clients.remove(conn)
    print(f"connection closed : {addr}")

print("Server started")
while True:
    conn,addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handleClient,daemon=True,args=(conn,addr)).start()