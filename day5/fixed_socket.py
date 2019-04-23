import socket,time
mysocket=socket.socket()
connected=False
while not connected:
    for port in [21,22,80,443,8000]:
        time.sleep(1)
        try:
           print("Trying",port,end=" ")
           mysocket.connect(("127.0.0.1",port))
        except socket.error:
           print("Nope")
           continue
        else:
           print("Connected")
           connected=True
           break

while True:
     print(mysocket.recv(2048))
