import socket
import threading

SERVER_IP = socket.gethostbyname(socket.gethostname())
tcpPort = 6007
udpPort = 6008

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(('0.0.0.0', 0))

udp.sendto(b"Hello from UDP!", (SERVER_IP, udpPort))

def recvMsg():
    while True:
        try:
            data, addr = udp.recvfrom(4096)
            print(f"\n[TCP client said] {data.decode()}")
            print("[You] Enter message: ", end='', flush=True)
        except Exception as e:
            print("Connection closed.", e)
            break

def sendMsg():
    while True:
        msg = input("[You] Enter message: ")
        if msg.lower() == 'exit':
            break
        try:
            udp.sendto(msg.encode(), (SERVER_IP, udpPort))
        except Exception as e:
            print("Error sending message:", e)
    udp.close()

threading.Thread(target=recvMsg, daemon=True).start()
sendMsg()
