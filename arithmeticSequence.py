#ARITHMETIC SEQUENCE - PERFORMANCE

import time

def sequence_sum_loop(num):
    sumBuffer = 0

    for num in range(1,num + 1):
        sumBuffer = sumBuffer + num
    return sumBuffer

def sequence_sum_loop_incr(num):
    sumBuffer = 0

    for num in range(1,num + 1):
        sumBuffer += num
    return sumBuffer

def sequence_sum_list(num):
    return sum([num for num in range(1,num + 1)])

def sequence_sum_set(num):
    return sum({num for num in range(1,num + 1)})

def sequence_sum_tuple(num):
    return sum((num for num in range(1,num + 1)))

def sequence_sum_formula(num):
    return (1 + num) / 2 * num

def finish_timer(start):
    end = time.perf_counter()
    return end - start

def function_performance(func, arg, reps = 1):
    sumBf = 0
    for i in range(0, reps):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sumBf += end - start
    return sumBf
    

print(function_performance(sequence_sum_loop, 123456, 30))
print(function_performance(sequence_sum_loop_incr, 123456, 30))
'''
print(function_performance(sequence_sum_list, 123456, 30))
print(function_performance(sequence_sum_set, 123456, 30))
print(function_performance(sequence_sum_tuple, 123456, 30))
print(function_performance(sequence_sum_formula, 123456, 30))
'''
