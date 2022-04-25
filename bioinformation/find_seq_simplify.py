#!/usr/bin/python
#coding:utf-8
#=========================================================================================================
# Yingying Dong.2019-10-30.Get gene sequence of high expression high translation from CDS sequence.
#=========================================================================================================
import os
import argparse

parser = argparse.ArgumentParser(description='find DNA sequence',prog='find seq', usage='%(prog)s [options]')
parser.add_argument('-i', nargs='?', type=str, help='input file name of gene names')
parser.add_argument('-o', nargs='?', type=int, help='output file name of gene sequences', default='output.fa')
args = parser.parse_args()


DNA = open('CDS_DNA.fa','r')
hE = open('{}'.format(args.i),'r')
hE_seq = open('{}'.format(args.o),'w')

hE_table = []
database = {}
for i in hE.readlines():
    hE_table.append(i.strip())
for j in DNA:
    if j.startswith('>'):
        keys = j.lstrip('>').strip()
        database[keys] = []
    else:
        database[keys].append(j.strip())
for line in hE_table:
    hE_seq.write('>' + str(line) + '\n' + str(''.join(database[line])) + '\n')

hE.close()
DNA.close()
hE_seq.close()