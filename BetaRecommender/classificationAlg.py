import requests
from User import User
from scraping_igdb import get_token
'''implement classification alg - KNN classifier'''

# Get user name and ratings
new_user = User()
new_user.printUser()

# pull data from indie games
features = ["name", "game", "studio", "console", "keywords", "similar games"]


'''# scraping IGDB
headers = get_token()
query = requests.post('https://api.igdb.com/v4/games', headers=headers)
'''
