import socket
server=socket.socket()
server.bind(("",9000))
server.listen(1)
c,r=server.accept()
print(len(c.recv(1024*1000)))
