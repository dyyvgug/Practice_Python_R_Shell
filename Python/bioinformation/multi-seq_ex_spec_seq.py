#coding:utf-8
# Read the SwissProt dataset multi-sequence file and write the Homo sapiens registration record to a new file.
fasta_file = open('SwissProt.fasta','r')
out_file = open('SwissProtHuman.fasta','w')
seq = ''
for line in fasta_file:
	if line.startswith('>') and seq == '':    # if line[0] == '>' and seq =='':
# The sequence title is now obtained.
		header = line
	elif line[0] != '>':
# Indicates that this line is a sequence.
		seq = seq + line
	elif line[0] == '>' and seq != '':
# The sequence has been filled.
# In subsequent lines starting with '>',write the previous header and sequence to the output file.
# Then re-initialize the header and seq variables for the next record.
		if "OS=Human" in header:
			out_file.write(header + seq)
		seq = ''
		header = line
# Take care of the very last record of the input file.
if "OS=Human" in header:     # What is the role of if? Maybe one day I can understand.
	out_file.write(header + seq)  
fasta_file.close()
out_file.close()
