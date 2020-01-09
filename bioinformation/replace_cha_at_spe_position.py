#!/usr/bin/python
#coding:utf-8
#Yingying Dong.
import re
p = re.compile('A{5,}')
string = 'ATGCAGAAAAATGCTACCGAAAAAAAAAAAAAAACGGGAAAAACCC'
# string = 'ATGCAGUUAATGCTACCXXXAAAACGGGAQQQACCC'
pos_list = []
while len(p.findall(string)):
	for m in p.finditer(string):
		pos = m.start()
		pos_list.append(pos)
	print(pos_list)
	for i in pos_list:
		if i % 3 == 0:
			print(string[i:i+3])
			string = string[:i] + 'UUU' + string[i+3:]
			print(string)
		elif i % 3 == 1:
			print(string[i -1 : i + 2])
			string = string[:i-1] + 'XXX' + string[i+2:]
			print(string)
		elif pos % 3 == 2:
			print(string[i + 1 : i + 4])
			string = string[:i+1] + 'QQQ' + string[i+4:]
			print(string)
print(string)


	
