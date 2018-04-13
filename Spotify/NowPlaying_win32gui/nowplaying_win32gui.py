import time
import win32gui

"""
This script used to be based on Spotilib, however its functionality
was broken in a Q2 2018 Spotify update. I have rewritten the script 
to restore its functionality.However, memory footprint has quadrupled 
as a result. From 1MB to 4MB.

Works as of Spotify 1.0.77.338.g758ebd78
"""


def find_active_window():
    """
    Tries to find an active Spotify window. Loops until window is found.
    """

    # Looks for a window with className "Chrome_WidgetWin_0" and title "Spotify"
    # Returns 0 if window isn't found.
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
    previously obtained `window_id`. If title is not Spotify, parse
    title and write it to text document. 
    
    After song info is parsed and
    written, sleeps for 10 seconds then resumes the loop as long as
    a Spotify window is active.

    Should the window be closed, the loop is exited and `find_active_window()`
    is executed again.
    """

    spotify_window_active = True

    while spotify_window_active:
        # Get Spotify window title.
        spotify_text = win32gui.GetWindowText(window_id)
        artist = ""
        song = ""
        
        if spotify_text == "Spotify":
            # This means a song isn't currently playing, but the application is running.
            time.sleep(5)

        elif spotify_text == '':
            # If the spotify window that was found with find_active_window() is not found, terminate loop.
            spotify_window_active = False
            find_active_window()

        else:
            # Else split the window title at the "-" symbol to get artist and song strings.
            artist, song = spotify_text.split("-", 1)

            # Concatenate
            songinfo = (artist + " - " + song + "       ")

            with open('np.txt', 'w', encoding="utf-8") as f:
                f.write(songinfo)
            time.sleep(10)


if __name__ == "__main__":
    find_active_window()
