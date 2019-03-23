import sys

def main():
	s = sys.argv[1]
	x = int(sys.argv[2])
	x = x % len(s)
	print (s[-x:] + s[:-x])

if __name__ == '__main__':
 		main()