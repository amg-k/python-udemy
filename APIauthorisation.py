import requests
import json
import webbrowser
from pprint import pprint

api_key_value = str(input("Type API key: "))

params = {
    'api_key' : api_key_value,
    'country' : 'pl',
    'year' : 2023,
    'month' : 12
    }

#print(params)
r = requests.get('https://calendarific.com/api/v2/holidays', params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print('Wrong data format')
else:
    holidayList = content['response']['holidays']
    for holiday in holidayList:
        print(holiday['name'], holiday['date']['iso'])

'''
    i = 1
    for record in content:
        if i <= params['limit']:
            webbrowser.open(record['url'])
            i += 1
        else:
            break
'''
