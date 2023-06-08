def fileRead(path):
    try:
        with open(path, "r", encoding = "UTF-8") as file:
            return file.read()
    except FileNotFoundError:
        return "No such file"
            
fileName = input("Wrtie file name to open: ")

fileContent = fileRead(fileName)

print(fileContent)
