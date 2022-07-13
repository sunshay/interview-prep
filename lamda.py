# write a python program that create a function that take a parameter, and that parameter will multiply with an unknown given number 

from audioop import mul


def mult(n):
    return lambda x:x * n

result = mult(2)
print f"Double the number of 15 =", result(15))

