#LIST SUMMARIZE

numList = [5, 42, -8, 4, 14, 0, 9]

def listSum(list_arg):
    listSumBuffer = 0
    for num in list_arg:
        if num > 0:
            listSumBuffer += num
        else:
            continue
    return listSumBuffer

print(listSum(numList))
    
        
def listPhrase(list_arg):
    return sum([num
                for num in list_arg
                if num > 0
                ])


print(listPhrase(numList))
