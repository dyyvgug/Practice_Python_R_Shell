#!/usr/bin/python
# coding:utf-8


def A():
    while True:
        print('---1---')
        yield None


def B():
    while True:
        print('---2---')
        yield None

if __name__ == '__main__':
    a = A()
    b = B()
    while True:
        next(a)
        next(b)