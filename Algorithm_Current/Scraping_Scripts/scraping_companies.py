# Kelly Romer

import requests
from igdb.wrapper import IGDBWrapper
import json

# Get Access Token
def get_token():
    client_id = '8kx354hpu7lzs6ga7c1ktafopq30qq'
    client_secret = 'yucgxc2bqiobcn2pfadu5bui5amuan'
    body = {
        'client_id': client_id,
        'client_secret': client_secret,
        "grant_type": 'client_credentials'
    }
    r = requests.post('https://id.twitch.tv/oauth2/token', body)
    keys = r.json()
    return keys['access_token']

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
