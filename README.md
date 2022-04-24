# spotify_playground
Playing around with the Spotify API


## Setup
Set up the [Authorization Code flow](https://spotipy.readthedocs.io/en/2.19.0/#getting-started) for Spotipy.

Add the following to your `.bashrc`:
```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url' # I use http://localhost:8080/
```

Make sure to add the redirect URI to your [app](https://developer.spotify.com/dashboard/).

Make a virtualenv and install spotipy
```
virtualenv venv
```

Activate the venv and install Spotipy
```
source venv/bin/activate
pip install spotipy
```

## Run the script!
```
python3 top_10_in_fredagslistan.py
```

You'll be propmted to give the app permission to use your Spotify data.
