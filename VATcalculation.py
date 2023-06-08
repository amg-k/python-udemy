#PRICE VAT CALCULATION

VAT = 8
calculatedVAT = 1 + VAT / 100

JavaNettoPrice = 50
PythonNettoPrice = 100

JavaBruttoPrice = JavaNettoPrice * calculatedVAT
PythonBruttoPrice = PythonNettoPrice * calculatedVAT

print("Java course brutto price: ",JavaBruttoPrice,"; Python course brutto price: ",PythonBruttoPrice)