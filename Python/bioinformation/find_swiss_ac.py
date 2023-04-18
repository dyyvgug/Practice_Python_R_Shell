#!/usr/bin/python
# -*- coding: UTF-8 -*-
swissprot = open("SwissProt.fasta","r")
insulin_ac = 'P61981'
seq = ''
result = None
while result == None :
	try:
		line = swissprot.next()
		if line.startswith('>'):
			ac = line.split('|')[1]
			if ac == insulin_ac:
				result = line.strip()
				print result
	except StopIteration:
		break
swissprot.close()

