#!/usr/bin/env python3

"""
parse a genom from an fsa file
use re to find the genoms
use mmap to save memory
use finditer 
tokenize the genom sequence
generate the window slices
"""

import numpy as np
import mmap
import re

rex=re.compile("^\>(.*?)\n(.*?)\n(?:>)",re.MULTILINE|re.DOTALL)

filename="Gnomon_mRNA.fsa"

with open(filename) as fh, mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ) as mfh:
    s = mfh.read().decode("utf-8")  
    resIter=re.finditer(rex,s)
    next(resIter)       # 1
    next(resIter)       # 2
    res=next(resIter)   # try genom 3
    s=re.sub("\n","",res.groups()[1])   # strip \n
    print(s)

# my tokenizer
s2t=dict(zip(sorted(set(s)),range(len(s))))     # tokenizer
t2s=dict(zip(s2t.values(),s2t.keys()))          # inverse tokenizer

print(s2t)

def slice_window_generator(lst, window_size=1):
    for i in range(len(lst) - window_size + 1):
        yield lst[i:i + window_size]

lst=([s2t[x] for x in window] for window in slice_window_generator(s, window_size=50))
print(lst) # a generator

X=np.array(list(lst),dtype=np.int8)

print(X)
print(X.shape)

# now create the one hots for Y ......

