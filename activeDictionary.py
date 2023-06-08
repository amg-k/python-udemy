#ACTIVE DICTIONARY

dictionary = {}
mode = 0

print("This is active dictionary. You can add your own phrases and its definitions. Additionaly you can call a definition or delete a phrase")
print("To add a definition type 'IN'; to delete tpye 'DEL'; to call a phrase 'CALL', to show whole dictionary 'ALL', to terminate program 'EXIT'.")
#mode = input()
'''
while (mode != "EXIT"):
    if mode == "IN":
        print("Input mode")
        key = input("Type a key: ")
        value = input("Type a value: ")
        dictionary.update({key:value})
        mode = input("Type IN/DEL/CALL/ALL/EXIT: ")
    elif mode == "DEL":
        print("Delete mode")
        delKey = input("Type a key to delete: ")
        while delKey not in dictionary:
            print("Such key not exist")
            delKey = input("Type a key to delete: ")
        del(dictionary[delKey])
        mode = input("Type IN/DEL/CALL/ALL/EXIT: ")
    elif mode == "CALL":
        print("Call mode")
        callKey = input("Type a key to call: ")
        while callKey not in dictionary:
            print("Such key not exist")
            callKey = input("Type a key to call: ")
        print(dictionary.get(callKey))
        mode = input("Type IN/DEL/CALL/ALL/EXIT: ")
    elif mode == "ALL":
        print("Whole dictionary: ")
        print(dictionary)
        mode = input("Type IN/DEL/CALL/ALL/EXIT: ")
    else:
        print("Wrong mode selected")
        mode = input("Type IN/DEL/CALL/ALL/EXIT: ")
'''

#USING FUNCTIONS
'''
def modeSelect(arg):
    while (arg != "EXIT"):
        if arg == "IN":
            inputMode()
        elif arg == "DEL":
            delMode()
        elif arg == "CALL":
            callMode()
        elif arg == "ALL":
            allMode()
        else:
            print("Wrong mode selected")
            mode = input("Type IN/DEL/CALL/ALL/EXIT: ")
        break

def inputMode():
    print("Input mode")
    key = input("Type a key: ")
    value = input("Type a value: ")
    dictionary.update({key:value})
    mode = input("Type IN/DEL/CALL/ALL/EXIT: ")
    modeSelect(mode)
    
def delMode():
    print("Delete mode")
    delKey = input("Type a key to delete: ")
    while delKey not in dictionary:
        print("Such key not exist")
        delKey = input("Type a key to delete: ")
    del(dictionary[delKey])
    mode = input("Type IN/DEL/CALL/ALL/EXIT: ")
    modeSelect(mode)
    
def callMode():
    print("Call mode")
    callKey = input("Type a key to call: ")
    while callKey not in dictionary:
        print("Such key not exist")
        callKey = input("Type a key to call: ")
    print(dictionary.get(callKey))
    mode = input("Type IN/DEL/CALL/ALL/EXIT: ")
    modeSelect(mode)
    
def allMode():
    print("Whole dictionary: ")
    print(dictionary)
    mode = input("Type IN/DEL/CALL/ALL/EXIT: ")
    modeSelect(mode)
    
modeSelect(mode)
'''
############################

def inputDict(dictArg, keyArg, valueArg):
    dictionary[keyArg] = valueArg
    print("Definition add succesfull")

def deleteDict(dictArg, keyArg):
    if keyArg in dictArg:
        dictArg.pop(keyArg)
        print(keyArg,"removed succesfully")
    else:
        print("Such key doesn't exist")
        
def callDict(dictArg, keyArg):
    if keyArg in dictArg:
        print(dictArg[keyArg])
    else:
        print("Such key doesn't exist")

def allDict(dictArg):
    print("Whole dictionary: ")
    print(dictArg)

while True:
    mode = input("Type IN/DEL/CALL/ALL/EXIT: ")
    if mode == "IN":
        print("Input mode")
        key = input("Type a key: ")
        value = input("Type a value: ")    
        inputDict(dictionary, key, value)
    elif mode == "DEL":
        print("Delete mode")
        delKey = input("Type a key to delete: ")
        deleteDict(dictionary, delKey)
    elif mode == "CALL":
        print("Call mode")
        callKey = input("Type a key to call: ")
        callDict(dictionary, callKey)
    elif mode == "ALL":
        allDict(dictionary)
    elif mode == "EXIT":
        print("Closing dictionary")
        break
    else:
        print("Wrong mode selected")
