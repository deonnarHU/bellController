import songPlayer
import json

#print("kacsatár és csacsitron")
offset = 2000


def readPlaylist(playlistName):
    with open(playlistName) as f:
        data = json.load(f)
    return data


def playPlaylist(playlistName):
    playlist = readPlaylist(playlistName)
    i = 0
    sumPreviousSongLength = 0
    for x in playlist["songs"]:
        #with open(playlist["songs"][i]) as g:
        with open("/songs/" + x) as g:
            currentSong = json.load(g)
        #songPlayer.playSong(playlist["songs"][i], i*offset, sumPreviousSongLength)
        songPlayer.playSong(x, i*offset, sumPreviousSongLength)
        songLength = currentSong["length"]
        #print(songLength)
        sumPreviousSongLength = sumPreviousSongLength + songLength
        #print("Scheduled song no" + playlist["songs"][i])
        i = i + 1