'''
try:
    file = open("test", "w")
    file.write("sample")
    i = 2 / 3
    file.write(str(i))
finally:
    file.close()
'''
'''
with open("testFile", "w") as file:
    file.write("sample ")
    #0/0
    i = 121/ 12134
    file.write(str(i))
'''
'''
with open("waluty.txt", "r", encoding="UTF-8") as file_waluty:
    waluty = file_waluty.read().splitlines()
    file_waluty.seek(0)
    print(waluty)
    lineWaluty = file_waluty.readlines()
    print(lineWaluty)
    file_waluty.seek(0)
    for line in file_waluty:
        print(line)

'''

with open("waluty.txt", "a+", encoding="UTF-8") as walutyFile:
    walutyFile.seek(0)
    print(walutyFile.read())
    walutyFile.write("test ")
