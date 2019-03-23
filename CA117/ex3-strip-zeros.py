import sys
l = sys.stdin.read()

removed = [s.strip("0") for s in l]
print " ".join(removed)