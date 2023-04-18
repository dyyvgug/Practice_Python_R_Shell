#!/usr/bin/python
# coding:utf-8
import time
import os
from multiprocessing import Process

class Process_Class(Process):

    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        print('The child processing {} will start, the parent processing is {}'.format(os.getpid(),os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_stop = time.time()
        print('{} is over, the time-consuming is {}'.format(os.getpid(), t_stop-t_start))

if __name__ == '__main__':
    t_start = time.time()
    print('The current processing is {}'.format(os.getpid()))
    p1 = Process_Class(2)
    p1.start()
    p1.join()
    t_stop = time.time()
    print('{} is over, the time-consuming is {}'.format(os.getpid(), t_stop-t_start))