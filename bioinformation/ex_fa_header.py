#coding:utf-8
# Extract the sequence header of the FASTA file to the new file
fasta_file = open("Ce_genome.fa","r")
out_file = open("Ce_genome_header.txt","w")
for line in fasta_file:
	if line.startswith('>'):   #if line[0:1] == '>':       
		out_file.write(line)
		print(line)
fasta_file.close()
out_file.close()
