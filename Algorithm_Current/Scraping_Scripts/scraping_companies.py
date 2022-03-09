# Kelly Romer
from igdb.wrapper import IGDBWrapper
import json
from VideoGameRecommender.Algorithm_Current.Scraping_Scripts.token import get_token

# Create Access Token
access_token = get_token()

# Create Wrapper
wrapper = IGDBWrapper('8kx354hpu7lzs6ga7c1ktafopq30qq', access_token)

# JSON API request
json_arr = []
offset = 0
for i in range(80):
    byte_array = wrapper.api_request('companies', 'fields id, name; limit 500; offset ' + str(offset) + ';')
    # append byte_array to same json every time we loop and save it to a file
    data = json.loads(byte_array)
    json_arr.append(data)
    with open('companies_to_ids.json', 'a') as outfile:
        json.dump(json_arr, outfile, indent=4)
    offset += 500
