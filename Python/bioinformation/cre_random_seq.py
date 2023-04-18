# Create a random sequence
import random
alphabet = "ATCG"
sequence = ""
for i in range(10):
	index = random.randint(0,3)
	sequence = sequence + alphabet[index]
	print (sequence)
print (sequence)
