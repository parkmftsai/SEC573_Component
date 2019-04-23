import socket,struct
s=socket.socket(socket.AF_PACKET, socket.SOCK_RAW,socket.ntohs(0x0003))
while True:
  data = s.recv(65535)
  iph = struct.unpack('!BBHHHBBHLL',data[14:34])
  print(iph)
  srcip = socket.inet_ntoa(struct.pack('!L',iph[8]))
  dstip = socket.inet_ntoa(struct.pack('!L',iph[9]))
  print("IP: SRC:{0} DST:{1}-{2}".format(srcip,dstip,iph))

