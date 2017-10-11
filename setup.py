import sys

with open('sowpods.txt') as f:
	mylist = list(map(str.strip, f))

rack = sys.argv
rack = rack[1:]
#print (rack)
if len(rack)==0:
	sys.exit('Error!\n Supply some rack')
for element in rack:
	if element.isupper()==False:
		sys.exit('Error!\n all rack must be in capital letters')



