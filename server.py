from websocket_server import WebsocketServer
import json
from gpiozero import LED
from time import sleep
from threading import Timer
import time
#import notePlayer
import scheduler

noteMap = {
    "B3": "1",
    "C4": "2",
    "D4": "3",
    "E4": "4",
   # "F4": "5",
    "F#4": "6",
    "G4": "7",
    "A4": "8",
    "B4": "9",
    "C5": "10"}

# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	#server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


#def send_message()
# Called when a client sends a message
def message_received(client, server, message):
    #if len(message) > 200:
       # message = message[:200]+'..'
    #print("Client(%d) said: %s" % (client['id'], message))
    splitMessage = message.split("SEPARATOR")
    print(message)
    #print(splitMessage[0])
    if(splitMessage[0] == "Play"):
        #print(splitMessage[1])
        #notePlayer.playNote(noteMap.get(splitMessage[1]))
        scheduler.playSingleNote(splitMessage[1])
        #notePlayer.playNote(splitMessage[1])
        
    elif(splitMessage[0] == "UpdateSchedule"):
        #Update scheduleTable
        updatedSchedule = json.loads(splitMessage[1])
        #updatedSchedule["schedules"] = splitMessage[1]["schedules"]
        #print(updatedSchedule)
        
        with open("./scheduleTable.json", "w") as outfile:
            json.dump(updatedSchedule,outfile)
        scheduler.updateScheduler()
            
    elif(splitMessage[0] == "UpdatePlaylist"):
        #Update playlistTable
        updatedPlaylist = json.loads(splitMessage[1])
        #print(updatedSchedule)
        
        with open("./playlistTable.json", "w") as outfile:
            json.dump(updatedPlaylist,outfile)
            
    elif(splitMessage[0] == "UpdateSonglist"):
        #Update playlistTable
        updatedSonglist = json.loads(splitMessage[1])
        #print(updatedSchedule)
        
        with open("./songlistTable.json", "w") as outfile:
            json.dump(updatedSonglist,outfile)
            
    elif(splitMessage[0] == "RequestSchedule"):
        #Load scheduletable
        with open("./scheduleTable.json") as f:
            scheduleTable = json.load(f)
        with open("./playlistTable.json") as g:
            playlistTable = json.load(g)
        finalData = str(scheduleTable) + "SEPARATOR" + str(playlistTable)   
        server.send_message(client, finalData)
        
    elif(splitMessage[0] == "RequestPlaylist"):
        #Load playlisttable
        with open("./playlistTable.json") as f:
            playlistTable = json.load(f)
        with open("./songlistTable.json") as g:
            songlistTable = json.load(g)
        finalData = str(playlistTable) + "SEPARATOR" + str(songlistTable)    
        server.send_message(client, finalData)
        
    elif(splitMessage[0] == "Recording"):
         #Create list from the notes
         songNoteList = splitMessage[2].split(",")
         
         #Normalize Timestamps, then form list of times
         songNoteTimeListRaw = splitMessage[3].split(",")
         songNoteTimeList = []
         startTime = int(songNoteTimeListRaw[0])
         i = 0
         #print (songNoteTimeListRaw)
         for x in songNoteTimeListRaw:
             songNoteTimeList.append(int(x) - startTime)
         i = i+1
         
         #calculate full length
         songLength = songNoteTimeList[len(songNoteTimeList)-1] + 200
         
         #Generate the full json with the full time and the 2 lists
         newSong = {}
         newSong["length"] = songLength
         newSong["noteList"] = songNoteList
         newSong["noteTime"] = songNoteTimeList
         
         
         #Save life with the title as filename
         title = ("./songs/" + splitMessage[1] + ".json")
         with open(title, "w") as outfile:
             json.dump(newSong,outfile)
             
             
        #Add song to songlist.json
        #Open songlist file
         with open("./songlistTable.json") as f:
             songlistTable = json.load(f)
             #print(songlistTable)
        #Check if song with name already existed
         didSongExist = 0
         for k in songlistTable["songs"]:
             if(k["songName"] == splitMessage[1]):
                 k["length"] = songLength
                 didSongExist = 1
        #Create new entry object IF song did not exist
         if(didSongExist == 0):        
             newSongEntryForList = {}
             newSongEntryForList["ID"] = len(songlistTable["songs"]) + 1 
             newSongEntryForList["songName"] = splitMessage[1]
             newSongEntryForList["length"] = songLength
             #print(newSongEntryForList)
            #Add new entry to list
             songlistTable["songs"].append(newSongEntryForList)
         #print(songlistTable)
        #Rewrite songlist file
         with open("./songlistTable.json", "w") as outfile:
             json.dump(songlistTable,outfile)
             
    return 0

PORT=9001
server = WebsocketServer(PORT, host='0.0.0.0')
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
#server.send_message(send_message)
server.run_forever()
#scheduler.initScheduler()
#scheduler.startScheduler()
