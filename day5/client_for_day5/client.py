import socket
import codecs
import time


mysocket=socket.socket()
mysocket.connect(("127.0.0.1",9000))

time.sleep(3)
def download_recv(mysocket):
    print(codecs.decode(mysocket.recv(1024),"utf-8"))
    k=input()
    mysocket.send(codecs.encode(k,"utf-8"))
    endoffile = codecs.encode("!EOF!")
    print(endoffile)
    data=b""
    while not data.endswith(endoffile):
       data+= mysocket.recv(1024)
    try:
       print(len(endoffile))
       fh = open(k,"wb")
       fh.write(bytes(codecs.decode(data[:-len(endoffile)],"base64")))
       #fh.write(codecs.decode(data[:-len(endoffile)],"base64").decode("latin-1"))
       fh.close
       print("ok")
    except Exception as e:
       print("no")

try:
	while True:
        
	    k=input()
        
	    if(k=="UPLOAD"):
		    mysocket.send(codecs.encode(k,"utf-8"))
		    print(codecs.decode(mysocket.recv(1024),"utf-8"))
		    k=input()
		    mysocket.send(codecs.encode(k,"utf-8"))
		    print(codecs.decode(mysocket.recv(1024),"utf-8"))
		    print("!EOF!")
		    mysocket.send(b"!EOF!")
		    try:
   			    data=codecs.encode(open(k,"rb").read(),"base64")
		    except Exception as e:
   			    data="fails"
		    mysocket.sendall(data+codecs.encode("!EOF!"))
	    elif(k=="DOWNLOAD"):
                    mysocket.send(codecs.encode(k,"utf-8"))
                    download_recv(mysocket)
	    else:
		    print("command:"+k)
		    mysocket.send(codecs.encode(k,"utf-8"))
		    print(codecs.decode(mysocket.recv(1024),"utf-8"))
except KeyboardInterrupt:
	print("aaa")
	mysocket.send(codecs.encode("CLOSE","utf-8"))
