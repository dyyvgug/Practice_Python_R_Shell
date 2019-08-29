#!/usr/bin/python
#coding:utf-8

from operator import itemgetter
# read table
in_file = open("Am_codonW.txt",'r')
output_file = open('Am_codonW_sortCAI','w')
table = []
header = in_file.readline()
for line in in_file:
	col = line.split('\t')
	col[5] = float(col[5])
	table.append(col)

table_sorted = sorted(table,key = itemgetter(5),reverse = True)
# write sorted table to an output file
output_file.write(header + '\n')
for row in table_sorted:
	row = [str(x) for x in row]
	output_file.write('\t'.join(row) + '\n')
in_file.close()
output_file.close()
