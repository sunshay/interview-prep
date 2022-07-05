# Write a Python program to find missing numbers from a list

# def missing_numbers_1(lst):
#     return [x for x in range(lst[0],lst[-1]+1) if x not in lst]

# lst = [6,7,10,11,13]
# print(missing_numbers_1(lst))

# 
# with open("cron.py","a") as f:
    # f.write("comment tu vas")

from functools import reduce
strings = [
    "Do not take life too seriously. You will never get out of it alive.",
    "My fake plants died because I did not pretend to water them.",
]

longest = reduce(lambda a,b: a if (len(a) > len(b)) else b, strings)
print(longest)
