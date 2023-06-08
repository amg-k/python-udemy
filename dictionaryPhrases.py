#DICTIONARY PHRASES

names = {"Adam", "Ann", "Jerry", "James", "Agness"}

aNamesLen = {
             name: len(name)
             for name in names
             if name.startswith("A")
             }
print(aNamesLen)

numSet = {1, 3, 4, 21, 6, 7, 21, 3, 6}

numModulo = {num: num % 3
             for num in numSet
            }

print(numModulo)
            
