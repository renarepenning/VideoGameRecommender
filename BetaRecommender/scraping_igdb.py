import requests

# Author: Kelly Romer
# Reference Source: https://github.com/BarryCarlyon/twitch_misc/blob/main/authentication/app_access_tokens/python/generate.py


def get_token():
    client_id = '8kx354hpu7lzs6ga7c1ktafopq30qq'
    client_secret = 'yucgxc2bqiobcn2pfadu5bui5amuan'

    body = {
        'client_id': client_id,
        'client_secret': client_secret,
        "grant_type": 'client_credentials'
    }
    r = requests.post('https://id.twitch.tv/oauth2/token', body)

    # data output
    keys = r.json()

    print(keys)

    headers = {
        'Client-ID': client_id,
        'Authorization': 'Bearer ' + keys['access_token']
    }
    return headers

# Functions to tag onto the end of the ML code to translate numerical id's to words
# Can also be used to scrape data in the same manner as Postman
