import sys
from collections import Counter

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

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
score_list = []
for word in result:
	sum = 0
	for letter in word:
		p = letter.lower()
		sum += scores[str(p)]
	score_list.append(sum)

fmt = '{:<10}{:<10}{}'

print(fmt.format('', 'Word', 'Score'))
for i, (word, score) in enumerate(zip(result, score_list)):
    print(fmt.format(i, word, score))






