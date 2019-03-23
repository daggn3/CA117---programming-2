import sys

def time(t):
	[minute, seconds] = t.split(":")
	total = int(minute) * 60 + int(seconds)
	return total
 

def sort(t):
	return time(t[-1])

def main():
	d = {}
	for lines in sys.stdin:
		try:
			tokens = lines.split()
			d[tokens[0]] = min(tokens[1:], key = time)
		except ValueError:
			continue
	winner = min(d.items(), key = sort )
	print("{} : {}".format(winner[0], winner[1]))
		


if __name__ == '__main__':
 		main()