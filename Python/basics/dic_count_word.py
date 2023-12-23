#!/usr/bin/python
import sys
params=sys.argv[1:]
filename=params.pop(0) if params else "biden1.txt"

d={}
bi = open(filename)
for line in bi:
    if line.strip():
        i = line.rstrip().lower().split()
        #print(i)
        for j in i:
            if not j in d:
                d[j] = 0
            d[j]+=1
print(d)
bi.close()

print(d["the"])
# extracting top 10 occurrence word
print(len(d))
result=sorted(d.items(),key=lambda x:-x[1])[:10]
print(result)

