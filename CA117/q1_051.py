import sys



def main():
	words = sys.argv[1]
	

	s = list(words)


	for i in range(1, len(words), 2):
		s[i - 1], s[i] = s[i], s[i - 1]

	print("".join(s))

if __name__ == '__main__':
 		main()