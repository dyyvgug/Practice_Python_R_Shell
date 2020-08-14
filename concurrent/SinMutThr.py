#!/usr/bin/python
# coding:utf-8
import time
import threading


def sayHello():
    print('Hello!')
    time.sleep(1)


'''if __name__ == '__main__':
    t_start = time.time()
    for i in range(5):
        sayHello()
    t_stop = time.time()
    print('End, the time-consuming is {}'.format(t_stop - t_start))'''

if __name__ == '__main__':
    t_start = time.time()
    for i in range(5):
        t = threading.Thread(target=sayHello)
        t.start()
    t_stop = time.time()
    print('End, the time-consuming is {}'.format(t_stop - t_start))
