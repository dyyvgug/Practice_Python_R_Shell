#!/usr/bin/python
#coding:utf-8
#DYY.2019-10-15.

import os,sys,re
os.chdir('/media/hp/disk1/DYY/reference/annotation/')
files = os.listdir(os.getcwd())
dirlist = []
all_name = open("species_name.txt",'w')
p1 = '_'
pattern1 = re.compile(p1)
for i in files:
	if (os.path.isdir(i)):
		dirlist.append(i)
		newKey = re.sub(p1,' ', i)
		print newKey
		all_name.write(newKey + '\n')
print dirlist
