import spotipy
from spotipy.oauth2 import SpotifyOAuth
from os import getenv
from dotenv import load_dotenv
from tqdm import tqdm

scope = ['user-read-private', 'user-library-read']

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def load_favourite_tracks():
    for i in tqdm(range(5565//20)):
        tracks = sp.current_user_saved_tracks(limit=20, offset=(i * 20))['items']
        with open('mymusic.txt', 'a', encoding='utf-8') as file:
            for song in tqdm(tracks):
                file.write(f"{song['track']['name']} - {song['track']['artists'][0]['name']} in album: {song['track']['album']['name']} \n")

def load_playlists():
    for k in tqdm(sp.current_user_playlists()['items']):
        # print(k['tracks'])
        playlist = sp.playlist(k['href'])
        with open(f"{playlist['name']}.txt", 'a', encoding='utf-8') as file:
            for song in tqdm(playlist['tracks']['items']):
                file.write(f"{song['track']['name']} - {song['track']['artists'][0]['name']} in album: {song['track']['album']['name']} \n")

load_playlists()