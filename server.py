import socket
from main import Gesture
from data import DataManager
import controller

app_id = 1
app = Gesture(app_id)
manager = DataManager()
app.train(manager.folders,manager.names,manager.labels)	
app.initClassifier()


s = socket.socket()
host = socket.gethostname() 
port = 8000
s.bind((host, port))
s.listen(5)

while True:
   c, addr = s.accept()
   print '\nGot connection from', addr
   
   msg= []                     
   msg = c.makefile().read(-1)
   #print(len(msg)) 
   msg = msg[2:]
   #print msg
   file = open("test.txt","w")
   file.write(msg)
   file.close()   
   
   if(len(msg)>=500):
       test = app.getDataFromFile("test.txt")
       result = app.predict(test)
       print manager.folders[result-1]
       app.plotImage("test.txt")
       controller.fun(result)
   else:
       print "data not recieved properly"
       
    
   c.close()    
