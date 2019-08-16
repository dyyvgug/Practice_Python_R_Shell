# Calculate the average and standard deviation of neuron
data = []
for line in open('neuron_data.txt'):
	length = float(line.strip())
	data.append(length)
n_items = len(data)
total = sum(data)
shortest = min(data)
longest = max(data)
ave = float(sum(data)) / len(data)
import math
sum_squ = 0.0
for value in data:
	sum_squ += (value - ave)**2
stddev = math.sqrt(sum_squ / len(data))
data.sort()
mid = int(len(data)/2)
if len(data) % 2 == 0 :
	median = (data[mid-1] + data[mid]) / 2.0 
else:
	midian = data[mid]
output = open("neuron_stadev.txt","w")
output.write("number of neuron lengths : %4i \n" % (n_items))
output.write("total length             : %6.1f \n" % (total))
output.write("shortest neuron          : {:>4.2f} \n".format(shortest))
output.write("longest neuron           : {:>4.2f} \n".format(longest))
output.write("average length           : {:>4.2f} \n".format(ave))
output.write("standard deviation       : {:>4.2f} \n".format(stddev))
output.write("median neuron            : {:>4.2f}".format(midian))
