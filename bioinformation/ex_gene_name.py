#!/usr/bin/python
#coding:utf-8
#2019-10-23.Yingying Done.

fa_file = open('transcripts.fa','r')
name_file = open('gene_name.txt','w')

for line in fa_file:
	if line.startswith('>'):    
# The sequence title is now obtained.
		header = line
		print (header)
		name_file.write(header)
fa_file.close()
name_file.close()
