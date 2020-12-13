from gpiozero import LED
from time import sleep
from threading import Timer
import time
import json

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(23)
led5 = 5
led6 = 6
led7 = 7
led8 = 8
led9 = 9
led10 = 10
led1.on()
led2.on()
led3.on()
led4.on()




def startNote(x):
    #print("startingu")
    if(noteSelector(x) == "Note exist NO"):
        print("no note")
    else:
        noteSelector(x).off()
    return 0

def stopNote(x):
    #print("stopperino")
    if(noteSelector(x) == "Note exist NO"):
        print("no note")
    else:
        noteSelector(x).on()
    return 0

def noteSelector(x):
    switcher = {
    "B3": led1,
    "C4": led2,
    "D4": led3,
    "E4": led4,
    #"F4": led5,
    "F#4": led6,
    "G4": led7,
    "A4": led8,
    "B4": led9,
    "C5": led10}
    '''switcher = {
        "1": led1,
        "2": led2,
        "3": led3,
        "4": led4
        }'''
    return switcher.get(x,"Note exist NO")

def playNote(x):
    starter = Timer(0, startNote, [x])
    stopper = Timer(0.1, stopNote, [x])
    starter.start()
    stopper.start()