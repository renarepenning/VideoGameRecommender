# Kelly Romer

import requests

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
