def file_search(fileName, word):
    try:
        with open(fileName, "r", encoding = "UTF-8") as file:
            return file.read().lower().count(word)
    except FileNotFoundError:
        print(f"File named {fileName} do not exist.")
    except PermissionError:
        print(f"No persission to read file {fileName}.")

fileName = input("Type file name: ")
searchWord = input("Type word to search: ")

wordCount = file_search(fileName, searchWord)
if wordCount != None:
    print(f"File named {fileName} contains {wordCount} of word {searchWord}.")
