#!/usr/bin/env python3

import socket

HOST = input('hostname: ')  # The server's hostname or IP address
PORT = input('port: ')        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)

print('Received', repr(data))
