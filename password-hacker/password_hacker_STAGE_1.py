import socket
import sys

args = sys.argv
hostname = args[1]
port = int(args[2])
message = args[3].encode()

sock = socket.socket()
sock.connect((hostname, port))
sock.send(message)
response = sock.recv(1024)
response = response.decode()
print(response)
sock.close()
