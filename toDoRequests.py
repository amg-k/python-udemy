import requests
import json
from collections import defaultdict

def count_completed_task_by_user(inputData):
    completedTaskByUser = defaultdict(int)
    for record in inputData:
        if record['completed'] == True:
            completedTaskByUser[record['userId']] += 1
    return completedTaskByUser

def highest_value(myDict):
    return max(myDict.values())

def show_users_max_completed_tasks(userTaskDict, maxComplTasks):
    usersMaxList = []
    for (user, complTasks) in userTaskDict.items():
        if complTasks == maxComplTasks:
            usersMaxList.append(user)
    return usersMaxList

def get_user_name(requestParameter):
    r = requests.get('https://jsonplaceholder.typicode.com/users' + requestParameter)
    data = r.json()
    usersNames = []
    for user in data:
        usersNames.append(user['name'])
    return usersNames

def request_param(myList, key = 'id'):
    lastIteration = len(myList)
    i = 1
    paramUser = '?' + key + '='
    for userID in myList:
        if (i == lastIteration):
            paramUser += str(userID)
        else:
            paramUser += str(userID) + '&' + key +'='
        i += 1
    return paramUser

######
        
r = requests.get('https://jsonplaceholder.typicode.com/todos')

try:
    inputData = r.json()
except json.decoder.JSONDecodeError:
    print('Wrong data format')
else:
    print('Data import correct')

    usersTaskDict = count_completed_task_by_user(inputData)
    usersMaxTasks = show_users_max_completed_tasks(usersTaskDict, highest_value(usersTaskDict))
    topUsersNameList = get_user_name(request_param(usersMaxTasks))
    print("User with top completed tasks amounnt:", topUsersNameList)
    
