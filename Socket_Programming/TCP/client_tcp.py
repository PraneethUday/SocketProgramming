import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('localhost',12003))
message = input("Enter the message:")
client_socket.send(message.encode())
modified_message = client_socket.recv(2048)
print(modified_message.decode())
client_socket.close()





























