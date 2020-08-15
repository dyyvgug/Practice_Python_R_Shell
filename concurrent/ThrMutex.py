#!/usr/bin/python
# coding:utf-8
import time
from threading import Thread, Lock

g_num = 0

def test1():
    global g_num
    for i in range(1000000):
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num += 1
            mutex.release()
    print('-----test1----- g_num = {}'.format(g_num))


def test2():
    global g_num
    for i in range(1000000):
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num += 1
            mutex.release()
    print('-----test2----- g_num = {}'.format(g_num))


if __name__ == '__main__':
    mutex = Lock()
    p1 = Thread(target=test1)
    p2 = Thread(target=test2)
    p1.start()
    p2.start()
    print('--- g_num = {} ---'.format(g_num))