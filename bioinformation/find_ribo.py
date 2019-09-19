#!/usr/bin/python
#coding:utf-8
import os
import re

os.chdir("/home/hp/Desktop/other_riboseq/C_elegans_Ensl_WBcel235/experiment2/aligned/ribo_num/")
other_ribo = open("SRR1804340_other_ribo_gene.txt",'r')
hE_hT = open("SRR1804340_hiE_ht_gene.txt",'r')
other_ribo_filter = open("40_other_ribo_filter.txt",'w')
hE_hT_filter = open("40_hE_ht__ribo_filter.txt",'w')
hE_hT_no_ribo = open("40_hE_ht-ribo.txt",'w')
keyword = re.compile(r'rpl|rps')
def findRibo(ribokey):
	for line in other_ribo:
		riboLine = ribokey.search(line)
		if riboLine:
			other_ribo_filter.write(line)
	for line in hE_hT:
		riboLine = ribokey.search(line)
		if riboLine:
			hE_hT_filter.write(line)
		else:
			hE_hT_no_ribo.write(line)
#findRibo(keyword1)
findRibo(keyword)
other_ribo_filter.close()
hE_hT_filter.close()
hE_hT_no_ribo.close()

		
