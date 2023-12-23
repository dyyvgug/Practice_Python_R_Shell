#!/usr/bin/python
import sys

print()
print("  a b c d e f g h")
def chess():
    rows, cols = 8, 8
    board = [['.' for _ in range(rows)] for _ in range(cols)]
    for n in range(1, len(sys.argv)):
        fig = sys.argv[n]
        x0 = int(fig[0])
        y0 = int(fig[1])
        c0 = fig[2]

        board[x0][y0]=c0
    #print(board)
    for sublist in board:
        print(' '.join(sublist))  # list2string
chess()