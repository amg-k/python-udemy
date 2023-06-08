#FIGURES AREA CALCULATION
import math

print("This application allows to calculate surface area of geometric figures")
print("To define what type of figure you want to calculate, choose from following")
print("square: SQR; rectangle: RECT; triangle: TRI; trapeze: TRAP; circle: CIRC")
modesTpl = ("SQR", "RECT", "TRI", "TRAP", "CIRC")

def modeSelect():
    while True:
        mode = input("Choose figure type: ")
        mode = mode.upper()
        if mode not in modesTpl:
            print("Wrong mode selected")
            continue
        return mode

def sqrArea():
    a = int(input("Type side of the square length: "))
    return a * a    

def rectArea():
    a = int(input("Type side 'a' of the rectangle length: "))
    b = int(input("Type side 'b' of the rectangle length: "))
    return a * b

def triArea():
    h = int(input("Type height of the triangle: "))
    a = int(input("Type base of the triangle: "))
    return (a * h)/2

def trapArea():
    h = int(input("Type height of the trapeze: "))
    a = int(input("Type base 'a' of the trapeze: "))
    b = int(input("Type base 'b' of the trapeze: "))
    return ((a+ b) * h)/2

def circArea():
    r = int(input("Type radius of the circle: "))
    return math.pi * (r ** 2)

def operation(mode):
    if mode == "SQR":
        print(sqrArea())
    elif mode == "RECT":
        print(rectArea())
    elif mode == "TRI":
        print(triArea())
    elif mode == "TRAP":
        print(trapArea())
    elif mode == "CIRC":
        print(circArea())
    else:
        print("Unknown error")


operation(modeSelect())

