#!/usr/bin/python
#coding:utf-8
sequences = {}
ac = ''
seq = ''
swissprot = open("SwissProt.fasta","r")
ac_seq = open("ac_seq.fa","w")
one_ac = 'P62258'
result = None
while result == None :
	try:
		line = swissprot.next()
		if line.startswith('>'):
			ac = line.split('|')[1]
			if ac == one_ac:
				result = line.strip()
				print result
	except StopIteration:
		break
ac_seq.write(result +'\n')
for line in swissprot:
	if line.startswith('>') and seq != '':
		sequences[ac] = seq
		seq = ''
	if line.startswith('>'):
		ac = line.split('|')[1]
	else:
		seq = seq + line.strip()
sequences[ac] = seq
#print sequences.keys()
print sequences[one_ac]
i = 0
while i < len(sequences[one_ac]):
	print sequences[one_ac][i:i+48]
	ac_seq.write(sequences[one_ac][i:i+48])
	i = i + 48

swissprot.close()
ac_seq.close()
