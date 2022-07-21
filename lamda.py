# write a python program that create a function that take a parameter, and that parameter will multiply with an unknown given number 

def mult(n):
    return lambda x:x * n

result = mult(2)
print(result(15))

# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument.

def fct(a):
    return lambda x:x+a

k = fct(10)
print(k(15))

#  also create a lambda function that multiplies argument x with argument y and print the result.

def res(x,y):
    return lambda x,y:x*y
k = res(12,4)
print(k(12,4))
print(k(2,3))