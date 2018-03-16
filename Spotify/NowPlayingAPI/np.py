import sys
import spotipy
import spotipy.util as util
import json
from pprint import pprint
import time

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
        #for artists in item["album"]["artists"]:
            #print (artists)
        print ("Artist:",item["artists"][0]["name"])
        print ("Song title:",item["name"])
        artistw = json.dumps(item["artists"][0]["name"])
        artistw = str(artistw)
        artistw = artistw.replace('"', '')
        songw = json.dumps(item["name"])
        songw = songw.strip('\"')
        f = open('np.txt','w')
        f.write(artistw)
        f.write(' - ')
        f.write(songw)
        f.write('      ')
        f.close

    else:
        print ("Can't get token for", username)
    time.sleep(75)