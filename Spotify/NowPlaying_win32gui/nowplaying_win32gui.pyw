import time
import win32gui

"""
Python script that retrieves currently playing artist and track
from an active Spotify instance on a computer running Windows. 
The data is written to a text file, which can be used for 
displaying "Now Playing" info when streaming.

This script used to be based on Spotilib, however its functionality
was broken in a Q2 2018 Spotify update. I have rewritten the script 
to restore its functionality. However, memory footprint has increased 
as a result. From 1MB to 4MB. Sleep values can be tweaked according 
to personal preferences.

Works as of Spotify 1.0.77.338.g758ebd78
"""


def find_active_window():
    """
    Tries to find an active Spotify window. Loops until window is found.
    """

    # Looks for a window with className "Chrome_WidgetWin_0" and title "Spotify"
    window_id = win32gui.FindWindow("Chrome_WidgetWin_0", "Spotify")

    # If win32gui.FindWindow returned 0, repeat until window is found.
    while window_id == 0:
        window_id = win32gui.FindWindow("Chrome_WidgetWin_0", "Spotify")
        time.sleep(2)

   # Run get_song_info with the window_id that was obtained
    get_song_info(window_id)


def get_song_info(window_id):
    """
    Gets Spotify window title using `win32gui.GetWindowText()` with the
    previously obtained `window_id`. If spotify_window_title is 
    not 'Spotify' or '', parse window title and write it to text document. 
    
    After song info is parsed and written to file, the process sleeps 
    for 10 seconds then resumes the loop as long as a Spotify window is active.

    Should the window be closed, the loop is exited and `find_active_window()`
    is executed again.
    """

    spotify_window_active = True
    last_track = ""

    while spotify_window_active:
        # Get Spotify window title.
        spotify_window_title = win32gui.GetWindowText(window_id)
        
        if spotify_window_title == "Spotify":
            # This means a song isn't currently playing, but the application is running.
            track_info = " "
            time.sleep(5)

        elif spotify_window_title == '':
            # If window is closed, win32gui.GetWindowText() returns empty string.
            track_info = " "
            
            # Terminate loop and look for new window.
            spotify_window_active = False
            find_active_window()

        else:
            # Else split the window title at the "-" symbol to get artist and song strings.
            # This isn't explicitly necessary, however it gives more flexibility with regards to formatting.
            artist, song = spotify_window_title.split("-", 1)

            # Concatenate
            track_info = (f"{artist} - {song}         ")
    
        if track_info != last_track:
            with open('np.txt', 'w+', encoding="utf-8") as f:
                    f.write(track_info)
        last_track = track_info
        time.sleep(5)


if __name__ == "__main__":
    find_active_window()
