#!/usr/bin/python
x0=3
y0=4
c0="T"

print('\n')
print('  a b c d e f g h')
x=1
while x<=8:
    print(x,end=' ')
    y=1
    while y<=8:
        print('.',end=' ')
        y=y+1
    print()
    x=x+1
    if x == 3 and y == 4:
        print('T')

print()