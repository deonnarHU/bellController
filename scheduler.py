import playListPlayer
import schedule
import time
import json

def schedulePlaylistOnce(playlistName):
    #play playlist
    playListPlayer.playPlaylist(playlistName)
    return  schedule.CancelJob

def schedulePlaylist(playlistName):
    #play playlist
    playListPlayer.playPlaylist(playlistName)

def loadScheduleTable():
    with open("scheduleTable.json") as f:
        data = json.load(f)
    return data

def startScheduler():
    scheduleTable = loadScheduleTable()

    for x in scheduleTable["schedules"]:
        if x["Type"] == 1:
            #Play it once at specific date and time today
            schedule.every().day.at(x["Hour"] + ":" + x["Minute"] + ":" + x["Second"]).do(schedulePlaylistOnce, playlistName = x["playListName"])
        elif x["Type"] == 2:
            #Play it every day at specific time
            schedule.every().day.at(x["Hour"] + ":" + x["Minute"] + ":" + x["Second"]).do(schedulePlaylist, playlistName = x["playListName"])
        elif x["Type"] == 3:
            #Play at specific day and time
            if x["Day"] == "monday":
                schedule.every().monday.at(x["Hour"] + ":" + x["Minute"] + ":" + x["Second"]).do(schedulePlaylist, playlistName = x["playListName"])
            elif x["Day"] == "tuesday":
                schedule.every().tuesday.at(x["Hour"] + ":" + x["Minute"] + ":" + x["Second"]).do(schedulePlaylist, playlistName = x["playListName"])
            elif x["Day"] == "wednesday":
               schedule.every().wednesday.at(x["Hour"] + ":" + x["Minute"] + ":" + x["Second"]).do(schedulePlaylist, playlistName = x["playListName"])
            elif x["Day"] == "thursday":
                schedule.every().thursday.at(x["Hour"] + ":" + x["Minute"] + ":" + x["Second"]).do(schedulePlaylist, playlistName = x["playListName"])
            elif x["Day"] == "friday":
                schedule.every().friday.at(x["Hour"] + ":" + x["Minute"] + ":" + x["Second"]).do(schedulePlaylist, playlistName = x["playListName"])
            elif x["Day"] == "saturday":
                schedule.every().saturday.at(x["Hour"] + ":" + x["Minute"] + ":" + x["Second"]).do(schedulePlaylist, playlistName = x["playListName"])
            elif x["Day"] == "sunday":
                schedule.every().sunday.at(x["Hour"] + ":" + x["Minute"] + ":" + x["Second"]).do(schedulePlaylist, playlistName = x["playListName"])
            else:
                print("Shit's fucked up, bruh!")
        elif x["Type"] == 4:
            #DEV OPTION - need to remove
            #Play at every minute at specific second
            schedule.every().minute.at(":" + str(x["Second"])).do(schedulePlaylist, playlistName = x["playListName"])
        else:
            print("shit happened bruh")



startScheduler()

while True:
    schedule.run_pending()
    time.sleep(1)