import requests
import json
import pprint
import webbrowser
from datetime import datetime, timedelta

timePeriod = timedelta(weeks=1)
pastTime = datetime.today() - timePeriod

params = {
    'site' : 'stackoverflow',
    'sort' : 'votes',
    'order' : 'desc',
    'fromdate' : int(pastTime.timestamp()),
    'tagged' : 'python',
    'min' : 5

}

r = requests.get('https://api.stackexchange.com/2.3/questions', params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print('Wrong data format')
else:
    for question in questions['items']:
        webbrowser.open_new_tab(question['link'])

