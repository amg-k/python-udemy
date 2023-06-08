import requests
import json
import webbrowser
from pprint import pprint

params = {
    'limit' : 3,
    'breed_ids' : 'norw'
    }

print(params)
r = requests.get('https://api.thecatapi.com/v1/images/search', params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print('Wrong data format')
else:
    pprint(content)

    i = 1
    for record in content:
        if i <= params['limit']:
            webbrowser.open(record['url'])
            i += 1
        else:
            break

