from gpiozero import LED
from time import sleep
from threading import Timer
import time
import json
import serial

led1 = LED(5)
led2 = LED(6)
led3 = LED(13)
led4 = LED(19)
led5 = LED(7)
led6 = LED(26)
led7 = LED(21)
led8 = LED(20)
led9 = LED(16)
led10 = LED(12)
led1.on()
led2.on()
led3.on()
led4.on()
led5.on()
led6.on()
led7.on()
led8.on()
led9.on()
led10.on()

#h = [1,3,4,1,1]
#ht = [120,120,780,1780,2780]
noteStarters = {}
noteStoppers = {}

ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 31250,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

def readSong(songName):
    title = "./songs/" + songName + ".json"
    with open(title) as f:
        data = json.load(f)
    return data

def startNote(x):
    #print("startingu")
    if(noteSelector(x) == "Note exist NO"):
        print("no note")
    else:
        noteSelector(x).off()
        ser.write(b'\x90')
        ser.write(serialNoteSelector(x))
        ser.write(b'\x45')
    return 0

def stopNote(x):
    #print("stopperino")
    if(noteSelector(x) == "Note exist NO"):
        print("no note")
    else:
        noteSelector(x).on()
        ser.write(b'\x90')
        ser.write(serialNoteSelector(x))
        ser.write(b'\x00')
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

def serialNoteSelector(x):
    switcher = {
    "B3": b'\x3B', #59
    "C4": b'\x3C', #60
    "D4": b'\x3E', #62
    "E4": b'\x40', #64
    #"F4": b'\x41', #65
    "F#4": b'\x42', #66
    "G4": b'\x43', #67
    "A4": b'\x45', #69
    "B4": b'\x47', #71
    "C5": b'\x48'} #72
    return switcher.get(x,"Serial-Note exist NO")

def playSingleNote(x):
    starter = Timer(0, startNote, [x])
    stopper = Timer(0.1, stopNote, [x])
    starter.start()
    stopper.start()

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
    
