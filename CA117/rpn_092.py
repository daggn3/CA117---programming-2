import math
import operator
from stack_092 import Stack

s = Stack()

d = {
	"+" : operator.add,
	"-" : operator.sub,
	"*" : operator.mul,
	"/" : operator.truediv,
	"r" : math.sqrt,
	"n" : operator.neg,
	}



def calculator(line):
	line = line.split()
	nums = []
	ops = []
	for x in line:
		if x not in "+-*/rn":
			s.push(float(x))
			nums.append(x)
		else:
			if x in "+-*/":
				num1 = s.pop()
				num2 = s.pop()
				s.push(d[x](num2 , num1))
			else:
				num = s.pop()
				s.push(d[x](num))
	return s.pop()