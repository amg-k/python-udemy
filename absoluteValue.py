print("Program zwracający wartość bezwlgędną podanej liczby")
'''
num = int(input("Podaj liczbę: "))

print("Wartość bezwględna =",abs(num))
'''

num = int(input("Podaj liczbę: "))

if(num < 0):
    num = -num
    print("Wartość bezwzględna: ",num)
else:
    print("Wartość bezwzględna: ",num)
