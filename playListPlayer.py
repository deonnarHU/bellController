import songPlayer
import json

#print("kacsatár és csacsitron")
offset = 2000


def readPlaylist(playlistName):
    #currentPlaylist
    with open("playlistTable.json") as f:
        data = json.load(f)
        #Get object where playListName == needed playlst name
        for j in data["playlists"]:
            print(playlistName)
            print(j)
            print(data)
            print(j["playlistName"])
            if j["playlistName"] == playlistName:
                currentPlaylist = j
            
    return currentPlaylist


def playPlaylist(playlistName):
    playlist = readPlaylist(playlistName)
    i = 0
    sumPreviousSongLength = 0
    for x in playlist["songs"]:
        #with open(playlist["songs"][i]) as g:
        print(x)
        with open("./songs/" + x) as g:
            currentSong = json.load(g)
        #songPlayer.playSong(playlist["songs"][i], i*offset, sumPreviousSongLength)
        songPlayer.playSong(x, i*offset, sumPreviousSongLength)
        songLength = currentSong["length"]
        #print(songLength)
        sumPreviousSongLength = sumPreviousSongLength + songLength
        #print("Scheduled song no" + playlist["songs"][i])
        i = i + 1