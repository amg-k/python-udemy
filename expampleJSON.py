import json
import pprint

'''
exValue = 1410
rawDataDict = {'kot': 'cat', 'ryba': 'fish', 'krowa': 'cow'}
rawDataList = ['test', '2321adaw2', 'ąćężźó', True, None, exValue]

print(json.dumps(rawDataDict, ensure_ascii=False, indent = 4, sort_keys = True))
print(json.dumps(rawDataList, ensure_ascii=False, indent = 4, sort_keys = False))

with open("DictJSON.json", "w", encoding = "UTF-8") as f:
    json.dump(rawDataDict, f, ensure_ascii=False, indent = 4, sort_keys = True)

with open("ListJSON.json", "w", encoding = "UTF-8") as f:
    json.dump(rawDataList, f, ensure_ascii = False, indent = 4, sort_keys = True)
'''

with open("sample.json", "r", encoding = "UTF-8") as f:
    JSONresult = json.load(f)

for key, value in JSONresult.items():
    print(key, ":", value)


pprint.pprint(JSONresult)
