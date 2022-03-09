# Kelly Romer
from igdb.wrapper import IGDBWrapper
import json
from VideoGameRecommender.Algorithm_Current.Scraping_Scripts.token import get_token

# Create Access Token
access_token = get_token()

# Create Wrapper
wrapper = IGDBWrapper('8kx354hpu7lzs6ga7c1ktafopq30qq', access_token)

# JSON API request
params = ['genres', 'themes', 'game_modes', 'platforms', 'keywords']
for item in params:
    byte_array = wrapper.api_request(item, 'fields id, name; limit 500;')
    data = json.loads(byte_array)
    with open(item+'_to_ids.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
