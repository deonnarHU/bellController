from gpiozero import LED
from time import sleep
from threading import Timer
import time
import json

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(23)
led1.on()
led2.on()
led3.on()
led4.on()


def startNote(x):
    #print("startingu")
    noteSelector(x).off()
    return 0

def stopNote(x):
    #print("stopperino")
    noteSelector(x).on()
    return 0

def noteSelector(x):
    switcher = {
        1: led1,
        2: led2,
        3: led3,
        4: led4
        }
    return switcher.get(x,"Note exist NO")

def playNote(x):
    starter = Timer(0, startNote, [x])
    stopper = Timer(0.1, stopNote, [x])
    starter.start()
    stopper.start()