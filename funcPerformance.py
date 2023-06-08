import time

def function_performance(func, arg1, arg2, reps = 1):
    sumBf = 0
    for i in range(0, reps):
        start = time.perf_counter()
        func(arg1, arg2)
        end = time.perf_counter()
        sumBf += end - start
    return sumBf

def check(container, element):
    if element in container:
        return True
    else:
        return False
        
setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

print(function_performance(check, setContainer, 600, 200))
print(function_performance(check, listContainer, 600, 200))
