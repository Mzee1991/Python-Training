import socket

s = socket.socket()
print('Socket Created')

s.bind(('192.168.1.1', 9999))

s.listen(3)
print('Waiting for connections')

while True:
    c, addr = s.accept()
    print("Connected with ", addr)
    c.send('Welcome to Kyojo')
    c.close()
