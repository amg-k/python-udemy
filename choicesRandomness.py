import collections
import random

enchantType = ["blue", "green", "red", "gold"]
enchantChance = [0.7, 0.2, 0.07, 0.03]
'''
def enchant(argType, argRep):
    result = []
    for i in range(argRep):
        result.append(random.choice(argType))
    return result

print(collections.Counter(enchant(enchantType, 10)))
'''

def enchantParameter(argType, argRep = 1, argChance = None):
    return random.choices(argType, argChance, k = argRep)
    

print(collections.Counter(enchantParameter(enchantType, 100, enchantChance)))
