#GENERATOR
#why only one method is working at once?
import sys

evenNumGen = (num
              for num in range(101)
              if num % 2 == 0
              )

#print(evenNumGen)

for num in evenNumGen:
    sumEven = sum(evenNumGen)

print(sumEven)

print(sys.getsizeof(evenNumGen))

'''
evenList = []
evenListSum = 0

for num in evenNumGen:
    evenList.append(num)

print(evenList)

for num in evenList:
    evenListSum += num

print(evenListSum)

print(sys.getsizeof(evenList))
'''
