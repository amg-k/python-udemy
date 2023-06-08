#ADDITION OF THREE EVEN AND POSITIVE NUMBERS

i = 0
result = 0
while(i < 3):
    num = int(input("Enter a number (positive, even) "))
    if(num > 0 and num % 2 == 0):
        result += num
    else:
        print("The given number does not meet the criteria, enter again") 
        continue
    i += 1
print("Addition result = ",result)
