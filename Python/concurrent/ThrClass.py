#!/usr/bin/python
# coding:utf-8

import threading
import time
import random


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(random.random())
            msg = "I'm " + self.name +' @ ' + str(i)
            print(msg)

if __name__ == '__main__':
    t = MyThread()
    t.start()