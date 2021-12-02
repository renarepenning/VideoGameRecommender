from scraping_igdb import get_token
from User import User
import pandas as pd
#!pip3 install openpyxl  # package to open xlsx files
#!pip3 install xlrd
'''implement classification alg - KNN classifier'''
features = ["name", "game", "studio", "console", "keywords", "similar games"]

# Get user name and ratings
new_user = User()
new_user.printUser()

# open excel file --> EXCEL READING NOT WORKING??
allGames = pd.read_csv("IGDB_games_beta.csv")
allGames.columns = ["id", "name", "category", "genres", "themes",
                    "involved_companies", "platforms", "key_words", "similar_games", "release_dates", ]
# allGames.reindex("")
print(allGames)
# .head() wont work # https://stackoverflow.com/questions/62624980/vscode-python-pandas-dataframe-intellisense-doesnt-show-attributes-method

userFeature = new_user.series
print(userFeature)


'''# scraping IGDB
headers = get_token()
query = requests.post('https://api.igdb.com/v4/games', headers=headers)
'''
