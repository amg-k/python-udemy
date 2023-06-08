#NESTED DICTIONARY OPERATIONS
'''
ratings1 = {
                "Adam": [5,4,3,4,2,4],
                "John": [4,2,3,4,5,2],
                "Brenda": [5,6,2,3,4]
            }

for elmt in ratings1:
    print("Ratings for", elmt,":",ratings1[elmt])
'''
'''
prices = [
            {"city": "Warsaw", "flat sq/m": 15000, "car": 89000},
            {"city": "Berlin", "flat sq/m": 20000, "car": 96000},
            {"city": "London", "flat sq/m": 21000, "car": 101000}
        ]

for dictionary in prices:
    print("\n")
    for record in dictionary:
        print(record,":",dictionary[record])
'''        

pricesID = {
                "aa123": {"city": "Warsaw", "flat sq/m": 15000, "car": 89000},
                "ab234": {"city": "Berlin", "flat sq/m": 20000, "car": 96000},
                "ac345": {"city": "London", "flat sq/m": 21000, "car": 101000}
            }

for key in pricesID:
    print("\n")
    print(key)
    for subkey in pricesID[key]:
        print(subkey,":",pricesID[key][subkey])






'''
for ID in pricesID:
    print("\n")
    print(ID)
    for record in pricesID[ID]:
        print(record, pricesID[ID][record])
'''


