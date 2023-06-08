#LISTS OPERATIONS


usrValue = 0
expenses = 0
expensesList = []

print("Summarize a daily expenses")

while(usrValue != "END"):
    usrValue = input("Enter a expense value (or type END)")
    if (usrValue != "END"):
        expenses += float(usrValue)
        expensesList.append(float(usrValue))

        
print("Your summarized daily expenses are:",expenses)
print("Your daily expenses list is:",expensesList)
expensesList.sort(reverse=True)
print("Expenses list sorted ascending:",expensesList)
print("Today's biggest expense was:",max(expensesList))
expensesList.clear()
print(expensesList)

'''
exList = [0,0,0,0,0]
print(exList)
exList[0] = 1
exList[1] = 2
exList[-3] = len(exList) - 2
exList[-2] = len(exList) - 1
exList[-1] = len(exList)
print(exList)
'''
