#Write a Python program to filter a list of integers using Lambda.

a=[1,2,3,4,5,6,7,8,9]
# b = list(filter(lambda x: x%2 == 0, nums))
# print(type(a))

for i in a :
    if i % 2 == 0 :
        print('This is odd')
    else:
        print('This is even')
