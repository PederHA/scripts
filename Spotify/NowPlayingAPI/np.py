import sys
import spotipy
import spotipy.util as util
import json
import time

"""
Based on Example from spotipy. Fetches information
about currently playing track from Spotify API and
writes to text file.

Limited by Spotify API rate limit, thus the win32gui
script is a better fit for this task.
"""

scope = 'user-read-playback-state'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()


while True:
    token = util.prompt_for_user_token(username, scope)
    if token:
        sp = spotipy.Spotify(auth=token)
        
        results = sp.current_user_playing_track()
        item = results['item']

        artist = json.dumps(item["artists"][0]["name"])
        artist = str(artist).replace('"', '')
        
        song = json.dumps(item["name"])
        song = song.strip('\"')

        with open('np.txt','w') as f:
            f.write(artist + ' - ' + song + '      ')


    else:
        print ("Can't get token for", username)
    time.sleep(75)