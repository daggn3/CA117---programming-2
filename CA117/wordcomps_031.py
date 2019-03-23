import sys 

words = sys.stdin.read().split()
v = "aeiou"

def seventeen(word):
	return[s for s in word if len(s.strip().lower()) == 17]

def eighteen(word):
	return [s for s in word if len(s.strip().lower()) > 17]

def vowels(s):
	s = s.lower()
	return "a" in s and "e" in s and "i" in s and "o" in s and "u" in s

def shortestvowel(word):
	return min([w for w in word if vowels(w)], key = len)
	
def foura(word):
	return [s for s in word if s.strip().lower().count("a") == 4]

def countq(word):
	return [s for s in word if s.strip().lower().count("q") >= 2]

def cie(word):
	return [s for s in word if "cie" in s.strip().lower()]

def anagram(word):
	return [ s for s in word if sorted(s.lower(), key = str) == sorted("angle", key = str) and s != "angle"]

def iary(word):
	return len([s for s in word if s[-4:] == "iary"])

def qnou(word):
	return[s for s in word if s.lower().count("q") > s.lower().count("qu")]

def moste(word):
	b = []
	most = 0
	for s in word:
		e = s.lower().count("e")
		if e > most:
			most = e

	list = []
	for s in word:
		if s.lower().count("e") == most:
			b.append(s)
	return b


print ("Words containing 17 letters:", seventeen(words))
print ("Words containing 18+ letters:", eighteen(words))
print ("Shortest word containing all vowels:", shortestvowel(words))
print ("Words with 4 a's:", foura(words))
print ("Words with 2+ q's:", countq(words))
print ("Words containing cie:", cie(words))
print ("Anagrams of angle:", anagram(words))
print ("Words ending in iary:", iary(words))
print ("Words with q but no u:", qnou(words))
print ("Words with most e's:", moste(words))

