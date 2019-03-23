import sys 


d = {
	"1": "one",
	"2": "two",
	"3": "three",
	"4": "four",
	"5": "five",
	"6": "six",
	"7": "seven",
	"8": "eight",
	"9": "nine",
	"10": "ten",
}

def main():
	for lines in sys.stdin:
		lines = lines.strip().split()
		for c in lines:
			if c in d.items():
				print(c)







if __name__ == '__main__':
 		main()