#!/usr/bin/python
# coding:utf-8
import random
from time import *

def reverse(seq):
    return seq[::-1]


def complement(seq):
    intab = "ATCGatcg"
    outab = "TAGCtagc"
    trantab = str.maketrans(intab, outab)
    result = seq.translate(trantab)
    print(result)
    return result

sequence = []
seq_len = 100
for i in range(seq_len):
    sequence.append(random.choice('ATGCatgc'))
sequence = ''.join(sequence)
print('original sequence: ', sequence, '\n')

begin_time = time()
sequence = reverse(sequence)
print('reverse complement sequence: ')
complement(sequence)
end_time = time()
run_time = end_time - begin_time
print('run time: ', run_time)

