import socket
from main import Gesture
from data import DataManager

app = Gesture()
manager = DataManager()
app.train(manager.folders,manager.labels)	
clf = app.initClassifier()

def startApp(PORT,appID,controller):   
        s = socket.socket()
        host = socket.gethostname() 
        port = PORT
        s.bind((host, port))
        s.listen(5)
        while True:
           c, addr = s.accept()
           print '\nGot connection from', addr
           
           msg= []                     
           msg = c.makefile().read(-1) 
           msg = msg[2:]
           filePath = appID + "test.txt"
           file = open(filePath,"w")
           file.write(msg)
           file.close()   
           
           if(len(msg)>=500):
               test = app.getDataFromFile(filePath)
               result = app.predict(test)
               print result
               app.plotImage(filePath)
               controller(result)
           else:
               print "data not recieved properly"
               
           c.close()   
    
