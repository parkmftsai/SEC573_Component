import socket
s=socket.socket()
s.connect(("127.0.0.1",9000))
s.send(b"a"*1024*1000)
