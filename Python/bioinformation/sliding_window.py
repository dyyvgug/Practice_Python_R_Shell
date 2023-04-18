# sliding window
# given window is 5 amino acid,step size of 1 amino acid.
seq = "PRQTEINSEQWENCE"
for i in range(len(seq)-4):
	print (seq[i:i+5])
