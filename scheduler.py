import playListPlayer
import schedule
import time
import json

print("suttyóság")
#scheduleTable

#Play it once at specific date and time
def getScheduleType1():
    return 0

#Play it every day at specific time
def getScheduleType2():
    return 0

#Play at specific day and time
def getScheduleType3():
    return 0

#DEV OPTION - need to remove
#Play at every minute at specific second
def getScheduleType4():
    return 0

def schedulePlaylistOnce(playlistName):
    #play playlist
    playlistName.playPlaylist(playlistName)
    return  schedule.CancelJob

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
            print("kacsa")
            #schedule.
        elif x["Type"] == 2:
            #Play it every day at specific time
            print("kacsa")
        elif x["Type"] == 3:
            #Play at specific day and time
            print("kacsa")
        elif x["Type"] == 4:
            #DEV OPTION - need to remove
            #Play at every minute at specific second
            print("kacsa4")
            print(x)
            print(x["Second"])
            print(x["playListName"])
            seconds = ":" + str(x["Second"])
            print(seconds)
            schedule.every().minute.at(":" + str(x["Second"])).do(job(x["playListName"]))
        else:
            print("shit happened bruh")

#type1
#schedule.




def job(playlistName):
    print("I'm working...")
    playListPlayer.playPlaylist()

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