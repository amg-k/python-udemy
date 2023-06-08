from pprint import pprint as pp

def generate_exponential_number():
    x = 1
    while True:
        yield x * x
        x += 1

def generate_exponential_number_send():
    num = 0
    while True:
        num = yield num * num

a = generate_exponential_number()
b = generate_exponential_number_send()


generatedNumbers = []
'''
for _ in range(20):
    generatedNumbers.append(next(a))

print(generatedNumbers)
print(len(generatedNumbers))

for _ in range(30):
    generatedNumbers.append(next(a))

print(generatedNumbers)
print(len(generatedNumbers))
'''

b.send(None)

for i in range(1, 21):
    generatedNumbers.append(b.send(i))

print(generatedNumbers)
print(len(generatedNumbers))

for i in range(21, 51):
    generatedNumbers.append(b.send(i))

print(generatedNumbers)
print(len(generatedNumbers))
