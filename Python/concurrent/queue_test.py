#!/usr/bin/python
# coding:utf-8
import os
import time
import random
from multiprocessing import Process, Queue


def write(q):
    for i in ['A','B','C']:
        print('Put {} to queue'.format(i))
        q.put(i)
        time.sleep(random.random())


def read(q):
    while True:
        if not q.empty():
            j = q.get(True)
            print('Get {} from queue.'.format(j))
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    print('All data have written and read.')
