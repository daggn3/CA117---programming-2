def matcher(s):
	from stack_092 import Stack 
	opp_symbols = set(")}]")
	line = s
	if line[0] in opp_symbols:
		return False

	else:
		s = Stack()
		opening = ["(", "[", "{"]
		closing = [")", "]", "}"]
		mapping = {closing[0]:opening[0],closing[1]:opening[1],closing[2]:opening[2]}
		for i in line:
			try:
				if i in opening:
					s.push(i)
				else:
					if s.top() == mapping[i]:
						s.pop()
					else:
						return False
			except ValueError:
				pass
	return s.is_empty()
