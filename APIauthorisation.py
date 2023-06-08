import requests
import json
import webbrowser
from pprint import pprint

params = {
    'api_key' : 'b0cf3ba4e2c0ebfcdcbe901c317fcffb17f57c95',
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
