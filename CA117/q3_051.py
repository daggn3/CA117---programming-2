import sys
from re import findall 

def main():
	for lines in sys.stdin:
		lines = lines.strip()
		print(max(findall(r'[A-Z]+', lines), key = len))



if __name__ == '__main__':
 		main()