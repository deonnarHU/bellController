from gpiozero import LED
from time import sleep
from threading import Timer
import time
import json

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(23)

#h = [1,3,4,1,1]
#ht = [120,120,780,1780,2780]
noteStarters = {}
noteStoppers = {}

def readSong(songName):
    with open("song0001.json") as f:
        data = json.load(f)
    return data

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


#Load Singysong
song = readSong("song0001.json")
h = song.noteList
ht = song.noteTime
i = 0
for x in h:
    timerOnName = "t" + str(i) + "On"
    timerOffName = "t" + str(i) + "Off"
    noteStarters[timerOnName] = Timer(ht[i]/1000, startNote, [x])
    noteStoppers[timerOffName] = Timer(ht[i]/1000 + 0.1, stopNote, [x])
    noteStarters[timerOnName].start()
    noteStoppers[timerOffName].start()
    i = i + 1
    
