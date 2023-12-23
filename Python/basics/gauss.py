#!/usr/bin/python

import sys
import random
import math

'''print(random.gauss(10,3))
print(math.sqrt(9))
print(3**2)'''

lst = []
n_samples = 100000
for i in range(n_samples):
    lst.append(random.gauss(10, 3))

mean = sum(lst) / len(lst)
variance = sum((x - mean) ** 2 for x in lst) / len(lst)
std = math.sqrt(variance)
print("the mean is ", mean)
print("the variance is ", variance)
print("the standard deviation is ", std)

# reading data from file
print("data from file")
params = sys.argv[1:]
filename = params[0] if params else "gauss_1_10_3.csv"

fh = open(filename)
for i in fh:
    lst.append(float(i))
fh.close()

mean = sum(lst) / len(lst)
variance = sum((x - mean) ** 2 for x in lst) / len(lst)
std = math.sqrt(variance)
print("the mean is ", mean)
print("the variance is ", variance)
print("the standard deviation is ", std)


