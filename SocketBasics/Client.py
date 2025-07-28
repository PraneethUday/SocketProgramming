import socket

header = 10
ADDR = socket.gethostbyname(socket.gethostname())
PORT = 6060

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ADDR,PORT))
print("Connection Successful")


while True:
    fullMsg = ""
    newMsg = True
    while True:
        msg = client.recv(16)
        if newMsg:
            msgLen = int(msg[:header].decode("utf-8"))
            newMsg = False
        fullMsg += msg.decode("utf-8")

        if (len(fullMsg)) - header == msgLen:
            print("Full message received")
            print(fullMsg[header:])
            newMsg = True
            fullMsg = ""


