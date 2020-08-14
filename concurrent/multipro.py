#!/usr/bin/python
# coding:utf-8

import os
from multiprocessing import Process
from time import sleep

def run_proc(name, age, **kwargs):
    for i in range(10):
        print('The child processing run on, name = {},age = {}, pid = {}'.format(name, age, os.getpid()))
        print(kwargs)
        sleep(0.5)

if __name__ == '__main__':
    print('The parent processing {}'.format(os.getpid()))
    p = Process(target=run_proc, args=('test', 18), kwargs={'m': 20})
    print('The child processing will run')
    p.start()
    sleep(1)
    p.terminate()
    p.join()
    print('The child processing is over')
