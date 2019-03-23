import sys
words = sys.stdin.read()
d = {}
with open("translation.txt","r") as f:
	i = 0
	t = f.readlines()
	while i < len(t):
		word = t[i].strip().split()
		d[word[0]] = word[1]
		i = i + 1

def trans(words, d):
	splitted = words.split()
	for i in range(len(splitted)):
		if splitted[i] in d:
			splitted[i] = d[splitted[i]]
	sentence = " ".join(splitted) 
	return sentence

print (trans(words,d))
