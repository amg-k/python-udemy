#DICTIONARY

stockPrice = {"ORLEN": 65.41, "AMBRA": 32.78, "VRG": 214.78}
print("Previous stock prices:",stockPrice)

stockPrice["ORLEN"] = float(input("Update ORLEN price: "))
stockPrice["AMBRA"] = float(input("Update AMBRA price: "))
stockPrice["VRG"] = float(input("Update VRG price: "))

print("Actual ORLEN price:",stockPrice["ORLEN"])
print("Actual AMBRA price:",stockPrice["AMBRA"])
print("Actual VRG price:",stockPrice["VRG"])
print("Actual stock prices:",stockPrice)

print(stockPrice.items())
