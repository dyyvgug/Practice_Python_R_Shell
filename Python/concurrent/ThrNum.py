#!/usr/bin/python
# coding:utf-8
import time
import random
import threading


def sing():
    for i in range(10):
        print('sing ~ {}'.format(i))
        time.sleep(random.random())


def dance():
    for j in range(10):
        print('dance ~ {}'.format(j))
        time.sleep(random.random())


if __name__ == '__main__':
    print('-----START-----: {}'.format(time.ctime()))
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

    while True:
        lenth = len(threading.enumerate())
        print('The current number of threads is {}'.format(lenth))
        if lenth <= 1:
            break
        time.sleep(random.random())

    print('-----ENA-----: {}'.format(time.ctime()))