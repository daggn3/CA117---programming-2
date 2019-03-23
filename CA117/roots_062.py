from math import sqrt
import sys

def b():
	for line in sys.stdin:
		line = line.strip().split()
		line[0] = int(line[0])
		line[1] = int(line[1])
		line[2] = int(line[2])
		a = line[0]
		b = line[1]
		c = line[2]
		roots = (b ** 3 - 4 * (a*c))
		if roots >= 0:
			r1 = (b * -1 + sqrt((b**2) - 4 * (a*c))) / (2 * a)
			r2 = (b * -1 - sqrt((b**2) - 4 * (a*c))) / (2 * a)
			print( "r1 = {}, r2 = {}".format(r1, r2))
		else:
			print("None")

if __name__ == '__main__':
 		b()