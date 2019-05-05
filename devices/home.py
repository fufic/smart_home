
import time
import devices



class Home:
    def handle_door(self, door_id, isOpened):
        print("door number ",door_id,"opened = ",isOpened)
        
    def __init__(self):   
        devices.initDevices()
        self.door = devices.Door(22, 33, self.handle_door)
    
    def __del__(self):      
        devices.cleanupDevices()
        
    def BeSmart(self):
        while True:
            time.sleep(2000)
            

home = Home()
home.BeSmart()
