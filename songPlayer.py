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

#h = [1,3,4,1,1]
#ht = [120,120,780,1780,2780]
noteStarters = {}
noteStoppers = {}

def readSong(songName):
    with open("./songs/" + songName) as f:
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
    return switcher.get(x,"Note exist NO")


def playSong(songTitle, offset, sumPreviousSongLength):
    song = readSong(songTitle)
    #song = readSong("song0001.json")
    h = song["noteList"]
    ht = song["noteTime"]
    i = 0
    for x in h:
        timerOnName = "t" + str(i) + "On"
        timerOffName = "t" + str(i) + "Off"
        hangTime = ht[i]
        noteStarters[timerOnName] = Timer(offset/1000 + sumPreviousSongLength/1000 + ht[i]/1000, startNote, [x])
        noteStoppers[timerOffName] = Timer(offset/1000 + sumPreviousSongLength/1000 + ht[i]/1000 + 0.1, stopNote, [x])
        noteStarters[timerOnName].start()
        noteStoppers[timerOffName].start()
        i = i + 1


#Load Singysong
""" song = readSong("song0001.json")
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
    i = i + 1 """
    
