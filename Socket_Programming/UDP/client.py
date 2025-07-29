import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
message = input("Enter the string in lowercase: ")
socket_adress=('localhost',12003)
server_socket.sendto(message.encode(),socket_adress)
print("Message sent to server")
modified_message,server_adress = server_socket.recvfrom(12003)
print("message reccieved:",modified_message.decode())
server_socket.close()