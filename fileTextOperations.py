namesList = []

with open("imionanazwiska.txt", "r", encoding="UTF-8") as file:
    for line in file:
        namesList.append(tuple(line.replace("\n", "").split(" ")))

with open("imiona.txt", "w", encoding="UTF-8") as file:
    for item in namesList:
        file.write(item[0] + "\n")

with open("nazwiska.txt", "w", encoding="UTF-8") as file:
    for item in namesList:
        try: 
            file.write(item[1] + "\n")
        except:
            file.write("\n")
