import sys



def main():
	s = sys.stdin.readlines()
	x = set()
	y = set()
	r = []
	for line in s:
		if len(line.strip()) >= 5:
			x.add(line.strip())
	for c in x:
		f = c
		c = c.lower()
		c = c[::-1]
		d = c.capitalize()
		if c in x or d in x:
				y.add(f)
	for f in y:
		r.append(f)
	r = sorted(r, key=str.lower)
	print (r)

		

	
if __name__ == '__main__':
	main()

