def build_dictionary(filename):
	with open(filename, "r") as f:
		lines = [w.strip() for w in f.readlines()]
		d = {}
		for i in lines:
			i = i.split()
			d[i[0]] = i[1]
	return d

def extract_range(d, lowest, highest):
	nd = {}
	for (k, v) in sorted(d.items()):
		if int(v) >= lowest and int(v) <= highest:
			nd[k] = v
	return nd













if __name__ == '__main__':
 		main()