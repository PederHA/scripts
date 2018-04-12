import time
import win32gui

"""
This script used to be based on Spotilib, however Spotify broke it in
some Q2 2018 update. I have rewritten the script to restore its functionality.
However, memory footprint has quadrupled as a result. From 1MB to 4MB.
"""

def find_active_window():

    window_id = win32gui.FindWindow("Chrome_WidgetWin_0", "Spotify")

    while window_id == 0:
        window_id = win32gui.FindWindow("Chrome_WidgetWin_0", "Spotify")
        time.sleep(2)
    get_song_info(window_id)

def get_song_info(window_id):
    
    spotify_window_active = True

    while spotify_window_active == True:
        #Get spotify window info.
        spotify_text = win32gui.GetWindowText(window_id)
        artist = ""
        song = ""
        if spotify_text == "Spotify":
            time.sleep(5)
        
        elif spotify_text == '':
            spotify_window_active = False
            find_active_window()
        
        else:
            artist, song = spotify_text.split("-",1)

            #Concatenate
            songinfo = (artist + " - " + song + "       ")

            with open('np.txt','w',encoding="utf-8") as f:
                f.write(songinfo)
            time.sleep(10)

if __name__ == "__main__":
    find_active_window()