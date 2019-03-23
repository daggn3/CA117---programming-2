import sys

def match(w, s):
	return [c for c in w if c in s] == s


def main():
	evil = list("evil")

	word = [line.strip() for line in sys.stdin]


	evillist = [w for w in word if match(w.lower(), evil)]


	for w in evillist:
		print(w)



if __name__ == '__main__':
 		main()

