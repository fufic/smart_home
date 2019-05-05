import time
import picamera
import sys

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("error at import. you must be root")
    

class Door:
    #channel = 22
    #door_id = 67
    
    def onDoorOpened(self, channel):
        kDoorOpen = 1
        kDoorClosed = 0
        self.counter += 1
        doorStatus = GPIO.input(self.channel)
        if (doorStatus == kDoorOpen):
            print("door closed " + str(self.door_id), " ", self.counter)
        else:
            print("door opened"," ", self.counter)
        self.signalDoor(self.door_id, doorStatus)
            
    def __init__(self, channel, door_id, signalDoor):
        self.counter = 0
        self.channel = channel
        self.door_id = door_id
        self.signalDoor = signalDoor;
        # self.channel - sensor number on the phisical board
        # GPIO.IN reading data from sensor, not writing it
        # pull_up_down=GPIO.PUD_UP default val is 1( when connected to the ground, we need 1)
        GPIO.setup(self.channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #  GPIO.BOTH we are detecting uo-down and down-up both
        #  callback is in separate thread. but 1 thread for all collbacks
        GPIO.add_event_detect(self.channel, GPIO.BOTH,  callback = self.onDoorOpened)
        
        
def initDevices():
    GPIO.setmode(GPIO.BCM)

def cleanupDevices():
    GPIO.cleanup()
   