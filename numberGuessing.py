#NUMBER GUESSING

hiddenNum = 42
userNum = 0

while (hiddenNum != userNum):
    userNum = int(input("Enter a number: "))
    if (userNum > hiddenNum):
        print("Given number is too large")
    elif (userNum < hiddenNum):
        print("Given number is too small")
    else:
        print("Great! Number is correct!")
