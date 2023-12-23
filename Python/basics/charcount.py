#!/usr/bin/python
import sys
# parse params
if len(sys.argv) != 3:
    print("usage: charcount <char> <filename>")
    exit(1)
char = sys.argv[1]
filename = sys.argv[2]

# main
n=0
fh = open(filename)
for i in fh:
    for c in i:
        if c==char:
            n+=1
fh.close()

print("{} occurs {} times in {}".format(char,n,filename))
