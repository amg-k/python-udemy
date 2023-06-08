#LIST PHRASES

numbers = [2, 3, 5, 6, 7, 8, 9]

'''
numExpo = []
numEven = []

for num in numbers:
    numExpo.append(num ** 2)

print(numExpo)

for num in numbers:
    if (num % 2 == 0):
        numEven.append(num)

print(numEven)
'''
'''
numExpo = [
            num ** 2
            for num in numbers
            ]

print(numExpo)

numEven = [
            num
            for num in numbers
            if (num % 2 == 0)
            ]

print(numEven)
'''

years = [1973, 1821, 1992, 1982, 1931, 2001]

y90 = [str(year)
       for year in years
       if (str(year) > "1990")
       ]

print(y90)
