
import time
import devices
import zero_messeger.zero_messeger as zm #??
#import config

class Home:
    def handle_door(self, door_id, isOpened):
        message=" ".join(["door number ",str(door_id),"opened = ",str(isOpened)])
        print(message)
        self.publisher.Send(message)
    
    def readConfig(self):
        cfg = {}
        cfg["publish_addr"] = 'tcp://127.0.0.1:8080'
        return cfg
    
    def initSensors(self):
        devices.initDevices()
        #door
        doorPort = 22
        doorId = 33
        self.door = devices.Door(doorPort, doorId, self.handle_door)
        
    def __init__(self):       
        cfg = self.readConfig()
        self.publisher = zm.Publisher(cfg["publish_addr"])
        self.initSensors()

    
    def __del__(self):      
        devices.cleanupDevices()
        
    def BeSmart(self):
        while True:
            time.sleep(2000)
            

home = Home()
home.BeSmart()
