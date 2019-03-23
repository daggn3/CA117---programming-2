import sys
def main():
	printtable = [x for x in sys.stdin if "a" in x.lower() and "e" in x.lower() and "i" in x.lower() and "o" in x.lower() and "u" in x.lower() and x.lower().count("a") == 1 and x.lower().count("e") == 1 and x.lower().count("i") == 1 and x.lower().count("o") == 1 and x.lower().count("u") == 1 and x.lower().find("a") < x.lower().find("e") and x.lower().find("e") < x.lower().find("i") and x.lower().find("i") < x.lower().find("o") and x.lower().find("o") < x.lower().find("u")]
	for i in range(0, len(printtable)):
		print(printtable[i].strip())


if __name__ == '__main__':
 		main()
