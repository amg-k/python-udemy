#CELSIUS TO FARENHEIT

celsius = {"t1": 21,
           "t2": 12,
           "t3": -5,
           "t4": 7,
           "t5": -11
           }

print(celsius)
#print(celsius.items())



farenheit = {
            temp: cels * 1.8 + 32
            for temp, cels in celsius.items()
            if cels < 0
             }

print(farenheit)

