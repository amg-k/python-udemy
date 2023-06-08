operation = input("Wybierz rodzaj działania: dodawanie (+), odejmowanie (-), mnożenie (*), dzielenie (/), potęga (**) ")
numA = int(input("Podaj pierwszą liczbę: "))
numB = int(input("Podaj drugą liczbę: "))

if(operation == "+"):
    print("Wynik działania:",numA,"+",numB,"=",numA + numB)
elif(operation == "-"):
    print("Wynik działania:",numA,"-",numB,"=",numA - numB)
elif(operation == "*"):
    print("Wynik działania:",numA,"*",numB,"=",numA * numB)
elif(operation == "/"):
    if(numB == 0):
        print("Druga liczba jest równa 0, zmień dane wejściowe")    
    else:
        print("Wynik działania:",numA,"/",numB,"=",numA / numB)
elif(operation == "**"):
    print("Wynik działania:",numA,"**",numB,"=",numA ** numB)
else:
    print("Wprowadziłeś/aś błędne dane wejściowe")
