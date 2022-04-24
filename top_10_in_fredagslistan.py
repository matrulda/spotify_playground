import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from collections import defaultdict, Counter

scope = "playlist-read-collaborative"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

playlists = sp.current_user_playlists()
artists = defaultdict(int)
molmed_lists = 0

while playlists:
    for playlist in playlists['items']:
        if "molmed" in playlist['name'].lower() or "hej då johan" in playlist['name'].lower():
            molmed_lists += 1
            tracks = sp.playlist_tracks(playlist["uri"])["items"]
            for track in tracks:
                artist_name = track["track"]["artists"][0]["name"]
                artists[artist_name] += 1
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

print(f"Top 10 artists in Fredagslistan (based on {molmed_lists} playlists):")
for artist, no_tracks in Counter(artists).most_common(10):
    print(f"{artist}: {no_tracks}")
