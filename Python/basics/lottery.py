#!/usr/bin/python

import random

lst = []
while len(lst)<6:
    z=random.randint(1,49)
    if not z in lst:
         lst.append(z)

print(lst)
s = '\n'.join(str(x) for x in lst)
print(s)

"""
print("method2")
lst2 = list(range(1,50))
random.shuffle(lst2)
selected_numbers = lst2[:6]

print(selected_numbers)
s = '\n'.join(str(x) for x in selected_numbers)
print(s)
"""
