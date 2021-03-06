#!/usr/bin/python
#coding:utf-8
import os


print(os.getcwd())              # get current path
print(os.listdir('.'))          # get all files of current path (list)
print(os.listdir(os.getcwd()))  # quality (list)

items = os.listdir(os.getcwd())     # one by one (str)
for item in items:
    if os.path.isfile(item):
        print(item)

print(os.walk('.'))                  # another way (str)
for root, dirs, files in os.walk('.'):
    for name in files:
        print(os.path.join(root, name))

syst = platform.system()            # transform path
        if syst == "Windows":
            os.chdir('.\\')
            the_path = '.\\a\\b\\'
        elif syst == "Linux":
            os.chdir('./')
            the_path = './a/b/'

if os.path.exists('{}{}'.format(the_path, "hello.txt")):
    c = open('{}{}'.format(the_path, "hello.txt"), 'r')

if not os.path.exists('./d/'):
    os.mkdir("./d/")


