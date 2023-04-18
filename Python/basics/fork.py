#!/usr/bin/python
# coding:utf-8
import os

pid = os.fork()

if pid == 0:
    print('if...')
else:
    print('else...')