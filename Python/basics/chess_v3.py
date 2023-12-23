#!/usr/bin/python
import sys

def chess(x0,y0,marker):
    print()
    print("  a b c d e f g h")
    for x in range(1, 9):
        print(f"{x}", end=" ")
        for y in range(1, 9):
            if x == x0 and y == y0:
                print(marker, end=" ")
            else:
                print(".", end=" ")
        print()
if IndexError:
    print("USAGE: chess_v3 <X> <Y> <c>")
    exit(1)
chess(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])
