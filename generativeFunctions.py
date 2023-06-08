evenNumberGenerator = (element
                       for element in range(10)
                       if (element % 2 == 0)
                       )

def generate_even_number():
    print('start')
    for element in range(4):
        print('przed yield')
        if (element % 2 == 0):
            yield element
            print('po yield')
    print('stop')
    
a = evenNumberGenerator

b = generate_even_number()

tenNumberGenerator = (x
                       for x in range(10)
                      )

def generate_ten_nubmers():
    #print('start')
    x = 0
    while x < 10:
        #print('przed yield')
        yield x
        x += 1
        #print('po yield')
    #print('stop')

def generate_ten_nubmers_for():
    print('start')
    for x in range(10):
        print('przed yield')
        yield x
        print('po yield')
    print('stop')

func = generate_ten_nubmers()
phrase = tenNumberGenerator

print(list(generate_ten_nubmers()))
print(list(func))

print(list(tenNumberGenerator))
print(list(phrase))
