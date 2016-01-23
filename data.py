import socket
import sqlite3

class DataManager(object):   
    def __init__(self): 
        self.createTable  = '''
            create table if not exists gestures(
                label INT PRIMARY KEY NOT NULL,
                name VARCHAR(50) NOT NULL,
                samples INT NOT NULL
            ); 
        '''
        self.getAllGestures = '''
            select * from gestures;
        '''
        self.getAllLabels = '''
            select distinct(label) from gestures;
        '''
        self.folders = {}
        self.labels = {}
        self.labelsUsed = []
        self.conn = sqlite3.connect('train.db')
        self.conn.execute(self.createTable)
        cursor = self.conn.execute(self.getAllGestures)
        
        for row in cursor:
            self.folders[row[1]] = row[2]
            self.labels[row[1]] = row[0]

        cursor = self.conn.execute(self.getAllLabels)
        for row in cursor:
            self.labelsUsed.append(row[0])
            
    def myfind(self,list,x):
        for i in list:
            if(i==x):
                return True
        return False
        
    def getInsertSQLQuery(self,x,y,z):
            insertGesture = "insert into gestures\
            values (" + str(x) + ", '" + str(y) + "' ," + str(z) + ");"
            return insertGesture
        
    def addGesture(self,gestureName,label,loopCount,PORT):
        
        if(self.myfind(self.labelsUsed,label)):
            print "Label Already Used Cant Add it"
            return
        
        self.conn.execute(self.getInsertSQLQuery(label,gestureName,loopCount))
        self.conn.commit()        
        self.folders[gestureName] = loopCount
        self.labels[gestureName] = label
        self.labelsUsed.append(label)
        
        while loopCount:
            inc = 1     
            s = socket.socket()
            host = socket.gethostname() 
            port = PORT
            s.bind((host, port))
            s.listen(5)
            while loopCount:
               c, addr = s.accept()
               print '\nGot connection from', addr
               
               msg= []                     
               msg = c.makefile().read(-1) 
               msg = msg[2:]
               if(len(msg)<500):
                   continue
               #filePath = appID + "test.txt"
               filePath = "./dataset/"+str(gestureName)+"/"+str(gestureName)+str(inc)+".txt"
               inc+=1
               file = open(filePath,"w")
               file.write(msg)
               file.close() 
               loopCount-=1
            break
           
            

trainer = DataManager()
trainer.addGesture("up",3,50,8000)
print trainer.folders
print trainer.labels