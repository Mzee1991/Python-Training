#!/usr/bin/python3
import socket

s = socket.socket()
print('Socket Created')

s.bind(('localhost', 9999))

s.listen(3)
print('Waiting for connections')

while True:
    c, addr = s.accept()
    print("Connected with ", addr)
    c.send('Welcome to Kyojo')
    c.close()
