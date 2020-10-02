import numpy as np
import timeit 



def multiply_numbers(a,b):
    return a*b

print(timeit.repeat("multiply_numbers(800,3)", setup="from __main__ import multiply_numbers",repeat=1))  

print(timeit.timeit("y = 'x' * 3", number=10000000))