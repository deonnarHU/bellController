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
            #Play it once at specific date and time
            #Need a specific function, which calls a schedule cancel after the run
            #schedule.
            schedule.every().day.at("10:30").do(schedulePlaylistOnce, playlistName = x["playListName"])
        elif x["Type"] == 2:
            #Play it every day at specific time
            schedule.every().day.at(x["Hour"] + ":" + x["Minute"] + ":" + x["Second"]).do(schedulePlaylist, playlistName = x["playListName"])
        elif x["Type"] == 3:
            #Play at specific day and time
            if x["Day"] == "monday":
                schedule.every().wednesday.at(x["Hour"] + ":" + x["Minute"] + ":" + x["Second"]).do(schedulePlaylist, playlistName = x["playListName"])
                #schedule.peepee
           #schedule.every()..at(x["Hour"] + ":" + x["Minute"] + ":" + x["Second"]).do(schedulePlaylist, playlistName = x["playListName"])
        elif x["Type"] == 4:
            #DEV OPTION - need to remove
            #Play at every minute at specific second
            schedule.every().minute.at(":" + str(x["Second"])).do(schedulePlaylist, playlistName = x["playListName"])
        else:
            print("shit happened bruh")

#type1
#schedule.

#schedule.every().minutes.do(job)
#schedule.every(10).seconds.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)
startScheduler()
while True:
    schedule.run_pending()
    time.sleep(1)
#playListPlayer.playPlaylist("playlist0001.json")