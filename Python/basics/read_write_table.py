#!/usr/bin/python
#coding:utf-8
## read table
table = []
for line in open('lowry_data.txt'):
	table.append(line.strip().split('\t'))
print (table)

## write table data to file
out = ''
for row in table:
	one = [str(cell) for cell in row]
	out = out + '\t'.join(one) + '\n'
open('new_data.txt','w').write(out)
