#FUNCTIONS
'''
nameList = ["adam", "Mike", "brenda"]

def message(name):
    print("Welcome",name,"!")


for name in nameList:
    message(name.capitalize())


def squareSrf(a,b):
    return a * b

sqrAB = (squareSrf(5,12))
print("Area of square AB =",sqrAB)
'''

def divide(a,b):
    if b == 0:
        return
    return a/b

div = divide(5,48)

if div != None:
    print(div)
else:
    print("Divide by 0")


def prnt():
    return 65

x = prnt()
print(x)
