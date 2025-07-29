import socket

addr = socket.gethostbyname(socket.gethostname())
port = 8002

print("Server Started")
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((addr,port))
print("Server Running")

while True:
    data,Addr = server.recvfrom(1024)
    print(data.decode("utf-8"))

    msg = "Hello I am UDP Server".encode("utf-8")
    server.sendto(msg,Addr)

