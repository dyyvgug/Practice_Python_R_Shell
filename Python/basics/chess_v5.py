#!/usr/bin/python
import sys

def chess():
    print()
    print("  a b c d e f g h")
    for x in range(1, 9):
        print(f"{x}", end=" ")
        for y in range(1, 9):
            c = '.'
            for z in range(1,len(sys.argv)):
                fig = sys.argv[1]
                x0 = int(fig[0])
                y0 = int(fig[1])
                c0 = fig[2]
                if x == x0 and y == y0:
                    c = c0
            print(c,end=' ')
        print()
    print()

chess()
