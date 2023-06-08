import requests

fileName = "unknowWWWlist.txt"
wwwStatusDict = {'wwwWorking': 200,
                 'wwwNotWorking': 404}
workingWWWlist = []
notWorkingWWWlist = []

try:
    with open(fileName, 'r', encoding = "UTF-8") as f:
        wwwDatabase = f.read().splitlines()
except:
    print("File error")  
        
for adress in wwwDatabase:
    try:
        response = requests.get(adress)
        if response.status_code == wwwStatusDict.get('wwwWorking'):
            print(adress, 'is working properly')
            workingWWWlist.append(str(adress))
    except:
        print(adress, 'is causing error')
        notWorkingWWWlist.append(str(adress))

print(workingWWWlist)
print(notWorkingWWWlist)

try:
    with open('workingWWW.txt', 'a', encoding = 'UTF-8') as f:
        for adress in workingWWWlist:
            f.write(adress + '\n')
except:
    print('File error')

try:
    with open('notWorkingWWW.txt', 'w', encoding = 'UTF-8') as f:
        for adress in notWorkingWWWlist:
            f.write(adress + '\n')
except:
    print('File error') 
