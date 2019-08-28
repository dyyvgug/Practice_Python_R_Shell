#!/usr/bin/python
#coding:utf-8
## nested list to nested dictionary
table = [
['protein','ext1','ext2','ext3'],
[0.16,0.038,0.044,0.040],
[0.33,0.089,0.095,0.091],
[0.66,0.184,0.191,0.191],
[1.00,0.280,0.292,0.283],
[1.32,0.365,0.367,0.365],
[1.66,0.441,0.443,0.444]
]
nested_dict = {}
n = 0 
key = table[0]
# to include the header,run the for loop over
# ALL table elements,including the first one
for row in table[1:]:
	n = n + 1
	entry = {key[0]:row[0],key[1]:row[1],key[2]:row[2],key[3]:row[3]}
	nested_dict['row' + str(n)] = entry
print (nested_dict)
print ('\n' + str(nested_dict['row1']['ext2']))
## nested dictionary to nested list
nested_list = []
for entry2 in nested_dict:
	key2 = nested_dict[entry2]
	nested_list.append([key2['protein'],key2['ext1'],key2['ext2'],key2['ext3']])
print (nested_list)
