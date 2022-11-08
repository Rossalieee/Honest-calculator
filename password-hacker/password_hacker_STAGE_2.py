import socket
import sys
import string
import itertools


def main():
    args = sys.argv
    hostname = args[1]
    port = int(args[2])
    symbols_list = list(string.ascii_lowercase) + list(string.digits)

    sock = socket.socket()
    sock.connect((hostname, port))

    count = 0
    response = 'Wrong password!'

    while response == 'Wrong password!':
        count += 1
        for symbol in itertools.product(symbols_list, repeat=count):
            password = ''.join(symbol)
            message = password.encode()
            sock.send(message)
            response = (sock.recv(1024)).decode()
            if response == 'Connection success!':
                print(password)
                sock.close()
                break


if __name__ == "__main__":
    main()
