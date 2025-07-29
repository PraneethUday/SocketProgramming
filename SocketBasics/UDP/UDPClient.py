import socket

addr = socket.gethostbyname(socket.gethostname())
port = 8003

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg = "Hello I am UDP client"
client.sendto(msg.encode("utf-8"),(addr,port))
data,Addr = client.recvfrom(4096)
print(data.decode("utf-8"))
client.close()
