#NESTED DATA STRUCTURE

nstList = []
iList1 = ["EURGBP", 4.4889, 9874562]
iList2 = ["EURUSD", 3.4897, 5135478]
iList3 = ["PLNUSD", 5.1257, 2324789]
listList = [iList1, iList2, iList3]

for listName in listList:
    nstList.append(listName)
    
'''
nstList.append(iList1)
nstList.append(iList2)
nstList.append(iList3)
'''

#print(nstList,"\n")

for ticker, price, volume in nstList:
    print("Ticker:", ticker)
    print("Price:", price)
    print("Volume:", volume)
    print("\n")

