#!/usr/bin/python
#coding:utf-8
## Retention order
input_file = open('UniprotID.txt','r')
output_file = open('UniprotID-unique.txt','w')
unique = []
for line in input_file:
	if line not in unique:
		out_file.write(line)
		unique.append(line)
output_file.close()

## not keep order
input_file = open('UniprotID.txt','r')
output_file = open('UniprotID-unique.txt','w')
unique = set(input_file)
for line in unique:
	output_file.write(line)
