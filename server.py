import socket
import threading

header = 64
decodeFormat = 'utf-8'
bufferSize = 1024
port = 5050
server = socket.gethostbyname(socket.gethostname())
addr = (server,port)
disconnect = "end"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addr)
def handleClient(conn,adddr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True

    while connected:
        msgLength = conn.recv(header).decode(decodeFormat)
        if msgLength:
            msgLength = int(msgLength)
            msg = conn.recv(msgLength).decode(decodeFormat)
            if msg == disconnect: 
                connected = False
            print(f"[{addr}] : {msg}")

    conn.close()


def acceptConnection():
    clientCount = 0
    server.listen()
    print("[LISTENING] server is listening for connection ")
    while True:
        clientCount = clientCount + 1
        conn,addr = server.accept()
        thread = threading.Thread(target=handleClient,args=(conn,addr))
        thread.start()
        print("[ACTIVE CONNECTIONS] total connection = ",threading.activeCount() - 1)

print("[STARTING] server has started running")
acceptConnection();

