#!pip3 install lxml

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from IPython.core.display import display, HTML
import datetime as dt
import numpy as np


url = "https://www.igdb.com/games/forza-horizon-5"
# needed in order for the server to think we're human so we can access the webpage for scraping
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content,  "html.parser")

main_info = soup.find(class_='optimisly-game-maininfo')
print(main_info)

IGDB_Id = main_info.find('span').text
release_dates = main_info.find_all('time')  # deal with this later

developer = main_info.find('a', class_="block").text
publisher = main_info.find_all('a', class_="block")[-1].text

print(publisher)

next_segment = soup.find(class_='optimisly-game-extrainfo1')

#modes, genres
extra_info1 = next_segment.find_all('a')

i = 0
mode_genre = []
while i < len(extra_info1):
    mode_genre.append(extra_info1[i].text)
    i = i+1
# mode_genre


game_mode = []
game_genre = []
modes = ["Battle Royale", "Co-operative",
         "Massively Multiplayer Online (MMO)", "Multiplayer", "Single player", "Split screen"]
genres = ["Point-and-click", "Fighting", "Shooter", "Music", "Platform", "Puzzle", "Racing",
          "Real Time Strategy (RTS)", "Role-playing (RPG)", "Simulator", "Sport", "Strategy", "Turn-based strategy (TBS)", "Tactical", "Quiz/Trivia", "Hack and slash/Beat ‘em up", "Pinball", "Adventure", "Arcade", "Visual Novel", "Indie", "Card & Board Game", "MOBA"]
for elm in mode_genre:
    if elm in modes:
        game_mode.append(elm)
    else:
        game_genre.append(elm)

# game_genre

next_segment2 = soup.find(class_='optimisly-game-extrainfo2')
extra_info2 = next_segment2.find_all('a')

i = 0
info_2 = []
while i < len(extra_info2):
    info_2.append(extra_info2[i].text)
    i = i+1
print(info_2)
info_2 = info_2[:-1]
print(info_2)

game_perspective = []
game_themes = []
game_series = []
perspectives = ["Auditory", "Bird view / Isometric", "First person",
                "Side view", "Text", "Third person", "Virtual Reality"]
themes = ["Fantasy", "Thriller", "Science Fiction", "Action", "Horror", "Survival", "Historical",
          "Stealth", "Business", "Comedy", "Drama", "Non-fiction", "Educational", "Sandbox", "Kids",
          "Open world", "Warfare", "4X (explore, expand, exploit, and exterminate)", "Eroitc", "Mystery", "Party", "Romance"]

for elm in info_2:
    if elm in perspectives:
        game_perspective.append(elm)
    elif elm in themes:
        game_themes.append(elm)
    else:
        game_series.append(elm)


# game_series

more_data = soup.find(class_='loaded')
#extra_info2 = next_segment2.find_all('a')
print(more_data)

wiki_path = 'https://en.wikipedia.org/wiki/Lists_of_video_games'
#wiki_path = 'https://en.wikipedia.org/wiki/List_of_graphic_adventure_games'

shit = '<table class="wikitable sortable" style="width:100%">'
r = requests.get(wiki_path, headers=headers)
data = r.text.split('href="/wiki/List_of')
data = list(
    map(lambda x: 'https://en.wikipedia.org/wiki/List_of' + x.split('" ')[0], data))
# data


for x in pd.read_html('https://en.wikipedia.org/wiki/List_of_Xbox_One_X_enhanced_games'):
    print("PENIS")
    print(x.columns)
