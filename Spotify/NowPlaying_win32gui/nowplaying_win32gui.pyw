"""
Python script that retrieves currently playing artist and track
from an active Spotify instance on a computer running Windows. 
The data is written to a text file, which can be used for 
displaying "Now Playing" info when streaming.

This script used to be based on Spotilib, however its functionality
was broken in a Q2 2018 Spotify update. I have rewritten the script 
to restore its functionality. Sleep values can be tweaked according 
to personal preferences.

Works as of Spotify 1.0.77.338.g758ebd78
"""

import time
import win32gui
import functools


def find_active_window() -> int:
    """
    Attempts to find an active Spotify window. Loops until window is found.
    """

    # Loops until win32gui.FindWindow returns anything but 0
    while True:
        _id = win32gui.FindWindow("Chrome_WidgetWin_0", "Spotify")
        if _id == 0:
            time.sleep(2)
        else:
            return _id
    

def get_song_info(window_id: int, sleep_duration: int=2, spaces: int=10) -> None:
    """
    Finds title of Spotify window with ID `window_id` and writes it to a text file.
    If no song is playing, an empty string is written to file.

    Loops until a Spotify window with the given `window_id` cannot be found any longer.
    """

    last_track = None
    spotify_window_title = None
    
    while spotify_window_title != "":
        # Get Spotify window title.
        spotify_window_title = win32gui.GetWindowText(window_id)
        
        if spotify_window_title == "Spotify":
            # This means a song isn't currently playing, but the application is running.
            track_info = ""
        else:
            spaces = " "*10
            track_info = f"{spotify_window_title}{spaces}"

        if track_info != last_track:
            with open('np.txt', 'w+', encoding="utf-8") as f:
                f.write(track_info)
        last_track = track_info
        time.sleep(sleep_duration)


def main():
    while True:
        window_id = find_active_window()
        get_song_info(window_id)


if __name__ == "__main__":
    main()
