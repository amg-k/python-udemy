import requests
import json
import webbrowser
from pprint import pprint
import ignore.APIauthHEADERcredentials

def get_json_from_response(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print('Wrong data format', response.text)
    else:
        return content

def get_favourite_cats(userId):
    params = {
        'sub_id' : userId
        }
    r = requests.get('https://api.thecatapi.com/v1/favourites', params,
                 headers=ignore.APIauthHEADERcredentials.headersParam)
    return get_json_from_response(r)

def get_random_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search',
                     headers=ignore.APIauthHEADERcredentials.headersParam)
    return get_json_from_response(r)[0]

def add_favourite_cat(catId, userId):
    catData = {
        'image_id' : catId,
        'sub_id' : userId
        }
    r = requests.post('https://api.thecatapi.com/v1/favourites', json = catData,
                     headers=ignore.APIauthHEADERcredentials.headersParam)
    return get_json_from_response(r)

def remove_favourite_cat(favouriteCatId):
    r = requests.delete('https://api.thecatapi.com/v1/favourites/' + favouriteCatId,
                     headers=ignore.APIauthHEADERcredentials.headersParam)
    return get_json_from_response(r)
'''
user enters login and password
credentials are compared with saved in database
if there is matching database returns userId and name
'''

userId = 'an3j16'
name = 'Adam'

print('Hello ' + name + '! Here\'re your favourite cats photos')
favouriteCats = get_favourite_cats('an3j16')
pprint(favouriteCats)
randomCat = get_random_cat()
print(randomCat['url'])

addToFavourite = input('Do you want to add cat to favourities? (Y/N)')

if (addToFavourite.upper() == 'Y'):
    addingFavouriteCatResult = (add_favourite_cat(randomCat['id'], userId))
    newlyAddedCatInfo = {addingFavouriteCatResult['id'] : randomCat['url']}
else:
    print('Try with another cat')

favouriteCatById = {
    favouriteCat['id'] : favouriteCat['image']['url']
    for favouriteCat in favouriteCats
    }
favouriteCatById.update(newlyAddedCatInfo)
pprint(favouriteCatById)

catIdToRemove = input('Type cat ID to remove from favourities: ')

print(remove_favourite_cat(catIdToRemove))
