#!/usr/bin/python
import random

fh=open("mydata","w")
for i in range(100000):
    print(random.gauss(10,3),file=fh)
fh.close()
