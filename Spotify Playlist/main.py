import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

load_dotenv()

URL = "https://www.billboard.com/charts/hot-100/"
ID = "f794eff1c1164c67884006540f4597f1"
SECRET = os.getenv("SECRET")
URI = "https://example.com"



date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    }
response = requests.get(url = URL + date,headers=header)
bilboard = response.text

soup = BeautifulSoup(bilboard,"html.parser")
songs = soup.select("li ul li h3")
song_titles = [song.getText().strip() for song in songs]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",redirect_uri=URI,client_id=ID,client_secret=SECRET,show_dialog=True,cache_path="token.txt",username="m4jki90"))
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify.Skipped.")

playlist = sp.user_playlist_create(user_id,name=f"{date} Bilboard 100", public=False,collaborative=False,description="Top 100 songs by Bilboard")
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

    

