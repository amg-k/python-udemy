#FIGURES AREA CALCULATION
from enum import IntEnum
import rawFiguresArea

Figures_Menu = IntEnum('Menu_Figures', {'Square':10, 'Rectangle':20, 'Triangle':30, 'Trapeze':40, 'Circle':50})

print(list(Figures_Menu))

print("""Figures area calculation, choose figure type:
10. square
20. rectangle
30. triangle
40. trapeze
50. circle
""")
mode = int(input())

while True:
    if mode == Figures_Menu.Square:
        a = float(input("Type square side (a): "))
        print("Square area =",rawFiguresArea.square_area(a))
    if mode == Figures_Menu.Rectangle:
        a = float(input("Type rectangle side (a): "))
        b = float(input("Type rectangle side (b): "))
        print("Rectangle area =",rawFiguresArea.rectangle_area(a, b))
    if mode == Figures_Menu.Triangle:
        h = float(input("Type triangle height (h): "))
        b = float(input("Type triangle base (b): "))
        print("Triangle area =",rawFiguresArea.triangle_area(h, b))
    if mode == Figures_Menu.Trapeze:
        h = float(input("Type trapeze height (h): "))
        a = float(input("Type trapeze base (a): "))
        b = float(input("Type trapeze base (b): "))
        print("Trapeze area =",rawFiguresArea.trapeze_area(h, a, b))
    if mode == Figures_Menu.Circle:
        r = float(input("Type circle radius (r): "))
        print("Circle area =",rawFiguresArea.circle_area(r))
    else:
        break
