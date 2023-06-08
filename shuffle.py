import random

cards = ["2", "3", "4", "5", "6", "7",
         "8", "9", "10", "Jack", "Queen",
         "King", "Ace", "Joker"]
print(cards)
'''
random.shuffle(cards)

print(cards)
'''
'''
result = set()
while len(result) < 6:
    result.add(random.randint(1, 10))

print(list(result))

print(random.sample(range(1,11), 6))
'''

random.shuffle(cards)
print(cards)

cardsA = []
cardsB = []

while len(cards) > 0:
    cardsA.append(cards.pop())
    cardsB.append(cards.pop())


print(cards, "\n",
      cardsA, "\n",
      cardsB)
