#!/usr/bin/python
#coding:utf-8
## Create an empty table,the first method:
table = []
for i in range(6):
	table.append([0] * 6)
print (table)
## The second method,list comprehension:
table = [[0] * 6 for i in range(6)]
print (table)
