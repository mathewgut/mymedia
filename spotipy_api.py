
import spotipy
from api_keys import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

scope = ("user-read-playback-state playlist-modify-public "
         "playlist-modify-private user-library-read user-library-modify user-top-read")


sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(
    scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI))

# basic method for returning x amount of top tracks, can customize term with short_term, medium_term, long_term
# short_term = 4 weeks, medium_term = 6 months, long_term = 1 year
def top_tracks(track_count=5,time_range='medium_term'):
    assert(type(time_range) == str)
    assert (type(track_count) == int)
    results = sp.current_user_top_tracks(limit=track_count, time_range=time_range)
    songs = {}
    counter = 0
    for track in results['items']:
        track_info = [(track['name']), track['artists'][0]['name']]
        counter += 1
        songs[counter] = track_info
    return songs

# parse the extremely dense api call results and organize by type
def parse_spotify_results(results):
    parsed_results = {
        "tracks": [],
        "artists": [],
        "albums": [],
    }

    # tracks
    if "tracks" in results:
        for track in results["tracks"]["items"]:
            parsed_results["tracks"].append({
                "name": track["name"],
                "artist": [artist["name"] for artist in track["artists"]],
                "album": track["album"]["name"],
                "image": track["album"]["images"][0]["url"] if track["album"]["images"] else None,
                "url": track["external_urls"]["spotify"],
            })

    # artists
    if "artists" in results:
        for artist in results["artists"]["items"]:
            parsed_results["artists"].append({
                "name": artist["name"],
                "image": artist["images"][0]["url"] if artist["images"] else None,
                "url": artist["external_urls"]["spotify"],
            })

    # albums
    if "albums" in results:
        for album in results["albums"]["items"]:
            parsed_results["albums"].append({
                "name": album["name"],
                "artist": [artist["name"] for artist in album["artists"]],
                "image": album["images"][0]["url"] if album["images"] else None,
                "url": album["external_urls"]["spotify"],
            })

    return parsed_results

def search_spotify(query, search_type="track,artist,album", limit=10):  # Use your Spotipy setup
    results = sp.search(q=query, type=search_type, limit=limit)
    return parse_spotify_results(results)

print(search_spotify('joji dancing in the dark')['artists'][0]['image'])



