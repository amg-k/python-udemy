from pprint import pprint
import json
import requests

params = {
    'animal_type' : ''

    }
animalTypes = ['cat', 'dog']

print('Let\'s get some facts about animals!')

while True:
    mode = input('Choose animal type you\'re interested in (cat/dog): ')
    if (mode in animalTypes):
        params['animal_type'] = str(mode)
        break
    else:
        print('Such animal does\'t exist')
    
r = requests.get('https://cat-fact.herokuapp.com/facts/random', params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print('Wrong data format')
else:
    print(content['text'])
