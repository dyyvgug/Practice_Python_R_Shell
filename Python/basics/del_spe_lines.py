#!/usr/bin/python
#coding:utf-8
## The first method,suitable for small files
lines = open('蜜蜂.txt').readlines() 
open('new.txt','w').writelines(lines[2:4]+lines[6:])

## The second method,suitable for large files
in_file = open('蜜蜂.txt','r')
out_file = open('new.txt','w')
index = 0
indices_to_remove = [1,2,5,6]
for line in in_file:
	index = index + 1
	if index not in indices_to_remove:
		out_file.write(line)
out_file.close()

## The third method,suitable for large files,did not use index.
out_file = open('new.txt','w')
indices_to_remove = [1,2,5,6]
for index,line in enumerate(open('蜜蜂.txt','r')):
	if (index + 1) not in indices_to_remove:
		out_file.write(line)
out_file.close()
