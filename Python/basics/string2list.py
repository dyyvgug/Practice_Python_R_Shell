#!/usr/bin/python
import sys
params=sys.argv[1:]
filename=params.pop(0) if params else "biden1.txt"
lst = []
wordset = []
bi = open(filename)
for line in bi:
    if line.strip():
        i = line.rstrip().lower().split()
        print(i)
        for j in i:
            lst.append(j)
            if not j in wordset:
                wordset.append(j)
bi.close()

print(len(lst))
