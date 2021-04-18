# import requests
# from bs4 import BeautifulSoup
#
# date_input = input("Enter the year you would like to travel to in YYY-MM-DD format: ")
#
# CLIENT_ID = 'b89e24859a3f43c888eef9b720e8b477'
# CLIENT_SECRET = '00253b59f0df430ba095dcce26c167ad'
# URL = f'https://www.billboard.com/charts/hot-100/{date_input}'
#
# response = requests.get(URL)
# billboard_html = response.text
#
# soup = BeautifulSoup(billboard_html, 'html.parser')
# top_100_songs = soup.find_all(name='span', class_='chart-element__information__song text--truncate color--primary')
# songs = [song.getText() for song in top_100_songs]
# print(songs)


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()