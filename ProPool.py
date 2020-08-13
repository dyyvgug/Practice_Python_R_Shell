#!/usr/bin/python
# coding:utf-8

import os
import time
import random
from multiprocessing import Pool

def worker(msq):
    t_start = time.time()
    print('{} start execution, the process number is {}'.format(msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, 'The execution is complete and time-consuming is {.2f}'.format(t_stop - t_start))

if __name__ == '__main__':
    po = Pool(3)  # Define a process pool.
    for i in range(0,10):
        po.apply_async(worker, (i,))
    print('-----start-----')
    po.close()
    po.join()
    print('-----end-----')
