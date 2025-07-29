import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('',12003))
server_socket.listen(1)
print("server ready for connection")
while True:
    client_socket,client_address = server_socket.accept()
    message=client_socket.recv(2048)
    modified_message = message.decode().upper()
    print("message")
    client_socket.send(modified_message.encode(),client_address)
    
    client_socket.close








































# import socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('', 12003))
# server_socket.listen(1)
# print('Server ready on port 12003')
# while True:
#     client_socket, client_address = server_socket.accept()
#     message = client_socket.recv(2048)
#     print(f"Received from {client_address}: {message.decode()}")
#     modified_message = message.decode().upper()
#     client_socket.send(modified_message.encode())
#     print(f"Sent to {client_address}: {modified_message}")
#     client_socket.close()