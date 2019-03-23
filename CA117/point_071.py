import math

class Point(object):

	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y


	def reflect(self):
		self.x = self.x * - 1
		self.y = self.y * - 1



	def distance(self, other):
		return math.sqrt((other.x - self. x) ** 2 + (other.y - self.y) ** 2)
		







if __name__ == '__main__':
 		main()