


class Score(object):


	def __init__(self, goals = 0, points = 0):
		self.goals = goals
		self.points = points


	def greater_than(self, other):
		if self.goals * 3 + self. points > other.goals * 3 + other.points:
			return True
		else:
			return False

	def less_than(self, other):
		if self.goals * 3 + self.points < other.goals * 3 + other.points:
			return True
		else:
			return False

	def equal_to(self, other):
		if self.goals * 3 + self.points == other.goals * 3 + other.points:
			return True
		else:
			return False