#!/usr/bin/env python3
#
# chess_v6 [<XYC>]
#
# e.g. chess_v6 34T 88q 26b 13k
#

import sys

# main -----------------------------------------------------

print()
print("  a b c d e f g h")
for y in range(1,9):
   print(y,end=" ")
   for x in range(1,9):
        c="."
        for n in range(1,len(sys.argv)):
            figure=sys.argv[n]
            x0=int(figure[0])     # 3
            y0=int(figure[1])     # 4
            c0=    figure[2]      # 'T'
            if x==x0 and y==y0:
                c=c0
        print(c,end=" ")
   print()
print()

