import socket

addr = socket.gethostbyname(socket.gethostname())
port = 8004  # This must match the server port

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(('0.0.0.0', 0))  # Optional: bind to any available port to receive responses

try:
    while True:
        msg = "Hello I am UDP client"
        client.sendto(msg.encode("utf-8"), (addr, port))
        data, Addr = client.recvfrom(4096)
        print(data.decode("utf-8"))
except KeyboardInterrupt:
    print("Client exiting...")
finally:
    client.close()
