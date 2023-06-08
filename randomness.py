#RANDOMNESS

import random
import collections

'''
for i in range(5):
    print("random()",random.random())

for i in range(5):
    print("uniform(1,10)",random.uniform(1,10))

for i in range(5):
    print("randrange(10)",random.randrange(0, 13, 3))

for i in range(5):
    print("randint(1, 6)",random.randint(1, 6))
'''
hitList = []
szczerbiecAccuracy = 0.75

def will_hit(weaponAcc):
    if random.random() <= weaponAcc:
        return True
    else:
        return False

for i in range(100):
    hitList.append(will_hit(szczerbiecAccuracy))

print("True:", hitList.count(True), "False:", hitList.count(False))

print(collections.Counter(hitList))
