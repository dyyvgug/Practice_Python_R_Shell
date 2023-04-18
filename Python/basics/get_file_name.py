#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def getFileName(path):
    f_list = os.listdir(path)
    print (f_list)
    for i in f_list:
        if os.path.splitext(i)[1] == '.fa':
            print(i)
            print(os.path.splitext(i)[0])


if __name__ == '__main__':

    path = '/media/hp/disk2/DYY2/cell_line/HEK293/experiment2/aligned/'
    getFileName(path)
