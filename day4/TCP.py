import socket,struct
s=socket.socket(socket.AF_INET, socket.SOCK_RAW,socket.IPPROTO_TCP)
while True:
  data = s.recv(65535)
  tcp=struct.unpack("!HHIIBBHHH",data[:20])
  print("TCP: ",tcp)

