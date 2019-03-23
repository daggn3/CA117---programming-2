import sys

def longest_substring(line1, line2):
	shortest, longest = min([line1, line2], key = len), max([line1, line2], key = len)

	if len(shortest) == len(longest):
		shortest = line1
		longest = line2

	maxsub = 0
	sub = ""

	i = 0
	while i < len(shortest):
		if shortest[i] in longest:
			j = i + 2
			while j <= len(shortest) and shortest[i:j] in longest:
				j  = j + 1

			if len(shortest[i : j - 1]) > maxsub:
				sub = shortest[i:j - 1]
				maxsub = len(sub)

		i = i + 1

	return sub

def biggest(line1, line2):
	substring = longest_substring(line1, line2)

	testcase = line2.split(substring)
	index = len(testcase[0])

	return (substring, len(substring), index)


def main():
	line1, line2 = sys.stdin.readline().strip(), sys.stdin.readline().strip()
	substring, length, index = biggest(line1, line2)
	print("{} {} {}".format(substring, length, index))

if __name__ == '__main__':
 		main()