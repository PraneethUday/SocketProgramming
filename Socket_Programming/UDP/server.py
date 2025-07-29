import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(('',12003))
print("Server is ready to receive messages")
while True:
    message,client_address = server_socket.recvfrom(2048)
    modified_message = message.decode().upper()
    server_socket.sendto(modified_message.encode(),client_address)
    print("message sent to client:", modified_message.encode())
server_socket.close()   