import sys
from collections import Counter


with open('sowpods.txt') as f:
	mylist = list(map(str.strip, f))

rack = sys.argv
rack = rack[1:]
#print (rack)
if len(rack)==0:
	sys.exit('Error!\n Supply some rack')

result = []

rack = [x.upper() for x in rack]
for rack_element in rack:
	for word in mylist:
		if len(word)<=len(rack_element):
			if not Counter(word) - Counter(rack_element):
				result.append(word)

print (result)




