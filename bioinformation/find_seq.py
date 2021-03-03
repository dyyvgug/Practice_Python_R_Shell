#!/usr/bin/python
#coding:utf-8
#=========================================================================================================
# Yingying Dong.2019-10-30.Modified date:2021-2-28.
# Get gene sequences of top 1% TPM from CDS sequence.
#=========================================================================================================
import os

print(os.getcwd())

#os.chdir('/media/hp/disk1/DYY/reference/annotation/{}/ref'.format(args.spe))
'''DNA = open('CDS_DNA.fa', 'r')
hE = open('{}.txt'.format(hE_path), 'r')
hE_seq = open('{}{}_{}_seq.fa'.format(hE_path,args.samp,args.per),'w')

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
    if line in database.keys():
        hE_seq.write('>' + str(line) + '\n' + str(''.join(database[line])) + '\n')

hE.close()
DNA.close()
hE_seq.close()'''
