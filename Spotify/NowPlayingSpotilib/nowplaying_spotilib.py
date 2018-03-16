import spotilib
import codecs
import time

while True:
    #Get spotify information
    spotilib.artist() #returns the artist of the current playing song
    spotilib.song() #returns the song title of the current playing song

    #Concetate
    songinfo = (spotilib.artist() + " - " + spotilib.song())


    f = codecs.open('np.txt','w',"utf-8")
    f.write(songinfo)
    time.sleep(10)