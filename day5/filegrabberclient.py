import socket
mysocket = socket.socket()
mysocket.connect(("127.0.0.1",8000))
while True:
    print(mysocket.recv(2048))
