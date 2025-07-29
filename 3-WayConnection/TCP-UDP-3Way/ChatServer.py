import socket
import threading

host = socket.gethostbyname(socket.gethostname())
tcpPort = 6007
udpPort = 6008

udpClientAddr = None
tcpConn = None

print("[TCP] :Starting TCP server")
tcpServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpServer.bind((host,tcpPort))
tcpServer.listen(1)
print("[TCP] : Server Started Successfully")

print("[UDP] :Starting TCP server")
udpServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpServer.bind((host,udpPort))
print("[UDP] : Server Started Successfully")

def UDPHandler():
    global udpClientAddr,tcpConn
    while True:
        msg,addr = udpServer.recvfrom(4096)
        if not udpClientAddr:
            udpClientAddr = addr
            udpServer.sendto("Registered with server".encode("utf-8"),udpClientAddr)
            print(f"[UDP] : UDP client registered {udpClientAddr}")
        print(f"[UDP] Message : {msg.decode("utf-8")}")
        if tcpConn:
            try:
                tcpConn.sendall(msg)
                print(f"[SERVER] Forwared to TCP client")
            except Exception as e:
                print(e)


def TCPHandler():
    global tcpConn,udpClientAddr
    tcpConn,addr = tcpServer.accept()
    print(f"[TCP] : Connected from TCP Client {addr}")
    while True:
        msg = tcpConn.recv(4096)
        if not msg:
            print("[TCP] : Disconnected")
            break
        print(f"[TCP] Message Received : {msg.decode()}")
        try:
            if udpClientAddr:
                udpServer.sendto(msg,udpClientAddr)
                print("[SERVER] : Message sent to UDP client")
            else:
                print("[SERVER] : No UDP client Registered")
        except Exception as e:
            print(e)
    tcpConn.close()

threading.Thread(target=UDPHandler,daemon=True).start()
TCPHandler()





