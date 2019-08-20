#coding:utf-8
# Extract the registration code in the GenBank annotation file
GenbankFile = open("Sj_genomic.gbff","r")
GenbankReg = open("Sj_genomic_reg.txt","w")
flag = 0
for line in GenbankFile:
	if line[0:9] == "ACCESSION":
		AC = line.split()[1].strip()
		print (AC)
		GenbankReg.write('>' + AC + '\n')
	elif line[0:6] == 'ORIGIN':
		 flag = 1
	elif flag == 1:
		fields = line.split()
		if fields != []:
			sep = ''.join(fields[1:])
			GenbankReg.write(sep.upper() + '\n')
GenbankFile.close()
GenbankReg.close()
