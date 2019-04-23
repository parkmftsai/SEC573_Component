import socket,struct
s=socket.socket(socket.AF_INET, socket.SOCK_RAW,socket.IPPROTO_UDP)
while True:
  ip_payload_data = s.recv(65535)
  print(struct.unpack('!HHHH',ip_payload_data[:8]),ip_payload_data[8:])
